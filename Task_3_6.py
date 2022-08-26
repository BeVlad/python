def int_func(string):
    return string.title()


print(int_func("text"))


def title_func(string):
    list_title = []
    lst = string.split()
    for el in lst:
        list_title.append(int_func(el))
    print(*list_title)


title_func("writing a text for an example task")
