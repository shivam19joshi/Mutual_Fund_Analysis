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

# 🎯 UI Title
st.title("📊 Mutual Fund Returns Explorer")

# 🔎 Select Category
categories = sorted(df['category'].unique())
selected_cat = st.selectbox("Select a Category", categories)

# Filter by Category
filtered_df = df[df['category'] == selected_cat]

# 🏢 Select AMC Name
amcs = sorted(filtered_df['AMC_name'].unique())
selected_amc = st.selectbox("Select an AMC", amcs)

# Filter by AMC
final_df = filtered_df[filtered_df['AMC_name'] == selected_amc]

# 📈 Select Return Period
return_period = st.radio("Select Return Period", ['return_1yr', 'return_3yr', 'return_5yr'], horizontal=True)

# 🔢 Number of Top Mutual Funds
top_n = st.slider("Top N Mutual Funds by Return", min_value=5, max_value=30, value=10)

# Sort & Trim Data
plot_df = final_df.sort_values(by=return_period, ascending=False).head(top_n)

# 📊 Plotting
st.subheader(f"Top {top_n} Mutual Funds by {return_period.replace('_', ' ').title()}")

fig, ax = plt.subplots(figsize=(12, 6))
barplot = sb.barplot(x='MutualFundName', y=return_period, data=plot_df, palette='coolwarm', ax=ax)
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# 📋 Data Table
st.subheader("📄 Filtered Mutual Funds Data")
st.dataframe(plot_df[['MutualFundName', return_period, 'category', 'AMC_name']])

# 📥 Download CSV
csv = plot_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_mutual_funds.csv',
    mime='text/csv',
)
