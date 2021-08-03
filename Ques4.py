#Loops
#Question4-1
num = int(input("Enter total number of elements you want to enter in the list"))

l1 = []
for i in range(0, num):
    inp = int(input(""))
    l1.append(inp)
result = ''
for i in l1:
        result = result + str(i)
print (result)

#Question4-2
color_list_1 = set(["White", "Black", "Red"])

color_list_2 = set(["Red", "Green"])

print("Result: ", color_list_1 - color_list_2)
