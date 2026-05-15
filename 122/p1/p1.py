# CS 122 Fall 2025 Project 1
# Author: Quinn Smiley
# Credit: Sources or 'None'
# Description: Introductory problem set exploring Python variables, expressions, and pseudocode

import math


##### Question 1 #####

# Initialize variables with values

children = 70
adults = 80
slices_per_child = 3
slices_per_adult = 2
slices_per_watermelon = 14
extra = 0.25

# Calculate total number of watermelon slices and display number of slices

total_slices = (children * slices_per_child) + (adults * slices_per_adult)
print("Total slices:", total_slices)

# Add extra amount and display number of slices

total_slices = total_slices + (total_slices * extra)
print("Total slices (including extra):", total_slices)

# Calculate number of watermelons and display number of watermelons

watermelons = total_slices / slices_per_watermelon
print("Total watermelons:", watermelons)

# Round the number of watermelons up and display number of watermelons

watermelons = math.ceil(watermelons)
print("Total watermelons (rounded up):", watermelons)




#### Question 2 ####

#Variables - 50
steps_per_floor = 14
floors = 4
one_trip = 112
target_steps = 50

#Target - 50
hit_target = (target_steps / one_trip)
trips = math.ceil(hit_target)
print('To reach', target_steps, 'steps:', trips, 'trip(s)')



#Variables - 100
steps_per_floor = 14
floors = 4
one_trip = 112
target_steps = 100

#Target - 100
hit_target = (target_steps / one_trip)
trips = math.ceil(hit_target)
print('To reach', target_steps, 'steps:', trips, 'trip(s)')



#Variables - 200
steps_per_floor = 14
floors = 4
one_trip = 112
target_steps = 200

#Target - 200
hit_target = (target_steps / one_trip)
trips = math.ceil(hit_target)
print('To reach', target_steps, 'steps:', trips, 'trip(s)')



#Variables - 500
steps_per_floor = 14
floors = 4
one_trip = 112
target_steps = 500

#Target - 500
hit_target = (target_steps / one_trip)
trips = math.ceil(hit_target)
print('To reach', target_steps, 'steps:', trips, 'trip(s)')



#Variables - 1000
steps_per_floor = 14
floors = 4
one_trip = 112
target_steps = 1000

#Target - 1000
hit_target = (target_steps / one_trip)
trips = math.ceil(hit_target)
print('To reach', target_steps, 'steps:', trips, 'trip(s)')



#### Question 3 ####

#Variables
cp_r_ft = 1200
cp_num = 6
insp_per_day = 2
days_per_week = 5
ft_per_mile = 5280

#Calculate
cp_circumference = (2 * math.pi * cp_r_ft)
weekly_distance_ft = (cp_circumference * insp_per_day * cp_num * days_per_week)
weekly_distance = (cp_circumference * insp_per_day * cp_num * days_per_week) / ft_per_mile

#Round
print('Weekly distance (feet):', round(weekly_distance_ft, 2))
print('Weekly distance (miles):', round(weekly_distance, 2))