
import altair as alt
from vega_datasets import data
import streamlit as st
import pandas as pd
pizza = pd.read_excel('Data Model - Pizza Sales.xlsx')
st.title('🍕pizza sales Application')
base = alt.Chart(pizza.head(500)).properties(width=550)

line = base.mark_line().encode(

    x='order_date',

    y='unit_price',

    color='pizza_category'

)


rule = base.mark_rule().encode(

    y='average(unit_price)',

    color='pizza_category',

    size=alt.value(2)

)

st.write(line + rule)

st.write("This is a Line Chart with Layered Aggregates. This example shows how to make a multi-series line chart of the unit price of pizza category chicken, classic, supreme and veggie by order date, along with a layered rule showing the average values.")


filter_data = pizza[pizza['order_date'] >='2015-06-01'].set_index("order_date")
st.markdown("This bar chart shows the dates of pizza orders from June 1, 2015, with the name of each pizza order")
# bar chart 
st.bar_chart(filter_data[['pizza_name']])
