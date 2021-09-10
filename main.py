# WAP sampling distribution for any population is a normal distribution therefore identify the relationship between the mean and standard deviation of a population and of a sample distribution

import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import pandas as pd 
import csv
import random 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

#population_mean = statistics.mean(data)
#print("Population 1 ",population_mean)

#std_deviation = statistics.stdev(data)
#print("Standard deviation 1",std_deviation)


# fig = ff.create_distplot([data],["temp"], show_hist= False)
# fig.show()

# code to find mean and standard deviation for 100 random data points
#dataset = []
#for i in range(0,100):
   # random_index = random.randint(0,len(data))
    #value = data[random_index]
   # dataset.append(value)
#mean2 = statistics.mean(dataset)
#std_deviation2 = statistics.stdev(dataset)
#print("Mean of sample: ", mean2)
#print("Standard deviation of sample : ", std_deviation2)

# code to find the mean and standard deviation for 1000 data points
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def plot_graph(mean_list):
    df = mean_list 
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"], show_hist = False)
    fig.show()

def main():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    plot_graph(mean_list)
    
    mean = statistics.mean(mean_list)
    print(mean)
    
main()    

# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print(std_deviation)
standard_deviation()
# the standard deviation of smapling mean is = 1/10 of population standard deviation. therefore the relation between standrd deviation of population and standard deviation of sampling mean distribution is given by: 
# standard deviation of sampling mean distribution  = standard deviation of population / √(number of data in each sample) 