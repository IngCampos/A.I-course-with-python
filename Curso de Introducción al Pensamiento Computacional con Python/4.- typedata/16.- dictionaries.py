# keys are used insted of indexes(like the lists)
# it does not have order
# it is mutable

my_dict = {
    'Martin': 35,
    'Salvador': 12,
    'Jose': 30,
}

print(my_dict['Martin'])

# print(my_dict['Juan']) this throw an error because the key does not exist
# in order to not throw an error, the next function could be used

print(my_dict.get('Juan', 18))  # it throws 18 as a default value

my_dict['Jose'] = 35  # we can update an value
my_dict['Chuy'] = 35  # we can add a new data0
print(my_dict)

del my_dict['Chuy']  # we can delete a data
print(my_dict)

####################################

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

####################################

print('Martin' in my_dict) 
print('Chuy' in my_dict) # it throws false because it does not exist