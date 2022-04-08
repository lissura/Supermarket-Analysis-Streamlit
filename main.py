import pandas as pd
import streamlit as st
import hypotest
import viz
import homepage

st.set_page_config(
    page_title="Insight Supermarket",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")
st.set_option('deprecation.showPyplotGlobalUse', False)

PAGES = {
"Homepage" : homepage,
"Visualization" : viz,
'Hypothesis Testing' : hypotest
}

@st.cache
def data_load():
    df = pd.read_csv('cleanData.csv')
    df = df.drop(columns='Unnamed: 0')
    return df


df= data_load()
selected = st.sidebar.radio('Select your page: ', PAGES.keys())
page = PAGES[selected]
page.data_load(df)
