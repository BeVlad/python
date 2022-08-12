elem_count = int(input("Please, enter the number of list items: "))
test_list = []
i = 0
elem = 0
while i < elem_count:
    test_list.append(input("Please, enter the following value: "))
    i += 1

for elem in range(int(len(test_list)/2)):
        test_list[elem], test_list[elem + 1] = test_list [elem + 1], test_list[elem]
        elem += 2
print(test_list)