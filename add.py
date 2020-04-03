
while True:
    n=int(input("Enter the number of elements you want to add: "))
    a=input("Do you want to re-enter the total numbers (yes/no): ")


    if a=="yes":
        continue


    elif a=="no":
        
        lst=[]
        for i in range(n):
            numbers=int(input("enter numbers: "))
            lst.append(numbers)

        print("sum is: ",sum(lst))
        b=input("Do you want to add again(yes/no)")
        if b=="yes":
            continue
        else:
            break
        
    else:
        print("command not understood, enter again")
        



'''
#old program
a=int(input("enter first integer: "))
b=int(input("enter second number: "))

c=a+b

print("addition of two number is: ", c)
'''
