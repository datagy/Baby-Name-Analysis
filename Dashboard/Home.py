import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.markdown("# Baby Name Analysis")
st.sidebar.markdown("# Home")


@st.cache
def load_data():
    df = pd.read_csv('names.csv')
    df['Proportion'] = df['Number'] / \
        df.groupby(['Year', 'Gender'])['Number'].transform('sum')

    df['Gender'] = df['Gender'].map({'M': 'Male', 'F': 'Female'})

    return df


df = load_data()
