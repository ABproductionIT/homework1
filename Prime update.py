from numba import njit

# for start install numba >> pip install numba
P = int(input("Input the number>>"))
if P < 0:
    P -= 2*P
    print("Your number  -", P, "is`")
elif P == 0:
     print("Your number is zero, cant  do NOT PRIME  /")
else:
    print("Your number", P, "is`")
    @njit
    def tivi():
        for i in range(2, P):
            x = P % i
            if x == 0:
                print("NOT")
                break
print("PRIME")
# 2147483647 prime for test 2 min*
# 2147483648 not prime for test 0000001 ms*