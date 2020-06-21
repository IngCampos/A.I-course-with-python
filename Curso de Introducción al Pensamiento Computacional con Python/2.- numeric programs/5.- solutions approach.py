import time

goal = int(input('Type a number!!'))
epsilon = 0.001
step = epsilon**2
response = 0.0

start_time = time.time()
while abs(response**2 - goal) >= epsilon and response <= goal:
    print(abs(response**2 - goal), response)
    response += step
if abs(response**2 - goal )>= epsilon:
    print(f'There is not square root of {goal}')
else:
    print(f'The square root of {goal} is {response}')
print("Processing time:  %s seconds " % (time.time() - start_time))