#Exercise 1: Formula
import math


c=50
h=30
numbers=input('enter numbers comma separated')
result=''
for d in numbers :
    Q=math.sqrt((2*c*int(d))/h)
    result=', '.join([str(Q)])
print(result)
