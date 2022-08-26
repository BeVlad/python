import json

with open("3.json", encoding='utf-8') as file_read:
    data_dict: object = json.load(file_read)
    print(type(data_dict))
    print("Workers earning less than $20,000 per year: ")
    for keys, values in data_dict.items():
        if values < 20000:
            print(keys)
    print(f'Average salary = {sum(data_dict.values()) / len(data_dict)} $ in year')