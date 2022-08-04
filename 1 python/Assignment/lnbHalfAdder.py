def XOR(a,b):
    if a!=b:
        return 1
    else:
        return 0


def halfAdder(a,b):
    s = XOR(a,b)
    c= a and b
    return s,c

print("A   B   (sum,carry)")
print("------------------")
print("0   0   ",halfAdder(0, 0))
print("0   1   ",halfAdder(0, 1))
print("1   0   ",halfAdder(1, 0))
print("1   1   ",halfAdder(1, 1))

