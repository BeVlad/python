test_list = [9, 7, 5, 3, 2]
print(f"Raiting - {test_list}")
digit = int(input("If you want to exit the program, enter 0. Please, enter digit: "))
while digit != 0:
    for i in range(len(test_list)):
        if test_list[i] == digit:
            test_list.insert(i + 1, digit)
            break
        elif test_list[0] < digit:
            test_list.insert(0, digit)
        elif test_list[-1] > digit:
            test_list.append(digit)
        elif test_list[i] > digit and test_list[i + 1] < digit:
            test_list.insert(i + 1, digit)
    print(f"Raiting - {test_list}")
    digit = int(input("Enter next digit: "))