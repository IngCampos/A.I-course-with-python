# silencing a bug is bad practice(just use the console to print the error)

def split_list_items(list, divisor):
    try:
        return [i / divisor for i in list]
    except ZeroDivisionError as e:
        print(e)
        return list


list = list(range(10))
divisor = 0

print(split_list_items(list, divisor))
