def NAND(A,B):
    if A==True and B==True:
        return False
    else:
        return True

A=10
B=20
ans1 = NAND(A<B, B>A)
ans =NAND(A>B, B>A)
print(ans1,ans)