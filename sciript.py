# 1. Example for the equal operator in Python
# promo_code = "flash50"
# user_promo_code = input("Enter your promo code: ")

# if user_promo_code == promo_code:
#     print("Promo code applied successfully! You get a 50% discount.") 
# else:
#     print("Invalid promo code. Please try again.")

#-----------------------------------------------------------------------

# 2. Example for the comparison operator in Python
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
    
# 2.1 Apps often compare numbers to decide what to show a user. Using the
# values below, use comparison operators inside f-strings to print a labeled
# result for each check. Your output should look like this:
#   Has unread messages (more than 0): False
#   Old enough to rent a car (25 or older): True
#   Under the $50 free-shipping minimum: True
#   Sold out (0 or fewer tickets left): False
# unread_messages = 0
# car_age = 25
# free_shipping_min = 60
# tickets_left = 10

# print(f"Has unread messages (more than 0): {unread_messages > 0}")
# print(f"Old enough to rent a car (25 or older): {car_age >= 25}")
# print(f"Under the $50 free-shipping minimum: {free_shipping_min > 50}")
# print(f"Sold out (0 or fewer tickets left): {tickets_left <= 0}")

#-----------------------------------------------------------------------

# 3. Example for the if-else statement in Python
# score = int(input("Enter your score: "))
# if score >= 90:
#     print("You got an A!")
# elif score >= 80:
#     print("You got a B!")
# elif score >= 70:
#     print("You got a C!")
# elif score >= 60:
#     print("You got a D!")
# else:
#     print("You got an F!")

# You're building a feature for a coffee shop that has spotty wi-fi. The feature should give
# customers a discount based on how many signal bars they're getting.
# Write an if/elif/else chain that prints a message for the customer's discount:
#   0 bars: "50% off, sorry about the Wi-Fi!"
#   1 or 2 bars: "25% off"
#   3 or 4 bars: "10% off"
#   5 bars: "Full bars, no discount today!"

# signal_bars = int(input("Enter the number of Wi-Fi signal bars (0-5): "))
# if signal_bars == 0:
#     print("50% off, sorry about the Wi-Fi!")
# elif signal_bars == 1 or signal_bars == 2:
#     print("25% off")
# elif signal_bars == 3 or signal_bars == 4:
#     print("10% off")
# elif signal_bars == 5:
#     print("Full bars, no discount today!")
    
#-----------------------------------------------------------------------

# 4. Example for string methods in Python
# You're building a sign-up form that tidies up whatever users type in.
# Each value below comes in messy. Figure out which string method (or
# methods) gets it to the clean version, then print the result. Some need
# just one method, and some need two chained together:
# 1. promo_code    "spring25"             ->  "SPRING25"
# 2. full_name     "jamie rivera"         ->  "Jamie Rivera"
# 3. email         "  Jamie@Example.COM"  ->  "jamie@example.com"
# 4. display_name  "  the ROCK  "         ->  "The Rock"

# promo_code = "spring25"
# full_name = "jamie rivera"
# email = "  Jamie@Example.COM"
# display_name = "  the ROCK  "

# print(promo_code.upper())
# print(full_name.title())
# print(email.strip().lower())
# print(display_name.strip().title())

#------------------------------------------------------------------------
#5. Example for the Tuple data type in Python and unpacking
# A tuple is a collection of values that are ordered and unchangeable. Tuples are defined by enclosing the values in parentheses. You can access individual elements of a tuple using indexing, and you can also unpack the values into separate variables.
# Here's an example of a tuple and how to unpack its values:     
# steel_blue = (70, 130, 180)

#unpacking 
# red, green, blue = steel_blue
# print(red)
# print(green)
# print(blue)

# color_palette = [
#   (70, 130, 180),
#   (240, 128, 128),
#   (60, 179, 113)
# ]

# red, green, blue = color_palette[0]
# print(f"RGB: {red}, {green}, {blue}")

