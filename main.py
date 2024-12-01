import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
city = st.text_input("City: ")

days = st.slider("Forecast Days: ", min_value=1,max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select Data Type:", ["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} days in  {city.title()}:")


if city:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(city, days)


        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            #Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]


            col1, col2, col3, col4 = st.columns(4)

            quater = int(len(image_paths)* 0.25)
            half = int(len(image_paths)* 0.5)
            seventyfifth = int(len(image_paths)* 0.75)


            with col1:
                st.image(image_paths[0:quater], width=115)
            with col2:
                st.image(image_paths[quater:half], width=115)
            with col3:
                st.image(image_paths[half:seventyfifth], width=115)
            with col4:
                st.image(image_paths[seventyfifth:], width=115)
    except KeyError:
        st.write("This city doesn't exist!!!")



