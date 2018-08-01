# coding: utf-8

# In[98]:


import pandas as pd
import numpy as np
import pycountry

aircrashdf = pd.read_csv("/home/drogon/Desktop/BI/aircrashes_raw.csv")

aircrashdf.isnull().sum()

del aircrashdf['Flight #']
del aircrashdf['cn/In']
del aircrashdf['Registration']
del aircrashdf['Summary']

print("length before dropping: ", len(aircrashdf.index))

aircrashdf = aircrashdf.dropna()

print("length after dropping: ", len(aircrashdf.index))

# find out the data types
aircrashdf.dtypes

# discretize time
for idx, val in enumerate(aircrashdf.Time):
    # print(idx, val)
    hour = int(val.split(":")[0])
    if hour in range(6, 13):
        # print ("Morning hour: ", hour)
        aircrashdf.iloc[idx, 1] = 'Morning'
    elif hour in range(13, 17):
        # print ("Afternoon hour: ", hour)
        aircrashdf.iloc[idx, 1] = 'Afternoon'
    elif hour in range(17, 21):
        # print ("Evening hour: ", hour)
        aircrashdf.iloc[idx, 1] = 'Evening'
    elif hour in range(21, 24) or hour in range(0, 6):
        # print ("Night hour: ", hour)
        aircrashdf.iloc[idx, 1] = 'Night'
    else:
        break

# list of all USA states
usa_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "DC", "Delaware",
              "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
              "Maine", "Maryland",
              "Massachusetts", "Michigan", "Minnesota", "Mississipi", "Missouri", "Montana", "Nebraska", "Nevada",
              "New Hampshire", "New Jersey",
              "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
              "Rhode Island", "South Carolina",
              "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
              "Wisconsin", "Wyoming"]

# get the list of all countries from pycountry
pycountries = []
for itera in pycountry.countries:
    pycountries.append(itera.name)

for idx, val in enumerate(aircrashdf.Location):
    location = val.split(",")
    country = location[len(location) - 1].strip()
    if country in pycountries:
        aircrashdf.iloc[idx, 2] = country
    elif country in usa_states:
        aircrashdf.iloc[idx, 2] = 'USA'
    else:
        aircrashdf.iloc[idx, 2] = 'Unknown'

print("Unknown: ", aircrashdf.Location.str.count("Unknown").sum())
print("USA: ", aircrashdf.Location.str.count("USA").sum())
# aircrashdf = aircrashdf[aircrashdf.Location != 'Unknown']

# tackling the Operator
for idx, val in enumerate(aircrashdf.Operator):
    if "Military" in val:
        aircrashdf.iloc[idx, 3] = "Military"
    else:
        aircrashdf.iloc[idx, 3] = "Civilian"

# tackling the type
for idx, val in enumerate(aircrashdf.Type):
    if "Aero Commander" in val:
        aircrashdf.iloc[idx, 5] = "Aero Commander"
    elif "Airbus" in val:
        aircrashdf.iloc[idx, 5] = "Airbus"
    elif "Antonov" in val:
        aircrashdf.iloc[idx, 5] = "Antonov"
    elif "Cessna" in val:
        aircrashdf.iloc[idx, 5] = "Cessna"
    elif "Avro" in val:
        aircrashdf.iloc[idx, 5] = "Avro"
    elif "Beech" in val:
        aircrashdf.iloc[idx, 5] = "Beech"
    elif "Boeing" in val:
        aircrashdf.iloc[idx, 5] = "Boeing"
    elif "Britten" in val:
        aircrashdf.iloc[idx, 5] = "Britten-Norman"
    elif "Convair" in val:
        aircrashdf.iloc[idx, 5] = "Convair"
    elif "Curtis" in val:
        aircrashdf.iloc[idx, 5] = "Curtis"
    elif "Havilland" in val:
        aircrashdf.iloc[idx, 5] = "de Havilland"
    elif "Douglas" in val:
        aircrashdf.iloc[idx, 5] = "Mcdonnel Douglas"
    elif "Fairchild" in val:
        aircrashdf.iloc[idx, 5] = "Fairchild"
    elif "Fokker" in val:
        aircrashdf.iloc[idx, 5] = "Fokker"
    elif "Ilyushin" in val:
        aircrashdf.iloc[idx, 5] = "Ilyushin"
    elif "Learjet" in val:
        aircrashdf.iloc[idx, 5] = "Learjet"
    elif "Lockheed" in val:
        aircrashdf.iloc[idx, 5] = "Lockheed"
    elif "Piper" in val:
        aircrashdf.iloc[idx, 5] = "Piper"
    elif "Zeppelin" in val:
        aircrashdf.iloc[idx, 5] = "Zeppelin"
    else:
        aircrashdf.iloc[idx, 5] = "Other"

# tackling the routes
aircrashdf['Source'] = aircrashdf.index
aircrashdf['Destination'] = aircrashdf.index

for idx, val in enumerate(aircrashdf.Route):
    if not val is False and '-' in val:
        route = val.split("-")
        source = route[0].strip()
        destination = route[len(route) - 1].strip()
        aircrashdf.iloc[idx, 9] = source
        aircrashdf.iloc[idx, 10] = destination
    elif not val is False and not '-' in val:
        aircrashdf.iloc[idx, 9] = val
        aircrashdf.iloc[idx, 10] = val

# # tackle source further
# for idx, val in enumerate(aircrashdf.Source):
#     if ',' in val:
#         source = val.split(",")
#         original = source[0].strip()
#         aircrashdf.iloc[idx, 9] = original
#
# #tackle destination further
# for idx, val in enumerate(aircrashdf.Destination):
#     if ',' in val:
#         destination = val.split(",")
#         original = destination[0].strip()
#         aircrashdf.iloc[idx,10] = original
#
# # drop route column from the dataframe
# del aircrashdf['Route']

aircrashdf.to_csv('/home/drogon/Desktop/BI/aircrashes_very_clean.csv')
# len(aircrashdf.index)
