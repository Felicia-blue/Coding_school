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

mport streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
#import plotly.express as px

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")
user_name = st.sidebar.text_input("Enter your name", "Dr. Felicia Khoza")
num_points = st.sidebar.slider("Number of random points on map", 100, 2000, 1000)
theme_option = st.sidebar.selectbox("Choose a theme", ["Light", "Dark"])

# Apply theme if desired (this example just displays the choice)
st.sidebar.write(f"You selected the **{theme_option}** theme.")

# Title of the app
st.title("Bioinformatics Inc")

# Basic information
field = "Bioinformatics"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Resume")
st.write(f"**Name:** {user_name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")



# Sidebar input for number of random points
num_points = st.sidebar.slider("Number of random points", 100, 2000, 1000)

# Create random data centered around Cape Town based on the slider input
df = pd.DataFrame(
    np.random.randn(num_points, 2) / [50, 50] + [33.9249, 18.4241],
    columns=["lat", "lon"],
)

# Define Cape Town's exact location
cape_town = pd.DataFrame({"lat": [33.9249], "lon": [18.4241]})

# Create a Pydeck layer for the random points (blueish color)
layer_random = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[lon, lat]",
    get_color="[0, 100, 200, 160]",  # [R, G, B, Alpha] for random points
    get_radius=100,
    pickable=True,
)

# Create a Pydeck layer for Cape Town's exact location (bright red)
layer_ct = pdk.Layer(
    "ScatterplotLayer",
    data=cape_town,
    get_position="[lon, lat]",
    get_color="[255, 0, 0, 255]",  # Bright red color
    get_radius=200,
    pickable=True,
)

# Set the initial view state centered on Cape Town
view_state = pdk.ViewState(
    latitude=33.9249,
    longitude=18.4241,
    zoom=10,
    pitch=0,
)

# Create the deck with both layers
deck = pdk.Deck(
    layers=[layer_random, layer_ct],
    initial_view_state=view_state,
    tooltip={"text": "Location: {lat}, {lon}"}
)

# Display the map in Streamlit
st.pydeck_chart(deck)

# Add a color picker widget
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

# Add an example Plotly chart widget
#st.header("Example Plot")
#x = np.linspace(0, 10, 100)
#y = np.sin(x)
#fig = px.line(x=x, y=y, title="Sine Wave")
#st.plotly_chart(fig)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Filtering publications by a keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

    # Visualize publication trends if a 'Year' column exists
    st.header("Publication Trends")
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section with a button to reveal contact details
st.header("Contact Information")
if st.button("Show Contact Email"):
    email = "feliciakhoza2@gmail.com"
    st.write(f"You can reach {user_name} at {email}.")
else:
    st.write("Click the button to reveal contact information.")

 
