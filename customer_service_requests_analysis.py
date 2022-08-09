# -*- coding: utf-8 -*-
"""Customer_Service_Requests_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16BxmeAJ6NkyvPfJcvF9bul0HezJOVY5B

**Project Customer Service Requests Analysis**
"""

# Commented out IPython magic to ensure Python compatibility.
### import libraries
#for linear algebra
import numpy as np
# for data processing session
import pandas as pd
#for data visualization
import matplotlib.pyplot as plt
from matplotlib import style
#seaborn is also data visualization library built on top of the matplotlib
import seaborn as sns 
#now we use matplotlib inline which is used for the output of plotting commands is displayed inline within frontends like jupitar notebook. 
#Mainly used for inline plotting
# %matplotlib inline

#Now import the csv file
Service_Request_csv = pd.read_csv("311_Service_Requests_from_2010_to_Present.csv")

#now showing the first five rows of the service request csv 
Service_Request_csv.head()

#now showing the last five rows of the service request csv 
Service_Request_csv.tail()

#how many rows & columns are present in this service request dataset
Service_Request_csv.shape

#how many columns are present inside the service request dataset
print(Service_Request_csv.columns.to_list())

#how many unique columns are present inside service request dataset for the column name "Complaint Type"
#The unique() function is used to find the unique elements of an array
Service_Request_csv["Complaint Type"].unique()

#how many unique columns are present inside service request dataset for the column name "Descriptor"
#The unique() function is used to find the unique elements of an array
Service_Request_csv["Descriptor"].unique()

#how many missing values are present or not inside this dataset
#using isNa function
Service_Request_csv.isna().any()

#total missing values are present inside this dataset
Service_Request_csv.isna().sum()

#information of the Service_Request_csv dataframe
Service_Request_csv.info()

#check the datatype of the dataset
Service_Request_csv.dtypes

#computes and displays summary statistics for a Service_Request_csv dataframe
Service_Request_csv.describe()

#create a custom dataframe with Complaint Type & City
customDataObject={'count':Service_Request_csv.groupby(['Complaint Type','City']).size()}
ComplaintTypeCity = pd.DataFrame(customDataObject).reset_index()

#show the custom complaint type city
ComplaintTypeCity

#just show first five rows from the dataset
ComplaintTypeCity.head()

#get the individual column size for the column name Borough, Complaint Type & Descriptor
#get an array of column name
getColumnArray=["Borough","Complaint Type","Descriptor"]
Service_Request_csv.groupby(getColumnArray).size()

"""**Python Dates**
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
"""

import datetime

#Create a dataframe with parsed date
#If True and parse_dates is enabled, pandas will attempt to infer the format of the datetime strings in the columns.
Service_Request_csv_withParsedDate=pd.read_csv(
    "311_Service_Requests_from_2010_to_Present.csv", 
    parse_dates=["Created Date","Closed Date"])

#calculate the Request Closing Time 
Service_Request_csv_withParsedDate["Request_Closing_Time"] = Service_Request_csv_withParsedDate["Closed Date"] - Service_Request_csv_withParsedDate["Created Date"]

#Visualize the status of the ticket
Service_Request_csv_withParsedDate["Status"].value_counts().plot(kind='bar',alpha=0.6,figsize=(7,7))
plt.show()

"""Matplotlib is a library in Python and it is numerical – mathematical extension for NumPy library. 
#The figure module provides the top-level Artist, the Figure, which contains all the plot elements. 
#This module is used to control the default spacing of the subplots and top level container for all plot elements
"""

#Complaint type Breakdown with bar plot to figure out majority of complaint types and top 10 complaints
#Matplotlib is a library in Python and it is numerical – mathematical extension for NumPy library. 
Service_Request_csv["Complaint Type"].value_counts().head(10).plot(kind='barh',figsize=(5,5))

#column wise groupby & size
Service_Request_csv.groupby(["Borough","Complaint Type","Descriptor"]).size()

#calculate the major complaint type
#subset: It's an array which limits the dropping process to passed rows/columns through list.
majorComplaints = Service_Request_csv.dropna(subset=["Complaint Type"])
majorComplaints = majorComplaints.groupby("Complaint Type")
#Pandas sort_values() function sorts a data frame in Ascending or Descending order of passed Column.
sortedComplaintType = majorComplaints.size().sort_values(ascending=False)
#Pandas reset_index() is a method to reset index of a Data Frame. reset_index() 
#method sets a list of integer ranging from 0 to length of data as index. ... level
sortedComplaintType = sortedComplaintType.to_frame('count').reset_index()

#how many complaints are there, that list i have find out
sortedComplaintType.head()

#create a pie chart of this complaint type
sortedComplaintType = sortedComplaintType.head()
plt.figure(figsize=(5,5))

#We use autopct to display the percent value using Python string formatting. 
#For example, autopct='%1.1f%%' means that for each pie wedge, the format string is '1.1f%'.

plt.pie(sortedComplaintType['count'], labels=sortedComplaintType['Complaint Type'], autopct="%1.1f%%")
plt.show()

#group dataset by complaint type to display plot against city
grouped_by_complaint_type = Service_Request_csv.groupby('Complaint Type')

#groupeddata with Blocked Driverway column type
#get how many groups are present on Blocked Driveway
grp_data = grouped_by_complaint_type.get_group("Blocked Driveway")

grp_data.columns.to_list()

#how many rows & columns are present for this Blocked Driveway dataset
grp_data.shape

#to get the null values for this dataset
Service_Request_csv.isnull().sum()

#drop blank values for City column
Service_Request_csv["City"].dropna(inplace=True)

#check shape after dropping null values
Service_Request_csv["City"].shape

#count of null values in grouped city column data
grp_data["City"].isnull().sum()

#fix those nan values with "Unknown city" value instead
#The fillna() function is used to fill NA/NaN values using the specified method.
grp_data["City"].fillna("Unknown City", inplace=True)

#Scatter plot displaying all the cities that raised complaint of type 'Blocked Driveway'
plt.figure(figsize=(25,15))
plt.scatter(grp_data["Complaint Type"], grp_data["City"])
plt.title("Plot showing list of cities that raised complaint of type Blocked Driveway")
plt.show()

#fix Location type those NAN with "unknown Location" value instead
Service_Request_csv["Location Type"].fillna("Unknown Loc",inplace=True)

#how many values are present for the column name Location Type
Service_Request_csv["Location Type"].values

#Find top 10 major complaint types and their counts
grouped_by_complaint_type["Complaint Type"].value_counts().nlargest(10)

#fix Location type those NAN with "unknown Location" value instead
Service_Request_csv["Location Type"].fillna("Unknown Loc", inplace=True)

Service_Request_csv['Location Type'].values

#count of null values in grouped location type column data
grp_data['Location Type'].isnull().sum()

#how many columns are present in group data
grp_data.columns.to_list()