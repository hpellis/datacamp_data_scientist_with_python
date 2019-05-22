###Index ordering
#In this exercise, the DataFrame election is provided for you.
#It contains the 2012 US election results for the state of Pennsylvania with county names as row indices.
#Your job is to select 'Bedford' county and the'winner' column. Which method is the preferred way?

election.loc['Bedford', 'winner']


###Positional and labeled indexing
#Given a pair of label-based indices, sometimes it's necessary to find the corresponding positions.
#In this exercise, you will use the Pennsylvania election results again. The DataFrame is provided for you as election.

#Find x and y such that election.iloc[x, y] == election.loc['Bedford', 'winner'].
#That is, what is the row position of 'Bedford', and the column position of 'winner'? Remember that the first position in Python is 0, not 1!

#To answer this question, first explore the DataFrame using election.head() in the IPython Shell and inspect it with your eyes.

# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])



###Indexing and column rearrangement
#There are circumstances in which it's useful to modify the order of your DataFrame columns.
#We do that now by extracting just two columns from the Pennsylvania election results DataFrame.

#Your job is to read the CSV file and set the index to 'county'.
#You'll then assign a new DataFrame by selecting the list of columns ['winner', 'total', 'voters'].
#The CSV file is provided to you in the variable filename.

# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())


###Slicing rows
#The Pennsylvania US election results data set that you have been using so far is ordered by county name.
#This means that county names can be sliced alphabetically.
#In this exercise, you're going to perform slicing on the county names of the election DataFrame from the previous exercises, which has been pre-loaded for you.

#Slice the row labels 'Perry' to 'Potter' and assign the output to p_counties.
#Print the p_counties DataFrame. This has been done for you.
#Slice the row labels 'Potter' to 'Perry' in reverse order. To do this for hypothetical row labels 'a' and 'b', you could use a stepsize of -1 like so: df.loc['b':'a':-1].
#Print the p_counties_rev DataFrame. This has also been done for you, so hit 'Submit Answer' to see the result of your slicing!

# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election['Perry':'Potter']

# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election['Potter':'Perry':-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)


###Slicing columns
#Similar to row slicing, columns can be sliced by value.
#In this exercise, your job is to slice column names from the Pennsylvania election results DataFrame using .loc[].

#It has been pre-loaded for you as election, with the index set to 'county'.


#Slice the columns from the starting column to 'Obama' and assign the result to left_columns
#Slice the columns from 'Obama' to 'winner' and assign the result to middle_columns
#Slice the columns from 'Romney' to the end and assign the result to right_columns

# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:, :'Obama']

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:, 'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:, 'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())


###Subselecting DataFrames with lists
#You can use lists to select specific row and column labels with the .loc[] accessor.
#In this exercise, your job is to select the counties ['Philadelphia', 'Centre', 'Fulton'] and the columns ['winner','Obama','Romney'] from the election DataFrame, which has been pre-loaded for you with the index set to 'county'.

#Create the list of row labels ['Philadelphia', 'Centre', 'Fulton'] and assign it to rows.
#Create the list of column labels ['winner', 'Obama', 'Romney'] and assign it to cols.
#Create a new DataFrame by selecting with rows and cols in .loc[] and assign it to three_counties.

# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows, cols]

# Print the three_counties DataFrame
print(three_counties)


###Thresholding data
#In this exercise, we have provided the Pennsylvania election results and included a column called 'turnout' that contains the percentage of voter turnout per county.
#Your job is to prepare a boolean array to select all of the rows and columns where voter turnout exceeded 70%.

#As before, the DataFrame is available to you as election with the index set to 'county'.


#Create a boolean array of the condition where the 'turnout' column is greater than 70 and assign it to high_turnout.
#Filter the election DataFrame with the high_turnout array and assign it to high_turnout_df.

# Create the boolean array: high_turnout
high_turnout = election['turnout'] > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)


###Filtering columns using other columns
#The election results DataFrame has a column labeled 'margin' which expresses the number of extra votes the winner received over the losing candidate.
#This number is given as a percentage of the total votes cast. It is reasonable to assume that in counties where this margin was less than 1%, the results would be too-close-to-call.

#Your job is to use boolean selection to filter the rows where the margin was less than 1.
#You'll then convert these rows of the 'winner' column to np.nan to indicate that these results are too close to declare a winner.


# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close, 'winner'] = np.nan

# Print the output of election.info()
print(election.info())



###Filtering using NaNs
#In certain scenarios, it may be necessary to remove rows and columns with missing data from a DataFrame.
#The .dropna() method is used to perform this action. You'll now practice using this method on a dataset obtained from Vanderbilt University, which consists of data from passengers on the Titanic.

#The DataFrame has been pre-loaded for you as titanic. Explore it in the IPython Shell and you will note that there are many NaNs.
#You will focus specifically on the 'age' and 'cabin' columns in this exercise.
#Your job is to use .dropna() to remove rows where any of these two columns contains missing data and rows where all of these two columns contain missing data.

#You'll also use the .shape attribute, which returns the number of rows and columns in a tuple from a DataFrame, or the number of rows from a Series, to see the effect of dropping missing values from a DataFrame.

#Finally, you'll use the thresh= keyword argument to drop columns from the full dataset that have less than 1000 non-missing values.





hh
