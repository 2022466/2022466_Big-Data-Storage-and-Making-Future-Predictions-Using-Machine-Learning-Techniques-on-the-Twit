import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Load Dataset
project = pd.read_csv("ProjectTweets.csv", encoding = 'latin', header=None) 

project = project.rename(columns={0: 'target', 1: 'ids', 2: 'date', 3: 'flag', 4: 'user', 5: 'text'})

# Create a Streamlit app
st.title('Word Cloud Dashboard')

# Sidebar for user input
user_input = st.sidebar.text_input("Enter a keyword:")
select_dataset = project[project['text'].str.contains(user_input, case=False)]


st.sidebar.write(f"Matching Results: {len(select_dataset)}")


wordcloud = WordCloud(width=800, height=400).generate(' '.join(select_dataset['text']))
st.image(wordcloud.to_array())


st.write(select_dataset)