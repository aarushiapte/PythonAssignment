#Functions
#Question5-1
def gcd(i, j):
    if (j == 0):
        return i
    else:
        return gcd(j, i%j)


print(gcd(72, 12))

#Question5-2
def res(x,y):
    return (x+y)**2

print(res(4,3))

