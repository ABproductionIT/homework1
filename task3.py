P = int(input("Input the number>>"))
print("Your number", P, "is`")
for i in range(2, P):
    x = P % i
    if x == 0:
        print("NOT")
        break
print("PRIME")
