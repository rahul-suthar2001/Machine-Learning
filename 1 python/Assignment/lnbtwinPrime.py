
def checkPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def twin_prime():
    twinPrime = []
    for i in range(1,1000,2):
        if checkPrime(i) and checkPrime(i+2):
            twinPrime.append([i,i+2])
            
    return twinPrime

print(twin_prime())

