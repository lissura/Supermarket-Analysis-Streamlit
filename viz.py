import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go



def data_load(df:pd.DataFrame):

     gross_income = df.groupby(['branch'])['gross_income'].sum()
     gross_income_max = gross_income.sort_values(ascending=False).reset_index()
     branch_income=px.histogram(df.sort_values('branch') ,x='branch', y='gross_income', color = 'branch',)
     busy_time_graph= px.histogram(df.sort_values("branch"), x='time', y='quantity', color='branch', barmode="group")
     total_Q = df.groupby(['branch','time'])['quantity'].sum().reset_index()
     total_Q1 = total_Q.groupby("time").mean().reset_index()
     profitable_product = df.groupby('product_line')['gross_income'].sum().sort_values(ascending=False).reset_index()
     busy_time_line=busy_time_graph.add_trace(go.Scatter(x=total_Q1['time'], y=total_Q1['quantity'], line_dash = 'dash', line_color = 'black', name="Quantity"))
     
     st.markdown(
         """ 
         <style>
          h2{text-align : center;
          font-size:100px;}
          h3{text-align:center;
          font-size:50px;}
          </style>

          <h2> INSIGHTS 🕵️‍♀️ </h2> 
          """,unsafe_allow_html=True)
     st.markdown(
         ''' <h3>
         Shown are Insights the Visualization of the dataset</h3>''', unsafe_allow_html=True)
    

     with st.expander('Revenue by Product Sales💰'):
        column1, column2 = st.columns([3,1])
        df = pd.read_csv('cleanData.csv')
        df['date']=  pd.to_datetime(df['date'], format = '%Y-%m-%d').dt.date
        date_min = df["date"].min()
        date_max = df["date"].max()
                #
        date_slider = column1.slider(label="Select Date",
                                min_value = date_min,
                                max_value = date_max,
                                value = (date_min, date_max))
        select_city = column2.selectbox('Select City', df.sort_values('City').City.unique())
        df_selec = df[ (df["date"] >= date_slider[0]) & 
                            (df["date"] <= date_slider[1]) & (df["City"] == select_city) ]
        a = df_selec.groupby('product_line')['gross_income'].sum().sort_values(ascending=False).reset_index()
        fig=px.bar(a, x='product_line', y='gross_income', color=a.product_line)
        column3,column4=st.columns([3,2])
        column3.plotly_chart(fig)
        column4.write(a)
        st.write(f'🧐 In  {select_city} city at {date_slider[0]} until {date_slider[1]} \
            the most profitable product is {a.values[0,0]} with {a.values[0,1]} gross income')
     
     with st.expander('Productivity 🚦'):
         col1, col2 = st.columns([3,1])
         values = col1.slider('Time Operating', int(df.time.min()), int(df.time.max()), step=1)
         select_branch=col2.selectbox('Select Branch',df.sort_values("branch").branch.unique())
         count = df[(df["branch"] == select_branch) & ( df.time == values)].quantity.sum()
         st.write(f'🧐 in branch {select_branch} at {values}  O`clock, {count} of product sold ') 
     
     with st.expander('Branch Gross Income 💰 '):
         #  branch_income=px.histogram(df.sort_values('branch') ,x='branch', y='gross_income', color = 'branch',)
         st.plotly_chart(branch_income, use_container_width=True)   
         st.write((f'🧐 The branch that have highest gross income is branch {gross_income_max.values[0,0]} by {gross_income_max.values[0,1]} of gross income'))
     
     with st.expander('Relation Between Price and Rating ✔️'):
         fig1=sns.relplot( x=df["unit_price"], y=df["rating"],ci=None).set(title='Relation Between Price and Rating')
         st.pyplot(fig1, use_container_width=True)
         st.write('🧐 There is no relation between Unit Price and Rating')