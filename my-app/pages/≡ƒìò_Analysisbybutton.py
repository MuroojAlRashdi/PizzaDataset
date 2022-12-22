import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.title('🍕pizza sales Application')
pizza = pd.read_excel('Data Model - Pizza Sales.xlsx')
st.write('The data for Pizza Category with  quantity')
st.write(pizza[['quantity','pizza_category']])

pizza.groupby('pizza_category')['quantity'].count().plot(kind='pie',autopct="%1.2f%%",explode=[0,0.5,0,1])

st.set_option('deprecation.showPyplotGlobalUse', False)
if st.button('show pie chart'):
  st.pyplot()
else:
  st.write('If you want to see a pie chert, click the button')
