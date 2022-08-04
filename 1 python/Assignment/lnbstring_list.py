para = input("Enter the string = ")

# initialize list for storing the words 
ans =[]

# loop through the string and split the string into words
for word in para.split(" "):
    # compare word length and  append the word to the list
    if len(word)>4:
        ans.append(word)
print(ans)