# CS 122 Fall 2025 Project 2 - Cement Calculator
# Author: Quinn Smiley
# Credit: (Partner or online help, or 'None')
# Description: Calculates cement volume in cubic yards for two slabs.
# References:
# - https://www.calculator.net/concrete-calculator.html
# - https://www.calculator.net/volume-calculator.html

import math

# Return cement amount in yards using thickness (t), width (w), and length (l) in inches
def calc_yards_cement(t, w, l):
    # TODO: Calculate the amount of cubic inches in a yard using math.pow()
    cubic_yard_in = math.pow(36, 3)
    # TODO: Calculate the total inches
    total_vol_in = (t * w * l)
    # TODO: Calculate the number of yards of cement to two decimal places using round()
    total_vol_yards = total_vol_in / cubic_yard_in
    result = round(total_vol_yards, 2)
    # TODO: Return the number of yards
    return result

#print(calc_yards_cement(4, 72, 120))

# Output results of calculating cement yards
def print_results(t, w, l):
    # TODO: Call calc_yards_cement() with t, w, l and assign to variable
    yards_needed = calc_yards_cement(t, w, l)
    # TODO: Output the results in required format
    print("A cement slab", t, "thick", w, "wide and", l, "long requires", yards_needed, "cubic yards of cement.")

# --- Test Section ---
print_results(4, 72, 120)
print_results(4, 120, 240)