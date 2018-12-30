# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:58:49 2018

@author: 612383249
"""

##### dictionaries
#consists of keys and values


world={'afghanistan': 30.55, 'albania': 2.77, 'algeria': 39.21}

print(world['albania'])



##### example of using lists

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger=countries.index('germany')


# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])


##### creating a dictionary

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)



##### finding a dictionaries keys

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())


# Print out value that belongs to key 'norway'
print(europe['norway'])



##### adding data to a dictionary

world={'afgahnistan': 30.55, 'albania': 2.77, 'algeria': 39.21}

print(world['albania'])

#to add sealand to this dict
world['sealand'] = 0.000027

print(world)

#another way to check it's in the list (prints True)
print('sealand' in world)



##### removing it from the list

del(world['sealand'])
print(world)


##### lists vs dict
# you can select, update and remove elements from both
# list --- indexed by a range of numbers
# dict --- indexed by unique keys

#use a list when you have a collection of values, when the order of those values matters or when you want to select entire subsets

# use a dict when you want a lookup table with unique keys



##### manipulating a dict

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany']='berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)



###### dictionary within a dictionary, adding more information

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france'] ['capital'])

# Create sub-dictionary data
data={'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy']=data

# Print europe
print(europe)



###### pandas

# good for working with tabular data
# numpy arrays can only handle elements with the same data type
# pandas are good for this
# high level data manipulation tool built on numpy
# in pandas, you store the data in something called a 'data frame'
# to create a data frame, there are several options
# you may build it manually, using a dictionary. the keys are the column labels, and the values as the data, column by column
# you then import pandas as pd
# then you creates a data frame using name=pd.DataFrame(dict)
# then you edit the row names with name.index ["name1", ]

# if you're working with large datasets though, you want to import that data from an external file that contains all this data
# e.g. a csv file
# pd.read_csv("path/to/name.csv")

#you tell th read csv function that the first column contains a row of indexes
# pd.read_csv("path/to/name.csv", index_col=0)


##### converting a dictionary to a DataFrame

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

# Print cars
print(cars)



##### labelling the rows

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index=row_labels

# Print cars again
print(cars)




##### importing file to convert to DataFrame

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars=pd.read_csv('cars.csv')
cars=pd.DataFrame(cars)

# Print out cars
print(cars)





####### using the first column as row labels

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)



##### advanced methods
# if you access a column with dataframename[colname], you get a weird result at the end
# prints out panda series
# (a DataFrame is a bunch of series)
# what you want to do to print out a column is dataframename[[colname]]

# you can get sub-dataframes by putting more col names inside the square brackets, separated by commas

# you can also use square brackets to get rows
# you do this by specifying a slice

#square brackets have limited functionality
# with arrays, you can be more specific my_array [rows, columns]
# to do a similar thing with pandas, you use loc and iloc 
#loc is a technique to select part of your data based on labels
#iloc is a technique to select part of your data based on integer position


#loc
# dataframename.loc[["rowname"]]

#dataframename.loc[["rowname", "rowname"]]

#you can specify which columns you want to show
# dataframename.loc[["rowname", "rowname"], ["colname", "colname"]]

#you can also do  - below does all rows, some columns
# dataframename.loc[:, ["country", "capital"]]


#iloc
#use index numbers to print out some columns
# dataframename.iloc[[1, 2, 3]]

# use index numbers to print some cols and rows
# dataframename.iloc[[1,2,3], [0,1]]


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])



##### printing out some data

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:4])

# Print out fourth, fifth and sixth observation
print(cars[3:6])



###### using loc and iloc

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc["JAP"])

print(cars.iloc[2])

# Print out observations for Australia and Egypt

print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])





###### loc and iloc

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['MOR', 'RU'], ['country', 'drives_right']])



###### printing parts of dataframe

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars["drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:, ["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ["cars_per_cap", "drives_right"]])




######