# red, green, blue = color_palette[1]
# print(f"RGB: {red}, {green}, {blue}")

# Build an inventory display feature for a small office supply store.
# 1. Unpack the item and quantity for each entry in the list of tuples.
# 2. Print each item and it's quantity in this format: "notebooks: 42 in stock"

# inventory = [
#     ("notebooks", 42),
#     ("pens", 130),
#     ("staplers", 8),
# ]

# for item, quantity in inventory:
#     print(f"{item}: {quantity} in stock")

#-----------------------------------------------------------------------
# 6. Example for the while loop in Python

# count = 1

# while count <= 5: 
#   if count == 3: 
#     break
#   print(count)
#   count += 1

# TOTAL_LAPS = 10
# lap = 1

# while lap <= TOTAL_LAPS: 
#   print(f"Lap: {lap}")
#   lap += 1

# Challenge: Boarding Passes
# You're building an airport app that prints a boarding pass for each
# passenger on a group booking.
# Write a while loop that prints one line per passenger, like this:
# "Printing boarding pass 1 of 5..."
# "Printing boarding pass 2 of 5..."
# ...and so on until the last passenger.
# Passengers = 5
# passenger = 1

# while passenger <= Passengers:
#     print(f"Printing boarding pass {passenger} of {Passengers}...")
#     passenger += 1


#Output: 
# Printing boarding pass 1 of 5...
# Printing boarding pass 2 of 5...
# Printing boarding pass 3 of 5...
# Printing boarding pass 4 of 5...
# Printing boarding pass 5 of 5...

#------------------------------------------------------------------------
# 7. Example for Append and Remove Methods in Python
# You're building a to-do list app. The user can add tasks to the list and remove tasks that are completed. Write a program that allows the user to add and remove tasks from a list. The program should continue to prompt the user for input until they type 'quit'.
# tasks = []

# tasks.append("Send invoices")
# tasks.append("Book the venue")
# tasks.append("Reply to emails")

# task_item = input("Add an item: ")

# tasks.append(task_item)

# print(tasks)

# Challenge: Game Lobby
# You're building a multiplayer game. Players join the lobby one at a time.
# 1. Start with an empty list called lobby.
# 2. Append these players in order: "Xena", "Thor", "Merlin", "Ripley".
# 3. Print the final list.

# lobby = []
# lobby.append("Xena")
# lobby.append("Thor")
# lobby.append("Merlin")
# lobby.append("Ripley")
# print(lobby)

# Challenge: Raffle Drawing
# Build a feature that manages a charity raffle. The program picks a random winner but
# makes sure nobody wins twice. If the random winner has already won a prize, keep 
# drawing a random winner until you land on someone new.
# 1. Draw a random name from entrants.
# 2. If that name is already in winners, keep drawing until you get one
#    that isn't.
# 3. Add the new winner to winners and print: "Winner: <name>"

# entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
# winners = ["Diego", "Sofia"]

# import random

# name = random.choice(entrants)
# while name in winners:
#     name = random.choice(entrants)
    
# winners.append(name)
# print(f"Winner: {name}")


#------------------------------------------------------------------------
# 8. Example for functions in Python
# Challenge: Write some functions!
# You've very generously decided to pick up coffee for six of your favorite coworkers this morning. 

# 1. Write a function announcing your coffee run. 
# Example output: "I am headed to the coffee shop! Who wants a latte?"

# 2. Write a function to calculate the total cost if you buy them each a latte for $5. In an f string, print how many lattes and what the total comes to.  
# Example output: 
# 6 lattes comes to $30.

# 3. Your coworkers thank you profusely. To save a little time, write a function that prints "You're welcome!" twice, then call it as many times as you need to thank all six coworkers.
# def thank_coworkers():
#     for _ in range(1):
#         print("I am headed to the coffee shop! Who wants a latte?")

# thank_coworkers()

# def calculate_total_cost(num_lattes):
#     cost_per_latte = 5
#     total_cost = num_lattes * cost_per_latte
#     print(f"{num_lattes} lattes comes to ${total_cost}.")

