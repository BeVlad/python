test_str = input("Please, enter the words: ")
test_words = []
num = 1
for i in range(test_str.count(' ') + 1):
    test_words = test_str.split()
    if len(str(test_words)) <= 10:
        print(f" {num} {test_words [i]}")
        num += 1
    else:
        print(f" {num} {test_words [i] [0:10]}")
        num += 1