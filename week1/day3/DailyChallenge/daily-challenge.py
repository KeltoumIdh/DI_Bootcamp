#Challenge 1: Letter Index Dictionary
from queue import Empty


word = input('Enter a word: ')
dic = {}
for index, letter in enumerate(word):
    if letter in dic:
        dic[letter].append(index)
    else:
        dic[letter] = [index]
print(dic)
#Challenge 2: Affordable Items
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
wallet=int(wallet.replace('$','').replace(',', ''))
for x,y in items_purchase.items():
        items_purchase[x] = y.replace('$', '').replace(',', '')
basket=[]
for x,y in items_purchase.items():
    if wallet>=int(y):
        wallet-=int(y)
        basket.append(x)
else:
    if Empty(basket):
        print('nothing')
print(sorted(basket))