# CS 122 Fall 2025 Lab 5
# Author: Quinn SMiley
# Credit: None
# Description: Series of labs

#Challenge 1: Inclusive Greeting (Boolean Functions)
def is_morning(hour):
    if hour in range(0, 12):
        return True
    else: 
        return False
    
#print(is_morning(11))

# def greeting(hour):
#     if is_morning(hour) == True:
#         return "Good Morning!"
#     else:
#         return "Good day!"
    
#print(greeting(12))



#Challenge 2: Optional Pronouns (Optional Parameters)
def introduce(name, pronouns="they/them"):
    greeting = "Hi, I'm " + name + " and my pronouns are " + pronouns + "."
    return greeting

#print(introduce("Quinn"))
#print(introduce("Quinn", "she/her"))



#Challenge 3: Safe Parameters and Division (Guardian Pattern)
def average_hours(total_hours, num_people):
    if not isinstance(total_hours, (int, float)) or num_people <= 0:
        return None
    else:
        return total_hours / num_people
    
#print(average_hours(6.0, 3))
#print(average_hours(5.0, 0))
#print(average_hours(4.0, str(3))) - caused TypeError
#print(average_hours(str(4.0), 8))



#Challenge 4: Health Check (Single Return)
def check_hydration(glasses_of_water):
    status = 'Low'
    if glasses_of_water >= 8:
        status = "Excellent"
    elif glasses_of_water >= 5:
        status = "Needs more"
    return status

#print(check_hydration(9))
#print(check_hydration(7))
#print(check_hydration(4))



#Challenge 5: Weather Message (Incremental Development & Scaffolding)
# def weather_advice(temp_f, raining):
#     "V1 scaffold:"
#     return "Check the weather"

#print(weather_advice(5, 4))

# def weather_advice(temp_f, raining):
#     "V2 add basic rules:"
#     if temp_f < 50:
#         return "Wear a jacket"
#     else:
#         return "Dress comfortably"
    
#print(weather_advice(45, 0))
#print(weather_advice(50, 0))

def weather_advice(temp_f, raining):
    if temp_f < 50 and raining:
        return "Bring an umbrella and a warm jacket"
    elif temp_f >= 50 and raining:
        return "Bring an umbrella and light layers"
    elif temp_f < 50 and not raining:
        return "Wear a warm jacket"
    else: 
        return "Looks good, dress comfortably"

# print(weather_advice(45, True))
# print(weather_advice(50, True))
# print(weather_advice(45, False))
# print(weather_advice(60, False))



#Challenge 6: The Compliment Machine (Composing Functions)
import random
def get_random_number(low, high):
    return random.randint(low, high)

#print(get_random_number(1, 100))

def choose_phrase(num):
    phrase = ''
    if num == 1:
        phrase = "You're doing great!"
    elif num == 2:
        phrase = "Keep being awesome!"
    elif num == 3:
        phrase = "You make a difference!"
    elif num == 4:
        phrase = "Your effort matters!"
    elif num == 5:
        phrase = "You've got this!"
    return phrase

#print(choose_phrase(3))

def positive_message(name):
    num = get_random_number(1, 6)
    phrase = choose_phrase(num)
    return "Hi, " + name + ", " + phrase

#print(positive_message("Quinn"))



#Challenge 7: Event Planner (Multiline Logic)
def should_schedule_event(guests, forecast = "clear", outdoor = True):
    schedule_event = False
    if forecast != "stormy" and (not outdoor or guests <50):
        schedule_event = True
    return schedule_event
# print(should_schedule_event(30, "clear", True))
# print(should_schedule_event(10, "stormy", False))



#Challenge 8: Lost and Found (Returning None)
def find_item(owner_name):
    if owner_name == "Jordan":
        return "Found: water bottle (" + owner_name
    else: 
        return None

#print(find_item("Jordan"))
#print(find_item("Taylor"))

# note = find_item("Taylor")
# if note is None: 
#     print("No item found")
# else: 
#     print(note)




#Challenge 9: Budget Helper (Temporary Variables)
def calculate_budget(income, rent, groceries, misc):
    total_expenses = rent + groceries + misc
    savings = income - total_expenses
    return savings

#print(calculate_budget(2000, 900, 400, 250))
#print(calculate_budget(misc = 250, groceries = 400, rent = 900, income = 2000))




#Challenge 10 Kind Notes Pipeline (Composition, Clarity, Realistic)
def make_greeting(name, pronoun = "they/them"):
    """
    Purpose: To create a greeting that includes the name and pronouns given by a person
    Arguments: 
        name (str): name of person
        pronoun (str): pronouns of person (defaults to they/them)
    Returns: string
    """
    phrase = 'Hi, '
    return phrase + name + " (" + pronoun + ")"

#print(make_greeting("Jordan"))
#print(make_greeting("Sam", "she/her"))

def add_appreciation(message, context):
    """
    Purpose: To append context to a message
    Arguments: 
        message (str): name of person
        context (str): context for message
    Returns: string
    """
    return message + " - " + context

#print(add_appreciation("Sam", "thanks for your help!"))

greeting = make_greeting("Tony")
appreciation = add_appreciation(greeting, "great job today!")
#print(appreciation)

print(add_appreciation(make_greeting("Tony"), "great job today!"))