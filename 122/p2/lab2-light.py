# CS 122 Fall 2025 Lab 2 Challenge
# Author: Quinn Smiley
# Credit: None
# Description: Calculate the time light takes to reach planets from the Sun

# Step 1: Define speed of light and distances to Earth and Jupiter
# Step 2: Create a fruitful function to calculate travel time
# Step 3: Create a void function to print the result
# Step 4: Call the void function for Earth and Jupiter

#Challenge

#Values:
#Speed of light: 186,282 miles/sec
#Distance to Earth: 93,000,000 miles
#Distance to Jupiter: 484,000,000 miles

#My Solution
#dist_to_earth = 93000000
#dist_to_jupiter = 484000000

#def trvl_time(num):
    #sol = 186282
    #result = num / sol
    #return result

#print("Light travels from the sun to the Earth an average of", round(trvl_time(dist_to_earth), 2), "seconds.")
#print("Light travels from the sun to Jupiter an average of", round(trvl_time(dist_to_jupiter), 2), "seconds.")

# Step 1: Define speed of light and distances to Earth and Jupiter
SPEED_OF_LIGHT = 186282  # miles per second
SUN_EARTH_DISTANCE = 93000000
SUN_JUPITER_DISTANCE = 484000000

# Step 2: Fruitful function
def avg_light_travel_seconds(distance_miles):
    return round(distance_miles / SPEED_OF_LIGHT, 2)

# Step 3: Void function
def print_results(planetary_object, time_to_object):
    print("Light travels from the sun to", planetary_object, "an average of", time_to_object, "seconds.")

# Step 4: Call the functions
print_results("the Earth", str(avg_light_travel_seconds(SUN_EARTH_DISTANCE)))
print_results("Jupiter", str(avg_light_travel_seconds(SUN_JUPITER_DISTANCE)))
