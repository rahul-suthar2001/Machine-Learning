months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
days = [31, [28,29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dic ={}
for i in range(len(months)):
    dic[months[i]] = days[i]

print(dic)