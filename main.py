import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random
import statistics

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("Mean Of The Data : ", mean)
print("Median Of The Data : ", median)
print("Mode Of The Data : ", mode)
print("Standard Deviation : ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * std_deviation), mean + (2 * std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3 * std_deviation), mean + (3 * std_deviation)

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]

list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]

list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% Of Data Lies Within 1 Standard Deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% Of Data Lies Within 2 Standard Deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% Of Data Lies Within 3 Standard Deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))

fig = ff.create_distplot([data], ["Reading Scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "Standard Deviation 2"))
fig.show()