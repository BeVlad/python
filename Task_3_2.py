def user_info(**kwargs):
    print(f"{kwargs['name']} {surname} {date_birth} year of birth, "
          f"live in {city}. email: {email}, phone number: {tel}")


name = input("Input your name: ")
surname = input("Input your surname: ")
date_birth = input("Input your date of birthday: ")
city = input("Input current city: ")
email = input("Input your email address: ")
tel = int(input("Input your phone number: "))

user_info(
    name=name,
    surname=surname,
    date_birth=date_birth,
    city=city,
    email=email,
    tel=tel
)
