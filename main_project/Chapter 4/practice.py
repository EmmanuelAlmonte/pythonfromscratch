import turtle

# 1. Bug Collector


"""
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.

"""
"""
total_bugs_collected = 0


for x in range(5):
    bugs_collected = int(input("Enter the amount of bugs collected: "))
    total_bugs_collected += bugs_collected

print("You collected {} bugs.".format(total_bugs_collected))
"""

# 2. Calories Burned

"""
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
"""
"""
calories_burned = 4.2

TIME = 10

while TIME < 35:
    print("The amount of calories burned in {} minutes is {}".format(TIME, (calories_burned * TIME)))
    TIME += 5  
"""

# 3 Lap Times
"""
Write a program that asks the user to enter the number of times that they have run around
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.
When the loop finishes, the program should display the time of their fastest lap, the time of
their slowest lap, and their average lap time.
"""
"""
# Get the number of laps ran.
num_of_laps = int(input("Enter the amount of laps run: "))
# This holds all the lap time
total_lap_time = []
# This for loop prompts user to enter their times
for x in range(num_of_laps):
    lap_time = int(input("Enter the time of lap {}: ".format(x)))
    total_lap_time.append(lap_time)
# Fastest and slowest times.
fastest_time = total_lap_time[0]
slowest_time = total_lap_time[0]

# Calculate the average time.
all_times =  0

for x in total_lap_time:
    all_times += x 

# calculate the fastest time.
for x in total_lap_time:
    if x < fastest_time:
        fastest_time = x

# Calculate the slowest time.
for x in total_lap_time:
    if x > slowest_time:
        slowest_time = x 

print("The fastest_time:{}".format(fastest_time),"\nThe slowest:{}".format(slowest_time),"\nThe average of all times: {}".format(all_times / len(total_lap_time)))
"""

#4. Distance Traveled
"""
The distance a vehicle travels can be calculated as follows:

distance = speed x time

For example, if a train travels 40 miles per hour for three hours, the distance traveled is
120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour)
and the number of hours it has traveled. It should then use a loop to display the distance
the vehicle has traveled for each hour of that time period. Here is an example of the desired
output:
"""
"""
speed_of_vehicle = int(input("Enter the vehicle speed in mph: "))
hours_traveled = int(input("Enter the amount of hours you have traveled: "))
print("""
#Hour\tDistance Traveled 
#----------------------------- 
""")
for x in range(hours_traveled):
    print(x + 1, "\t", (speed_of_vehicle * (x + 1)))
"""
# 5. Average Rainfall

"""
Write a program that uses nested loops to collect data and calculate the average rainfall over
a period of years. The program should first ask for the number of years. The outer loop will
iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.
"""
"""

num_of_years = int(input("Enter the number of years: "))

total_rainfall = 0

amount_of_rain_for_month = []
months = 12

for y in range(num_of_years):
    amount_of_rain_for_month = []
    for m in range(months):
        inches_in_rainfall = int(input("Enter the amount of inches in rainfall for month {}: ".format(m + 1)))
        amount_of_rain_for_month.append(inches_in_rainfall)
        total_rainfall += inches_in_rainfall
    
    print("There were {} months\n the total inches in rain: {}\nThe average was {}".format(months * (y + 1), total_rainfall, (total_rainfall / months * (y + 1)))) 

"""

