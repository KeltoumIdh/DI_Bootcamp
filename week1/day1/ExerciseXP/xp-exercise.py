#Exercise 1: Hello World
print('**** exercise 1 ****')
print("Hello World \n" * 3)

#Exercise 2: Some Math
print('**** exercise 2 ****')
result = (99 ** 3) * 8
print(result)

# Exercise 3: What is the output?
print('**** exercise 3 ****')
print(5 < 3) #false
print(3 == 3) #true
print(3 == "3") #false
#print("3" > 3) #fasle
print("Hello" == "hello") #false

# Exercise 4: Your computer brand
print('**** exercise 4 ****')
computer_brand='ASUS'
print('i have a {} computer'.format(computer_brand))

#Exercise 5: Your information
print('**** exercise 5 ****')
name='keltoum'
age=23
shoe_size=38
info='my name is {} and my age is {} years old and i am wearing {} in my shoes '.format(name,age,shoe_size)
print(info)

#Exercise 6: A & B
print('**** exercise 6 ****')
a=5
b=3
if a>b:
    print('hello world')

#Exercise 7: Odd or Even
print('**** exercise 7 ****')
num=int(input('enter the number'))
if num%2==0:
    print('even')
else:
    print('odd')

#Exercise 8: What’s your name?
print('**** exercise 8 ****')
name=input('enter your name')
my_name = "Keltoum"
if name.strip().lower() == my_name.lower():
    print("No way! We have the same name ,its impossible")
else:
    print(f"Nice to meet you, {name}! But {my_name} is still the cooler and unique name ")

#Exercise 9: Tall enough to ride a roller coaster
print('**** exercise 9 ****')
height=int(input('enter your height in centimeters'))
if height >= 145:
    print('you are tall enough to ride.')
else :
    print('you need to grow some more to ride')