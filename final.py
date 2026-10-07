#ETL Final Project: Analyzing Unemployment Trends in California
#Dataset Used: https://catalog.data.gov/dataset/unemployment-rate-by-age-groups?from_hint=eyJrZXl3b3JkIjoidW5lbXBsb3ltZW50IHJhdGUgZGVtb2dyYXBoaWNzIn0%3D

import pandas as pd
import matplotlib.pyplot as plt

#Extract - Extracting the information from the data set
unemployment_info = pd.read_csv("unemployment_data.csv")
unemployment_info['Date'] = pd.to_datetime(unemployment_info['Date'])

print("Extract:\nData Loaded!")

#Transform - Organizing the information into reasonable grouping
age_groups = ['Age 16-19', 'Age 20-24', 'Age 25-34', 'Age 35-44', 'Age 45-54', 'Age 55-64', 'Age 65+']

#2008 Financial Crisis Impact
#The crisis timeline was Sept 2008 to June 2009
crisis_2008 = unemployment_info[(unemployment_info['Date'] >= '2008-09-16') & (unemployment_info['Date'] <= '2009-06-01')]

#Finding highest unemployment rate per age group during 2008 crisis
highest_2008 = crisis_2008[age_groups].max()

#COVID Impact
#The COVID timeline was March 2020 to May 2023
covid_2020 = unemployment_info[(unemployment_info['Date'] >= '2020-03-13') & (unemployment_info['Date'] <= '2023-05-05')]

#Finding highest unemployment rate per age group during COVID
highest_2020 = covid_2020[age_groups].max()

#Label the severity of each crisis based on highest unemployment rate
#2008
if highest_2008.max() >= 0.20:
    severity_2008 = "Severe (20%+)"
elif highest_2008.max() >= 0.10:
    severity_2008 = "Moderate (10-20%)"
else:
    severity_2008 = "Mild (<10%)"
    if highest_2008.max() > 0.04 and highest_2008.max() < 0.05:
        severity_2008 = "Best (4-5%)"

#2020
if highest_2020.max() >= 0.20:
    severity_2020 = "Severe (20%+)"
elif highest_2020.max() >= 0.10:
    severity_2020 = "Moderate (10-20%)"
else:
    severity_2020 = "Mild (<10%)"
    if highest_2020.max() > 0.04 and highest_2020.max() < 0.05:
        severity_2020 = "Best (4-5%)"

print(f"Transform:\n2008 Crisis severity: {severity_2008}\nCOVID Crisis severity: {severity_2020}")


#Load - Loading the data and creating visualizations (Two Charts)
#Unemployment Rate by Year Chart

#Combined line chart of unemployment information

for group in age_groups:
    plt.plot(crisis_2008['Date'], crisis_2008[group], color='purple')                              
    plt.plot(covid_2020['Date'], covid_2020[group], color='blue')

plt.title("California Unemployment Trends: 2008 Crisis vs. COVID-19")
plt.ylabel("Unemployment Rate")
plt.xlabel("Year")
plt.legend(["2008 Crisis", "COVID-19"], loc = "upper left")
plt.grid(True)

plt.savefig('UnemploymentChart.jpg')
plt.show()
plt.close()

#Highest Unemployment Rate by Age Group Chart
highest_unempinfo = pd.DataFrame({'2008 Crisis': highest_2008, 'COVID Crash': highest_2020})

highest_unempinfo.plot(kind='bar')
plt.title("Highest Unemployment Rate by Age Group in California")
plt.ylabel("Unemployment Rate")
plt.xlabel("Age Group")
plt.xticks(rotation=0)
plt.tight_layout()
plt.grid(True)

plt.savefig('HighestUnemploymentChart.jpg')
plt.show()
plt.close()

print("Load:\nCharts saved!")
#After running the program, exiting out of the first chart should make the second chart show up!!