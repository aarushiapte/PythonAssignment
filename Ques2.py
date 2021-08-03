#Operators
#Question2-1
from math import pi
r = float(input("Enter radius of circle: "))
area = pi*r**2
print("Area is: ", area)

#Question2-2
n = int(input())
print("Result = ", n+((n*10)+n)+((n*100)+(n*10)+n))

#Question2-3
from datetime import date
startDate = date(2021, 6, 10)
endDate = date(2021, 6, 19)
numOfDays = endDate-startDate
print(numOfDays.days)
