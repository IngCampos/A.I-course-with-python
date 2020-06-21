import time

# 4.- Enumeration

def enumeration(goal):
    response = 0
    while response**2 < goal:
        print(response)
        response += 1

    if response**2 == goal:
        return (f'The square root of {goal} is {response}')
    else:
        return (f'{goal} does not have square root')

# 5.- Solution approach

def approach(goal):
    epsilon = 0.001
    step = epsilon**2
    response = 0.0

    while abs(response**2 - goal) >= epsilon and response <= goal:
        response += step
    if abs(response**2 - goal) >= epsilon:
        return (f'There is not square root of {goal}')
    else:
        return (f'The square root of {goal} is {response}')

# 6.- Binary search

def binary(goal):
    epsilon = 0.001
    low = 0
    up = max(1.0, goal)
    response = (up+low)/2

    start_time = time.time()
    while abs(response**2 - goal) >= epsilon:
        if response**2 < goal:
            low = response
        else:
            up = response
        response = (up+low)/2

    return (f'The square root of {goal} is {response}')

# Main

print('Algorithm\n1.-Enumeration\n2.-Approach\n3.-Binary search')
option = int(input('Type the number of the option: '))
goal = int(input('Type a number!!'))
start_time = time.time()

if option == 1:
    print(enumeration(goal))
elif option == 2:
    print(approach(goal))
elif option == 3:
    print(binary(goal))
else:
    print('Number no valid')

print("Processing time:  %s seconds " % (time.time() - start_time))
