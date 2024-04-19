#Here I will expirment with if statments, loops, lists and more
weight = int(input ("How much do you weigh? "))
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
    print ("Please try again")

i = 1
while i < 10:
    print (i * '*')
    i = i + 1

x = 10
while x > 1:
    print (x * '*')
    x = x - 1

books = ['Frankenstein', 'David Copperfield', 'Brave New World', 'Moby Dick', 'Little Woman']
authors = ['Shelley', 'Dickens', 'Huxley', 'Melville', 'Alcott']

for x in range(len(books)):
    input ('Who wrote ' + books[x] + '? ')

print ('\nThe correct book titles and authors are:')

for x in range(len(authors)):
    print (books[x] + ' - ' + authors[x])

print ('Little Woman' in  books)
books.clear ()
authors.clear()
print (books)
print (authors)