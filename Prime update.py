from numba import njit
#  coment @njit for dont use GPU
@njit
def fast():
    print("Your number", P, "is`")
    for i in range(2, P):
        x = P % i
        if x == 0:
            print("NOT")
            break
P = int(input("Input the number>>"))
fast()
print("PRIME")

# 2147483647 prime for test 2 min*
# using numba>> 2147483647 prime for test 4-10s !!!!!!
# 2147483648 not prime for test 0000001 ms*
# using numba>> number 545554545457 is` not PRIME 0000001 ms