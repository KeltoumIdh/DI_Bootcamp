#🌟 Exercise 1 : Student Grade Summary
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
student_averages={}
student_letter_grades={}
for x,y in student_grades.items():
    avg = sum(y) / len(y)
    student_averages[x] = int(avg)
    if avg >= 90 :
        student_letter_grades[x]='A'
    elif 80<=avg<=89:
        student_letter_grades[x]='B'
    elif 70<=avg<=79:
        student_letter_grades[x]='C'
    elif 60<=avg<=69:
        student_letter_grades[x]='D'
    else :
        student_letter_grades[x]='F'
print(student_averages)
print(student_letter_grades)
total_avg = sum(student_averages.values()) / len(student_averages)
print('the average of all students', total_avg)
for i,j in student_averages.items() :
    for x,y in student_letter_grades.items():
        if i==x :
            print(f'the student {x} have : {j} , {y}')

#🌟 Exercise 2 : Advanced Data Manipulation and Analysis

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]
total_sales={}
for i in sales_data:
    print(i)
    for j,z in i.items():
            total_sales['product']=i['product']
            # total_sales['total']+=i['price']
print('total:',total_sales)