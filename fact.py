num = int(input("enter the number : "))
factorial = 1
if num < 0 :
    print("enter correct number")

elif num == 0 :
    print("factorial of",num,"is 1")
    
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("factorial of",num,"is ",factorial)
