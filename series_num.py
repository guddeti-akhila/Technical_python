'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Following Series.

Constraints  :- No 


Example:
Input 1  :    10

                  -12

Output 1:    

50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, (-5), (-10), (-15), (-20), (-25), (-30), (-35), (-40), (-45), (-50), (-55), (-60)

 

Input 2  :    -6

                  8

Output 2:     (-30), (-25), (-20), (-15), (-10), (-5), 0, 5, 10, 15, 20, 25, 30, 35, 40


Explanation:
NA'''

num1 = int(input())
num2 = int(input())


for i in range(num1, num2+1):
    if 0>i:
        print(f"({i*5})",end="")
    else:
        print(i*5,end="")
    if i!=num2:
        print(",",end=" ")
        

for i in range(num1, num2-1, -1):
    if 0>i:
        print(f"({i*5})", end="")
    else:
        print(i*5,end="")
    if i!=num2:
        print(",",end=" ")
        
        
    

   
        
        
# list = [2,3,4,5,6,7,8]
# rev = list[::-1]
# print(rev)

'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Following Series.

Constraints  :- No 


Example:
Input 1  :    10

Output 1:    1, 2, factor of three, 4, 5, factor of three, 7, 8, factor of three, 10

 

Input 2  :    24

Output 2:    1, 2, factor of three, 4, 5, factor of three, 7, 8, factor of three, 10, 11, factor of three, 13, 14, factor of three, 16, 17, factor of three, 19, 20, factor of three, 22, 23, factor of three.


Explanation:
NA'''

num1 = int(input())

for i in range(1,num1+1):
    if i %3==0:
        print("factor of three",end="")
    else:
        print(i,end="")
    if i!=num1:
        print(",",end=" ")


'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Following Series.

Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".


Example:
Input 1  :    10

                  31

Output 1:    10^2, 12^2, 14^2, 16^2, 18^2, 20^2, 22^2, 24^2, 26^2, 28^2, 30^2

 

Input 2  :    -6

                  8

Output 2:     Invalid Inputs

 

Input 3  :    5

                  27

Output 3:    5^2, 7^2, 9^2, 11^2, 13^2, 15^2, 17^2, 19^2, 21^2, 23^2, 25^2, 27^2


Explanation:
NA'''

num1 = int(input())
num2 = int(input())
if num1>0 and num2>0:
    c=0
    for i in range(num1,num2+1,2):
        c+=1
        if c>1:
            print(",",end=" ")
        print(f"{i}^2",end="")
else:
    print("Invalid Inputs")


'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Following Series.

Constraints  :- No 


Example:
Input 1  :    25

Output 1:     1, 3, divisible by five, 7, 9, 11, 13, divisible by five, 17, 19, 21, 23, divisible by five

 

Input 2  :    38

Output 2:    1, 3, divisible by five, 7, 9, 11, 13, divisible by five, 17, 19, 21, 23, divisible by five, 27, 29, 31, 33, divisible by five, 37


Explanation:
NA


'''

num1 = int(input())
c=0
for i in range(1, num1+1):
    if i%2==1:
        c+=1
        if c>1:
            print(",",end=" ")
        if i%5 == 0:
            print("divisible by five",end="")
        else:
            print(i,end="")


'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Following Series.

Constraints  :- Given Input Must be Greater than Zero or else Print Invalid Input.


Example:
Input 1  :    10

Output 1:    5, 10, 5, 10, 5, 10, 5, 10, 5, 10

 

Input 2  :    -6

Output 2:     Invalid Input

 

Input 3  :    5

Output 3:    5, 10, 5, 10, 5


Explanation:
Print 5 and 10 Alternatively'''

num1 = int(input())
c = 0
if num1>0:
    for i in range(1,num1+1):
        c+=1
        if c>1:
            print(",",end=" ")
        if i%2==1:
            print("5",end="")
        else:
            print("10",end="")
            
else:
    print("Invalid Input")


'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Following Series.

Constraints  :- No 


Example:
Input 1  :    10

                  -12

Output 1:    

5*10, 5*9, 5*8, 5*7, 5*6, 5*5, 5*4, 5*3, 5*2, 5*1, 5*0, 5*(-1), 5*(-2), 5*(-3), 5*(-4), 5*(-5), 5*(-6), 5*(-7), 5*(-8), 5*(-9), 5*(-10), 5*(-11), 5*(-12)

 

 

Input 2  :    -6

                  8

Output 2:     5*(-6), 5*(-5), 5*(-4), 5*(-3), 5*(-2), 5*(-1), 5*0, 5*1, 5*2, 5*3, 5*4, 5*5, 5*6, 5*7, 5*8

 

Input 3  :    5

                  8

Output 3:    5*5, 5*6, 5*7, 5*8


Explanation:
NA'''

