n = int(input())
printout = "long " * (n//4)

print(printout + "int" if n % 4 == 0 else printout + "long int")