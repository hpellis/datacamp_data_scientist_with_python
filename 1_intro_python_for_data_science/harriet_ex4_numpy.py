# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:00:43 2018

@author: 612383249
"""

##### numpy array

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


##### baseball players' height

# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height: np_height_in
np_height_in=np.array(height_in)

# Print out np_height
print(np_height_in)

# Convert np_height to m: np_height_m
np_height_m=np_height_in * 0.0254

# Print np_height_m
print(np_height_m)


##### baseball player's bmi

# height and weight are available as regular lists

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg=np.array(weight_lb)*0.453592

# Calculate the BMI: bmi
bmi=np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)


##### lightweight baseball players

# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light=bmi<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])


##### average vs median

# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in=np.array(np_baseball[:,0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))



##### exploring baseball data

# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1] )
print("Correlation: " + str(corr))


##### more

# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights

np_positions= np.array(positions)
np_heights= np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights=np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights=np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
