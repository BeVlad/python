type_list = [12, None, -77, 'True', True, 9.5]
def test_type(el):
    for el in range(len(type_list)):
        print(type(type_list[el]))
    return
test_type(type_list)