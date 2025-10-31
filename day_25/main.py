import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
#
# print(type(data))
# print(data)
#
# print(data["temp"])
#
# data_dict = data.to_dict()
#
# print(data_dict)

# def get_average_temp():
#     return sum(data["temp"]) / len(data["temp"])
#
# average = get_average_temp()
#
# print(get_average_temp())
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition == data["condition"])
#
# print(data.loc[[0], ["day", "temp", "condition"]])
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
#
# def celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32
#
# print(celsius_to_fahrenheit(monday.temp))
#
# student_data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_frame = pandas.DataFrame(student_data_dict)
#
# data_frame.to_csv(path_or_buf="student_grades.csv", sep=",", index=False)


data_frame = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data_frame[data_frame["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data_frame[data_frame["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data_frame[data_frame["Primary Fur Color"] == "Black"])

squirrels_count_by_colors = {

    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]

}


squirrel_count_data_frame = pandas.DataFrame(squirrels_count_by_colors)

squirrel_count_data_frame.to_csv("squirrel_count.csv")


