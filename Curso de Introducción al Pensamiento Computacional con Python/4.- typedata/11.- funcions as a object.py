def multiply2(n):
    return n * 2

def add2(n):
    return n + 2

def operation(f, numeros):
    results = []
    for numero in numeros:
        result = f(numero)
        results.append(result)
    return results

nums = [1, 2, 3, 4]
print(operation(multiply2, nums))
print(operation(add2, nums))

# ------------------------------

sum = lambda x, y: x + y

print(sum(2, 3))

# ------------------------------

def execute_operations(num):
    operations = [abs, float]

    result = []
    for operation in operations:
        result.append(operation(num))
    return result

print(execute_operations(-2))
