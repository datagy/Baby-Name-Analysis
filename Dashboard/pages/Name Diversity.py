import streamlit as st

st.header('Under construction')

# import plotly.express as px
# import pandas as pd
# from Home import df
# import streamlit as st
# import numpy as np


# def get_unique_names_by_year(df):
#     unique_by_year = pd.pivot_table(
#         data=df,
#         index=['Year', 'Gender'],
#         values='Name',
#         aggfunc='nunique'
#     ).reset_index()

#     return px.line(
#         data_frame=unique_by_year,
#         x='Year',
#         y='Name',
#         color='Gender',
#         title='Name Diversity over Time',
#         labels={
#             'Name': '# of Unique Names',
#         }
#     )


# def get_unique_names_by_starting_letter(df):
#     unique_by_starting_letter = pd.pivot_table(
#         data=df,
#         index=['Starting Letter', 'Gender'],
#         values='Name',
#         aggfunc='nunique',
#     ).reset_index()

#     unique_by_starting_letter['Name'] = np.where(
#         unique_by_starting_letter['Gender'] == 'F',
#         unique_by_starting_letter['Name'] * -1,
#         unique_by_starting_letter['Name']
#     )

#     return px.bar(
#         data_frame=unique_by_starting_letter,
#         y='Starting Letter',
#         x='Name',
#         color='Gender',
#         labels={
#             'Name': '# of Unique Names'
#         },
#         height=600,
#         title='# of Unique Names by Starting Letter'
#     )


# unique_names_by_year = get_unique_names_by_year(df)
# unique_by_starting_letter_chart = get_unique_names_by_starting_letter(df)
# st.plotly_chart(unique_by_starting_letter_chart)
# st.plotly_chart(unique_names_by_year)
