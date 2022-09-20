
from os import supports_effective_ids
from telnetlib import theNULL


# The question I have is based around dictionaries and getting stuff out of them.
# I don't know if what I want to do is possible, so before I go about looking to 
# figure out how to do an impossible thing on the internet. 

# Suppose you have a complex dictionary - maybe a dictionary with nested dictionaries.
# You want to check some kind of input against the contents of the dictionary - but only 
# some sections of the dictionary. 

# Take the following situation as an example to demonstrate what I am looking to do.
# You have a request to make some kind of app that will take input from a user and then 
# return whether that day is a weekday or on the weekend. 

# The way I want to solve the problem is by building a dictionary and then check the input 
# from the user against that dictionary. I solved the problem for class by building a simple 
# dictionary and then filled two different lists with information from the dictionary and 
# checked the input against the list. I would like to be able to do it by checking the 
# dictionary's contents by referencing it's keys. 


week_dict = {   # dictionary with a few items related to days of the week
    1 : 'sunday',
    2 : 'sun',
    3 : 'monday',
    4 : 'm',
    5 : 'tuesday',
    6 : 't',
    7 : 'wednesday',
    8 : 'w',
    9 : 'thursday',
    10: 'th',
    11: 'friday',
    12: 'f',
    13: 'saturday',
    14: 'sat'
}




weekday =[] # filled list with items from week dictionary
for i in range(3,13):
   weekday.append(week_dict[i])
weekend =[] # filled list with items from week dictionary
for i in range(1,2):
    weekend.append(week_dict[i])
for i in range(13,14):
    weekend.append(week_dict[i])



# this section is how I solved the problem. 


    # a is a dummy variable that may be repeated whenever I need to fill and use immediately
a = input('What day of the week is it?')
if a in weekday:
    print(f'{a} is a weekday')
elif a in weekend:
        print(f'{a} is a weekend day')


# What I would want to do, however - because it seems like something that would be very useful 
# in the future - is to take input from the user, and then do an if then statement that references
# a range of keys in order to check the input against the values that those keys reference. So, 
# I would want to do something like " if a = week_dict[range(1-2)]: then ..."

# Is that possible? How would you do it? 