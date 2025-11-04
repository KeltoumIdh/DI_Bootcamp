#Exercise 1: Favorite Numbers
print('**** exercise 1 ****')
my_fav_numbers=set([7,13,21,17])
my_fav_numbers.add(8)
my_fav_numbers.add(9)
my_fav_numbers.remove(9)
print(my_fav_numbers)

friend_fav_numbers=set([20,40,80,100])
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2: Tuple
print('**** exercise 2 ****')
my_tuple=(1,2,3,4,5)
my_tuple=my_tuple+(2, 4, 6, 8)
print(my_tuple)

#Exercise 3: List Manipulation
print('**** exercise 3 ****')
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
print(basket.count('Apples'))
basket.clear()
print(basket)

#Exercise 4: Floats
print('**** exercise 4 ****')
#What is a float? What’s the difference between a float and an integer?
print('a float is a decimal number and an integer is a whole number')
list_of_numbers=[]
number=1.5
while number<5:
    list_of_numbers.append(number)
    number+=0.5
print(list_of_numbers)

#Exercise 5: For Loop
print('**** exercise 5 ****')
for number in range(1,21):
    print(number)
for number in range(1,21):
    if number%2==0:
        print(number)

#Exercise 6: While Loop
print('**** exercise 6 ****')
name=input('enter your name : ')
while True:

    if len(name)<3:
        name=input('give correct name for your name (at least 3 characters long) : ')
        continue
    elif name.isdigit():
        name=input('give correct name for your name (no numbers) : ')
        continue
    else:
        print(f'thank you {name}')
        break

#Exercise 7: Favorite Fruits
fav_fruits=input('enter your favorite fruits : ')
list_of_fruits=fav_fruits.split(' ')
print('list of fruits : ',list_of_fruits)
fruit=input('enter a fruit : ')
if fruit in list_of_fruits:
    print('you chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy it!')

#Exercise 8: Pizza Toppings
# print('**** exercise 8 ****')
pizza_toppings=[]
topping=input('enter a topping : ')
while True:
    if topping =='quit':
        break
    else:

        pizza_toppings.append(topping)
        print(f'Adding {topping} to your pizza.')
        topping=input('enter a topping : ')
        continue
print('your pizza toppings are : ')
for topping in pizza_toppings :
    if topping !='quit':
        print(topping)
    else:
        break
print(f'total price is : {len(pizza_toppings)*1.5 + 10}$')

#Exercise 9: Cinemax Tickets
print('**** exercise 9 ****')
ages=input('enter the ages for each member of the family (separated by spaces) : ')
list_of_ages=ages.split(' ')
total_price=0
for age in list_of_ages:
    if int(age)<3:
        total_price+=0
    elif int(age)>=3 and int(age)<12:
        total_price+=10
    else:
        total_price+=15
print(f'total price is : {total_price}$')

#Bonus:
print('**** bonus ****')
list=[]
groupe_members=input('enter the number of members in the group : ')
for member in range(1,int(groupe_members)+1):
    name=input(f'enter the name of member {member} ')
    age=int(input(f"enter {name}'s age : "))
    if 16 <= age <= 22 :
        list.append(name)
    continue
print('the list is : ' ,list)