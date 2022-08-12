n = abs(int(input("Please, enter a positive integer (from 10 to 999): ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Maximum digit: ", max)
        break