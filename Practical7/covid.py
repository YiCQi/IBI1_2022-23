# This code aims to analyse data in full_data.csv and draw plots to visualize the results.
# Matplotlib is the most important library used.
# The answer to a question also includes.

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/祁意城/Desktop/py_work/learn/homework/practical7")
os.getcwd()
os.listdir()

covid_data = pd.read_csv("full_data.csv")

# showing the second column from every 100th row from the first 1000 rows (inclusive)
first_1000 = covid_data.iloc[:1001]
print(first_1000.iloc[0::100, 1])

# used a Boolean to show “total cases” for all rows corresponding to Afghanistan
Afghanistan_cases = []
for item in covid_data.loc[:,"location"]:
    Afghanistan_cases.append(item == "Afghanistan")
print('Boolean:', Afghanistan_cases)

# compute the mean number of new cases and new deaths on 31 March 2020
march_31_column = []
for item in covid_data.loc[:,"date"]:
    march_31_column.append(item == "2020-03-31")
new_cases = covid_data.loc[march_31_column,'new_cases']
new_deaths = covid_data.loc[march_31_column,'new_deaths']
mean_new_cases = np.mean(new_cases)
mean_new_deaths = np.mean(new_deaths)
print('mean of new cases:',mean_new_cases,'mean of new deaths:',mean_new_deaths)


# create boxplot of new cases and new deaths on 31 March 2020
plt.boxplot([new_cases,new_deaths])
plt.xticks(ticks=[1, 2], labels=["New Cases", "New Deaths"])
plt.ylabel("Number of Cases")
plt.title("New Cases and New Deaths on 31 March 2020")
plt.show()

# plot both new cases and new deaths worldwide over time
world_data = covid_data[covid_data['location'] == 'World']
world_new_cases = world_data.loc[:,"new_cases"]
world_new_deaths = world_data.loc[:,"new_deaths"]
world_dates = world_data.loc[:,"date"]

plt.figure(figsize=(10,8))
plt.plot(world_dates, world_new_cases, 'b-',label='New Cases')
plt.plot(world_dates, world_new_deaths, 'r-',label='New Deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Number of New cases/New deaths')
plt.title('New Cases and New Deaths Worldwide over Time')
plt.xticks(fontsize = 7)
plt.legend()
plt.show()

# answer the question stated in file question.txt
UK_data = covid_data[covid_data['location'] == 'United Kingdom']
UK_new_cases = UK_data.loc[:,"new_cases"]
UK_total_cases = UK_data.loc[:,"total_cases"]
UK_dates = UK_data.loc[:,"date"]

plt.figure(figsize=(10,8))
plt.plot(UK_dates, UK_new_cases, 'b-',label='New Cases')
plt.plot(UK_dates, UK_total_cases, 'r-',label='Total Cases')
plt.xticks(UK_dates.iloc[0:len(UK_dates):3],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Number of New cases/Total cases')
plt.title('New Cases and Total Cases Developed over Time in the UK')
plt.xticks(fontsize = 7)
plt.legend()
plt.show()
