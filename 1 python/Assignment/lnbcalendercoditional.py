# Take input form user and store in a variable
year = int(input("Enter the year = "))
month = int(input("Enter the month(In integer format) = "))
day = int(input("Enter the day = "))


if(month > 12 or month < 1):
    print("Invalid month")
    exit()
elif(day > 31 or day < 1):
    print("Invalid day")
    exit()

if(month==4 or month==6 or month==9 or month==11 ):
    if(day > 31 or day < 1):
        print("Invalid day")
        exit()
elif(month==2):
    if(year%4==0):
        if(day > 29 or day < 1):
            print("Invalid day")
            exit()
    else:
        if(day > 28 or day < 1):
            print("Invalid day")
            exit()
else:
    if(day > 30 or day < 1):
        print("Invalid day")
        exit()



# check season
def checkSeason():
        if (month == 12 or month==1 ):
            print("The month is ", month, "and the day is ", day, "of ", year, "is a Winter day")
        elif (month==2 or month==3 ):
            print("The month is ", month, "and the day is ", day, "of ", year, "is a Spring day")
        elif (month==4 or month==5 or month==6 ):
            print("The month is ", month, "and the day is ", day, "of ", year, "is a Summer day")
        elif (month==7 or month==8  ):
            print("The month is ", month, "and the day is ", day, "of ", year, "is a Monsoon day")
        else:
            print("The month is ", month, "and the day is ", day, "of ", year, "is a Autumn day")


def nextLeapyear(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        print("The next leap year is ", year, "and In this year 366 days" )
    else:
        nextLeapyear(year+1)



# leap year
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is ", year, "and it is a leap year and In this year 366 days" )
    checkSeason()
else:
    nextLeapyear(year)
    checkSeason()



        
