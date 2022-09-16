from operator import truediv
import os
def clear_console():
    os.system('clear')
clear_console()


# ██████╗░███████╗░██████╗░██╗███╗░░██╗  ███████╗██╗░░██╗███████╗██████╗░░█████╗░██╗░██████╗███████╗
# ██╔══██╗██╔════╝██╔════╝░██║████╗░██║  ██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝
# ██████╦╝█████╗░░██║░░██╗░██║██╔██╗██║  █████╗░░░╚███╔╝░█████╗░░██████╔╝██║░░╚═╝██║╚█████╗░█████╗░░
# ██╔══██╗██╔══╝░░██║░░╚██╗██║██║╚████║  ██╔══╝░░░██╔██╗░██╔══╝░░██╔══██╗██║░░██╗██║░╚═══██╗██╔══╝░░
# ██████╦╝███████╗╚██████╔╝██║██║░╚███║  ███████╗██╔╝╚██╗███████╗██║░░██║╚█████╔╝██║██████╔╝███████╗
# ╚═════╝░╚══════╝░╚═════╝░╚═╝╚═╝░░╚══╝  ╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝╚═════╝░╚══════╝



# 1. You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know 
# yet if they're going to like it). If price for a movie per day is 3 dollars, 
# how much will you have to pay?

lm = 3
bb = 5
her= 1
price = 3

print('Price for rentals',(lm+bb+her)*price)


# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? You worked 10 
# hours for Facebook, 6 hours for Google and 4 hours for Amazon.

goog = 400
amaz = 380
face = 350
hours= [10, 6, 4]
pay = goog*hours[0]+amaz*hours[1]+face*hours[2]
print('You got paid! How much did those tech giants pay this week? $',pay)


# 3. A student can be enrolled to a class only if the class is not full and the class schedule 
# does not conflict with her current schedule.

class_conflict = False
class_full = False

print('Can you enroll in the class?',class_conflict and class_full)


# 4. A product offer can be applied only if people buys more than 2 items, and the offer 
# has not expired. Premium members do not need to buy a specific amount of products.

items_more_than_2 = True
offer_expired = False 
member = True 

print('Does the person qualify for the offer?',(items_more_than_2 or member) and offer_expired)



# 5. Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_long_enough = len(username) < 5
username_good_length = len(username) < 21 and len(username) > 0
name_password_check = username != password 

print('Does this username and password pass the check?',password_long_enough and username_good_length and name_password_check)