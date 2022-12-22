
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
st.title('🍕pizza sales Application')
st.title('welcome to home page')

st.write('This is a Dataset')
pizza = pd.read_excel('Data Model - Pizza Sales.xlsx')
st.write(pizza)

st.sidebar.markdown("#The lollipop chart show total price and pizza category")
# creating an empty chart
fig, axes = plt.subplots()

# plotting using plt.stem
axes.stem(pizza['total_price'], pizza['pizza_category'],
		use_line_collection=True, basefmt='')
axes.set_ylim(0)

plt.title("total_price Vs pizza_id")
plt.xlabel("total_price")
plt.ylabel("pizza_category")
plt.xticks(pizza.total_price)
fig.set_figwidth(25)
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

