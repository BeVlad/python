seasons = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Autumn'}
month = int(input("Please, enter the day of the month: "))
if month == 1 or month == 12 or month == 2:
        print(seasons.get(1))

elif month == 3 or month == 4 or month == 5:
        print(seasons.get(2))

elif month == 6 or month == 7 or month == 8:
        print(seasons.get(3))

elif month == 9 or month == 10 or month == 11:
        print(seasons.get(4))

else:
        print("Sorry, this month does not exist. Try again")
