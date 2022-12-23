#Choose another number, check y and n as well. Present errors are only for y and n and choose another option
#y = var (input (y))
# n = var (input (n)

num = int ( input ("Is this number a multiple of 2, 3, 5 or 7: "))
if num % 2 == 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print ("The number is a multiple of 2")
elif num % 3 == 0 and num % 2 != 0 and num % 5 != 0 and num % 7 != 0:
    print ("The number is a multiple of 3")
elif num % 5 == 0 and num % 2 != 0 and num % 3 != 0 and num % 7 != 0:
    print ("The number is a multiple of 5")
elif num % 7 == 0 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
    print ("The number is a multiple of 7")
elif num % 2 == 0 and num % 3 == 0 and num % 5 != 0 and num % 7 != 0:
    print ("The number is a multiple of 2 and 3")
elif num % 2 == 0 and num % 5 == 0 and num % 3 != 0 and num % 7 != 0:
    print ("The number is a multiple of 2 and 5")
elif num % 2 == 0 and num % 7 == 0 and num % 3 != 0 and num % 5 != 0:
    print ("The number is a multiple of 2 and 7")
elif num % 3 == 0 and num % 5 == 0 and num % 2 != 0 and num % 7 != 0:
    print ("The number is a multiple of 3 and 5")
elif num % 3 == 0 and num % 7 == 0 and num % 2 != 0 and num % 5 != 0:
    print ("The number is a multiple of 3 and 7")
elif num % 5 == 0 and num % 7 == 0 and num % 2 != 0 and num % 3 != 0:
    print ("The number is a multiple of 5 and 7")
elif num % 2 == 0 and num % 3 == 0 and num % 5 == 0 and num % 7 != 0:
    print ("The number is a multiple of 2,3 and 5")
elif num % 3 == 0 and num % 5 == 0 and num % 7 == 0 and num % 2 != 0:
    print ("The number is a multiple of 3,5 and 7")
elif num % 2 == 0 and num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
    print ("The number is a multiple of 2,3,5 and 7")
else:
    print ("You have chosen a prime number!")
print ("Do you want to choose another number(y/n): ")
if y (repeat())
    print ("Choose another number")
If n (exit())
         print ("Thank you for running this program") 
