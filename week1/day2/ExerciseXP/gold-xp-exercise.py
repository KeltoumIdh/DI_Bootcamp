from contextlib import nullcontext
import string
import random

#Exercise 1: Concatenate lists
print('****exo1****')
list1=[1,3]
list2=[2,5]
new_list=[*list1,*list2]
print(new_list)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#Exercise 2: Range of numbers
print('****exo2****')
for i in range(1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


#Exercise 3: Check the index
print('****exo3****')
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus','V']
# name=input('enter name')
# for n in names :
#     if name==n:
#         print ('the index :',names.index(n))
#         break

#Exercise 4: Greatest Number
print('****exo4****')
# num1=int(input('enter first number :'))
# num2=int(input('enter second number :'))
# num3=int(input('enter third number :'))
# print('the greatest number is :',max(num1,num2,num3))

#Exercise 5: The Alphabet
print('****exo5****')
# alphabets=list(string.ascii_lowercase)
# for  i in alphabets :
#     if i in ['e','o','i','y','a','u']:
#         print(f'{i} is vowel')
#     else:
#         print(f'{i} is consonant')

#Exercise 6: Words and letters
print('****exo6****')
# words=input('enter 7 words separated by space ')
# words_list=words.split(' ')
# print(words_list)
# while len(words_list)<7 or len(words_list)>7:
#     words=input('enter 7 ')
#     words_list=words.strip().split(' ')
# letter=input('enter single caracter')
# indexes=[]
# for i in words_list:
#     index=''
#     if letter in i:
#         index_letter=i.index(letter)
#         index=index_letter
#         print(index_letter)
#     else:
#         index=''
#     if index is not  '' :
#         indexes.append(index)
#     else:
#         indexes.append(f'this letter {letter} , does not exist in this word {i}')
# print(indexes)

#Exercise 7: Min, Max, Sum
print('****exo7*****')
# numbers=range(1,1000001)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

#Exercise 8 : List and Tuple
print('****exo8*****')
# numbers = input('Enter a sequence of numbers separated by comma: ')
# number_list = numbers.split(',')
# number_tuple = tuple(number_list)
# print(number_list)
# print(number_tuple)

#Exercise 9 : Random number
print('****exo9*****')
games_won = 0
games_lost = 0

while True:
    random_number = random.randint(1, 9)
    number = input('Type a number from 1 to 9 (or type "quit" to exit): ')

    if number.lower() == 'quit':
        break
    if not number.isdigit():
        print("Invalid input. Please enter a number from 1 to 9, or type 'quit' to exit.")
        continue

    guess = int(number)
    if guess < 1 or guess > 9:
        print("Number must be between 1 and 9.")
        continue

    if guess == random_number:
        print('Winner!')
        games_won += 1
    else:
        print('Better luck next time.')
        print(f"The correct number was: {random_number}")
        games_lost += 1

    play_again = input("Do you want to play again? (yes to continue, anything else to quit): ")
    if play_again.lower() not in ['yes', 'y']:
        break

print(f"Total games won: {games_won}")
print(f"Total games lost: {games_lost}")

