# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# condition=list(filter(lambda x : len(x)<=4 ,people))
# result=list(map(lambda x : f'hello {x}',condition))
# print(result)

# 🌟 Exercise 1: What Are You Learning?
import random


def display_message():
    print("I am learning about functions in Python.")
display_message()
#🌟 Exercise 2: What’s Your Favorite Book?
def favorite_book(title):
    print(f'One of my favorite books is {title}')
favorite_book("Alice in Wonderland")
#🌟 Exercise 3: Some Geography
def describe_city(city,country='Unknown'):
    print(f'{city} is in {country}')
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
#Exercise 4: Random
def randomFunc(num):
    random_num=random.randint(1, 100)
    if num == random_num :
        print('Success!')
    else :
        print(f'try again , the number was {random_num} and yours {num}')
num=int(input('enter number between 1 and 100'))
randomFunc(num)
#🌟 Exercise 5: Let’s Create Some Personalized Shirts!
def make_shirt(size='large',text='I love Python'):
    print(f'the size of the shirt is {size} and the text is {text}')
make_shirt()
make_shirt('medium',)
make_shirt('xl','love you')
make_shirt(size="small", text="Hello!")
#🌟 Exercise 6: Magicians…
magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for x in magician_names:
        print(x)
def make_great(magician_names):
    for i,x in enumerate(magician_names):
        magician_names[i]=f'{x} the great'
make_great(magician_names)
show_magicians(magician_names)
print(magician_names)
# 🌟 Exercise 7: Temperature Advice
def get_random_temp():
    return random.uniform(-10,40)
def main():
    x=get_random_temp()
    print(f'The temperature right now is {x} degrees Celsius.')
    if x == 0:
        print(f'Brrr, that’s freezing! Wear some extra layers today.')
    elif 0<x<16:
        print('Quite chilly! Don’t forget your coat.')
    elif 16<x<23:
        print('Nice weather.')
    elif 24<x<32:
        print('A bit warm, stay hydrated')
    elif 32<x<40:
        print('It’s really hot! Stay cool.')
main()