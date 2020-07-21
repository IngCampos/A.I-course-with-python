# the tuples are immutable

my_tuple = ()
my_tuple = (1, 'dos', True)
print(my_tuple)

# my_tuple[0] = False
# print(my_tuple)
# each place in the tuple cannot be updated
# just all the tuple can be updated

my_tuple = (1)
print(type(my_tuple))
my_tuple = (1,)  # the , is neccesary in the tupple in order to be a tuple
print(type(my_tuple))

my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple  # the content in my_tuple is added
print(my_tuple)

x, y, z = my_other_tuple  # unpack the tuple
print(x)
print(y)
print(z)

def coordinates():
    return (5, 4)
coordenate = coordinates()
print(coordenate)

x, y = coordenate
print(x)
print(y)
