# # Exercise 3 Study Drill 3 from Learn Python the Hard Way 
# by Zed Shaw [https://learncodethehardway.org/python/]
# 3. Find something you need to calculate and write a new .py file that does it.

number1 = int(input('Please enter a numerical value:'))
number2 = int(input('Please enter a second numerical value:'))

# print('Your total is ' + str(number1 + number2))  integers need to be converted to strings to concatenate

# using a comma creates a 'tuple' which is an ordered finite list. 
print('Your total is', number1 + number2)
