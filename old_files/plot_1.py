import streamlit as st
import pandas as pd
import plotly.express as px


labels = ['Manzanas', 'Naranjas', 'Plátanos']
values = [30, 45, 25]

fig = px.pie(values=values, names=labels)

st.plotly_chart(fig)