
def fact(num):
    ans = 1
    while num>0:
        ans = ans*num
        num-=1
    return ans

def permutations(n,r):
    return (fact(n)/fact(n-r))

def combinations(n,r):
    return (fact(n)/(fact(r) * fact(n-r)))


n = int(input("Enter the value of n : "))
r= int (input("Enter the value of r : "))

p = int(permutations(n, r))
c = int(combinations(n,r))
print("permutations of ",n,r," is ",p)
print("combinations of ",n,r," is ",c)

