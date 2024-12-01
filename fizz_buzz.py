while True:   
    num=int(input("Enter a number : "))
    if (num == 0) :
        print("Exiting program")
        exit(2)
    elif(num %3 ==0 and num %5==0):
        print("Fizzbuzz")
    elif num%5 == 0:
        print("Buzz")
    elif num %3 == 0:
        print("Fizz")
    
    else:
        print(num)