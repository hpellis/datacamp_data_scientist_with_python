#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:18:12 2018

@author: harriet
"""
# Case Study - World Bank Development Indicators Dataset

#For this exercise, you'll use what you've learned about the zip() function and combine two lists into a dictionary.
#The first list feature_names contains header names of the dataset and the second list row_vals contains actual values of a row from the dataset, corresponding to each of the header names.
#
#Create a zip object by calling zip() and passing to it feature_names and row_vals. Assign the result to zipped_lists.
#Create a dictionary from the zipped_lists zip object by calling dict() with zipped_lists. Assign the resulting dictionary to rs_dict.

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)


#In this exercise, you will create a function to house the code you wrote earlier to make things easier and much more concise.
#This way, you only need to call the function and supply the appropriate lists to create your dictionaries!
#Again, the lists feature_names and row_vals are preloaded and these contain the header names of the dataset and actual values of a row from the dataset, respectively.
#
#Define the function lists2dict() with two parameters: first is list1 and second is list2.
#Return the resulting dictionary rs_dict in lists2dict().
#Call the lists2dict() function with the arguments feature_names and row_vals. Assign the result of the function call to rs_fxn.

# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)


# Using list comprehension

#This time, you're going to use the lists2dict() function you defined in the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.
#The lists2dict() function has already been preloaded, together with a couple of lists, feature_names and row_lists.
#feature_names contains the header names of the World Bank dataset and row_lists is a list of lists, where each sublist is a list of actual values of a row from the dataset.
#Your goal is to use a list comprehension to generate a list of dicts, where the keys are the header names and the values are the row entries.

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])


# Creating a DataFrame

#You will now use of all these to convert the list of dictionaries into a pandas DataFrame.
#You will see how convenient it is to generate a DataFrame from dictionaries with the DataFrame() function from the pandas package.
#The lists2dict() function, feature_names list, and row_lists list have been preloaded for this exercise.

# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())


#Processing data in chunks (1)
#Sometimes, data sources can be so large in size that storing the entire dataset in memory becomes too resource-intensive.
#In this exercise, you will process the first 1000 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.

#The csv file 'world_dev_ind.csv' is in your current directory for your use.
#To begin, you need to open a connection to this file using what is known as a context manager.
#For example, the command with open('datacamp.csv') as datacamp binds the csv file 'datacamp.csv' as datacamp in the context manager.
#Here, the with statement is the context manager, and its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)


#Writing a generator to load data in chunks (2)
#In the previous exercise, you processed a file line by line for a given number of lines.
#What if, however, you want to do this for the entire file?

#In this case, it would be useful to use generators.
#Generators allow users to lazily evaluate data.
#This concept of lazy evaluation is useful when you have to deal with very large datasets because it lets you generate values in an efficient manner by yielding only chunks of data at a time instead of the whole thing at once.

#In this exercise, you will define a generator function read_large_file() that produces a generator object which yields a single line from a file each time next() is called on it.
#The csv file 'world_dev_ind.csv' is in your current directory for your use.

#Note that when you open a connection to a file, the resulting file object is already a generator! So out in the wild, you won't have to explicitly create generator objects in cases such as this.
#However, for pedagogical reasons, we are having you practice how to do this here with the read_large_file() function. Go for it!
