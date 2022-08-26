from sys import argv

if len(argv) > 1:
    name_script, time_work, salary, premium = argv
    time_work = int(time_work)
    rate = int(salary)
    prize = int(premium)
    print((time_work * salary) + premium)
else:
    time_work = int(input("Inpute time work: "))
    salary = int(input("Inpute salary: "))
    premium = int(input("Inpute premium: "))
    print((time_work * salary) + premium)