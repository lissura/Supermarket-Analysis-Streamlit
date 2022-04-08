import pandas as pd
import streamlit as st

def data_load(df:pd.DataFrame):
    # data=data_load()
    st.markdown(
    """
    <style>
    h2 {background-color:#191970;
        font-size:50px;
        color: 	#F0F8FF;
        border: 2px solid;
        padding: 20px 20px 20px 70px; */
        padding: 5% 5% 5% 10%;
    text-align: center
    }

    </style>
    <h2> 📊 Supermarket Analysis for Milestone1 📊</h2>

    ---
    Introduction:
    - **Name** : Cindra Chatami <br>
    - **Buddy**: Sardi Irfansyah <br>
    - **Email**: cindrac05@gmail.com
    ---

    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    h3 {background-color: #66CDAA;
            color: #000000;
        font-family: "Helvetica";
        font-size: 50px;
        text-align: center;
        border-radius: 15px 50px;
        margin: 5px 5px 5px 5px;
        }
    h4{ font-family: "Helvetica";
    font-size : 20px;
    text-align: justify}
    </style>
    <h3> 📜 Data Description 📜 </h3>


    ----
    <h4> As time goes by, the competition and the behaviour of buyer is changing and we  need to adapt. \
        This application helps you get insights\
        , analyze, and predict your supermarket to adapt with current situation.
        The datasets we use is\
        information of sales history in a supermarket for 3 months.
    </h4>

    ----
    """
    ,unsafe_allow_html=True)

    show_df=st.checkbox('Show Table')
    if show_df:
        st.caption('This is the table of the dataset')
        st.dataframe(df)


    about_df = st.checkbox('Attribute Information')
    if about_df:
        st.caption('Information of each column')
        st.markdown(
            " Invoice id    : Computer generated sales slip invoice identification number<br>\
            Branch : Branch of supercenter (3 branches are available identified by A, B and C)<br>\
            City   : Location of supercenters<br>\
            Customer type  : Type of customers, recorded by Members for customers using member card and Normal for without member card.<br>\
            Gender : Gender type of customer<br>\
            Product line   : General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel<br>\
            Unit price : Price of each product in $<br>\
            Quantity   : Number of products purchased by customer<br>\
            Tax    : 5% tax fee for customer buying<br>\
            Total  : Total price including tax<br>\
            Date   : Date of purchase (Record available from January 2019 to March 2019)<br>\
            Time   : Purchase time (10am to 9pm)<br>\
            Payment    : Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)<br>\
            COGS   : Cost of goods sold<br>\
            Gross margin percentage    : Gross margin percentage<br>\
            Gross income   : Gross income<br>\
            Rating : Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)",
            unsafe_allow_html=True)