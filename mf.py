import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# 📁 Load dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/shivam19joshi/Mutual_Fund_Analysis/main/mutual_funds_india.csv"
    df = pd.read_csv(url)
    df.columns = df.columns.str.replace(" ", "")
    df = df.fillna(0)
    return df

# Load data
df = load_data()

# Streamlit UI
st.title("Mutual Fund 1-Year Returns Explorer")

# Dropdown for Category
categories = df['category'].unique()
selected_cat = st.selectbox("Select a Category", categories)

# Filter based on selected category
filtered_df = df[df['category'] == selected_cat]

# Dropdown for AMC Name
amcs = filtered_df['AMC_name'].unique()
selected_amc = st.selectbox("Select an AMC", amcs)

# Filter based on selected AMC
final_df = filtered_df[filtered_df['AMC_name'] == selected_amc]

# Plot
st.subheader("1-Year Returns of Mutual Funds")
plt.figure(figsize=(12, 6))
sb.barplot(x='MutualFundName', y='return_1yr', data=final_df, palette='ocean')
plt.xticks(rotation=90)
plt.tight_layout()

st.pyplot(plt)
