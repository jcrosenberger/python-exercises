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

############################################################################################
################################## Conditional Basics ######################################
############################################################################################



week_dict = {
    1 : 'Sunday',
    2 : 'sun',
    3 : 'Monday',
    4 : 'm',
    5 : 'Tuesday',
    6 : 't',
    7 : 'Wednesday',
    8 : 'w',
    9 : 'Thursday',
    10: 'th',
    11: 'Friday',
    12: 'f',
    13: 'Saturday',
    14: 'sat'
}
# weekend = list(week_dict.keys())[range(12)]
weekday =[]
for i in range(3,13):
   weekday.append(week_dict[i])
weekend =[]
for i in range(1,2):
    weekend.append(week_dict[i])
for i in range(13,14):
    weekend.append(week_dict[i])

################### a. ###################

# a is a dummy variable to fill over and again in this exercise
a = input('What day of the week is it?')
if a == week_dict[3] or a == week_dict[4]:
    print(f'{a} is Monday')
else:
        print(f'{a} is not Monday')


################### b. ###################

a = input('What day of the week is it?')
if a in weekday:
    print(f'{a} is a weekday')
elif a in weekend:
        print(f'{a} is a weekend day')


################### c. ###################


hours_worked = 45
pay_per_hour = 100
weekly_earnings = 0

if hours_worked > 40:
    weekly_earnings = (hours_worked-40)*pay_per_hour*1.5 + 40*pay_per_hour
else: 
    weekly_earnings = hours_worked*pay_per_hour
print(f'{weekly_earnings}')



############################################################################################
##################################    Loop Basics     ######################################
############################################################################################


################### a. ###################

i = 5
while i <= 15:
    print(i)
    i +=1

i = 0
while i <102:
    print(i)
    i +=2

i = 100
while i >= -15:
    print(i)
    i -= 5

i = 2
while i < 1000000:
    print(i)
    i *= i

i = 100
while i > 0:
    print(i)
    i -= 5


################### b. ###################

a = int(input('Pick a number, any number (please not a giant number)'))
for i in range(1,11):
    print(f'{a} * {i} = {a*i}')


for i in range (1,10):
    print(f'{str(i)*i}')


################### c. ###################

a = int(input('Pick a number, any positive number (please not a giant number)'))
while a > 0:
    print(f'{a}')
    a -= 1