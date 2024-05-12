#Here I will expirment with if statments, loops, and more
import random
import time
weight = input ("How much do you weigh? ")
if weight.isdigit():
    weight = float(weight)
    metric = input ("(K)g or (L)bs: ")
    if metric.upper() == 'K': # upper method used to turn lowercase 'k' to uppercase
        weight = weight * 2.205
        weight = round(weight,2)
        print ('Weight in Lbs: ' + str(weight))
    elif metric.upper() == 'L':
        weight = weight / 2.205
        weight = round(weight,2)
        print ("Weight in Kg: " + str(weight))
else:
    print ("Please enter a number")

print ('.'); time.sleep(1); print ('.'); time.sleep(1); print ('.'); time.sleep(1)

i = 1
while i < 10:
    print (i * '*')
    i = i + 1

x = 10
while x > 1:
    print (x * '*')
    x = x - 1

#Calculates the sum of all the even numbers from 1 to X.
target = int(input("Type a number: "))
target += 1
total = 0
for number in range(0, target, 2):
  total += number
print (total)