goal = int(input('Type a number!!'))
response = 0
while response**2 < goal:
    print(response)
    response += 1

if response**2 == goal:
    print(f'The square root of {goal} is {response}')
else:
    print(f'{goal} does not have square root')