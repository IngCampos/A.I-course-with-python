counter = 0

while counter < 10:
    print(counter)
    counter += 1

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit)

iterador = iter(fruits)
print(next(iterador))
print(next(iterador))
print(next(iterador))
# print(next(iterador)) error

print(iter('cadena'))  # string
print(iter(['a', 'b', 'c']))  # list
print(iter(('a', 'b', 'c')))  # tuple
print(iter({'a', 'b', 'c'}))  # set
print(iter({'a': 1, 'b': 2, 'c': 3}))  # dict_key


students = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for country in students:
    print(country)

for country in students.keys():
    print(country)

for number_students in students.values():
    print(number_students)

for country, number_students in students.items():
    print(country+" " + str(number_students))
