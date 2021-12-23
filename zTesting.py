import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random as rd
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean = st.mean(data)
sd = st.stdev(data)
print("mean of the entire data set is ", mean)
print("standard deviation of the entire data set is " , sd)
 
def random_setOf_data():
    dataSet = []
    for i in range(0,100):
        randomIndex = rd.randint(0,len(data)-1)
        dataSet.append(data[randomIndex])
    mean = st.mean(dataSet)
    return mean

meanList = []
for i in range(0,1000):
    meanOf_Data_Set = random_setOf_data()
    meanList.append(meanOf_Data_Set)
samplingMean = st.mean(meanList)
sd_Ofsampling = st.stdev(meanList)
print("mean of sampling distribution is ",samplingMean)
print("standard deviation of sampling distribution  is ",sd_Ofsampling)

first_sd_start , first_sd_end = mean-sd_Ofsampling ,mean+sd_Ofsampling
second_sd_start , second_sd_end = mean-(2*sd_Ofsampling) ,mean+(2*sd_Ofsampling)
third_sd_start , third_sd_end = mean-(3*sd_Ofsampling) ,mean+(3*sd_Ofsampling)
'''
fig = ff.create_distplot([meanList],["studentMarks"],show_hist= False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.2],mode = "lines",name = "First sd start"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.2],mode = "lines",name = "First sd end"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.2],mode = "lines",name = "second sd start"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.2],mode = "lines",name = "second sd end"))
fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.2],mode = "lines",name = "third sd start"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.2],mode = "lines",name = "third sd end"))

fig.show()
'''
df1 = pd.read_csv("medium_data.csv")
data1 = df1["claps"].tolist()
meanOfSample1 = st.mean(data1)
print("mean of sample one is" , meanOfSample1)
'''
fig = ff.create_distplot([meanList],["data1"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode = "lines" ,name ="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample1,meanOfSample1],y=[0,0.2],mode="lines",name = "Mean of sample one"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.2],mode = "lines",name = "First sd end"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.2],mode = "lines",name = "Second sd end"))
fig.show()
'''


df2 = pd.read_csv("medium_data.csv")
data2 = df2["image"].tolist()
meanOfSample2 = st.mean(data2)
print("mean of sample two is" , meanOfSample2)
'''
fig = ff.create_distplot([meanList],["data2"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode = "lines", name ="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample2,meanOfSample2],y=[0,0.2],mode ="lines", name ="Mean of sample two"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.2],mode="lines",name ="First sd end"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.2],mode="lines",name = "Second sd end"))
fig.show()
'''

df3 = pd.read_csv("medium_data.csv")
data3=df3["subtitle"].tolist()
meanOfSample3 = st.mean(data3)
print("mean of sample three is" , meanOfSample3)

fig = ff.create_distplot([meanList],["data3"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode = "lines", name ="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,0.2],mode ="lines", name ="Mean of sample three"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.2],mode="lines",name ="First sd end"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.2],mode="lines",name = "Second sd end"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.2],mode="lines",name="Third sd end"))
fig.show()

zScore = (mean-meanOfSample3)/sd
print("Z score data3 set is ",zScore)

df4 = pd.read_csv("medium_data.csv")
data4=df4["publication"].tolist()
meanOfSample3 = st.mean(data3)
print("mean of sample four is" , meanOfSample3)

fig = ff.create_distplot([meanList],["data3"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode = "lines", name ="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,0.2],mode ="lines", name ="Mean of sample three"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.2],mode="lines",name ="First sd end"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.2],mode="lines",name = "Second sd end"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.2],mode="lines",name="Third sd end"))
fig.show()

zScore = (mean-meanOfSample3)/sd
print("Z score data3 set is ",zScore)