import streamlit as st
import plotly.express as px
from backend import get_data,get_dataa
import geopandas as gpd
import pandas as pd
from collections import Counter
from datetime import datetime


# Add title, text input, slider, select box, and sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "streamlit-weather-forecast-master/images/clear.png", "Clouds": "streamlit-weather-forecast-master/images/cloud.png",
                      "Rain": "streamlit-weather-forecast-master/images/rain.png", "Snow": "streamlit-weather-forecast-master/images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115, caption=dates)

    except KeyError:
        st.write("That place does not exist.")

l= [                                                                                                   
"	Abadou",                                                                                                   
"	Abaynou",                                                                                                   
"	Abbou Lakhal",                                                                                                   
"	Abdelghaya Souahel",                                                                                                   
"	Abteh",                                                                                                   
"	Adaghas",                                                                                                   
"	Adar",                                                                                                   
"	Adassil",                                                                                                   
"	Aday",                                                                                                   
"	Adis",                                                                                                   
"	Adrej",                                                                                                   
"	Afalla Issen",                                                                                                   
"	Afella Ighir",                                                                                                   
"	Afella N'Dra",                                                                                                   
"	Aferkat"]                                                                     
frames = []
for place in l:
    if place:
        # Get the temperature/sky data
        try:
            data=get_dataa(place,5)
            if data["message"] !=  'city not found':
                input("ça existe")
                t=data["list"]
                temp=[]
                lag=[]
                prss=[]
                humd=[]
                wind=[]
                cl=[]
                for dic in t:
                    r=dic["main"]
                    pp=dic['clouds']
                    ppp=dic['weather']
                    e=dic['wind']
                    ee=dic['main']
                    


                    y=dic["dt_txt"]
                    lag.append(y)

                    o=dic["main"]["temp"]
                    temp.append(o)

                    p=dic["main"]["pressure"]
                    prss.append(p)

                    h=dic["main"]['humidity']
                    humd.append(h)

                    w=dic['wind']['speed']
                    wind.append(w)
                    cc=dic['weather'][0]['description']
                    cl.append(cc)
                input("i get the data")
                ################"
                # from collections import Counter
                def count_occurrences(dates):
                    # Convert the input strings to datetime objects
                    datetime_objects = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in dates]

                    # Extract the date portion from each datetime object
                    date_strings = [datetime_object.strftime('%Y-%m-%d') for datetime_object in datetime_objects]

                    # Use Counter to count occurrences of each date
                    occurrences = Counter(date_strings)

                    # Convert the Counter object to a list of tuples (date, count)
                    result = list(occurrences.items())

                    return result
                input("fonction de compter")
                # Example usage
                input_dates =lag
                output = count_occurrences(input_dates)

                def calculate_mean_consecutive(groups, values):
                    result = []
                    start = 0

                    for group_size in groups:
                        end = start + group_size
                        group_values = values[start:end]
                        mean_value = sum(group_values) / len(group_values)
                        result.append(mean_value)
                        start = end

                    return result
                def calculate_mean_consecutivee(groups, values):
                    result = []
                    start = 0

                    for group_size in groups:
                        end = start + group_size
                        group_values = values[start:end]
                        mean_value = group_values[1]
                        result.append(mean_value)
                        start = end

                    return result
                # Example usage:
                groups = [output[i][1] for i in range(len(output))]

                result = calculate_mean_consecutive(groups, temp)
                press=calculate_mean_consecutive(groups, prss)
                hmudi=calculate_mean_consecutive(groups, humd)
                windd=calculate_mean_consecutive(groups, wind)
                
            ##########

                # Initialize an empty GeoDataFrame
                gdf = gpd.GeoDataFrame(columns=['city_name', 'lat', 'lon','popu', 
                                                'temp_0', 'temp_1', 'temp_2', 'temp_3', 'temp_4', 'temp_5',
                                                'hmudi_0', 'hmudi_1', 'hmudi_2', 'hmudi_3', 'hmudi_4', 'hmudi_5',
                                                'wind_0', 'wind_1', 'wind_2', 'wind_3', 'wind_4', 'wind_5',
                                                
                                                'pr_0', 'pr_1', 'pr_2', 'pr_3', 'pr_4', 'pr_5',
                                                ])

                # Sample data (replace this with your actual data)

                dataa = [
                    {
                        'city_name': data["city"]['name'],
                        'lat': data["city"]['coord']['lat'],
                        'lon': data["city"]['coord']['lon'],
                        'popu': data["city"]['population'],
                        'temp_0': result[0],
                        'temp_1': result[1],
                        'temp_2': result[2],
                        'temp_3': result[3],
                        'temp_4': result[4],
                        'temp_5': result[5],
                        'hmudi_0': hmudi[0],
                        'hmudi_1': hmudi[1],
                        'hmudi_2': hmudi[2],
                        'hmudi_3': hmudi[3],
                        'hmudi_4': hmudi[4],
                        'hmudi_5': hmudi[5],
                        'wind_0': windd[0],
                        'wind_1': windd[1],
                        'wind_2': windd[2],
                        'wind_3': windd[3],
                        'wind_4': windd[4],
                        'wind_5': windd[5],
                        
                        'pr_0': press[0],
                        'pr_1': press[1],
                        'pr_2': press[2],
                        'pr_3': press[3],
                        'pr_4': press[4],
                        'pr_5': press[5],
                    }
                ]
            
            # Add rows to the GeoDataFrame
                for row in dataa:
                    geometry = gpd.points_from_xy([row['lon']], [row['lat']])
                    row_df = pd.DataFrame([row], columns=gdf.columns)
                    row_gdf = gpd.GeoDataFrame(row_df, geometry=geometry)
                    frames.append(row_gdf)
                    gdf = pd.concat(frames, ignore_index=True)
            # Print the final GeoDataFrame
            
                    
        except KeyError:
            print(f"That place ({place}) does not exist.")
            continue
print(gdf)

