digit = input('Enter the number : ')

def productOfDigit(num):
    product=1
    for i in str(num):
        product=product*int(i)
    return product

#MDR

def MDR(num,count):
    if len(str(num))==1:
        return num,count
    else:
        count+=1
        return MDR(productOfDigit(num),count)

print(MDR(digit,0))


