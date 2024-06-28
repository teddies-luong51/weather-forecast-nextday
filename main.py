import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
kind = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{kind} for the next {days} days in {place}")

if place:
    try:
        filter_data = get_data(place, days)

        if kind == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filter_data]
            date_points = [dict["dt_txt"] for dict in filter_data]
            figure = px.line(x=date_points, y=temperatures, labels={"x":"Dates", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if kind == "Sky":
            rule = {"Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"image/snow.png", "Clear":"images/clear.png"}
            conditions = [dict["weather"][0]['main'] for dict in filter_data]
            image_condition = [rule[condition] for condition in conditions]
            st.image(image_condition, width=100)
    except KeyError:
        st.write("You should enter the right city name")