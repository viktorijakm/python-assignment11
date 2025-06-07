import streamlit as st  # Importing the Streamlit library

# Basic text elements
st.title("My First Streamlit App")  # Adds a big title at the top of the app
st.header("Section 1")  # Adds a section header — good for breaking content into parts
st.subheader("Header")  # Slightly smaller than header — useful for structure
st.subheader("Subheader")  # Another level down — keeps things organized
st.text("Simple text")  # Displays plain, unformatted text — like a basic message
st.markdown("**Bold** and *italic* text")  # Markdown lets you add simple formatting like bold and italics

# Display data
st.write("Automatic data display")  # Streamlit's flexible method — handles strings, numbers, dataframes, and more
st.code("print('Hello World')", language='python')  # Nicely formats code blocks with syntax highlighting
st.latex(r"\int_{a}^{b} x^2 dx")  # Renders LaTeX math formulas — great for equations

# Section 2: Interactive Inputs
st.header("Section 2")  # A new section to group interactive input components

# Text input
name = st.text_input("Enter your name", "John Doe")
description = st.text_area("Description", "Write something...")

# Numeric input
age = st.number_input("Age", min_value=0, max_value=120, value=25)
score = st.slider("Score", 0, 100, 50)

# Selection widgets
option = st.selectbox("Choose an option", ["A", "B", "C"])
options = st.multiselect("Multiple options", ["X", "Y", "Z"])

# Date and time pickers
date = st.date_input("Select date")
time = st.time_input("Select time")

# Button interaction
if st.button("Click me"):
    st.write("Button clicked!")

# Checkbox toggle
if st.checkbox("Show/Hide"):
    st.write("Visible content")
