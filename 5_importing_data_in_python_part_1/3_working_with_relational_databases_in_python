###Creating a database engine
#Here, you're going to fire up your very first SQL engine.
#You'll create an engine to connect to the SQLite database 'Chinook.sqlite', which is in your working directory.

# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')


###What are the tables in the database?
#In this exercise, you'll once again create an engine to connect to 'Chinook.sqlite'.
#Before you can get any data out of the database, however, you'll need to know what tables it contains!

#To this end, you'll save the table names to a list using the method table_names() on the engine and then you will print the list.

# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)


###The Hello World of SQL Queries!
#In this exercise, you'll perform the Hello World of SQL queries, SELECT, in order to retrieve all columns of the table Album in the Chinook database.

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * FROM Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())


###Customizing the Hello World of SQL Queries
#Congratulations on executing your first SQL query! Now you're going to figure out how to customize your query in order to:

#Select specified columns from a table;
#Select a specified number of rows;
#Import column names from the database table.

#Execute the SQL query that selects the columns LastName and Title from the Employee table. Store the results in the variable rs.
#Apply the method fetchmany() to rs in order to retrieve 3 of the records. Store them in the DataFrame df.
#Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())


###Filtering your database records using SQL's WHERE
#You can now execute a basic SQL query to select records from any table in your database and you can also perform simple query customizations to select particular columns and numbers of rows.

#Complete the argument of create_engine() so that the engine for the SQLite database 'Chinook.sqlite' is created.
#Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6. Use the >= operator and assign the results to rs.
#Apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
#Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.

import pandas as pd
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())

###Ordering your SQL records with ORDER BY
#You can also order your SQL query results.

#Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
#In the context manager, execute the query that selects all records from the Employee table and orders them in increasing order by the column BirthDate. Assign the result to rs.
#In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
#Set the DataFrame's column names to the corresponding names of the table columns.

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()


# Print head of DataFrame
print(df.head())


###Pandas and The Hello World of SQL Queries!
#Here, you'll take advantage of the power of pandas to write the results of your SQL query to a DataFrame in one swift line of Python code!

#You'll first import pandas and create the SQLite 'Chinook.sqlite' engine. Then you'll query the database to select all records from the Album table.

#Import the pandas package using the alias pd.
#Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
#Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from the table Album.
#The remainder of the code is included to confirm that the DataFrame created by this method is equal to that created by the previous method that you learned.

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * from Album', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))


###Pandas for more complex querying
#Here, you'll become more familiar with the pandas function read_sql_query() by using it to execute a more complex query: a SELECT statement followed by both a WHERE clause AND an ORDER BY clause.

#You'll build a DataFrame that contains the rows of the Employee table for which the EmployeeId is greater than or equal to 6 and you'll order these entries by BirthDate.

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())


###The power of SQL lies in relationships between tables: INNER JOIN
#Here, you'll perform your first INNER JOIN! You'll be working with your favourite SQLite database, Chinook.sqlite.
#For each record in the Album table, you'll extract the Title along with the Name of the Artist.
#The latter will come from the Artist table and so you will need to INNER JOIN these two tables on the ArtistID column of both.


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())


###Filtering your INNER JOIN
#Congrats on performing your first INNER JOIN!
#You're now going to finish this chapter with one final exercise in which you perform an INNER JOIN and filter the result using a WHERE clause.

#Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId that satisfy the condition Milliseconds < 250000.

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())
