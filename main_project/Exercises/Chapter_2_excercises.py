import turtle
#Programming Excercises 

# 1. personal Information
"""
Write a program that displays the following information:

Your name,
Your address, with city name, state, and zip
Your telephone number
Your college major
"""
"""
name = input("Enter your name: ")

address =  input("Enter your city: ")

tele = input("Enter your phone number: ")

major = input("Enter your major: ")

print("Hello: ", name, "\nYour address: ", address, "\nPhone number: ", tele, "\nMajor: ", major)
"""

# 2. Sale prediction
"""
A company has determined that its annual profit is typically 23 percent of total sales. Write
a program that asks the user to enter the projected amount of total sales, then displays the
profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent. """
"""
projected_sales = int(input("Enter projected sales: "))

projected_annual_profit =  projected_sales * .23

print("Your projected profit is: {}".format(projected_annual_profit))
"""

# 3. Pounds to Kilograms
"""
One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
the mass of an object in pounds and then calculates and displays the mass of the object in
kilograms.
"""
"""
kilos = 0.454

pounds = int(input("Enter a weight in pounds to convert to kilograms: "))

pounds_to_kilos = pounds * kilos

print("The converted weight is: {}".format(pounds_to_kilos))
"""

# 4. Total Purchase

"""
A customer in a store is purchasing five items. Write a program that asks for the price of
each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 7 percent.
"""
"""
num_of_items = 5

list_of_items = []

total_sub_cost = 0

total_cost_plus_tax = 0

# input items purchased and add them to a list.
for num in range(0, num_of_items):
    current_item = int(input("Enter the price of item {}: ".format(num + 1)))
    list_of_items.append(current_item)

# get the total in for loop.
for item in list_of_items:
    total_sub_cost += item 

# Get the cost plus tax.
total_cost_plus_tax = total_sub_cost + (total_sub_cost * .07)
# Display value.
print("The sub total cost is: {} ".format(total_sub_cost))
print("The total cost is: {}".format(total_cost_plus_tax))
"""

# Distance travelled 

"""
Assuming there are no accidents or delays, the distance that a car travels down the inter-
state can be calculated with the following formula:
Distance = Speed X Time
A car is traveling at 70 miles per hour. Write a program that displays the following:
• The distance the car will travel in 6 hours
• The distance the car will travel in 10 hours
• The distance the car will travel in 15 hours
"""
"""
six_hours = 6

ten_hours = 10 

fifthteen_hours = 15

car_speed =  70 

# Displays the car speed, hours travelled, and calculates/displays the distance travelled.
print("Car speed: 70")
print("Hours travelled: {} \t Distance travelled: {}".format(six_hours, six_hours * car_speed))
print("Hours travelled: {} \t Distance travelled: {}".format(ten_hours, ten_hours * car_speed))
print("Hours travelled: {} \t Distance travelled: {}".format(fifthteen_hours, fifthteen_hours * car_speed))
"""

# 6. Payments Installments.

"""
Write a program that asks the user to enter the amount of a purchase and the desired
number of payment instalments. The program should add 5 percent to the amount to get
the total purchase amount, and then divide it by the desired number of instalments, 
then display messages telling the user the total amount of the purchase and how much each
instalment will cost.
"""
"""

total_item_cost = int(input("Enter the amount of the purchase: "))

amount_of_installments = int(input("Enter the amount of installments for purchase: "))

installment_cost = (total_item_cost + (total_item_cost * 0.05)) / amount_of_installments 

print("The amount you have to pay each month is: {}".format(installment_cost))
"""

# 7. Miles-per-Gallon
"""
A car's miles-per-gallon (MPG) can be calculated with the following formula:
MPG = Miles driven / Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car's MPG and display the result."""
"""
miles_driven = int(input("Enter the number miles driven: "))

gallons_used = int(input("Enter the amount of gas used in gallons: "))

miles_per_gallon = miles_driven / gallons_used 

print("The miles per gallon for your vehicle is: {}".format(miles_per_gallon))
"""

#8. Tip, Tax, and Total
"""Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, then calculate the amounts
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
"""
"""
tax = 0.07
tip = 0.18
# Calculate the bill, bill with tip, bill with tax + tip. Display all. 

user_sub_total_bill = int(input("Enter the total bill cost: "))

print("The subtotal of the bill: {}".format(user_sub_total_bill))

print("The bill + tax: {}".format(user_sub_total_bill + (user_sub_total_bill * tax)))

print("The total bill, tax, and tip: {}".format(user_sub_total_bill + (user_sub_total_bill * tax + (user_sub_total_bill * tip))))
"""

# 9. Circle Measurements
"""
Write a program that asks the user to enter the radius of a circle. The program should cal-
culate and display the area and circumference of the circle using πr 2 for the area and 2πr
for the circumference.
Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
to the start of the program and then use "math.pi" wherever you need the value of pi in
the program.
"""
"""
# User input circle radius
user_custom_radius = float(input("Enter the radius of the circle: "))

# Calculate the circumfirence of the circle.

user_circle_circum = 3.14159 * (user_custom_radius ** 2)

user_circle_area = 2 * 3.1459 * user_custom_radius

print(The radius of the circle: {}\n
The circumference of the circle: {}\n
The area of the circle: {}.format(user_custom_radius, user_circle_circum, user_circle_area))

"""

# 10 Ingredient Adjuster

"""
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, then displays the number of cups
of each ingredient needed for the specified number of cookies.
"""
"""
cups_of_sugar = 0.31

cup_of_butter = 0.0208

cups_of_flour = 0.057

user_total_cookies = int(input("Enter the number of cookies. "))

print("You will need {} cups of sugar!".format(cups_of_sugar * user_total_cookies))
print("You will need {} cups of butter!".format(cup_of_butter * user_total_cookies))
print("You will need {} cups of flour!".format(user_total_cookies * cups_of_flour))
"""

