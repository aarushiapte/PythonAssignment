#Data type
# Question1-1
inp = input()
result = ""
length = len(inp)

for i in range(0, length):
    if length < 2:
        print('Empty string')
        break
    else:
        result = inp[0:2] + inp[-2:]

print(result)

# Question1-2
num = int(input("Enter total number of elements you want to enter in the list"))

l1 = []
for i in range(0, num):
    inp = int(input(""))
    l1.append(inp)

print("Largest number is: ", max(l1))

#Question1-3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}

for i in (dic1, dic2, dic3):
    dic4.update(i)

print(dic4)


