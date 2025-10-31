#Exercise 1 : Hello World-I love Python
print("**** exercise 1 ****")
print(("Hello world\n" * 4) + ("I love python\n" * 4))

#Exercise 2 : What is the Season ?
print("**** exercise 2 ****")
month=int(input("Enter a month from 1 to 12 : "))
if month in range(3,6):
    print("Spring")
elif month in range(6,9):
    print("Summer")
elif month in range(9,12):
    print("Autumn")
else:
    print("Winter")
