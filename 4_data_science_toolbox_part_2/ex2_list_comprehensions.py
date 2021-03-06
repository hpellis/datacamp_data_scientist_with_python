#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 15:05:02 2018

@author: harriet
"""

#### list comprehension

# collapse for loops for building lists into a single line
# more efficient than for loops
# work on any iterable, not just lists

nums = [12, 8, 3, 16]

new_nums = [num + 1 for num in nums]


#Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.

# Create list comprehension: squares
squares = [i**2 for i in range(10)]

print(squares)


#In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions. 
#Let's step aside for a while from strings. 
#One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. 
#Matrices can be represented as a list of lists in Python. 
#Your task is to recreate this matrix by using nested listed comprehensions. 
#Recall that you can create one of the rows of the matrix with a single list comprehension. 
#To create the list of lists, you simply have to supply the list comprehension as the output expression of the overall list comprehension:
#[[output expression] for iterator variable in iterable]
#Note that here, the output expression is itself a list comprehension.

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)


#### using conditionals in comprehensions
    
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)


#### using an if-else conditional

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)



#### dictionary comprehension

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member:len(member) for member in fellowship}

# Print the new list
print(new_fellowship)



#### generator expressions
# list comprehension returns a list
# a generator returns a generator object, doesn't store anything in memory
# both can be iterated over
# generator objects can be useful for working with really large datasets because they don't immediately create a list that is stored in memory

# generator functions are functions that produce generator objects when they are called
# same syntax (def) but instead of returning values they yield a sequence of values

#e.g.

def num_sequence(n):
    """Generate values from 0 to n"""
    i=0
    while i > n:
        yield i
        i+=1
        
result=num_sequence(5)

# this produces a generator object
print(type(result))

for item in result:
    print item
    
    
    
#Now, you will start simple by creating a generator object that produces numeric values.

#Create a generator object that will produce values from 0 to 30. Assign the result to result and use num as the iterator variable in the generator expression.
#Print the first 5 values by using next() appropriately in print().
#Print the rest of the values by using a for loop to iterate over the generator object.

# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)



#### changing the output in generator expressions
    
#Write a generator expression that will generate the lengths of each string in lannister. Use person as the iterator variable. Assign the result to lengths.
#Supply the correct iterable in the for loop for printing the values in the generator object.    
    
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)


#### build a generator function
    
#Complete the function header for the function get_lengths() that has a single parameter, input_list.
#In the for loop in the function definition, yield the length of the strings in input_list.
#Complete the iterable part of the for loop for printing the values generated by the get_lengths() generator function. Supply the call to get_lengths(), passing in the list lannister.

# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)
# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)



#### list comprehension for time-stamped data
    
#Extract the column 'created_at' from df and assign the result to tweet_time. 
#Fun fact: the extracted column in tweet_time here is a Series data structure!
#Create a list comprehension that extracts the time from each row in tweet_time. 
#Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. 
#Use entry as the iterator variable and assign the result to tweet_clock_time. Remember that Python uses 0-based indexing!
    
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)


#### conditional list comprehension for time-stamped data

#Extract the column 'created_at' from df and assign the result to tweet_time.
#Create a list comprehension that extracts the time from each row in tweet_time. 
#Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. 
#Use entry as the iterator variable and assign the result to tweet_clock_time. 
#Additionally, add a conditional expression that checks whether entry[17:19] is equal to '19'.

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)

