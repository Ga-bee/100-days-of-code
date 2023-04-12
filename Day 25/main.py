import pandas as pd

# df = pd.read_csv('weather_data.csv')
# data_dict = df.to_dict()
# avg_temp = df['temp'].max()
#print(avg_temp)


# print(data_dict)

# Get data in row
# print(df[df['temp'] == df['temp'].max()], end = '\n')
# print('')
# print('')
# print(df[df['condition'] == 'Rain'])


# monday = df[df['day'] == 'Monday']
# monday_temp = monday.temp
# monday_fahrenheit = monday_temp * 9/5 + 32
# print(monday_fahrenheit)

# # Create a Dataframe from scratch

# data_dict = {
#     "students" : ["Amy", "James" , "Angela"],
#     "scores" : [76,56,65]
# }

# data = pandas.DataFrame(data_dict)

# print(data)

squirtle_data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey =  len(squirtle_data[squirtle_data["Primary Fur Color"] == "Gray"])
black =  len(squirtle_data[squirtle_data["Primary Fur Color"] == "Black"])
cinnamon =  len(squirtle_data[squirtle_data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinamon"],
    "Count": [grey, black, cinnamon ]
}

sq_count = pd.DataFrame(data_dict)

print(sq_count)
#df = filtered_data.groupby(['Primary Fur Color']).count()

#adat = df[df['Primary Fur Color'], ['Count']]
# print(filtered_data)

#print(df)
