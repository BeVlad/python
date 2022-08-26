list_number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_number[i] for i in range(len(list_number)) if list_number[i-1] < list_number[i]]
print("Start List: " + str(list_number))
print("New List: " + str(new_list))

'''без lc

list_number = []
for el in range(1, len(list_number)):
    if list_number[el] > list_number[el - 1]:
        list_number.append(list_number[el])

print(list_number)

'''