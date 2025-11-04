# number=int(input("enter number :"))
# for num in range(1,11):
#     print(f"{number}*{num}={number*num}")

# num=1
# while num<=10 :
#     print(num)
#     num+=1

current_number = 0
while current_number <= 10:
    current_number += 1
    if 3 < current_number < 7: # If the number is between 3 and 7
        continue                # Go back to the beginning of the loop
    print(current_number)