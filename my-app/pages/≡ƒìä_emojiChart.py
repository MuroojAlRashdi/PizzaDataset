
import altair as alt

import pandas as pd

import streamlit as st

st.title('🍕pizza sales Application')

find = '<p style="font-family:Courier; color:Blue; font-size: 20px;">📊 analysis by emoji Chart:</p>'

st.markdown(find, unsafe_allow_html=True)


pizza = pd.DataFrame([

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Mexicana Pizza', 'veg': 'Hot Pepper'},

    ])




pizza2 = pd.DataFrame([

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'cheese'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Mushroom'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

      {'pizza_name': 'The Hawaiian Pizza', 'veg': 'Hot Pepper'},

    ])




p = alt.Chart(pizza).mark_text(size=45, baseline='middle').encode(

    alt.X('x:O', axis=None),

    alt.Y('veg:N', axis=None),

    alt.Row('pizza_name', header=alt.Header(title='The Mexicana Pizza')),

    alt.Text('emoji:N')

).transform_calculate(

    emoji="{'cheese': '🧀', 'Mushroom': '🍄', 'Hot Pepper': '🌶️'}[datum.veg]"

).transform_window(

    x='rank()',

    groupby=['pizza_name', 'veg']

).properties(width=550, height=200)




p2 = alt.Chart(pizza2).mark_text(size=45, baseline='middle').encode(

    alt.X('x:O', axis=None),

    alt.Y('veg:N', axis=None),

    alt.Row('pizza_name', header=alt.Header(title='The Hawaiian Pizza')),

    alt.Text('emoji:N')

).transform_calculate(

    emoji="{'cheese': '🧀', 'Mushroom': '🍄', 'Hot Pepper': '🌶️'}[datum.veg]"

).transform_window(

    x='rank()',

    groupby=['pizza_name', 'veg']

).properties(width=550, height=200)




Mexicana = st.checkbox('The Mexicana Pizza')

Hawaiian  = st.checkbox('The Hawaiian Pizza')




if Mexicana:

    st.write(p)

if Hawaiian:

    st.write(p2)
