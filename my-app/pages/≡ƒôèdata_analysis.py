
import pandas as pd
import altair as alt
import streamlit as st
st.title('🍕pizza sales Application')
pizza = pd.read_excel('Data Model - Pizza Sales.xlsx')

st.sidebar.markdown("#1️⃣mark_line")
st.sidebar.markdown("#2️⃣mark_bar")
st.sidebar.markdown("#3️⃣mark_circle")


st.write('Line marker is a line that is drawn on chart plot and bound to some value on an axis. In this example, x axis is quantity and y axis is pizza category. we have only the 100 head of the dataset.')

pl =alt.Chart(pizza.head(100)).mark_line().encode(

    x = 'total_price',

    y = 'quantity',
    color='pizza_category',

    tooltip = ['order_details_id','total_price']

).interactive()
st.altair_chart(pl, use_container_width=True)


st.write('A bar chart or bar graph is a chart or graph that presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent. In this example x axis is pizza siza and y axis is order id .')
pl2 =alt.Chart(pizza.head(500)).mark_bar().encode(

    x = 'pizza_size',

    y = 'order_id',
    size='order_details_id',
    color='pizza_category',


    tooltip = ['order_details_id','pizza_size','order_id','pizza_category']

).interactive()
st.altair_chart(pl2,use_container_width=True)

st.write('show circle Chart')
pl2 =alt.Chart(pizza.head(1000)).mark_circle().encode(

    x = 'order_id',

    y = 'total_price',
    size='order_details_id',
    color='pizza_category',


    tooltip = ['order_details_id','order_id','total_price','pizza_category']

).interactive()
st.altair_chart(pl2, use_container_width=True)
