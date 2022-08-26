def division(*args):
    try:
        arg1 = int(input("Input first digit: "))
        arg2 = int(input("Input Input second digit: "))
        resuslt = arg1 / arg2
    except ZeroDivisionError:
        return "Error! Can't divide by zero"

    return resuslt

print(f' Division result:  {division()}')