#Arithmetic operators:
print (10 + 3, 10 - 3, 10 * 3, 10 ** 3, 10 / 3, 10 // 3, 10 % 3)
x = 10
x += 3 # this is know as an augmented assigned operator which is the same as x = x + 3
print (x)
I = (10+3) * 2 # Python uses PEMDAS
print (I)
# Comparison operators include: >, <, >=, <=, ==, !=
# Logical operators include: and, or, not
price = 5
print (price > 1 and price < 10)
print (price == 1 or price > 1)
print (not price >=5)
# conversions: int() float() bool() str()
# Lets make a simple calculator
print ('Type 2 numbers for the sum')
first_num = input ('First: ') # you can also convert to float here ex: float(input ('First: '))
second_num = input ('Second: ') # you can also convert to float here
sum = float(first_num) + float(second_num)
print ('Sum: ' + str(sum))