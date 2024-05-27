# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(data)

# avg_temp = round(sum(temp_list) / len(temp_list), 2)
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)

# monday = data[data.day == "Monday"]
# monday_f = monday.temp * 9/5 + 32
# print(monday_f)
#
# data_dic = {
#     "Students" : ["Beatrix", "Eli", "Blythe"],
#     "Marks" : [97, 96, 95]
# }
# data = pandas.DataFrame(data_dic)
# data.to_csv("students_marks.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
Cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
Gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
#print(squirrel_data["Primary Fur Color"])

squirrel_summary = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count" : [Black, Cinnamon, Gray]
}
s_summary = pandas.DataFrame(squirrel_summary)
s_summary.to_csv("Summary Squirrel Data.csv")


