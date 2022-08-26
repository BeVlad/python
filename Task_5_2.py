count_lines = 0
count_words = 1

with open("2.txt", "r", encoding='utf-8') as file_open:
    for line in file_open:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                count_words += 1
        count_lines += 1
        print(f"Number of words per line {count_lines} = {count_words} \n")
        count_words = 1
    print(f"In file {count_lines} lines")