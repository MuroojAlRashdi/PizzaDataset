
import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
st.title('welcome to home page')

st.write('This is a Dataset')
pizza = pd.read_excel('Data Model - Pizza Sales.xlsx')
st.write(pizza)


intr = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Introduction:</p>'

st.markdown(intr, unsafe_allow_html=True)

st.write('pizza, dish of Italian origin consisting of a flattened disk of bread dough topped with some combination of olive oil, oregano, tomato, olives, mozzarella or other cheese, and many other ingredients, baked quickly')


find = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Finding:</p>'

st.markdown(find, unsafe_allow_html=True)
st.write('This dataset shows that the number of requests is 48,620,000,000. And the average sum of the price is 16.821474. The lowest price of the group was 9.750000 and the highest price of the group was 83.000000. It also appears in the data set that the lowest order quantity was one and the highest four.')
