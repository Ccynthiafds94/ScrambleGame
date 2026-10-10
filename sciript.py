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
