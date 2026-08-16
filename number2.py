'''Description:
Write a Program to Print the Biggest Number out of the Given three Numbers?


Constraints:
Input      :  Three integer values.

Output   :  Print the Biggest Number from the Given Numbers.


Example:
Input 1     :  25

                    69

                    819 

Output 1  :  819 is a Biggest Number from the Given Numbers

 

Input 2     :  100

                    222

                    212

Output 2  :  222 is a Biggest Number from the Given Numbers

 

Input 3    :  999

                   565 

                   729

Output 3 :  999 is a Biggest Number from the Given Numbers


Explanation:
NA


'''

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1>num2 and num1>num3:
    print(f"{num1} is a Biggest Number from the Given Numbers")
elif(num2>num1 and num2>num3):
    print(f"{num2} is a Biggest Number from the Given Numbers")
else:
    print(f"{num3} is a Biggest Number from the Given Numbers")


'''Description:
write a program to perform all these tasks

a.     Store a number in a variable

b.    If value is not in range (100-1000) prints WRONG NUMBER else follows the steps

c.     Check even or odd

d.    If even divide the number by 3 and print the remainder

e.     If odd divide the number by 2 and print the remainder.


Constraints:
Input : First line of input contains an Integer n reperesent number


Example:
Input :         498

Output :      0

 


Explanation:
in the above example number is in range of 100-1000 and it is even we are dividing with 3 and printing remainder 0


'''

num = int(input())

if num>100 and num<1000:
    if num%2==0:
        print(num%3)
    else:
        print(num%2)
else:
    print("WRONG NUMBER")
    
'''Description:
Write a program to print CVCORP for 'N' times


Constraints:
Input :              One Integer Value Consists in First Line of Input.

Output :           Print CVCORP for 'N' Times.

Constraints :    10<N<100


Example:
Input 1 :      11

Output 1 :

CVCORP

CVCORP

CVCORP

CVCORP

CVCORP

CVCORP

CVCORP

CVCORP

CVCORP

CVCORP

CVCORP

 

Input 2 :      111

Output 2 :   Invalid Input


Explanation:
NA


'''

num = int(input())
if 10< num<100:
    for i in range(num):
        print("CVCORP")
else:
    print("Invalid Input")


'''Description:
Write a program to convert temperature from degree celcisu (C) to Farenheit (F).


Constraints:
Input           :    First line of input contains Integer 'n' represents temperature in celcius

Output         :   Temperature in farenheit

 


Example:
Input     :   96

Output  :   204.8F


Explanation:
In the above example input is 96,now you have to convert it into farenheit 

if we convert the value of 96 to farenheit we will get 204.8

note:  f=(c*9/5)+32
'''

num = int(input())
f = num*(9/5)+32
print(f"{f}F")

'''Description:
Write a program to print all numbers which are divisible by 11 in given range if no such numbers print NO NUMBERS if starting range is greater than ending range then print INVALID RANGE


Constraints:
Input :            First line of input contains an Integer n reperesent starting range

                       Second line of input contains an Integer n1 reperesent ending range

output :         all numbers which are divided by 11 in range


Example:
Input :       30 100

Output :     33 44 55 66 77 88 99


Explanation:
in the above example you have to print all 11 divisiors in range of 30 and 100'''

num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID RANGE")
else:
    c = 0
    for i in range(num1+1, num2):
        if i%11 == 0:
            print(i,end=" ")
            c += 1
 
    if c == 0:
        print("NO NUMBERS")


'''Description:
Write a program to perform Addition, Subtraction, Multiplication and Division of 2 Numbers based on the user inputs by using Switch condition.(+ , - , * , /, %).

 


Constraints:
Input :               First line of input contains an Integer 

                          Second line of input contains an Integer 

                          Third line of Input Consists of Operator

Output :            Print Respective Output.

Constraints :    Operators Must accept only one of this Operators( +, -, *, //, % ) only.


Example:
Input  :     30

                 10

                 +

Output :   40 


Explanation:
NA'''

num1 = int(input())
num2 = int(input())
op1 = input()
op = ["+","-","*","//","%"]

if op1 == op[0]:
    print(num1+num2)
elif op1 == op[1]:
    print(num1-num2)
elif op1 == op[2]:
    print(num1*num2)
elif op1==op[3]:
    print(num1//num2)
else:
    print(num1%num2)

'''Description:
write a progrm to perform given tasks

Declare & initialize a number.

Check whether the number is in range 0-100 or not.

If not in range print INVALID INPUT

Else – if the number is in range 91-100 then print SUPER SMART,

81-90 print SMART,

71-80 print SMART ENOUGH,

61-70 print JUST SMART,

36-60 print NO SMART,

0-35 print DUMB.


Constraints:
Input :          First line of input contains an Integer n reperesent number

Output :       Print their status


Example:
Input :       62

Output :   JUST SMART


Explanation:
here the input is in 61-70 range so you have to print JUST SMART
'''
num = int(input())

if num < 0 or num > 100:
    print("INVALID INPUT")
        
elif(num >= 91 and num <= 100):
    print("SUPER SMART")
elif(num >= 81 and num <= 90):
    print("SMART")
elif(num >=71 and num <= 80):
    print("SMART ENOUGH")
elif(num >= 61 and num <= 70):
    print("JUST SMART")
elif(num >= 36 and num <= 60):
    print("NO SMART")
else:
    print("DUMB")

'''Description:
Write a program to find sum of all the numbers in given range if starting index is greater than ending index print INVALID RANGE


Constraints:
Input :                First line of input contains integer n represent strating range

                           Second line of inputs contains integer n1 represent ending range

Output :            Print sum of numbers

 


Example:
Input :           10

                      20

Output :        165


Explanation:
print sum of all numbers in given range
'''
num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID RANGE")
else:
    add = 0
    for i in range(num1, num2+1):
        add = add + i
    print(add)

'''Description:
 Write a program to print all even numbers in range .if starting range is greater than ending range print "INVALID RANGE"


Constraints:
Input :               First line of input contains an Integer n represents starting range

                          Second line of input contains an Integer n1 represents ending range

Output :            Print All the Even Numbers in a Given Range.

 


Example:
Input :      1 10

output :   2 4 6 8 10


Explanation:
In the above example we have to print all the even numbers in the range of 1 to 10 with spaces'''

num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID RANGE")
else:
    for i in range(num1, num2+1):
        if i%2 == 0:
            print(i,end=" ")

'''Description:
write a program to convert kg values into gram values?


Constraints:
Input :           First line of input contains a decimal value represent weight in kgs

Output :        Print weight in grams


Example:
Input :          5.6

Output :       5600 Grams


Explanation:
in the above example we have to convert the 5.6kg to grams so you have to print 5600Grams.'''

num = float(input())
grams = num*1000
print(int(grams),"Grams")