# 6. Miles to Kilometers Table
"""
Write a program that displays a table of distances in miles and their equivalent distances in
kilometers, rounded to 2 decimal places. One mile is equivalent to 1.60934 kilometers. The
table should be generated using a loop, and should include values in 10 mile increments from
10 to 80.
"""
"""
# Print the table 

print("Miles\tKilometers\n-------------------")

for m in range(10, 81, 10):
    print(m,"\t",round((m * 1.609), 2))
"""
# 7. Pennies for pay
"""
Write a program that calculates the amount of money a person would earn over a period of
time if his or her salary is one penny the first day, two pennies the second day, and contin-
ues to double each day. The program should ask the user for the number of days. Display
a table showing what the salary was for each day, then show the total pay at the end of the
period. The output should be displayed in a dollar amount, not the number of pennies.
"""
"""
# ask the user the number of days the penny will accumulate
num_of_days = int(input("Enter the number of days: "))
# The table is being displayed  
print("Days \t Pennies")
pennies = 1
dollars = 0

# iterate through the number of days user entered. 
for p in range(num_of_days):    
    # Determine if the amount of pennies is over 100, if so convert to dollars and print in that format.
    if pennies > 100:
        dollars = pennies / 100 
        print(p + 1,"\t", format( dollars, ','))
    else:
        # Print in the pennies only format if the amount of pennies is less than 100.
        print(p + 1,"\t",".",pennies)
    pennies *= 2    
"""
# 8. Average word Length
"""
Write a program with a loop that repeatedly asks the user to enter a word. The user should
enter nothing (press Enter without typing anything) to signal the end of the loop. Once the
loop ends, the program should display the average length of the words entered, rounded to
the nearest whole number.
"""
"""
# create a list with the words user entered.

user_words = []
average_len_of_words = 0
# Capture user input.
words_entered = input("Enter a word: ")
user_words.append(words_entered)
# Determine whether input was just enter or a word.

while words_entered != "":
    enter_another_word = input("Enter another word: ")
    if enter_another_word == "":
        break
    else: 
        user_words.append(enter_another_word)
        continue

for words in user_words:
    average_len_of_words += len(words)

if len(user_words) != 0:
    print("The average length of words: {}".format(average_len_of_words / len(user_words)))
"""
# 9. Ocean Levels
"""
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
application that displays the number of millimeters that the ocean will have risen each year
for the next 25 years.
"""
"""
ocean_level = 0

for years in range(25):
    print("The ocean level at year {} is {}".format(years + 1,round(ocean_level, 2)))
    ocean_level += 1.6  
"""
# 10 Tuition Increase
"""
full_time_tuition = 8_000
inter_rate = .03
for years in range(5):
    print("Year {}".format(years + 1),"Tution cost: {}".format(round(full_time_tuition, 2)))
    full_time_tuition += full_time_tuition * inter_rate
"""
# 11. Sleep Debt
"""
A “sleep debt” represents the difference between a person’s desirable and actual amount
of sleep. Write a program that prompts the user to enter how many hours they slept each
day over a period of seven days. Using 8 hours per day as the desirable amount of sleep,
determine their sleep debt by calculating the total hours of sleep they got over the seven-day
period and subtracting that from the total hours of sleep they should have got. If the user
does not have a sleep debt, display a message expressing your jealousy.
"""
"""
total_sleep_hours = 0

for days in range(7):
    hours_of_sleep = int(input("Enter the hours of sleep for day {}: ".format(days +1)))
    total_sleep_hours += hours_of_sleep
    if total_sleep_hours >= (8 * 7): 
        print("Nice your got enough sleep")

"""
# 12. Calculating the Factorial of a Number
"""In mathematics, the notation n! represents the factorial of the nonnegative integer n. The
factorial of n is the product of all the nonnegative integers from 1 to n. For example,
"""
"""
enter_a_factorial = int(input("Enter a factorial: "))

total_sum_of_factorial = 1

for n in range(1,(enter_a_factorial + 1)):
   total_sum_of_factorial *= n  


print(total_sum_of_factorial)
"""

# 13 Population 

"""
Write a program that predicts the approximate size of a population of organisms.
The application should use text boxes to allow the user to enter the starting number of organ-
isms, the average daily population increase (as a percentage), and the number of days the
organisms will be left to multiply. For example, assume the user enters the following values:
"""

# starting amount of organisms in the populaion.
start_num_of_organisms = int(input("Enter the start number of population: "))

# Average of the daily increase
average_daily_increase = int(input("Enter the percentage at which the populations increases: "))

# Number of days to multiply 
num_of_days_to_multi = int(input("Enter the number of days the population will mulitply: "))

# Display title
print("Day Approximate\tPopulation")

# Population growth 
population = 0
average_daily_increase = average_daily_increase / 100
for n in range(num_of_days_to_multi): 
    print(n + 1, "\t", start_num_of_organisms)
    population = start_num_of_organisms **((average_daily_increase * n + 1))
    start_num_of_organisms = population

"""
# This program displays a triangle pattern.
BASE_SIZE = 8
for r in range(BASE_SIZE, 1, -1):
    for c in range(r - 1):
        print('*', end='')
    print()

"""