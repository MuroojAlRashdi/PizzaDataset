
import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
st.title('🍕pizza sales Application')


st.write('This is a Dataset')
pizza = pd.read_excel('Data Model - Pizza Sales.xlsx')
st.write(pizza)

pizzaname = st.select_slider("Slect your pizza name", pizza['pizza_name'].unique())
st.write(pizzaname)

mult = st.multiselect(
  'choose a chart',
  ['scatter','point','bar', 'line', 'area'])

  
if 'scatter' in mult:
    pl1 = alt.Chart(pizza[pizza['pizza_name']==pizzaname]).mark_circle().encode(
      x='total_price', y='quantity',
      tooltip=['order_id','pizza_id','total_price','quantity','unit_price','pizza_size','pizza_category','pizza_ingredients']
    ).interactive()
    st.altair_chart(pl1)

if 'point' in mult:
    pl5 = alt.Chart(pizza[pizza['pizza_name']==pizzaname]).mark_point().encode(
      x='total_price', y='quantity',
      tooltip=['order_id','pizza_id','total_price','quantity','unit_price','pizza_size','pizza_category','pizza_ingredients']
    ).interactive()
    st.altair_chart(pl5)

if 'bar' in mult:
    pl2 = alt.Chart(pizza[pizza['pizza_name']==pizzaname]).mark_bar().encode(
      x='total_price', y='quantity',
      tooltip=['order_id','pizza_id','total_price','quantity','unit_price','pizza_size','pizza_category','pizza_ingredients']
    ).interactive()
    st.altair_chart(pl2)

if 'line' in mult:
    pl3 = alt.Chart(pizza[pizza['pizza_name']==pizzaname]).mark_line().encode(
      x='total_price', y='quantity',
      tooltip=['order_id','pizza_id','total_price','quantity','unit_price','pizza_size','pizza_category','pizza_ingredients']
    ).interactive()
    st.altair_chart(pl3)

if 'area' in mult:
    pl4 = alt.Chart(pizza[pizza['pizza_name']==pizzaname]).mark_area().encode(
      x='total_price', y='quantity',
      tooltip=['order_id','pizza_id','total_price','quantity','unit_price','pizza_size','pizza_category','pizza_ingredients']
    ).interactive()
    st.altair_chart(pl4)
