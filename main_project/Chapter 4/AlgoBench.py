"""
1. Write a while loop that lets the user enter a number. The number should be multiplied
by 10, and the result assigned to a variable named product . The loop should iterate as
long as product is less than 100.

"""
"""
user_num = int(input("Enter a number: "))

while user_num < 100:
    user_num *= 10
    print(user_num)

"""

"""
5. Write a loop that calculates the total of the following series of numbers:
"""
"""
bottom_list = []
total_list = 0
top_list = []
for x in range(1, 31):
    top_list.append(x)

for x in range(30, 0, -1):
    bottom_list.append(x)


print(bottom_list, top_list)


fraction_length = 30

while fraction_length > 0:
    counter = 0
    total_list += bottom_list[counter] /top_list[counter]
    counter += 1
    fraction_length -= 1
print(total_list)
"""










