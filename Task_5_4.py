dict_int = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("4.txt", encoding='utf-8') as file_open:
    for line in file_open:
        for key in dict_int.keys():
            line = line.replace(key, dict_int[key])
        print(line)
        with open("4ru.txt", "a") as file_rus:
            file_rus.write(f"\n {line}")
