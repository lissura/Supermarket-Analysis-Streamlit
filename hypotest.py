import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


def data_load(df : pd.DataFrame) : 
    st.markdown(
         """ 
         <style>
          h2{text-align : center;
          font-size:100px;}
          h3{text-align:justify;
          font-size:50px;}
          h4{font-size:35px}
          h4{text-align:justify;
          front-size:25px}
          </style>

          <h2> 📝 Hypothesis Testing 📝 </h2> 
          """,unsafe_allow_html=True)
    st.markdown(
         ''' <h3>
         I've been told that branch B has the lowest productivity. Is that true? If it is true then I\
          will hire new sales man.</h3>''', unsafe_allow_html=True)
    st.info('We will test whether the productivity in branch A B C is different or not')


    with st.expander('Show Productivity in each branch'):
         busy_time_graph= px.histogram(df.sort_values("branch"), x='time', y='quantity' ,color='branch', barmode='group')
         total_Q = df.groupby(['branch','time'])['quantity'].sum()
         total_Q= total_Q.groupby("time").mean().reset_index()
         busy_line_graph=busy_time_graph.add_trace(go.Scatter(x=total_Q.time, y=total_Q['quantity'],line_color = 'yellow', name="Quantity"))
         st.plotly_chart(busy_line_graph,use_container_width=True)
         A_time= (df[df['branch']=='A'][['time','quantity']].groupby('time').sum())
         B_time= (df[df['branch']=='B'][['time','quantity']].groupby('time').sum())
         C_time= (df[df['branch']=='C'][['time','quantity']].groupby('time').sum())
         sample_A = A_time.reset_index() 
         sample_B = B_time.reset_index() 
         sample_C = C_time.reset_index() 
         maxA=sample_A[sample_A['quantity']==sample_A['quantity'].max()]
         maxB=sample_B[sample_B['quantity'] == sample_B['quantity'].max()]
         maxC=sample_C[sample_C['quantity'] == sample_C['quantity'].max()]
         st.write('Productivity in branch A is : ', maxA.values[0,0], f'serving {maxA.values[0,1]} of quantity')
         st.write('Productivity hour in branch B is : ',maxB.values[0,0], f'serving {maxB.values[0,1]} of quantity')
         st.write('Productivity hour in branch C is : ',maxC.values[0,0], f'serving {maxC.values[0,1]} of quantity')

    A_time= (df[df['branch']=='A'][['time','quantity']].groupby('time').sum())
    B_time= (df[df['branch']=='B'][['time','quantity']].groupby('time').sum())
    C_time= (df[df['branch']=='C'][['time','quantity']].groupby('time').sum())
    st.write('The average of quantity in branch A is : ', A_time.quantity.mean())
    st.write('The average of quantity in branch B is : ',B_time.quantity.mean())
    st.write('The average of quantity in branch C is : ',C_time.quantity.mean())
    
    st.write(''' <h4>
    - H0 : myuA = myuB = myuC 🔴 <br>
    - H1 : myuA != myuB != myuC 🔵
    </h4>
    ''', unsafe_allow_html = True)

    st.write('''
    ----

    The Productivity in each branch is slightly different,  but is that significant? \
         We need to use **ANOVA** to do the hypothest. <br>
    With the use of **95% confidence interval** (0.05 Critical Value), here are the results: <br>

    ''', unsafe_allow_html = True)

    f_stat, p_val = stats.kruskal(A_time,B_time,C_time)
    st.write(f'P-value: {p_val}, F stat : {f_stat}')
    st.write('With the use of 95 Confidence Interval (0.05), P value is higher than Critical Value')
    

    viz_hypo=st.checkbox('See Visualization')
    if viz_hypo:
          A_Population = np.random.normal(A_time.quantity.mean(),A_time.quantity.std(),80)
          B_Population = np.random.normal(B_time.quantity.mean(),B_time.quantity.std(),80)
          C_Population = np.random.normal(C_time.quantity.mean(),C_time.quantity.std(),80)
          st.write(f'{A_Population.std()}, {B_Population.std()}, {C_Population.std()}')

          ci = stats.norm.interval(0.95, A_time.quantity.mean(), A_time.quantity.std())
          fig = plt.figure(figsize=(16,5))
          sns.distplot(A_Population, label='Population of Branch A',color='orange')
          sns.distplot(B_Population, label='Population of Branch B',color='blue')
          sns.distplot(C_Population, label='Population of Branch C',color='red')

          plt.axvline(B_time.quantity.mean(), color='blue', linewidth=2, label='France mean')
          plt.axvline(C_time.quantity.mean(), color='red',  linewidth=2, label='Germany mean')

          plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
          plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2)

          plt.axvline(A_Population.mean()+f_stat[0]*A_Population.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
          plt.axvline(A_Population.mean()-f_stat[0]*A_Population.std(), color='black', linestyle='dashed', linewidth=2)
          plt.legend()
          st.pyplot(fig)

    with st.expander('Show Conclusion'):
         st.markdown('''
         <h3>
        ✔️Accept Null Hypothesis✔️
         </h3>
         ''', unsafe_allow_html=True)
         st.markdown('''

         <h4>The blackline (our H1) is within our confidence interval. \
              This means we FAIL TO REJECT H0. Therefore Branch B is not the lowest\
               because the differences between branches are not significant. You dont need to hire new salesman.</h4>
         ''' , unsafe_allow_html=True)
         col1,col2,col3=st.columns([1,1,1])
         col2.image('image0031.jpeg')
