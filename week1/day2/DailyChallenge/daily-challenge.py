#Challenge 1: Multiples of a Number
number=int(input('enter number '))
lenght=int(input('enter lenght '))
list=[]
for l in range(1, lenght + 1):
    list.append(l * number)
print(list)

#Challenge 2: Remove Consecutive Duplicate Letters
word=input('enter word ')
new_word=''
last_letter=''
for w in word :
    if w in new_word and last_letter == w :
        continue
    else:
        new_word += w
        last_letter= w
print(new_word)
