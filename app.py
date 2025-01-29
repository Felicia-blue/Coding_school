# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import streamlit as st

#st.title("Streamlit is amazing!")
#st.title("hello Fesh")
#st.write("Lets create an app Feli...")


#number = st.slider("Pick a number", 1,200)
#st. write ("Pick a  {number}")

# My Plot of data

#import pandas as pd
#import plotly.express as px
#import streamlit as st

#st.title("Title heading")

#st.write("Hello, Streamlit!")

#st.header("Sample Data")

#data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
#st.write(data)

# Create a Plotly figure
#fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
#st.plotly_chart(fig)

#exampl of the app created on streamlit

import streamlit as st
import pandas as pd
import numpy as np


# Title of the app
st.title("Bioinformatics inc")

# Collect basic information
name = "Dr. Felicia Khoza"
field = "Bioinformatics"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Resume")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Create random data centered around Cape Town
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [33.9249, 18.4241],
    columns=["lat", "lon"],
)

# Mark Cape Town's exact location
cape_town = pd.DataFrame({"lat": [33.9249], "lon": [18.4241]})

# Combine random data with Cape Town location
df_combined = pd.concat([df, cape_town])

# Display map with Cape Town's location
st.map(df_combined)

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "feliciakhoza2@gmail.com"
st.write(f"You can reach {name} at {email}.")