# CS 122 Fall 2025 Project 2 - Travel Time Calculator
# Author: Your Name
# Credit: (Partner or online help, or 'None')
# Description: Compares travel times given distance and speed
# References:
# - https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php

# Return travel time in minutes
def calc_travel_time(distance, speed):
    # TODO: Calculate and return the travel time (try to use a single line of code)
    return (distance / speed) * 60

#print(calc_travel_time(90, 55))

# Print travel time in hr, min, sec
def print_travel_time(distance, speed):
    # TODO: Calculate total minutes using calc_travel_time()
    total_min = calc_travel_time(distance, speed)
    # TODO: Calculate hours
    hrs = int(total_min // 60)
    # TODO: Calculate minutes
    mins = int(total_min % 60)
    # TODO: Calculate seconds
    seconds = round((total_min - int(total_min))*60)
    # TODO: Output distance, speed, hours, minutes and seconds in required format
    print("To travel", distance, "miles at", speed, "MPH will take", hrs, "hr,", mins, "min and", seconds, "sec.")

# --- Test Section ---
print_travel_time(90, 55)
print_travel_time(90, 70)
print_travel_time(10, 25)
print_travel_time(10, 35)