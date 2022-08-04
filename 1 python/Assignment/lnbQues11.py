nums =[2,5,11,15,13,7,6]
target= 13


def findtarget(ls,target):
    n = len(ls)
    if n<2:
        print("List must contain more than 1 element")
        return
    else:
        for num in ls:
            if (target-num) in ls:
                return [ls.index(num),ls.index(target-num)]

print(findtarget(nums, target))