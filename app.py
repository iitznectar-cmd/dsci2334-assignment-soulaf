import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Qahwa Corner Sales", page_icon="☕")
st.title("☕ Qahwa Corner Sales Dashboard")
st.write("Explore branch sales and product revenue across Qahwa Corner locations.")


@st.cache_data
def load_data():
    df = pd.read_csv("cafe_sales.csv")
    df.columns = df.columns.str.strip()
    return df


df = load_data()


branches = ["All"] + sorted(df["branch"].unique().tolist())
selected_branch = st.selectbox("Select Branch", branches)

view = df
if selected_branch != "All":
    view = view[view["branch"] == selected_branch]

total_revenue = view["total_sar"].sum()
st.metric("Total Revenue", f"{total_revenue:,.2f} SAR")


product_rev = view.groupby("product")["total_sar"].sum()

fig, ax = plt.subplots()
ax.bar(product_rev.index, product_rev.values)
ax.set_xlabel("Product")
ax.set_ylabel("Revenue (SAR)")
ax.set_title("Revenue by Product")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)
st.metric(label="Total Revenue", value=f"{total_revenue:,.2f} SAR")


product_rev = filtered_df.groupby("product")["total_sar"].sum()
st.bar_chart(product_rev)
