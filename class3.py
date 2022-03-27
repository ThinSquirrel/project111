import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import random
import statistics

df = pd.read_csv("data2.csv")

data = df["reading_time"].tolist()

def RandSet(counter):

    dataSet = []

    for i in range(0,counter):

        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean



meanList = []

for i in range(0,1000):

    setOfMeans = RandSet(100)
    meanList.append(setOfMeans)

mean = statistics.mean(meanList)

print("Mean of sampling distribution is: ",mean)

graph = ff.create_distplot([meanList],["Reading Time"],show_hist = False)
graph.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.20],mode = "lines", name = "MEAN"))
graph.show()