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
