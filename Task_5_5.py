def sum_digit():
    try:
        with open('5.txt', 'w+', encoding='utf-8') as file_obj:
            line = input('Input digit: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error!')
    except ValueError:
        print('Wrong number dialed')


sum_digit()
