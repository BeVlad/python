s = int(input("Please, enter your first day's run in kilometrs: "))
s1 = int(input("Enter the total desired result in kilometrs: "))
res_days = 1
res_km = s
while res_km < s1:
        s = s + 0.1 * s
        res_days += 1
        res_km = res_km + s
print(f"You will reach the required indicators for %.d days" % res_days)