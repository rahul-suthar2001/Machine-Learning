
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcdList(ls):
    res=ls[0]
    for i in ls:
        res=gcd(res,i)
    return res




num= int(input("How many numbers do you want to enter? "))
nums = []
if(num <2):
    print("Enter more than 2 number next time") 
    exit()
else:
    for i in range(num):
        nums.append(int(input("Enter number " + str(i+1) + ": ")))
    ans=gcdList(nums)  
    print(ans)