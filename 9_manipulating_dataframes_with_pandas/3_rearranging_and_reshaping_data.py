###Pivoting a single variable
#Suppose you started a blog for a band, and you would like to log how many visitors you have had, and how many signed-up for your newsletter.
#To help design the tours later, you track where the visitors are. A DataFrame called users consisting of this information has been pre-loaded for you.

#Inspect users in the IPython Shell and make a note of which variable you want to use to index the rows ('weekday'), which variable you want to use to index the columns ('city'), and which variable will populate the values in the cells ('visitors').
#Try to visualize what the result should be.

#For example, in the video, Dhavide used 'treatment' to index the rows, 'gender' to index the columns, and 'response' to populate the cells. Prior to pivoting, the DataFrame looked like this:

   id treatment gender  response
0   1         A      F         5
1   2         A      M         3
2   3         B      F         8
3   4         B      M         9

#After pivoting:

gender     F  M
treatment
A          5  3
B          8  9

#In this exercise, your job is to pivot users so that the focus is on 'visitors', with the columns indexed by 'city' and the rows indexed by 'weekday'.


# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index='weekday', columns='city', values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)


###Pivoting all variables
#If you do not select any particular variables, all of them will be pivoted. In this case - with the users DataFrame - both 'visitors' and 'signups' will be pivoted, creating hierarchical column labels.

#You will explore this for yourself now in this exercise.

# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday', columns='city', values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday', columns='city')

# Print the pivoted DataFrame
print(pivot)



###Stacking & unstacking I
#You are now going to practice stacking and unstacking DataFrames. The users DataFrame you have been working with in this chapter has been pre-loaded for you, this time with a MultiIndex.
#Explore it in the IPython Shell to see the data layout. Pay attention to the index, and notice that the index levels are ['city', 'weekday'].
#So 'weekday' - the second entry - has position 1. This position is what corresponds to the level parameter in .stack() and .unstack() calls.
#Alternatively, you can specify 'weekday' as the level instead of its position.

#Your job in this exercise is to unstack users by 'weekday'. You will then use .stack() on the unstacked DataFrame to see if you get back the original layout of users.

# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))



###Stacking & unstacking II
#You are now going to continue working with the users DataFrame. As always, first explore it in the IPython Shell to see the layout and note the index.

#Your job in this exercise is to unstack and then stack the 'city' level, as you did previously for 'weekday'.

# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))



###Restoring the index order
#Continuing from the previous exercise, you will now use .swaplevel(0, 1) to flip the index levels. Note they won't be sorted.
#To sort them, you will have to follow up with a .sort_index(). You will then obtain the original DataFrame.
#Note that an unsorted index leads to slicing failures.

#To begin, print both users and bycity in the IPython Shell. The goal here is to convert bycity back to something that looks like users.

# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0, 1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))



###Adding names for readability
#You are now going to practice melting DataFrames. A DataFrame called visitors_by_city_weekday has been pre-loaded for you.
#Explore it in the IPython Shell and see that it is the users DataFrame from previous exercises with the rows indexed by 'weekday', columns indexed by 'city', and values populated with 'visitors'.

#Recall from the video that the goal of melting is to restore a pivoted DataFrame to its original form, or to change it from a wide shape to a long shape.
#You can explicitly specify the columns that should remain in the reshaped DataFrame with id_vars, and list which columns to convert into values with value_vars.
#As Dhavide demonstrated, if you don't pass a name to the values in pd.melt(), you will lose the name of your variable. You can fix this by using the value_name keyword argument.

#Your job in this exercise is to melt visitors_by_city_weekday to move the city names from the column labels to values in a single column called 'city'.
#If you were to use just pd.melt(visitors_by_city_weekday), you would obtain the following result:

      city value
0  weekday   Mon
1  weekday   Sun
2   Austin   326
3   Austin   139
4   Dallas   456
5   Dallas   237

#Therefore, you have to specify the id_vars keyword argument to ensure that 'weekday' is retained in the reshaped DataFrame, and the value_name keyword argument to change the name of value to visitors.

# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday = visitors_by_city_weekday.reset_index()

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars='weekday', value_name='visitors')

# Print visitors
print(visitors)



###Going from wide to long
#You can move multiple columns into a single column (making the data long and skinny) by "melting" multiple columns.
#In this exercise, you will practice doing this.

#The users DataFrame has been pre-loaded for you. As always, explore it in the IPython Shell and note the index.


# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday' ,'city'])

# Print skinny
print(skinny)



###Obtaining key-value pairs with melt()
#Sometimes, all you need is some key-value pairs, and the context does not matter. If said context is in the index, you can easily obtain what you want.
#For example, in the users DataFrame, the visitors and signups columns lend themselves well to being represented as key-value pairs.
#So if you created a hierarchical index with 'city' and 'weekday' columns as the index, you can easily extract key-value pairs for the 'visitors' and 'signups' columns by melting users and specifying col_level=0.

# Set the new index: users_idx
users_idx = users.set_index(['city', 'weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx, col_level=0)

# Print the key-value pairs
print(kv_pairs)



###Setting up a pivot table
#Recall from the video that a pivot table allows you to see all of your variables as a function of two other variables.
#In this exercise, you will use the .pivot_table() method to see how the users DataFrame entries appear when presented as functions of the 'weekday' and 'city' columns.
#That is, with the rows indexed by 'weekday' and the columns indexed by 'city'.

#Before using the pivot table, print the users DataFrame in the IPython Shell and observe the layout.

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index='weekday', columns='city')

# Print by_city_day
print(by_city_day)



###Using other aggregations in pivot tables
#You can also use aggregation functions within a pivot table by specifying the aggfunc parameter.
#In this exercise, you will practice using the 'count' and len aggregation functions - which produce the same result - on the users DataFrame.

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday', aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index='weekday', aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))



###Using margins in pivot tables
#Sometimes it's useful to add totals in the margins of a pivot table. You can do this with the argument margins=True.
#In this exercise, you will practice using margins in a pivot table along with a new aggregation function: sum.

#The users DataFrame, which you are now probably very familiar with, has been pre-loaded for you.

# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index='weekday', aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total
signups_and_visitors_total = users.pivot_table(index='weekday', aggfunc=sum, margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)



d
