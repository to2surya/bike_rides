import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Load Main Data 
bike_df = pd.read_csv("../dashboard/main_data.csv")

# Reindex date column
datetime_columns = ["date"]
bike_df.sort_values(by="date", inplace=True)
bike_df.reset_index(inplace=True)

# Change data type to datetime
for column in datetime_columns:
    bike_df[column] = pd.to_datetime(bike_df[column])
    
min_date = bike_df["date"].min()
max_date = bike_df["date"].max()

# Create Sidebar
with st.sidebar:
    # Load Image
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Get start_date & end_date from date_input
    start_date, end_date = st.date_input(
        label='Date Range',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
# Create Data Filter Range
main_df = bike_df[(bike_df["date"] >= str(start_date)) & 
                (bike_df["date"] <= str(end_date))]

# Create Header Text
st.header(':sparkles: Bike Riding Collection Dashboard :sparkles:')

# Question Business 1
st.subheader('1. Total of bikeshare rides by Month')

# Visualize data
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x='month', y='counts', data=main_df, hue='year', ax=ax, palette='bright')
ax.set_xlabel("Month")
ax.set_ylabel("Total Rides")
ax.set_title("Total of bikeshare rides per Month")
st.pyplot(fig)

# Question Business 2
st.subheader('2. Total of bikeshare rides by Season')

# Visualize data
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x='season', y='counts', data=main_df, hue='year', ax=ax, palette='pastel')
ax.set_xlabel("Season")
ax.set_ylabel("Total Rides")
ax.set_title("Total of bikeshare rides per Season")
st.pyplot(fig)

# Question Business 3
st.subheader('3. Total of bikeshare rides by Weather')

# Visualize data
fig, ax = plt.subplots(figsize=(10,6))
sns.boxplot(x='weather', y='counts', data=main_df, hue='weather', ax=ax, palette='colorblind')
ax.set_xlabel("Weather")
ax.set_ylabel("Total Rides")
ax.set_title("The effect of Weather on the daily bikeshare rides")
st.pyplot(fig)

# Question Business 4
st.subheader('4. Clusters of bikeshare rides by season and temperature')

# Visualize data
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(x='temp', y='counts', data=main_df, hue='season', ax=ax, palette='muted')
ax.set_xlabel("Temperature ($^\\circ$C)")
ax.set_ylabel("Total Rides")
ax.set_title("Clusters of bikeshare rides by season and temperature")
st.pyplot(fig)