# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:19:26 2018

@author: 612383249
"""

import matplotlib.pyplot as plt

##### introductory example
year= [1950, 1970, 1990, 2010]
pop=[2.519, 3.692, 5.263, 6.972]

#first argument is the x axis, second argument is the y axis
plt.plot(year, pop)

plt.show()


##### scatter plot example

plt.scatter(year,pop)
plt.show


#### log scale

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()


##### histogram

#only need argument of list
#will automatically give you 10 bins, but can also specify this

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# Build histogram with 5 bins
plt.hist(life_exp, 5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, 20)

# Show and clean up again
plt.show()
plt.clf()


# Histogram of life_exp, 15 bins
plt.hist(life_exp, 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, 15)

# Show and clear plot again
plt.show()
plt.clf()


###### labels
plt.plot(xaxis, yaxis)

plt.xlabel('name')
plt.ylabel('name2')
plt.title('Title of plot')

#this maps the numbers on teh y axis to the labels in the second part of the list/dict
plt.ytickets([0, 2, 4, 5, 8, 10],
             ['0', '2B', '4B', '6B', '8B', '10B'])

plt.show()

##### adding more data
#you cna also add more datapoints to the lists
new_year=[1800, 1900, 1950] + old_year_list
new_pop=[1.0, 1.262, 1.650] + old_pop_list


##### customising

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()


###### changing sizes of dots on a scatter plot

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop=np.array(pop)

# Double np_pop
np_pop=np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


##### changing color and opacity
# changing the opacity is by specifying the alpha value when you create the plot
# to change the color of the datapoints, the code below calls on a dict called col which has mapped colors to country names

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c=col, alpha=0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()


##### more customisation
# this puts the names of India and China on the plot
# the coordinates state where to put these labels
# the plt.grid(True) makes this possible

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()

