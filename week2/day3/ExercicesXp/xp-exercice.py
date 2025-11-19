
#Exercises 1 Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount
        else:
            raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
        else:
            raise TypeError("Unsupported type for in-place addition")
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)

print('Exercise 1 : ')

print(c1)        # "5 dollars"
print(int(c1))   # 5
print(repr(c1))  # "5 dollars"
print(c1 + 5)    # 10
print(c1 + c2)   # 15
c1 += 5
print(c1)        # "10 dollars"
c1 += c2
print(c1)        # "20 dollars"
# print(c1 + c3)   # TypeError

#Exercise 2 Import
print("Exercise 2 : ")
from func import add_numbers
add_numbers(3, 7)   # La somme de 3 et 7 est 10

#Exercise 3  String Module
print("Exercise 3 : ")
import string
import random

def generate_random_string(length=5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

print(generate_random_string())   # Exemple : 'aBcDe'

#Exercise 4 Current Date
print("Exercise 4 : ")
import datetime

def display_current_date():
    today = datetime.date.today()
    print("To day date is  :", today)

display_current_date()

#Exercise 5 Amount of time left until january 1st
print("Exercise 5 : ")

def time_until_new_year():
    now = datetime.datetime.now()
    next_year = now.year + 1
    new_year = datetime.datetime(next_year, 1, 1)

    time_left = new_year - now

    print("time left until january 1st :")
    print("Day :", time_left.days)
    print("Hours :", time_left.seconds // 3600)
    print("Minutes :", (time_left.seconds % 3600) // 60)
    print("Secondes :", time_left.seconds % 60)

time_until_new_year()

#Exercise 6 Birthday and minutes
print("Exercise 6 : ")

def minutes_lived():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.datetime.now()

    time_lived = now - birthdate
    minutes_lived = int(time_lived.total_seconds() / 60)

    print(f"You have lived approximately {minutes_lived} minutes.")

minutes_lived()

#Exercise 7 Faker Module
print("Exercise 7 : ")

from faker import Faker

faker = Faker()

def generate_users(n):
    users = []
    for _ in range(n):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        }
        users.append(user)
    return users

# Example: generate 5 fake users
fake_users = generate_users(5)
for user in fake_users:
    print(user)