num1 = int(input())
num2 = int(input())
# if num1>0 and num2>0:
#     c = 0
#     for i in range(num1,num2+1):
#         c+=1
#         if c>1:
#             print(",",end=" ")
#         print(f"5*{i}",end="")
# if num1>0 and num2<0:
#     c=0    
#     for i in range(num1, num2-1,-1):
#         c+=1
#         if c>1:
#             print(",",end=" ")
#         if i<0:
#             print(f"5*({i})",end="")
#         else:
#             print(f"5*{i}",end="")
# if num1<0 and num2>0:
#     c = 0
#     for i in range(num1, num2+1):
#         c+=1
#         if c>1:
#             print(",",end=" ")
#         if i<0:
#             print(f"5*({i})",end="")
#         else:
#             print(f"5*{i}",end="")

if num1<num2:
    c=0
    for i in range(num1, num2+1):
        c+=1
        if c>1:
            print(",",end=" ")
        if i >= 0:
            print(f"5*{i}",end="")
        else:
            print(f"5*({i})",end="")
else:
    c = 0
    for i in range(num1,num2-1,-1):
        c+=1
        if c>1:
            print(",",end=" ")
        if i>=0:
            print(f"5*{i}",end="")
        else:
            print(f"5*({i})",end="")


'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One float Value.

                     Second Line of Input Consists of One float Value.

Output        :- Print the Following Series.

Constraints  :- No 


Example:
Input 1  :    10.7

                  12.1

Output 1:    

10.7^2, 10.9^2, 11.1^2,11.3^2, 11.5^2, 11.7^2, 11.9^2, 12.1^2.

 

Input 2  :    6.1

                  8.9

Output 2:     6.1^2, 6.3^2, 6.5^2, 6.7^2, 6.9^2, 7.1^2, 7.3^2, 7.5^2, 7.7^2, 7.9^2, 8.1^2, 8.3^2, 8.5^2, 8.7^2, 8.9^2.


Explanation:
NA'''

num1 = float(input())
num2 = float(input())
i=num1
c=0
while i<=num2:
    c+=1
    if c>1:
        print(',',end=" ")
    print(f"{i}^2",end='')
    i +=0.2
    
    i = round(i,1)
print(".")

'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Following Series.

Constraints  :- No 


Example:
Input 1  :    36

Output 1:    1, even, 3, even, 5, even, 7, even, 9, even, 11, even, 13, even, 15, even, 17, even, 19, even, 21, even, 23, even, 25, even, 27, even, 29, even, 31, even, 33, even, 35, even

 

Input 2  :    9

Output 2:    1, even, 3, even, 5, even, 7, even, 9


Explanation:
NA'''

num1 = int(input())
c = 0
for i in range(1,num1+1):
    c+=1
    if c>1:
        print(",",end=" ")
    if i%2==0:
        print("even",end="")
    else:
        print(i,end="")

'''Description:
Write program to print the following series which is shown in Given Examples.


Constraints:
Input         :-   First Line Of Input consists of One Integer value.

                      Second Line Of Input consists of One Integer value.

Output       :-   Print the Following Series.

Constraints :-   All the Values Should be Greater than Zero or else print "Invalid Inputs".


Example:
Input 1   : 100

                1000

Output 1 : 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000

 

Input 2   : 300

                2500

Output 2 : 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500

 


Explanation:
NA


'''

num1 = int(input())
num2 = int(input())
c = 0
for i in range(num1,num2+1,100):
    c+=1
    if c>1:
        print(",",end=" ")
    print(i,end="")
else:
    if num1<0 or num2<0:
        print("Invalid Inputs")

'''Description:
Write a program to print following pattern 

if input is 10 and -5

output will be 10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6

 


Constraints:
Input :          First line of input contains integer denotes starting range

                     Second line of input contains integer denotes ending range

Output :      Print pattern

 


Example:
 Input :            10   

                        -5

Output :         10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6


Explanation:
N/A'''


num1 = int(input())
num2 = int(input())
if num1>num2:
    c = 0
    for i in range(num1,num2-1,-1):
        c+=1
        if c>1:
            print(",",end="")
        print(f"{i}@{i-1}",end="")
else:
    c= 0
    for i in range(num1,num2+1):
        c+=1
        if c>1:
            print(",",end="")
        print(f"{i}@{i+1}",end="")