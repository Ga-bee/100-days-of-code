##EX01


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
splited = sentence.split()
result = {word:len(word) for word in splited}

# result = {for word in sentence result= word:en(word)}
# Write your code below:

# print(splited)

print(result)

##EX02

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {key:(value*9/5) + 32 for key, value in weather_c.items()}

print(weather_f)
