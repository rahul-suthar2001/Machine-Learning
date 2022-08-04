def even_filter(n):
    ls = []
    for i in n:
        if i % 2 != 0:
            ls.append(i)
    return ls
def odd_filter(dict):
    ls = []
    for i in dict.values():
        if i % 2 == 0:
            ls.append(i)
    return ls

dict = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}
ls  =[10,20,31,42,53]

print(odd_filter(dict))
print(even_filter(ls))
