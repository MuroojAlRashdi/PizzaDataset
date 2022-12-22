
import pandas as pd
import streamlit as st
import altair as alt
pizza = pd.read_excel('Data Model - Pizza Sales.xlsx')
st.title('🍕pizza Application')


pizzaname = st.selectbox("Select your Pizaa",pizza['pizza_name'].unique())

st.write(pizzaname)
plot_type = st.radio("Select the plot type",['scatter','line'])
if plot_type == 'scatter':

 pl = alt.Chart(pizza).mark_circle().encode(

    x = 'order_id',

    y = 'unit_price',

    tooltip = ['order_id','unit_price']

).interactive()

else:

   pl = alt.Chart(pizza).mark_line().encode(

    x = 'order_id',

    y = 'unit_price',

    tooltip = ['order_id','unit_price']

).interactive()

st.altair_chart(pl)
