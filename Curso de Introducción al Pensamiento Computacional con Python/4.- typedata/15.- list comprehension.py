# Other way to use the lists

my_list = list(range(100))
print(my_list)

double = [i*2 for i in my_list]
print(double)

par = [i for i in my_list if i % 2 == 0]
print(par)
