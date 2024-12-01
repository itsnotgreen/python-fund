# a leap year if it is divisible by 4

attempts = int(input("How many years do you want to check?  "))

for i in range (attempts):
    year=int(input("Enter the year : "))
    if (year % 4 == 0 and year % 100 != 0):#if yes leap year
        print(f"{year} is a leap year ")
    elif (year % 400 ==0)  :
        print(f"{year} is a leap year")
    else:
        print(f"{year} is  not a leap year")