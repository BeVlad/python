start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
finish_list = [i for i in start_list if start_list.count(i) == 1]
print(finish_list)