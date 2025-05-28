year=int(input("Enter the year "))

if (year % 4 ==0):
    if (year % 100 ==0):
        print("not a leap year")
    else:
        print("leap year")
elif(year% 400 ==0):
    print("Leap year")
else:
    print("Not a leap year")