# 11. Male and Female Percentages.

"""
Write a program that asks the user for the number of males and the number of females regis-
tered in a class. The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage
of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

"""
"""
female_in_class = int(input("Enter the number of females in your class: "))

male_in_class = int(input("Enter the number of males in your class: "))

percentage_of_males = male_in_class / (female_in_class + male_in_class) 
percentage_of_females = female_in_class / (female_in_class + male_in_class)
print("{:.2%}".format(percentage_of_males))
print("{:.2%}".format(percentage_of_females))"""

# 12. Stock Transaction Program
"""
Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the
purchase:
• The number of shares that Joe purchased was 2,000.
• When Joe purchased the stock, he paid $40.00 per share.
• Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid
for the stock.
Two weeks later, Joe sold the stock. Here are the details of the sale:
• The number of shares that Joe sold was 2,000.
He sold the stock for $42.75 per share.
• He paid his stockbroker another commission that amounted to 3 percent of the amount
he received for the stock.
Write a program that displays the following information:
The amount of money Joe paid for the stock.
The amount of commission Joe paid his broker when he bought the stock.
The amount for which Joe sold the stock.
The amount of commission Joe paid his broker when he sold the stock.
Display the amount of money that Joe had left when he sold the stock and paid his
broker (both times). If this amount is positive, then Joe made a profit. If the amount is
negative, then Joe lost money.

"""
"""
joe_shares =  2000

initial_stock_worth = 40.00

initial_stock_broker_tax = .03 * (joe_shares * initial_stock_worth)

sold_stock_worth = 42.75 
total_stock_worth_after_sale = sold_stock_worth * joe_shares
sold_stock_broker_tax = .03 * (total_stock_worth_after_sale)

print("Joe paid an initial amount of: {} for the stock.".format(joe_shares * initial_stock_worth))
print("Joe paid his stock broker three percent or ${}".format(initial_stock_broker_tax))
print("Joe sold the stock for ${}".format(total_stock_worth_after_sale))
print("Joe paid the stock broker {}".format(sold_stock_broker_tax))

if total_stock_worth_after_sale - sold_stock_broker_tax > initial_stock_worth - initial_stock_broker_tax:
    print("Joe made a profit.")
else:
    print("Joe lost money.")
"""

# 13. Planting Grapevines
"""
A vineyard owner is planting several new rows of grapevines, and needs to know how many
grapevines to plant in each row. She has determined that after measuring the length of a
future row, she can use the following formula to calculate the number of vines that will fit
in the row, along with the trellis end-post assemblies that will need to be constructed at
each end of the row:
V =  (R - 2E) / (S)

The terms in the formula are:
V is the number of grapevines that will fit in the row.
R is the length of the row, in feet.
E is the amount of space, in feet, used by an end-post assembly.
S is the space between vines, in feet.
Write a program that makes the calculation for the vineyard owner. The program should
ask the user to input the following:
• The length of the row, in feet
• The amount of space used by an end-post assembly, in feet
• The amount of space between the vines, in feet
Once the input data has been entered, the program should calculate and display the num-
ber of grapevines that will fit in the row.
"""
"""
length_of_row = int(input("Enter the length of the row in ft: "))

end_post_space = int(input("Enter the amount of space in the end post assembly in ft: "))

space_between_vines = int(input("Enter the space between vines in ft: "))

number_of_grapevines_per_row = (length_of_row - (2 * end_post_space)) / (space_between_vines)

print("The number of grapevines that will fit in a row is: {}".format(number_of_grapevines_per_row))
"""
# 14. Compound Interest
"""
When a bank account pays compound interest, it pays interest not only on the principal
amount that was deposited into the account, but also on the interest that has accumulated
over time. Suppose you want to deposit some money into a savings account, and let the
account earn compound interest for a certain number of years. The formula for calculating
the balance of the account after a specified number of years is:
A = P * (1 + (r / n )) ** (n * t)
The terms in the formula are:
A is the amount of money in the account after the specified number of years.
P is the principal amount that was originally deposited into the account.
r is the annual interest rate.
n is the number of times per year that the interest is compounded.
t is the specified number of years.Programming Exercises
Write a program that makes the calculation for you. The program should ask the user to
input the following:
• The amount of principal originally deposited into the account
• The annual interest rate paid by the account
• The number of times per year that the interest is compounded (For example, if interest
is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.)
• The number of years the account will be left to earn interest
Once the input data has been entered, the program should calculate and display the amount
of money that will be in the account after the specified number of years.

"""
"""
initial_money_deposited = int(input("Enter the amount of money you deposited: "))

annual_interest_rate = int(input("Enter the annual interest rate: "))

annual_interest_rate /= 100

num_of_times_interest_compounds = int(input("Enter the number of times interest compounds: "))

total_amount_of_years_compounding = int(input("Enter the total numbers of years that you will be compounding: "))

total_amount_compounded = initial_money_deposited * (1 + (annual_interest_rate / num_of_times_interest_compounds)) ** (num_of_times_interest_compounds * total_amount_of_years_compounding)

print("Total amount after {} years, is {} ".format(total_amount_of_years_compounding, total_amount_compounded))

"""

# 15. Turtle Graphics Drawings
"""
Use the turtle graphics library to write programs that reproduce each of the designs shown
in Figure 2-34.

"""
"""
turtle.left(25)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
second_square_start = turtle.pos()
print(turtle.xcor())
print(turtle.ycor())
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
turtle.penup()
turtle.goto(second_square_start)
turtle.pendown()
turtle.left(-50)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
turtle.mainloop()

"""





