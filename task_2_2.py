list_elem = input("Please, enter the number of list items: ").split(' ')
i = 0
j = 1
while len(list_elem) > j:
    list_elem[i], list_elem[j] = list_elem[j], list_elem[i]
    i += 2
    j += 2
print('Your digits: ', *list_elem)
