def fibonnaci(n):

    if n == 0 or n == 1:
        return 1

    return fibonnaci(n-1) + fibonnaci(n-2)


n = int(input('Type a number!!!'))
print(fibonnaci(n))

# Example about the recursion
