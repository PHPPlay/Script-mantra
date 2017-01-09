#!/usr/bin/python3

# This prorgam verify the number is zero or other number

###"""Comparison operator
##== - ls Equal to
##!= -Not Equal to
###> -Greater than
###< = Less than
###>= - Greater than or equal to
##<= -Less than or equal to '''
# num = int(input("Please enter a number: "))
# if num != 0:
#   print("the number is not zero")
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))
if num_1 > num_2:
    print("The num1 is greater than num2")
    print("The difference is " + str(num_1 - num_2))
elif num_1 < num_2:
    print("The num1 is lesser than num2")
    print("The difference is "+ str(num_2 - num_1))
elif num_1 == num_2:
    print("The num1 and num2 are equal ")
    print("The difference is " + str(num_1 - num_2))
#if num > 0:
 #   print("The number is greater than zero")
#elif num < 0:
 #   print("The number is less than zero ")
#else:
 #   print('The number is zero ')
#print(num)
