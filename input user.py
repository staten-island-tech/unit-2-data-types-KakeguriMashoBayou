
_______________________________________________________________
bill=float(input("Bill cost: $") )
treatment = input("How did it go? Good / Great / Bad / Okay: ")
if treatment == "Good" : 
    print( "$", bill*1.25)
elif treatment == "Great":
   print( "$", bill*1.2)
elif treatment == "Okay":
   print("$", bill*1.15)
elif treatment == "Bad":
   print("$", bill*1)
_______________________________________________

number = int(input("put a number:  "))
if number % 2 == 0: 
    print(number, "is even")
else:print(number, "is odd")
________________________________________________

x = input("son i'm crine:  ")
y= x.split( )
k=len(y)
if k== 1:
    print("your sentence has",k, "word")
else: print("your sentence has",k, "word")
