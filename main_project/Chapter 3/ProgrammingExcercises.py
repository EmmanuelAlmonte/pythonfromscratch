#Programming exercises

# 1. Number Analyser

"""
# 1. Number Analyser
Write a program that asks the user to enter an integer. The program should display
“Positive” if the number is greater than 0, “Negative” if the number is less than 0, and
“Zero” if the number is equal to 0. The program should then display “Even” if the number
is even, and “Odd” if the number is odd.

user_integer = int(input("Enter a number: "))

# Determine if user input is greater than 0 or not.
if user_integer < 0:
    print("Number is less than zero.")
elif user_integer > 0:
    print("Number is greater than zero.")
else:
    print("Number is equal to zero.")

if user_integer % 2 == 0:
    print("Number is also even.")
else:
    print("Number is also odd.")

"""
# 2. Areas of Rectangle
"""
# 2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectan-
gle has the greater area, or if the areas are the same.
"""
"""
# Length and width of the rectangle 0 = 1 and 1 = 2 second rectangle.
length_of_rectangle = []
width_of_rectangle = []
num_of_rec = 2

while num_of_rec > 0:
    rectangle_user_Length = int(input("Enter the length of a rectangle: "))
    rectangle_user_width = int(input("Enter the width of a recangle: "))

    length_of_rectangle.append(rectangle_user_Length)
    width_of_rectangle.append(rectangle_user_Length)
    
    num_of_rec -= 1

if (length_of_rectangle[0] * width_of_rectangle[0]) > (length_of_rectangle[1] * width_of_rectangle[1]):
    print("the first rectangel has a bigger area. \n Area {}".format(length_of_rectangle[0] * width_of_rectangle[0]))
elif (length_of_rectangle[0] * width_of_rectangle[0]) < (length_of_rectangle[1] * width_of_rectangle[1]):
    print("the second   rectangel has a bigger area. \n Area {}".format(length_of_rectangle[1] * width_of_rectangle[1]))
else:
    print("They are both equal.")
"""

# 3. Quarter of the Year

"""
Write a program that asks the user for a month as a number between 1 and 12. The
program should display a message indicating whether the month is in the first quarter,
the second quarter, the third quarter, or the fourth quarter of the year. Following are the
guidelines:

If the user enters either 1, 2, or 3, the month is in the first quarter.
If the user enters a number between 4 and 6, the month is in the second quarter.
If the number is either 7, 8, or 9, the month is in the third quarter.
If the month is between 10 and 12, the month is in the fourth quarter.
If the number is not between 1 and 12, the program should display an error.
"""
"""
user_enter_month = int(input("Enter a month of the year (1-12): "))

if user_enter_month <= 3:
    print("The month is in the first quarter")
elif user_enter_month >= 4 and user_enter_month <= 6:
    print("The month is in the second quarter")
elif user_enter_month <= 9:
    print("The month is in the third quarter")
elif user_enter_month <= 12:
    print("The month is in the fourth quarter")
else:
    print("Error number is not between 1 - 12")
"""


# 4. Roman Numerals
"""

Write a program that prompts the user to enter a number within the range of 1 through 10.
The program should display the Roman numeral version of that number. If the number is
outside the range of 1 through 10, the program should display an error message. The fol-
lowing table shows the Roman numerals for the numbers 1 through 10:
"""
"""
user_num_to_roman = int(input("Enter a number 1-10 to convert to Roman Numeral: "))

if user_num_to_roman == 1:
   print("\u2160")
elif user_num_to_roman == 2:
    print("\u2161")
elif user_num_to_roman == 3:
    print("\u2162")
elif user_num_to_roman == 4:
    print("\u2163")
elif user_num_to_roman == 5:
    print("\u2164")
elif user_num_to_roman == 6:
    print("\u2165")
elif user_num_to_roman == 7:
    print("\u2166")
elif user_num_to_roman == 8:
    print("\u2167")
elif user_num_to_roman == 9: 
    print("\u2168")
elif user_num_to_roman == 10:
    print("\u2169")
else:
    print("Not a number 1-10")

"""

#5. Mass and Weight

"""

Scientists measure an object’s mass in kilograms and its weight in newtons. If you know
the amount of mass of an object in kilograms, you can calculate its weight in newtons with
the following formula:
weight = mass X 9.8
Write a program that asks the user to enter an object’s mass, then calculates its weight. If
the object weighs more than 500 newtons, display a message indicating that it is too heavy.
If the object weighs less than 100 newtons, display a message indicating that it is too light."""
"""
mass = int(input("Enter the mass of the object: "))

weight = mass * 9.8

if weight <= 100:
    print("Too light!")
elif weight >= 500:
    print("Too heavy!")
else:
    print("Object weight is fine.")
"""

#6. Magic Dates

