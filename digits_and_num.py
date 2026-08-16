'''Description:
Write a program to find Sum of first 'n' Natural Numbers Without Using formula?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print Sum of first 'N' Natural Numbers.

Constraints  :- Given Input is Zero then Print "InvaLid Input.".

                      If Given Input is Negative then Print "Sorry! you have Entered Negative Values.".


Example:
Input 1  :    10

Output 1:    Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.

 

Input 2  :   5

Output 2:   Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 = 15.

 

Input 3  :    8

Output 3:    Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36.


Explanation:
Input 1  :    10

Output 1:    Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.

Explanation:

First 'N' Numbers is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Sum of First 'N' Numbers is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

 

Input 2  :   5

Output 2:   Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 = 15.

Explanation:

First 'N' Numbers is 1, 2, 3, 4, 5

Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 = 15.

 

Input 3  :    8

Output 3:    Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36.

Explanation:

First 'N' Numbers is 1, 2, 3, 4, 5, 6, 7, 8

Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36.


'''

num = int(input())
if num == 0:
    print("InvaLid Input.")
elif num<0:
    print("Sorry! you have Entered Negative Values.")
else:
    c=0
    sum =0
    print("Sum of 'N' Natural Numbers is ", end="")
    for i in range(1,num+1):
        sum+=i
        c+=1
        if c>1:
            print(f" + ", end="")
        print(f"{i}", end="")
    print(f" = {sum}.")


'''Description:
Write a Program to print the Highest digit in a Given Number?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print Highest Digit in a Given Number.

Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input.".


Example:
Input 1  :    25696

Output 1:    Highest Digit in a Given Number is 9.

 

Input 2  :   -81

Output 2:    Invalid Input.

 

Input 3  :    2683651

Output 3:    Highest Digit in a Given Number is 8.


Explanation:
Print the Highest Digit in a Given Number as shown in Example.


'''

num = int(input())
if num <=0:
    print("Invalid Input.")

else:
    max = 0
    while num >0:
        r = num%10
        if max<r:
            max = r
        num = num//10
    print(f"Highest Digit in a Given Number is {max}.")

'''Description:
Write a program to find Sum of first 'n' Natural Numbers by Using formula?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print Sum of first 'N' Natural Numbers.

Constraints  :- Given Input is Zero then Print "InvaLid Input.".

                      If Given Input is Negative then Print "Sorry! you have Entered Negative Values.".


Example:
Input 1  :    10

Output 1:    Sum of 'N' Natural Numbers is 55.

 

Input 2  :   5

Output 2:   Sum of 'N' Natural Numbers is 15.

 

Input 3  :    8

Output 3:    Sum of 'N' Natural Numbers is 36.


Explanation:
Input 1  :    10

Output 1:    Sum of 'N' Natural Numbers is 55.

Explanation:

n * ( n  + 1 ) / 2

= 10 * 11 / 2

= 55

 

Input 2  :   5

Output 2:   Sum of 'N' Natural Numbers is 15.

Explanation:

n * ( n + 1 ) / 2

= 5 * 6 / 2

= 15

 

Input 3  :    8

Output 3:    Sum of 'N' Natural Numbers is 36.

Explanation:

n * ( n + 1 ) / 2

= 8 * 9 / 2

= 36'''

num = int(input())
if num==0:
    print("InvaLid Input.")
elif num<0:
    print("Sorry! you have Entered Negative Values.")
    
else:
    sum = 0
    for i in range(1, num+1):
     
        sum+=i
     
    print(f"Sum of 'N' Natural Numbers is {sum}.")

'''Description:
Write a Program to print the smallest digit in a Given Number?


Constraints:
 

Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print Smallest Digit in a Given Number.

Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input.".


Example:
Input 1  :    25696

Output 1:    Smallest Digit in a Given Number is 2.

 

Input 2  :   -81

Output 2:    Invalid Input.

 

Input 3  :    2683651

Output 3:    Smallest Digit in a Given Number is 1.


Explanation:
Print the Lowest Digit in a Given Number as shown in Example.'''
num = int(input())
if num <=0:
    print("Invalid Input.")
else:
    
    min = 9
    while num>0:
        r = num%10
        if r<min:
            min = r
        num= num//10
    print(f"Smallest Digit in a Given Number is {min}.")


