# data that is mutabled could generate bugs in programs

# Lists have some functions for updated the data: append, pop, remove, insert, etc.

my_list = [1, 2, 3]

print(my_list[0])
print(my_list[1:])  # slice notation
print(my_list[:1])  # [indice_start:number of element]

my_list.append(4)
print(my_list)
my_list[0] = '10'  # Lists can have different type of data, exclusive to python
print(my_list)
my_list.pop()
print(my_list)

for element in my_list:
    print(element)

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(b)

a.append(5)  # 5 is also added in b

print(b)
print(a)
print(id(a))
print(id(b))
# there are not two values but just one
# values from a and b are in the same address in memory


# list funcion clone the value in other address in memory
c = list(a)
print(id(a))
print(id(c))

# slice notation is also used to clone the list
d = a[::]