"""
The date June 10, 1960, is special because when it is written in the following format, the
month times the day equals the year:
6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two-
digit year. The program should then determine whether the month times the day equals the
year. If so, it should display a message saying the date is magic. Otherwise, it should display
a message saying the date is not magic.
"""
"""
user_month = int(input("Enter a month: "))
user_day = int(input("Enter a day: "))
user_year = int(input("Enter 2 digit year: "))

if user_month * user_day == user_year:
    print("The date is magic")
else:
    print("The date is not magic")


"""
# 7. Grade Calculator
"""
A class has two tests worth 25 points each along with a main exam worth 50 points. For a stu-
dent to pass the class, they must obtain an overall score of at least 50 points, and must obtain at
least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than
25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows:
If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
If they get less than 80 but more than 60, they get a “Credit” grade.
If they get less than 60, they get a ”Pass” grade.
Write a program that prompts the user to enter their points for both tests and the exam and
converts the values to integers. The program should first check if the points entered for the
tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam
score is not between 0 and 50, the program should display an error message. Otherwise,
the program should display the total points and the grade.
"""
"""
user_enter_grade = int(input("Enter you overall class score: "))
user_enter_test_score = int(input("Enter your test score: "))

if user_enter_grade < 50 or user_enter_test_score < 25:
    print("Fail!!")
elif user_enter_grade > 80: 
    print("Distinction, Pass")
elif user_enter_grade < 80 and user_enter_grade > 60:
    print("Credit")
else:
    print("Pass")

"""

# 8. Hot Dog Cookout Calculator

"""Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
program that calculates the number of packages of hot dogs and the number of packages of
hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
should ask the user for the number of people attending the cookout and the number of hot
dogs each person will be given. The program should display the following details:
The minimum number of packages of hot dogs required
The minimum number of packages of hot dog buns required
The number of hot dogs that will be left over
The number of hot dog buns that will be left over"""

"""
num_of_people_attending = int(input("Enter the number of people attending: "))
num_of_hot_dogs_per_people = int(input("How many hot dogs per person: "))

total_hotdogs = num_of_hot_dogs_per_people * num_of_people_attending

hotdog_bun_pack = 8
hotdog_pack = 10

num_of_hotdog_needed = total_hotdogs // hotdog_pack
num_of_hotdog_bun_needed = total_hotdogs // hotdog_pack
num_of_hotdog_remaining = total_hotdogs % hotdog_pack
num_hotdog_bun_remaining = total_hotdogs % hotdog_bun_pack

print("The number of hotdog packs needed {}".format(num_of_hotdog_needed))
print("The number of hotdog bun packs needed: {}".format(num_of_hotdog_bun_needed))
print("The number of hot dogs left: {}".format(num_of_hotdog_remaining))
print("The number of hotdog buns remaining: {} ".format(num_hotdog_bun_remaining))
"""

# 9. Roulette Wheel Colors
"""
On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
as follows:
• Pocket 0 is green.
• For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
pockets are red.
• For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
pockets are red.
Write a program that asks the user to enter a pocket number and displays whether the
pocket is green, red, or black. The program should display an error message if the user
enters a number that is outside the range of 0 through 36.
"""
"""
user_pocket_number = int(input("Enter a pocket number: "))

if user_pocket_number == 0:
    print("The pocket is green")
elif user_pocket_number <= 10:
    if user_pocket_number % 2 == 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif user_pocket_number <= 18:
    if user_pocket_number % 2 == 0:
        print("The pocket is red")
    else:
        print("The pocket is black")
elif user_pocket_number <= 28:
    if user_pocket_number % 2 == 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif user_pocket_number <= 36:
    if user_pocket_number % 2 == 0:
        print("The pocket is red")
    else:
        print("The pocket is black")
else:
    print("Enter a number 0-36")

"""

# 10. Money Counting Game
"""
Create a change-counting game that gets the user to enter the number of coins required
to make exactly one dollar. The program should prompt the user to enter the number of
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
dollar, the program should congratulate the user for winning the game. Otherwise, the
program should display a message indicating whether the amount entered was more than
or less than one dollar.
"""
"""
penny = 1
nickle = 5
dime = 10 
quarter = 25

user_pennies = int(input("Enter the amount of pennies you have: "))
user_nickles = int(input("Enter the amount of nickles you have: "))
user_dimes = int(input("Enter the number of dimes you have: ")) 
user_quarters = int(input("Enter the number of quarters you have: "))

penny *= user_pennies
nickle *= user_nickles
dime *= user_dimes
quarter *= user_quarters

total_amount_of_money = penny + nickle + dime + quarter

if total_amount_of_money == 100:
    print("You Won!")
elif total_amount_of_money < 100:
    print("Not enough money")
else:
    print("Too much money")

"""

# 11. Book Club Points
"""
Serendipity Booksellers has a book club that awards points to its customers based on the
number of books purchased each month. The points are awarded as follows:


if a customer purchases 0 books, he or she earns 0 points.
if a customer purchases 2 books, he or she earns 5 points.
if a customer purchases 4 books, he or she earns 15 points.
if a customer purchases 6 books, he or she earns 30 points.
if a customer purchases 8 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has pur-
chased this month, then displays the number of points awarded.
"""     

