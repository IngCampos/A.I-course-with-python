# range(start, end, steps)
# the final is not included
my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)

my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

print(my_range == my_other_range) # it throws true because both have the same numbers

print(id(my_range))  # address of the data in memory
print(id(my_other_range))  # address of the data in memory

print(my_range is my_other_range) #it throws false because both data is in different address in memory

# challenge: print the non numbers  of 0 to 100
my_challenge_range = range(-1, 100, 2)
for i in my_challenge_range:
    print(i)