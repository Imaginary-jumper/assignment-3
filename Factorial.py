n= int(input("enter a number you want to find factorial:"))
def factorial(a):
    if a < 2:
        print (1)
    else:
        b=1
        for i in range(1,a+1):
            b=b*i
        print("factorial of",a,"is:",b)
factorial(n)