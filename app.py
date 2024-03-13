import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setting up OpenAI API key
openai_api_key = st.sidebar.text_input("OpenAI API Key", key="chatbot_api_key", type="password")


# Function to load CSV data
def load_data(filename='scraped_products.csv'):
    return pd.read_csv(filename)

# Attempt to convert 'Product Price' to float
def process_data(df):
    try:
        df['Product Price'] = df['Product Price'].str.replace('[^\d.]', '', regex=True).astype(float)
    except Exception as e:
        st.write(f"Error converting Product Price to numeric: {e}")
    return df

# Initialize chat session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# UI for Chatbot
st.title("💬 H&M Color Trends")

df = load_data()
df = process_data(df)

# Display data and visualizations in tabs
tab1, tab2 = st.tabs(["HM ColorTrends Chatbot", "HM Product info Visualizations"])

with tab1:
    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.success(msg["content"])
        else:
            st.info(msg["content"])

    user_input = st.text_input("Ask about our products:")

    if user_input:
        if not openai_api_key:
            st.warning("Please add your OpenAI API key to continue.")
            st.stop()

        openai.api_key = openai_api_key
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages + [{"role": "user", "content": user_input}]
            )
            msg = response.choices[0].message['content']
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.success(msg)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

with tab2:
    st.header("H&M Price Tracking")
    st.dataframe(df)  # Display data frame
    
    # Price Distribution Plot
    if 'Product Price' in df.columns:
        st.subheader("Product Price Distribution")
        fig, ax = plt.subplots()
        sns.kdeplot(data=df, x='Product Price', ax=ax)
        ax.set_title('Price Distribution')
        st.pyplot(fig)

    # Product Colors Pie Chart
    if 'Product Colors' in df.columns:
        st.subheader("Detailed Product Color Distribution")
        color_list = df['Product Colors'].str.split(',').explode().str.strip().value_counts()
        top_colors = color_list[:10]  # Top 10 colors
        fig, ax = plt.subplots()
        ax.pie(top_colors, labels=top_colors.index, autopct='%1.1f%%', startangle=140)
        ax.set_title('Top 10 Color Distribution')
        st.pyplot(fig)
