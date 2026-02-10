one = int(input("Put a number:  "))
two = int(input("Put a number:  "))
print("factors of", one and two)
for i in range(1, one+1):
    if i <= two: 
        if one%i == 0 and two%i == 0:
            gcf = i
            
print ("The GCF is:", gcf)