# calculate_total_cost(6)

# Challenge: Write two functions with parameters
# Write each function underneath its instructions, then call it with the values given.

# 1. Write a function called add_numbers that prints the sum of the two numbers you pass in.
#    Call it a couple of times with different numbers.
#    Example output:
#    add_numbers(2, 3) prints 5
#    add_numbers(10, 45) prints 55


# 2. You've scrambled a word before: turn it into a list of letters, shuffle them, and
#    join them back together. Let's make that reusable. Write scramble(word) so it takes
#    any word and prints a scrambled version of it.
#    Example output:
#    scramble("python") might print nohtyp

# import random

# def add_numbers(num1, num2):
#     print(num1 + num2)

# input1 = int(input("Enter first number: "))
# input2 = int(input("Enter second number: "))
# add_numbers(input1, input2)

# def scramble(word):
#     letters = list(word)
#     random.shuffle(letters)
#     scrambled_word = "".join(letters)
#     print(scrambled_word)

# scramble("python")
# o/p
# PS C:\Users\asus\Desktop\Learnings\python\PythonLearning> python sciript.py
# Enter first number: 7
# Enter second number: 8
# 15
# nhoytp


# Challenge: Returning functions 
# For each function, save the result to a variable, then use the result to print an f string.

# 1. Write room_area(length, width) that returns the area of a room. Get the area of a
#    12 by 10 room.
#    Example output:
#    The room is 120 square feet.

# 2. Write add_tax(price) that returns a price with 8% tax added (multiply by 1.08). Get
#    the total for a $50 item.
#    Example output:
#    With tax, that comes to $54.0.

# 3. Write full_name(first, last) that returns a first and last name joined with a space.
#    Use it to build a name, then print a greeting with it.
#    Example output:
#    Welcome, Mike Reed!

# def room_area(length, width):
#     return length * width

# def add_tax(price):
#     return price * 1.08

# def full_name(first, last):
#     return f"{first} {last}"

# print(f"The room is {room_area(12, 10)} square feet.")
# print(f"With tax, that comes to ${add_tax(50)}.")   
# print(f"Welcome, {full_name('Mike', 'Reed')}!")

#------------------------------------------------------------------------
# 9. Example for the For loop in Python

# Challenge: Award Night!
# It's awards night, and here are the nominees for Best New App. The list can grow or
# shrink year to year, so your program shouldn't care how many names are on it.

# nominees = ["PixelPal", "TaskTanic", "SnackMap", "MoodTunes"]

# 1. Loop over the nominees and print each one on its own line, formatted like the
#    example below so it reads like a real program.
#    Each line should look like:
#    Nominated for Best New App: PixelPal

# for nominee in nominees:
#     print(f"Nominated for Best New App: {nominee}")

# 2. After the loop, print one closing line: "And those are your nominees!"
#    It should print just once, after all the names.

# print("And those are your nominees!")

# Challenge: Festival Lineup
# Each act in this festival lineup is a tuple: the band, their genre, and how many
# minutes they play.

lineup = [
    ("The Wailers", "reggae", 45),
    ("Daft Punk", "electronic", 90),
    ("Adele", "pop", 60),
    ("Metallica", "metal", 100),
]

# Loop over the lineup, unpacking each act into band, genre, and minutes. Use if/else to
# print a "long set" line for any act playing 90 minutes or more, and a normal line for
# the rest:
#    The Wailers (reggae) plays 45 minutes
#    Daft Punk (electronic) plays a long set: 90 minutes
#    Adele (pop) plays 60 minutes
#    Metallica (metal) plays a long set: 100 minutes

for band, genre, minutes in lineup:
    if minutes >= 90:
        print(f"{band} ({genre}) plays a long set: {minutes} minutes")
    else:
        print(f"{band} ({genre}) plays {minutes} minutes")
        
print("And that's the festival lineup!")