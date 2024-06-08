years = input("Give year")
year = int(years)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else: 
            print("Not a leap year")
    else :
        print("Leap year")
    
else: 
    print("Not a Leap Year")