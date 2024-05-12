#Here I practice with lists
import random
books = ['Frankenstein', 'David Copperfield', 'Brave New World', 'Moby Dick', 'Little Woman']
authors = ['Shelley', 'Dickens', 'Huxley', 'Melville', 'Alcott']

for x in range(len(books)):
    input ('Who wrote ' + books[x] + '? ')

print ('\nThe correct book titles and authors are:')

for x in range(len(authors)):
    print (books[x] + ' - ' + authors[x])

print ('Little Woman' in  books) #looks for string and prints true or false
books.clear () #clears books list
authCount = authors.count("Shelley") # variable that checks for every occurance of "Shelley" in list
print (authCount)
print (books)
print (authors)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
two_lists = [fruits, vegetables]
number2 = random.randint(0,4)
number1 = random.randint(0,6)
 
print(two_lists[0][2])
print(two_lists[1][2])
print(two_lists[0][number1])
print(two_lists[1][number2])