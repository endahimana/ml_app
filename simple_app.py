# simple streamlit app
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Simple Streamlit App")

# Create a sample random DataFrame
np.random.seed(42)
data = pd.DataFrame({
    "Region": np.random.choice(['North', 'South', 'East', 'West'], size=100),
    "Product": np.random.choice(['Apple', 'Banana', 'Mango', 'Orange'], size=100),
    "Sales": np.random.randint(500, 1000, size=100)
})

# Filter by Region
region = st.sidebar.selectbox("Select Region", options=data['Region'].unique())
product = st.sidebar.multiselect("Select Product", options=data['Product'].unique())

## filter data based on selected region
filtered_data = data[(data['Region'] == region) & (data['Product'].isin(product))]

## Subheader for KPIs of total sales, average sales, and number of transactions
st.subheader(f"Key Performance Indicators for {region} Region and {product} Product")
c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", f"${filtered_data['Sales'].sum():,.0f}")
c2.metric("Average Sales", f"${filtered_data['Sales'].mean():,.2f}")
c3.metric("Number of Transactions", f"{filtered_data.shape[0]}")


## subheader for sales filtered table
st.subheader(f"Sales Data for {region} Region and {product} Product")
st.dataframe(filtered_data)

## subheader for sales bar chart total sales by product
st.subheader(f"Total Sales by Product in {region} Region")
sales_by_product = filtered_data.groupby('Product')['Sales'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(sales_by_product['Product'], sales_by_product['Sales'], color='skyblue')
ax.set_xlabel('Product')
ax.set_ylabel('Total Sales')
ax.set_title('Total Sales by Product')
st.pyplot(fig)