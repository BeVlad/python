total = 0
print(f' Please, input digit, then press enter and continue input digits: ')


while True:
    user_inp = input().split(' ')
    try:
        total += sum(map(int, user_inp))
        print(total)
        print(f' Input any symbol to complete')
    except ValueError:
        break
