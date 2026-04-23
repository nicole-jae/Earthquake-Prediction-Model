#Nicole Jae Olandria

import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_resources():
    model = joblib.load('logistic_regression_model.pk1')
    le = joblib.load('label_encoder.pk1')
    data_cleaned = pd.read_csv('cleaned_quake_data.csv')
    return model, le, data_cleaned

model, le, data_cleaned = load_resources()

st.set_page_config(layout="wide")
st.title("Earthquake Prediction Application")

st.sidebar.header("Input Parameters")

location_input = st.sidebar.text_input("Enter a city and state (e.g., 'Pecos, Texas'):")
date_input = st.sidebar.date_input("Select a date:")

if st.sidebar.button("Predict & Map"):
    if location_input and date_input:
        try:
            user_date = pd.to_datetime(date_input)
            user_month = user_date.month
            user_day = user_date.day
            user_day_of_week = user_date.dayofweek


            try:
                user_location_encoded = le.transform([location_input])[0]

                new_data = pd.DataFrame({
                    'month': [user_month],
                    'day': [user_day],
                    'day_of_week': [user_day_of_week],
                    'location_encoded': [user_location_encoded]
                })

                probability = model.predict_proba(new_data)[:, 1][0]

                st.subheader(f"Prediction for {location_input} on {date_input}:")
                st.write(f"Probability of earthquake occurring: **{probability:.4f}**")

                # --- Streamlit Native Map Display ---
                location_coords = data_cleaned[data_cleaned['place'] == location_input][['latitude', 'longitude']]
                if not location_coords.empty:
                    st.success("Reached map display block!")
                    input_lat = location_coords['latitude'].mean()
                    input_lon = location_coords['longitude'].mean()

                    st.markdown("### Interactive Map:")

                    # Create a DataFrame for st.map
                    map_df = pd.DataFrame({
                        'latitude': [input_lat],
                        'longitude': [input_lon]
                    })

                    st.map(map_df, zoom=8)

                else:
                    st.warning(f"Could not find coordinates for location '{location_input}' in the dataset to display on map.")

            except ValueError:
                st.error(f"'{location_input}' is not found in the trained locations. Please choose a known location.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
            print(f"DEBUG: General Error: {e}") # Debug terminal print

    else:
        st.warning("Please enter both a location and a date to get a prediction.")
        print(f"DEBUG: Missing location or date input. Location: {location_input}, Date: {date_input}") # Debug terminal print

        st.sidebar.markdown("--- ")
st.sidebar.header("Available Locations")

search_location = st.sidebar.text_input("Check if a location is available:")
if st.sidebar.button("Check Location"):
    if search_location:
        all_locations = data_cleaned['place'].unique()
        if search_location in all_locations:
            st.sidebar.success(f"'{search_location}' is found in the list of available locations.")
        else:
            st.sidebar.error(f"'{search_location}' is NOT found in the list of available locations.")
    else:
        st.sidebar.warning("Please enter a location to check.")

if st.sidebar.button("Show all available locations"):
    all_locations = data_cleaned['place'].unique().tolist()
    st.sidebar.write("**List of all locations in the dataset:**")
    for loc in all_locations:
        st.sidebar.write(loc)