'''Description:
Write a Program to check if the Given Number is Perfect Square or Not a perfect Square?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print Given Number is Perfect Square or Not.

Constraints  :- Given Input is a Zero or a Negative Value then Print "InvaliD Input".


Example:
Input 1  :    10

Output 1:    Given Number is Not a Perfect Square.

 

Input 2  :   5

Output 2:   Given Number is Not a Perfect Square.

 

Input 3  :    16

Output 3:    Given Number is a Perfect Square.


Explanation:
Input 1  :    10

Output 1:    Given Number is Not a Perfect Square.

Explanation :

The resultant of an integer multiplied by itself is a perfect square.

Given Number is 10 so it is in between the 3*3=9 and 4*4=16, So it is Not a Perfect Square. 

 

Input 2  :   5

Output 2:   Given Number is Not a Perfect Square.

Explanation :

The resultant of an integer multiplied by itself is a perfect square.

Given Number is 5 so it is in between the 2*2=4 and 3*3=9, So it is Not a Perfect Square. 

 

Input 3  :    16

Output 3:    Given Number is a Perfect Square.

Explanation :

The resultant of an integer multiplied by itself is a perfect square.

Given Number is 16 so it is in between the 4*4=16, So it is a Perfect Square. 


'''

import math
num = int(input())
if num<=0:
    print("InvaliD Input")
else:
    
    sq = int(math.sqrt(num))

    if sq*sq==num:
        print("Given Number is a Perfect Square.")
    else:
        print("Given Number is Not a Perfect Square.")

'''Description:
Write a program to Find Sum of Digits of a Given Number?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print Sum of Digits as Given in Examples.

Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input.".


Example:
Input 1  :    25696

Output 1:    2 + 5 + 6 + 9 + 6.

 

Input 2  :   -81

Output 2:    Invalid Input.

 

Input 3  :    2683651

Output 3:    2 + 6 + 8 + 3 + 6 + 5 + 1.


Explanation:
If Given Number is Positive then print the following pattern.


'''
num = int(input())
if num<=0:
    print("Invalid Input.")
else:
    # c = 0
    # while num>0:
    #     r = num%10
    #     c+=1
    #     if c>1:
    #         print(" + ", end="")
    #     print(f"{r }", end="")
    #     num = num//10
    # print(".")
    
    s = str(num)
    c = 0
    for i in s:
        c+=1
        if c>1:
            print(" + ", end="")
        print(i, end="")
    print(".")

'''Description:
Write a Program to Print The Sum of all odd Positions in a Given Number?

 

If the Input is 5432 then, print the output as 6.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Sum of Digits in Odd Positions.

Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".


Example:
Input 1  :    5432

Output 1:    6

 

Input 2  :    -6896

Output 2:     Invalid Input

 

Input 3  :    6481

Output 3:    5


Explanation:
5432       -->   5  4  3  2

positions -->   4  3  2  1

Pick Digits at Odd Positions-->2 + 4 = 6

 

-6896     -->  Invalid Input

 

6481       -->   6  4  8  1

positions -->    4  3  2  1

Pick Digits at Odd Positions-->1 + 4 = 5


'''

num = int(input())
if num<=0:
    print("Invalid Input")
else:
    sum = 0
    c = 0
    while num>0:

        r = num%10
        c+=1
        if c%2==1:
            sum+=r
        num = num//10
    print(sum)


'''Description:
Write a Program to Print Count no of Digits in a Given Number?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print Integer Number ( No of Digits in Given Number ).

Constraints  :- Given Input is Zero then Print "InvaliD Input".


Example:
Input 1  :    418

Output 1:    Given Number consists of 3 Digits.

 

Input 2  :   -81

Output 2:    Given Number consists of 2 Digits and it is Negative Value.

 

Input 3  :    2683651

Output 3:    Given Number consists of 7 Digits.


Explanation:
Find and count no of Digits in a given Number and check if it's a Negative value or a Positive value.'''

num = int(input())
if num==0:
    print("InvaliD Input")
    
elif num < 0:
    num = -num
    c=0
    while num>0:
        r = num%10
        c+=1
        num //=10

    if c == 1:
        print("Given Number consists of only 1 Digit and it is Negative Value.")
    else:
        
        print(f"Given Number consists of {c} Digits and it is Negative Value.")
else:
    c=0
    while num>0:
        r = num%10
        c+=1
        num //=10
    if c == 1:
        print("Given Number consists of only 1 Digit.")
    else:
        print(f"Given Number consists of {c} Digits.")
    # if c==1:
    #     print("K")

'''Description:
Write a Program to Print The Sum of the Even Digits in a Given Number?

 

If your input is 212 then, you have to print 4 as the output.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Sum of the Even Digits.

Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".


Example:
Input 1  :    212

Output 1:    4

 

Input 2  :    -634

Output 2:     Invalid Input

 

Input 3  :    515

Output 3:    0


Explanation:
212  -->  2 + 2 = 4

-634 -->   Invalid Input  ( Given Value is Less than Zero )

515  -->  0'''

num = int(input())
if num <= 0:
    print("Invalid Input")
else:
    sum = 0
    while num>0:
        r = num%10
        if r%2==0:
            sum+=r
        num = num//10
    print(sum)