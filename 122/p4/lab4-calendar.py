# CS 122 Fall 2025 Lab 4
# Author: Quinn SMiley
# Credit: None
# Description: Functions practice w dates


# Months
def get_full_month(month_num):
    name = ""
    if month_num < 1: 
        print("Must be an integer between 1 and 12 (" + str(month_num) + " is invalid).")
    elif month_num == 1: 
        name = "January"
    elif month_num == 2: 
        name = "February"
    elif month_num == 3: 
        name = "March"
    elif month_num == 4: 
        name = "April"
    elif month_num == 5: 
        name = "May"
    elif month_num == 6: 
        name = "June"
    elif month_num == 7: 
        name = "July"
    elif month_num == 8: 
        name = "August"
    elif month_num == 9: 
        name = "September"
    elif month_num == 10: 
        name = "October"
    elif month_num == 11: 
        name = "November"
    elif month_num == 12: 
        name = "December"
    else: 
        print("Must be an integer between 1 and 12 (" + str(month_num) + " is invalid).")

    print(month_num, name)
    

def test_get_full_month():
    for n in range(0, 14):
        get_full_month(n)

test_get_full_month()


# Leap Year
def is_leap_year(year):
    is_leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap = True
        else:
            is_leap = True

    return is_leap
            
def test_leap_year(start_year, end_year):
    for n in range(start_year, end_year):
        if is_leap_year(n):
            print(n)

test_leap_year(1996, 2113)