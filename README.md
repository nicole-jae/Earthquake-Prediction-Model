# Earthquake Predictions in Conterminous US

## Capstone Project

### By Nicole Jae Olandria

For this project I used the earthquake data from https://earthquake.usgs.gov/earthquakes/search/ in order to
create a model that predicts the likelihood of an earthquake occurring at a specific city.

### Data Details

For the data I used earthquakes with a magnitude of 2.5+ or higher from 1/1/2020 to 1/1/2025 to get a wide range
of data to use. I saved this file as 'quake data.csv'

### Quake Prediction Back

This backend part focused on cleaning the data and training the model. The data was cleaned to only show 
location and date information and then each earthquake was counted at that specific location. The model was
trained and then saved to be easier to load for the frontend portion.

### Quake Prediction Front

This frontend part is focused on the code that appears for streamlit. The three files that were saved from
the backend were loaded in. The app includes an input to put in a city and state as well as a date. If the 
location is present in the dataaset, a map would then appear showing that location as well as the prediction 
of the likelihood that an earthquake would happen at that date. It is also includes an input to check whether 
the location is present in the data as well as a list of all locations that are in the data to avoid errors.
