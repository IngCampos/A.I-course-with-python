import time

goal = int(input('Type a number!!'))
epsilon = 0.001
low = 0
max = max(1.0, goal)
response = (max+low)/2

start_time = time.time()
while abs(response**2 - goal) >= epsilon:
    print(f'low={low}, max={max}, response={response}')
    if response**2 < goal:
        low = response
    else:
        max = response
    response = (max+low)/2

print(f'The square root of {goal} is {response}')
print("Processing time:  %s seconds " % (time.time() - start_time))
