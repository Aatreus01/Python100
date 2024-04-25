#with open("..\\day25-csv\\weather_data.csv") as f:
##data = f.readlines()
##print(data)

#import csv

#with open("..\\day25-csv\\weather_data.csv") as f:
#data = csv.reader(f)
#temperatures = []
#for row in data:
#if row[1] != "temp":
#temperatures.append(int(row[1]))
#print(temperatures)

import pandas
'''
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
temp_list = data["temp"].to_list()
sum = 0
max_temp = data["temp"].max()
print(data[data.temp == max_temp])
'''

data = pandas.read_csv("..\\day25-csv\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")