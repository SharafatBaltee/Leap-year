
year = int(input("Enter the year: "))
if year%4==0:
    print("This is a leap year")
elif year%100==0:
    print("This is a century: ")
else:
    print("Not a leap year and a century")