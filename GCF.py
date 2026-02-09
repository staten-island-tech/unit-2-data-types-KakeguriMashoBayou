one = int(input("Put a number:  "))
two = int(input("Put second number:  "))
print("factors of", one and two)
for i in range(two, one+1):
    if one + two%i == 0:
        print (i)
