#Daily challenge GOLD : Happy birthday
day=int(input('enter day '))
month=int(input('enter month'))
year=int(input('enter year '))
birthdate=f'{day}/{month}/{year}'
age=2025-year
number_of_candles=str(age)[-1]
print(number_of_candles)  # Use the string, not the int
print(age)
print(birthdate)
number=11-int(number_of_candles)
tire=number//2

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)) :
    print(f'    {'_'*tire}{'i'*int(number_of_candles)}{'_'*tire}')
    print(f'   |:H:a:p:p:y:|')
    print(f' __|___________|__')
    print(f'|^^^^^^^^^^^^^^^^^|')
    print(f'|:B:i:r:t:h:d:a:y:|')
    print(f'|                 |')
    print(f'~~~~~~~~~~~~~~~~~~~')
    print(f'    {'_'*tire}{'i'*int(number_of_candles)}{'_'*tire}')
    print(f'   |:H:a:p:p:y:|')
    print(f' __|___________|__')
    print(f'|^^^^^^^^^^^^^^^^^|')
    print(f'|:B:i:r:t:h:d:a:y:|')
    print(f'|                 |')
    print(f'~~~~~~~~~~~~~~~~~~~')
else :
    print(f'    {'_'*tire}{'i'*int(number_of_candles)}{'_'*tire}')
    print(f'   |:H:a:p:p:y:|')
    print(f' __|___________|__')
    print(f'|^^^^^^^^^^^^^^^^^|')
    print(f'|:B:i:r:t:h:d:a:y:|')
    print(f'|                 |')
    print(f'~~~~~~~~~~~~~~~~~~~')
