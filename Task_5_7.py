import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit: {prof_aver:.2f}')
    else:
        print(f'Average profit missing. Negative growth')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit per company: {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    jsn_str = json.dumps(profit)
    print(f'Result: \n '
          f' {jsn_str}')