###Changing index of a DataFrame
###As you saw in the previous exercise, indexes are immutable objects.
#This means that if you want to change or modify the index in a DataFrame, then you need to change the whole index.
#You will do this now, using a list comprehension to create the new index.

#A list comprehension is a succinct way to generate a list in one line.
#For example, the following list comprehension generates a list that contains the cubes of all numbers from 0 to 9: cubes = [i**3 for i in range(10)].
#This is equivalent to the following code:

#cubes = []
#for i in range(10):
#    cubes.append(i**3)

# Create the list of new indexes: new_idx
new_idx = [item.upper() for item in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)



###Changing index name labels
#Notice that in the previous exercise, the index was not labeled with a name. In this exercise, you will set its name to 'MONTHS'.

#Similarly, if all the columns are related in some way, you can provide a label for the set of columns.

#To get started, print the sales DataFrame in the IPython Shell and verify that the index has no name, only its data (the month names).

# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)



###Building an index, then a DataFrame
#You can also build the DataFrame and index independently, and then put them together.
#If you take this route, be careful, as any mistakes in generating the DataFrame or the index can cause the data and the index to be aligned incorrectly.

#In this exercise, the sales DataFrame has been provided for you without the month index.
#Your job is to build this index separately and then assign it to the sales DataFrame.
#Before getting started, print the sales DataFrame in the IPython Shell and note that it's missing the month information.

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)



###Extracting data with a MultiIndex
#In the video, Dhavide explained the concept of a hierarchical index, or a MultiIndex.
#You will now practice working with these types of indexes.

#The sales DataFrame you have been working with has been extended to now include State information as well.
#In the IPython Shell, print the new sales DataFrame to inspect the data. Take note of the MultiIndex!

#Extracting elements from the outermost level of a MultiIndex is just like in the case of a single-level Index.
#You can use the .loc[] accessor as Dhavide demonstrated in the video.

# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales.loc['CA':'TX'])



###Setting & sorting a MultiIndex
#In the previous exercise, the MultiIndex was created and sorted for you. Now, you're going to do this yourself!
#With a MultiIndex, you should always ensure the index is sorted. You can skip this only if you know the data is already sorted on the index fields.

#To get started, print the pre-loaded sales DataFrame in the IPython Shell to verify that there is no MultiIndex.

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)



###Using .loc[] with nonunique indexes
#As Dhavide mentioned in the video, it is always preferable to have a meaningful index that uniquely identifies each row.
#Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique.
#To see an example of this, you will index your sales data by 'state' in this exercise.

#As always, begin by printing the sales DataFrame in the IPython Shell and inspecting it.

# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])



###Indexing multiple levels of a MultiIndex
#Looking up indexed data is fast and efficient. And you have already seen that lookups based on the outermost level of a MultiIndex work just like lookups on DataFrames that have a single-level Index.

#Looking up data based on inner levels of a MultiIndex can be a bit trickier. In this exercise, you will use your sales DataFrame to do some increasingly complex lookups.

#The trickiest of all these lookups are when you want to access some inner levels of the index.
#In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual :, or use pd.IndexSlice.
#You can refer to the pandas documentation for more details. For example, in the video, Dhavide used the following code to extract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:

#stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]

#Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).


# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY', 1), :]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2), :]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2), :]