# 11 is a dumb program.

# 12. Software Sales
"""
A software company sells a package that retails for $99. Quantity discounts are given
according to the following table:


Write a program that asks the user to enter the number of packages purchased. The pro-
gram should then display the amount of the discount (if any) and the total amount of the
purchase after the discount.
"""
"""
quantity_of_items_purchased = int(input("Enter the quantity of software purchased: "))

ten_percent_discount = 0.10
twenty_percent_discount = .20
thirty_percent_discount = .30
forty_percent_discount = .40

cost =  99

if quantity_of_items_purchased >= 10 and quantity_of_items_purchased <= 19:
    
    print("The cost for {}, is {}".format(quantity_of_items_purchased, (quantity_of_items_purchased * cost - (quantity_of_items_purchased * cost * ten_percent_discount))))

elif quantity_of_items_purchased >= 20 and quantity_of_items_purchased <= 49:
    print("The cost for {}, is {}".format(quantity_of_items_purchased, (quantity_of_items_purchased * cost - (quantity_of_items_purchased * cost * twenty_percent_discount))))

elif quantity_of_items_purchased >= 50 and quantity_of_items_purchased <= 99:
    print("The cost for {}, is {}".format(quantity_of_items_purchased, (quantity_of_items_purchased * cost - (quantity_of_items_purchased * cost * thirty_percent_discount))))

elif quantity_of_items_purchased >= 100:
    print("The cost for {}, is {}".format(quantity_of_items_purchased, (quantity_of_items_purchased * cost - (quantity_of_items_purchased * cost * forty_percent_discount))))
"""
# 13. Shipping Charges
"""
The Fast Freight Shipping Company charges the following rates:

Write a program that asks the user to enter the weight of a package then displays the ship-
ping charges.

"""
"""
weight_of_package = int(input("Enter the amount of weight for a package: "))

less_two_pound_rate = 1.50
over_two_below_six_rate = 3.00
over_six_below_ten_rate = 4.00
over_ten = 4.75

if weight_of_package > 0 and weight_of_package < 2:
    print("Your shipping rate = {}".format(less_two_pound_rate * weight_of_package))

elif weight_of_package >= 2 and weight_of_package <= 6:
    print("Your shipping rate = {}".format(over_two_below_six_rate * weight_of_package))

elif weight_of_package > 6 and weight_of_package <= 10:
    print("Your shipping rate = {}".format(over_six_below_ten_rate * weight_of_package))
elif weight_of_package > 10:
    print("Your shipping rate = {}".format(over_ten * weight_of_package))

"""

# 14. Body Mass Index
"""
Write a program that calculates and displays a person’s body mass index (BMI). The BMI
is often used to determine whether a person is overweight or underweight for his or her
height. A person’s BMI is calculated with the following formula:

BMI 5 weight 3 703/height 2

where weight is measured in pounds and height is measured in inches. The program should
ask the user to enter his or her weight and height, then display the user’s BMI. The pro-
gram should also display a message indicating whether the person has optimal weight, is
underweight, or is overweight. A person’s weight is considered to be optimal if his or her 
BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered to be
underweight. If the BMI value is greater than 25, the person is considered to be overweight.
"""



# 15. Time Calculator
"""
Write a program that asks the user to enter a number of seconds and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should convert the number of seconds to minutes and
seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should convert the number of seconds to
hours, minutes, and seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is
greater than or equal to 86,400, the program should convert the number of seconds to
days, hours, minutes, and seconds.

"""
"""
minutes = 0
hour = 0
secs = 0
days = 0


num_of_secs = int(input("Enter an amount of secs: "))
if num_of_secs > 1:
    days = num_of_secs // 86400
    hour = (num_of_secs % 86400) // 3600 
    minutes = ((num_of_secs % 86400) % 3600) // 60
    secs = (((num_of_secs % 86400) % 3600) % 60) % 60
else:
    secs = 1

print("Mins: {}\nSecs: {}\n Hours: {}\nDays: {}".format(minutes, secs, hour, days)) 
"""

 
# 16. February Days
"""
The month of February normally has 28 days. But if it is a leap year, February has 29 days.
Write a program that asks the user to enter a year. The program should then display the
number of days in February that year. Use the following criteria to identify leap years:
1. Determine whether the year is divisible by 100. If it is, then it is a leap year if and only
if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
2. If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4.
For example, 2008 is a leap year, but 2009 is not.

"""

"""
enter_year = int(input("Enter a year: "))

if enter_year % 100 == 0 and enter_year % 400 == 0:
    print("It is a leap year")
elif enter_year % 100 != 0 and enter_year % 4 == 0: 
    print("It is a leap year")
else:
    print("It is not leap year")
"""
 



