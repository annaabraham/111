import csv
import pandas as pd
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go
import random

df=pd.read_csv("studentMarks.csv")
marks=df["Math_score"].tolist()

def randomSetOfData(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(marks)-1)
        value=marks[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return(mean)

def showFig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],['average'],show_hist=False)
    fig.show()

meanList=[]
for i in range(0,1000):

    setOfMeans=randomSetOfData(100)
    meanList.append(setOfMeans)
    showFig(meanList)

mean=statistics.mean(meanList)
meanListStdev=statistics.stdev(meanList)
populationMean=statistics.mean(marks)
populationStdev=statistics.stdev(marks)
print(mean)
print(meanListStdev)
print(populationMean)
print(populationStdev)
