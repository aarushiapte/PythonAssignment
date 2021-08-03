#Decision control
#Question3-1
inp = input()

if inp[0:2] == 'ls':
    print(inp)
else:
    str = "ls" + inp
    print(str)

#Question3-2
num = int(input())
if num%2==0:
    print(num, " is even.")
else:
    print(num, "is odd.")

#Question3-3
inp = input().upper()
vowels= 'AEIOU'
if inp in vowels:
    print('Vowel')
else:
    print('Not a vowel')

