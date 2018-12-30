#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:27:17 2018

@author: harriet
"""

##### while loops

#The while loop is like a repeated if statement. 
#The code is executed over and over again, as long as the condition is True
#while condition :
#    expression


#### basic while loop

# Initialize offset
offset=8

# Code the while loop
while offset > 0:
    print("correcting...")
    offset=offset-1
    print(offset)


#### while loop with conditionals
    
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset=offset-1
    else:
        offset=offset+1
    print(offset)
    

#### using a for loop to loop over a list
    
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for space in areas:
    print (space)
    
    
#### using enumerate() to loop over two iterators
    
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room "+ str(index) +":" + str(a))
    


#### looping over a list of lists
    
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch

for name, area in house:
    print("the " + str(name) + " is " + str(area) + " sqm")



##### using items() to loop over a dictionary
    
# example 
world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))

# another example
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print ("the capital of " + key + " is " + value)


##### looping over a numpy array (np_height is 1D, np_baseball is 2D)

# Import numpy as np
import numpy as np

# For loop over np_height
for h in np_height:
    print(str(h) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print (x)
    


#### using iterrows() to loop over a dataframe

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, rows in cars.iterrows():
    print(lab)
    print(rows)
    

##### using square brackets to select variables

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ": " + str(row["cars_per_cap"]))


#### using iterrows() to add a column to a dataframe

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"]=row["country"].upper()


# Print cars
print(cars)


#Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to understand, but not very efficient. 
#On every iteration, you're creating a new Pandas Series.
#
#If you want to add a column to a DataFrame by calling a function on another column, the iterrows() method in combination with a for loop is not the preferred way to go. 
#Instead, you'll want to use apply().    

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
    
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)

