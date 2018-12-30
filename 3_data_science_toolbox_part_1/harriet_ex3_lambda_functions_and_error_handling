#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:47:01 2018

@author: harriet
"""

#### lambda functions

#In this exercise, you will practice writing a simple lambda function and calling this function. Recall what you know about lambda functions and answer the following questions:
#
#How would you write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a?
#How would you call add_bangs with the argument 'hello'?
#
#The lambda function definition is: add_bangs = (lambda a: a + '!!!'), and the function call is: add_bangs('hello').


#### writing a lambda function

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word, echo: word * echo)

# Call echo_word: result
result = echo_word("hey", 5)

# Print result
print(result)


#### using map() to apply a function over an object

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda spell: spell + "!!!", spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list=list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)



#### using filter() to filter out elements that don't satisfy certain criteria

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list=list(result)

# Convert result into a list and print it
print(result_list)



#### using reduce() and lambda function
# reduce() performs computations on a list and returns a single result

# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda x, y: x + y, stark)

# Print the result
print(result)


#### error handling with try-except

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word=""
    shout_words=""
    

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + "!!!"
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")


#### error handling by raising an error

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError ("echo must be greater than 0")

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)



#### writing a lambda function to filter the twitter dataset for RTs

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == "RT", tweets_df['text'])

# Create list from filter object result: res_list
res_list=list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
    
    
#### adding a try-except block to count_entries function
    
    # Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print("The DataFrame does not have a " +col_name + "column.")

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)


#### raise a value error in the count_entries function

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError ("The DataFrame does not have a " + col_name + " column.")

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1=count_entries (tweets_df, "lang")

# Print result1
print(result1)