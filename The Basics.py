import time
print ('Welcome to The Basics!')
#time.sleep(1)
print ('Lets practice variables.')
#time.sleep(1)
print ('I will set \'age\' to 20 and \'price\' to 9.95, then print')
age = 20
price = 9.95
print (age)
print (price)
print ('Now lets get ur input')
name = input ('What is your name? ')
print ('Hey ' + name + '!')
course = 'Python for beginners' # this string is an object
print (course.upper()) # the function after the variable is called a method
# I like to think of it as manipulating an object
print (course.find('n')) # We can also set a parameter
print (course.replace('for', '4')) # We can also set MULTIPLE parameters
print ('for' in course) # Strings are immunitable so this will be true