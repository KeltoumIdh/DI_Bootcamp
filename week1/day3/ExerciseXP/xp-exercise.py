#🌟 Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1={}
for i in zip(keys,values) :
    dict1[i[0]]=i[1]
print(dict1)
#🌟 Exercise 2: Cinemax #2
# family = {}
# while True:
#     name=input('type  member name (or type done) ')
#     if name == 'done':
#         break
#     age=int(input('type  member age '))
#     family[name]=age
# print('family',family)
# cost=0
# for x,y in family.items():
#     if y < 3 :
#         print(f'{x} will pay nothing')
#         pass
#     elif 3<=y<=12 :
#         print(f'{x} has 10$')
#         cost+=10
#     else:
#         print(f'{x} has 15$')
#         cost+=15
# print('the total cost: ',cost)
#🌟 Exercise 3: Zara
brand={
'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color':{
    'France': 'blue',
    'Spain': 'red',
    'US': ['pink', 'green']}
}
more_on_zara={
'creation_date': 1975,
'number_stores': 25,
}

# brand['number_stores']=2
# type_of_clothes =brand['type_of_clothes']
# print(f'type of cloths in zara brand are {type_of_clothes[0]},{type_of_clothes[1]},{type_of_clothes[2]},{type_of_clothes[3]}')
# brand['country_creation']='Spain'
# if 'international_competitors' in brand:
#     brand['international_competitors'].append('Desigual')
# del brand['creation_date']
# print(brand['international_competitors'][-1])
# print(brand['major_color']['US'])
# print(len(brand.keys()))
# print(brand.keys())
# new_dict= brand | more_on_zara
# print(new_dict)

#🌟 Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
character_dict = {user: index for index, user in enumerate(users)}
print(character_dict)
print(dict(enumerate(users)))
sorted_users = sorted(users)
alphabetical_character_dict = {user: index for index, user in enumerate(sorted_users)}
print(alphabetical_character_dict)
