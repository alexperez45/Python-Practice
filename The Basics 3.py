#Here I will expirment with if statments, loops, lists and more
weight = int(input ("How much do you weigh? "))
metric = input ("(K)g or (L)bs: ")
if metric.upper() == 'K':
    weight = weight * 2.205
    weight = round(weight,2)
    print ('Weight in Lbs: ' + str(weight))
elif metric.upper() == 'L':
    weight = weight / 2.205
    weight = round(weight,2)
    print ("Weight in Kg: " + str(weight))
else:
    print ("Please try again")