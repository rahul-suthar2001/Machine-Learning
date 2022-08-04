cards = [ 1 , 5 , 3 , 4 , 2 , 3 , 2 ]
def nextCard ( cards ):
    next = cards[0]
    newHand = cards[1:] + [ cards[0] ]
    return next , newHand


''' -> It return tuple which contains number and list
-> function takes list of cards and store first item form list and store in "next" variable
       and createlist "newHand" in this we store all item but we store first item at last index
-> It would be a simple matter for this function to alter the input list
so that the first element becomes the last. This would simplify
the return value, which is currently two items. Why might this
be considered a poorer solution because this alter the original list
 while above function not alter the original list
     
'''
# Write a loop that calls this function repeatedly, printing out the
#card from the top of the deck each time.

t = int(input("how many times you want to nextCard : "))
prev=0
isFound = False


for i in range(t):
    top,newHand = nextCard(newHand)
    print(top)
    if prev==top:
        isFound=True
    prev=top

'''
Using the given function and your answer to the previous question as a starting point,
write a program that checks a deck of
cards for consecutive identical pairs (a 2 followed by a 2, for
example). If a pair is found, a message should be displayed
'''

if isFound:
    print(" Pair FOund ")


'''What happens if the input list is empty? Correct the function so
that it returns ( None , [ ] ) when an empty list is used as input.'''

def nextCard ( cards ):
    if len(cards)==0:
        return (None,[])
    next = cards[0]
    
    newHand = cards[1:] + [ cards[0] ]
    return next , newHand