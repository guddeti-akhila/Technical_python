'''Description:
Write a program to print all Odd Numbers in Given Range.if starting range is greater than ending range print "INVALID RANGE"


Constraints:
Input :              First line of input contains Integer n represent starting index

                         Second line of input contains Integer n1 represents ending index

Output :           Print All the Odd Numbers in a Given Range

 


Example:
Input :            1

                       10

Output :         1 3 5 7 9


Explanation:
in the above example you have to print all the odd numbers in range of 1 to 10 they are 1 3 5 7 9


'''

num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID RANGE")
for i in range(num1, num2+1):
    if i%2 != 0:
        print(i,end=" ")


'''Description:
Write a program to find the average of all even numbers in the given range.if the strating range is Greater than ending range then print 

"INVALID RANGE"


Constraints:
Input :             First line of input contains Integer which denotes starting range

                        Second line of input contains Integer which denotes ending range

Output :         Average(decimal value)

 


Example:
Input :         10

                     30

Output :       20.0


Explanation:
in the above example even numbers in range are 10,12,14,16,18,20,22,24,26,28,30

avarage of those numbers is 20.0'''


num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID RANGE")
else:
    c=0
    a=0
    for i in range(num1, num2+1):
        if i%2 == 0:
            a = a+1
            c = c+i
    print(float(c/a))

'''Description:
Write a program to print sum of squares of the numbers in given range .if starting range is Greater than ending range print "INVALID RANGE"


Constraints:
Input :              First line of input contains a integer that denotes strating range

                         Second line of input contains a integer that denotes ending range

Output :           Integer that denotes sum


Example:
Input :          5 

                     23

Output :       4294


Explanation:
Input :        5 

                   23

Output :     4294

Explanation :

52 + 62 + 72 + 82 + 92 + 102 + 112 + 122 + 132 + 142 + 152 + 162 + 172 + 182 + 192 + 202 + 212 + 222 + 232

=25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 + 169 + 196 + 225 + 256 + 289 + 324 + 361 + 400 + 441 + 484 + 529

=4294


'''

num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID RANGE")
else:
    c = 0
    for i in range(num1, num2+1):
        c+=i**2
    print(c)

'''Description:
Write a program to print A,B in given number of times alternatively


Constraints:
Input :          First line of input contains Integer n 

Output :       Print A,B for n no of times


Example:
Input :          5

Output :       A,B,A,B,A,B,A,B,A,B


Explanation:
N/A'''

num1 = int(input())
c = 0
for i in range(num1):
    c+=1
    if c>1:
        print(",",end="")
    print("A,B",end="")


'''Description:
Write a Program to Print the following series 2*3,3*4,4*5,......16*17   (Print in two ways – Pattern & Multiplied value) .


Constraints:
Input     :  Two Integer Values

Output  :  Print the Respective Pattern from the Given Number(First Number) to the Given Number(Second Number),

               And

               Print the Respective Multiplied Value from the Given Number(First Number) to the Given Number(Second Number).


Example:
Input 1    :    2

                     16

Output 1 :    2*3, 3*4, 4*5, 5*6, 6*7, 7*8, 8*9, 9*10, 10*11, 11*12, 12*13, 13*14, 14*15, 15*16, 16*17

                     6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272

 

Input 2    :    10

                      1

Output 2 :    1*2, 2*3, 3*4, 4*5, 5*6, 6*7, 7*8, 8*9, 9*10, 10*11

                      2, 6, 12, 20, 30, 42, 56, 72, 90, 110


Explanation:
NA'''

num1 = int(input())
num2 = int(input())
if num1>num2:
    num1,num2 = num2,num1
c = 0
for i in range(num1, num2+1):
    c += 1
    if c>1:
        print(",",end=" ")
    print(f"{i}*{i+1}",end="")
print()
c = 0
for i in range(num1,num2+1):
    c = c+1
    if c>1:
        
        print(",",end=" ")
    print(i*(i+1),end="")


'''Constraints :  All the Given inputs Must be Greater than Zero, or else Print "Invalid Inputs".


Example:
Input 1    :  10

                   30

Output 1 :  12 16 20 24 28

 

Input 2    :  5

                   25

Output 2 :  6 10 14 18 22 

 

Input 3     :  -5

                    25

Output 3  :  Invalid Inputs


Explanation:
NA'''

num1 = int(input())
num2 = int(input())
if num1<=0 or num2<=0:
    print("Invalid Inputs")
else:
    c =0  
    for i in range(num1+1, num2):
        if i%2 == 0:
            c+=1
            if c%2==1:
                print(i,end=" ")


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
N/A


''' 

num = int(input())
num1 = int(input())
if num<=num1:
    
    c = 0
    for i in range(num, num1+1):
        c+=1
        if c>1:
            print(",",end="")
        print(f"{i}@{i+1}",end="")
else:
        
    c =0
    for i in range(num, num1-1,-1):
        c+=1
        if c > 1:
            print(",",end="")
        print(f"{i}@{i-1}",end="")


'''Description:
Write a program to find the count of even numbers in given range.if no even numbers print NO NUMBERS if Strating range is greater than ending range print INVALID RANGE


Constraints:
Input :                First line of input contains Integer n represent staring range

                           Second line of input contains Integer n1 represent ending range

Output :             Print Count of the All even Numbers in a Given Range

 


Example:
Input :      10

                  20

Output :   6


Explanation:
In the above example there are 6(including 10,20) even numbers in range of 10 and 20 are 10,12,14,16,18,20


'''

num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID RANGE")
else:
    c = 0
    for i in range(num1, num2+1):
        if i%2 == 0:
            c+=1
  
    if c == 0:
        print("NO NUMBERS")
    else:
        print(c)


'''Description:
Write a program to print sum of all even numbers in between the Given Numbers if no even numbers print NO NUMBERS if starting range is greater than ending range then print INVALID RANGE


Constraints:
Input :                First line of input contains an Integer n reperesent starting range

                           Second line of input contains an Integer n1 reperesent ending range

Output :            Print sum of all even numbers in given range

 


Example:
Input :          20

                     40

Output :       270


Explanation:
in the above example we have to sum all the even numbers in between 20 and 40

22+24+26+28+30+32+34+36+38=270'''

num1 = int(input())
num2 = int(input())
if num1> num2:
    print("INVALID RANGE")
else:
  
    c = 0
    for i in range(num1+1, num2):
        if i%2 == 0:
           
            c+=i
    if c == 0:
        print("NO NUMBERS")
    else:
        print(c)


'''Description:
Write a program to print all alternative even numbers in the given range if no numbers then print NO NUMBERS if starting range is greater than ending range print INVALID INPUTS


Constraints:
Input :             First line contains an Integer n  represents starting range

                        Second line contains an Integer n1 represent ending range

Output :         Print Alternative Even Numbers in Range

 


Example:
Input  :           10

                       30

Output :        10 14 18 22 26 30


Explanation:
int the above example we have to print all the alternative even numbers in the range of 10 to 30 they are 10 14 18 22 26 30'''


num1 = int(input())
num2 = int(input())
if num1>num2:
    print("INVALID INPUTS")
else:
    c = 0
    for i in range(num1, num2+1):
        if i%2 ==0:
            c += 1
            if c%2==1:
                print(i, end=" ")
    if c==0:
        print("NO NUMBERS")

        # hii akhila