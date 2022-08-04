# Take user input
user_input = input("Enter a string: ")

# initialize variables for counting 
cat=0
dog=0
#convert whole string into lower case
user_input= user_input.lower()

# count the number of times the word "cat" occurs in the string
if "cat"  in user_input:
    cat =user_input.count("cat")

# count the number of times the word "dog" occurs in the string

if "dog" in user_input:
    dog = user_input.count("dog")

 # compare dog and cat count and print the result   
if dog==0 or cat==0:
    print( False)
elif dog==cat:
     print(True)
else:
    print(False)
