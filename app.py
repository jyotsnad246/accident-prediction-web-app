
import streamlit as st
import pandas as pd
#import pickle
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Get the directory path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative image path
image_path = os.path.join(current_dir, "images", "logo.png")

# Open the image
image = Image.open(image_path)


# Function to display the UI
def main():
    st.set_page_config(page_title="DPS AI", layout="wide")

    # App header
    st.title("DPS AI Challenge : Prediction of Accidents using Time Series Forecasting")

    st.markdown("""
                The app forecasts the number of accidents in a month based on the **“Monatszahlen Verkehrsunfälle”** Dataset from the München Open Data Portal.  
            """)
    st.write("[Link to the Dataset](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7)")

    st.markdown("---")

    # Sidebar for input values

    st.sidebar.image(image)
    st.sidebar.title("Enter the input values")
    options_for_category = st.sidebar.selectbox("Category", ("Alkoholunfälle", "Fluchtunfälle", "Verkehrsunfälle"))
    options_for_accident = st.sidebar.selectbox("Accident Type", ("insgesamt", "mit Personenschäden", "Verletzte und Getötete"))
    year = st.sidebar.number_input("Year", value=2021)
    options_for_month = st.sidebar.selectbox("Month", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    #st.sidebar.markdown("---")

    # Formatting input values
    en_cat = 2
    if options_for_category == 'Alkoholunfälle':
        en_cat = 0
    elif options_for_category == 'Fluchtunfälle':
        en_cat = 1

    en_type = 2
    if options_for_accident == 'insgesamt':
        en_type = 0
    elif options_for_accident == 'mit Personenschäden':
        en_type = 1

    # Create input data
    input_data = [[en_cat, en_type, int(year), int(options_for_month)]]
    input_data = np.array(input_data)

    #model_path = os.path.join(current_dir, "models", "mymodel.pkl")
    model_path = os.path.join(current_dir, "models", "mymodel.h5")
    # Loading the model
    #with open(model_path, 'rb') as f:
    #    model = pickle.load(f)
    
    model = tf.keras.models.load_model(model_path)

    # Prediction section
    if st.sidebar.button("Forecast"):
        prediction = model.predict(input_data)
        st.success('The forecasted number of accidents is: **{}**'.format(int(prediction[0])))
        st.write("This result is generated using a GRU Netural Network Model")
        st.sidebar.markdown("---")

    # Display Future Forecast Trends
    st.subheader("Future Forecast of Total Accidents - Generated Using Prophet")
    if en_cat == 0:
        st.write("For Alkoholunfälle")
        st.image(Image.open('images/prophetAlkoholunfälle.png'))
    elif en_cat == 1:
        st.write("For Fluchtunfälle")
        st.image(Image.open('images/prophetFluchtunfälle.png'))
    else:
        st.write("For Verkehrsunfälle")
        st.image(Image.open('images/prophetVerkehrsunfälle.png'))

    
    st.write("[GitHub Code Link](https://github.com/jyotsnad246/accident-prediction-web-app)")


if __name__ == '__main__':
    main()

    st.markdown("---")