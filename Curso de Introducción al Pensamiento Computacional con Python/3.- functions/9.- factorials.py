def factorial(n):
    ''' Calculate the factorial of n

    n int > 0
    return n!
    '''

    if(n == 1):
        return 1

    return n * factorial(n-1)

n = int(input('Type a number!!!'))
print(factorial(n))

# Example about the recursion