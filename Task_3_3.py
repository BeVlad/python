def my_func(*args):
    lst = list(args)
    i = 0
    result = 0
    while i != 2:
        max_dig = max(lst)
        result += max_dig
        lst.remove(max_dig)
        i += 1

    print(f'Maximum digit: {result}')


my_func(200, 1, 600)