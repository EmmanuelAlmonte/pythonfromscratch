# 1. Kilometer Converter
"""
Write a program that asks the user to enter a distance in kilometers, then converts that
distance to miles. The conversion formula is as follows:

Miles = Kilometers X 0.6214

"""
"""
def kilom_to_miles(miles):
    return miles * 0.6214

user_data_in_kilometers= int(input("Enter distance in kilometers: "))
print(kilom_to_miles(user_data_in_kilometers))

"""
# 2. String Repeater
"""
Python allows you to repeat a string by multiplying it by an integer, e.g. 'Hi' * 3 will give
'HiHiHi' . Pretend that this feature does not exist, and instead write a function named
repeat that accepts a string and an integer as arguments. The function should return a
string of the original string repeated the specified number of times, e.g. repeat('Hi', 3)
should return 'HiHiHi' .
"""
"""
# Accepts a string and integer returns the string repeated times the integer.
def str_repeater(string:str, integer:int):
    return (string + " ") * integer 

print(str_repeater("hello", 6))

"""

# 3. How much insurance? 
"""
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a program
that asks the user to enter the replacement cost of a building, then displays the minimum
amount of insurance he or she should buy for the property.
"""
"""
# contains a reference to the value of how much a building or home cost to repair. 
building_replace_cost = int(input("Enter the replacement cost for a building: "))

def minimum_insurance(replace_cost:int):
    minimum_percent = .20
    return replace_cost -  (replace_cost * minimum_percent)

print(minimum_insurance(building_replace_cost))

"""
# 4. Automobile Costs

"""
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
"""
"""
def main():
    # Display
    print("Enter Cost per month")
    user_loan_cost = int(input(("Enter loan cost per month: ")))
    
    user_insurance_cost = int(input(("Enter insurance cost per month: ")))
     
    user_gas_cost = int(input(("Enter gas cost per month: ")))
 
    user_oil_cost = int(input(("Enter oil cost per month: ")))
 
    user_tires_cost = int(input(("Enter tires cost per month: ")))
 
    user_maintence_cost = int(input(("Enter maintence cost per month: ")))
    user_car_cost = total_cost_of_owning_car(user_loan_cost, user_insurance_cost, user_gas_cost, user_oil_cost, user_tires_cost, user_maintence_cost)
    print("Per month your cost is: {}".format(user_car_cost))
 
def total_cost_of_owning_car(loan_cost:int, insurance_cost:int, gas_cost:int, oil_cost:int, tires_cost:int, maintence_cost:int):
    costs_list = [loan_cost, insurance_cost, gas_cost, oil_cost, tires_cost, maintence_cost]
    total_per_month = 0
    total_per_year = 0
    for item in costs_list:
        total_per_month += item
    total_per_year = total_per_month * 12
    return total_per_month, total_per_year 
 
if __name__ == "__main__":
       main()
"""

# 5. Property Tax
"""
A county collects property taxes on the assessment value of property, which is 60 percent of
the property’s actual value. For example, if an acre of land is valued at $10,000, its assess-
ment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
actual value of a piece of property and displays the assessment value and property tax.
"""
"""
def main():
    home_real_value = int(input("Enter the actual value of home: "))
    print(round(property_tax(home_value=home_real_value), 2))

def property_tax(home_value:int):
    home_value = home_value // 100
    property_tax_amount = .72
    return home_value * property_tax_amount

if __name__ == "__main__": 
    main() 
"""
# 6. Calories from Fat and Carbohydrates 

"""
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula: 

calories from fat = fat grams X 9
"""
"""
def main():
    num_of_fat_grams = int(input("Enter the num of fat grams you consumed: "))
    num_of_fat_carbs = int(input("Enter carbs grams: "))    
    converted_carbs_and_grams = fat_grams_to_calories_fat(num_of_fat_grams, num_of_fat_carbs)
    print("Calorie per fat:", converted_carbs_and_grams(), "\nCalorie per carb: ", converted_carbs_and_grams())

def fat_grams_to_calories_fat(num_of_fat_grams:int, carb_grams:int):
    calorie_per_fat = 9
    calorie_per_carb = 4
    return num_of_fat_grams * calorie_per_fat, carb_grams * calorie_per_carb

if __name__ == "__main__":
    main()

"""
# 7. Stadium Seating
"""
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
$15, and Class C seats cost $10. Write a program that asks how many tickets for each class
of seats were sold, then displays the amount of income generated from ticket sales.
"""
"""
class_a_seat = 20

class_b_seat = 15

class_c_seat = 10

def main():
    class_a_tickets_sold = int(input("Enter the amount of class A seat tickets sold: "))

    class_b_tickets_sold = int(input("Enter the amount of class B seat tickets sold: "))

    class_c_tickets_sold = int(input("Enter the amount of class C seat tickets sold: "))
    event_sales = total_tickets_sold(class_a_tickets_sold, class_b_tickets_sold, class_c_tickets_sold)
    print("Total tickets sold: {}".format(event_sales))

def total_tickets_sold(class_a, class_b, class_c):
    class_a *= class_a_seat
    class_b *= class_b_seat
    class_c *= class_c_seat
    total = class_a + class_b + class_c
    return total

if __name__ == "__main__":
    main()
"""

# 8. Paint Job Estimator
"""
A painting company has determined that for every 112 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $35.00 per hour
for labor. Write a program that asks the user to enter the square feet of wall space to be
painted and the price of the paint per gallon. The program should display the following data:
"""
"""
sqrt_of_wall_space = 112

def main():
    user_amount_of_wall_space = int(input("Enter the total sqrt feet of wall space: "))
    price_of_paint_per_gallon = int(input("Enter the cost of paint per gallon: "))
    total_gallons = gallons_required(user_amount_of_wall_space)
    print("The gallons required is: {}".format(round(total_gallons, 2)))
    print("The paint cost is: {}".format(round(gallons_cost(total_gallons, price_of_paint_per_gallon), 2)))
def gallons_required(sqrt_feet_total):
    num_of_gallons = sqrt_feet_total / sqrt_of_wall_space
    return num_of_gallons

def gallons_cost(gallons_required, price):
    return gallons_required * price 


if __name__ == '__main__':
    main()

"""





