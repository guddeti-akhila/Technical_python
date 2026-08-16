'''Description:
Write a Program to Check if The given year is Leap Year or not?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the "Leap Year." or "Not a Leap Year.".

Constraints  :- Given Input Must be Greater than Zero or else Print "Given Year is Invalid Input.".


Example:
Input 1  :    1983

Output 1:    Not a Leap Year.

 

Input 2  :    -6

Output 2:     Given Year is Invalid Input.

 

Input 3  :    2016

Output 3:    Leap Year.


Explanation:
Input 1  :    1983

Output 1:    Not a Leap Year.

Explanation:

1983 is not a 4 multiple, So it is Not a Leap Year.

 

Input 2  :    -6

Output 2:     Given Year is Invalid Input.

Explanation:

-6 is a Negative Value, So it is Given Year is Invalid Input. .

 

Input 3  :    2016

Output 3:    Leap Year.

Explanation:

2016 is a 4 multiple, So it is a Leap Year.'''

n = int(input())
if n > 0:
    if (n%400==0) or (n%4==0 and n%100!=0):
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
else:
    print("Given Year is Invalid Input.")


'''Description:
Write a program to swap the two given numbers. ( without using a third variable)


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Given 2 Numbers after Swapping.


Example:
Input 1  :    210

                  208

Output 1:    208

                  210

 

Input 2  :    66

                  144

Output 2:     144

                   66

 

Input 3  :    58

                  1001

Output 3:    1001

                  58


Explanation:
Print the Given Two Values After swapping.'''

n = int(input())
n1 = int(input())
t = n
n = n1
n1 = t
print(n)
print(n1)

'''Description:
Write a program to Count the Number of digits in a Given Number?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Count of Digits in a Given Number.

Constraints  :- Given Input Must be Greater than Ten or else Print "Invalid Input".

 


Example:
Input 1  :    25

Output 1:    2

 

Input 2  :   -6

Output 2:    Invalid Input


Explanation:
Input 1  :    25

Output 1:    2

Explanation : 

Given Number 25 Consists of 2 Digits So Print 2.

 

Input 2  :   -6

Output 2:    Invalid Input

Explanation : 

Given Input is less than 10 so, Print "Invalid Input". '''

n = int(input())
if n > 10:
    c = 1
    while n>10:
        r = n%10
        c+=1
        n//=10
    print(c)
else:
    print("Invalid Input")


'''Description:
Write a program to print the Sum of the Armstrong Numbers in the Given Range?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Sum of All Armstrong Numbers.

Constraints  :- Either of the Given Input is Equal to Zero then Print "Invalid Inputs".

                      If there are No Armstrong Numbers Between the Given Range then, print "No Armstrong Numbers in a Given Range.".

                      If Either of the Given Inputs is Negative then Convert into Positive and then Print the Sum of all Armstrong Numbers.


Example:
Input 1  :    1 

                  200

Output 1:    Armstrong Numbers in the Given Range is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 153 = 198.

 

Input 2  :   500

                 150

Output 2:  Armstrong Numbers in the Given Range is 153 + 370 + 371 + 407 = 1301.

 

Input 3  :    8208

                  93084

Output 3:    Armstrong Numbers in the Given Range is 8208 + 9474 + 54748 + 92727 + 93084 = 258241.


Explanation:
Input 1  :    1 

                  200

Output 1:    Armstrong Numbers in the Given Range is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 153 = 198.

Explanation:

Armstrong Numbers in the Range of 1 to 200 is 1, 2, 3, 4, 5, 6, 7, 8, 9, 153.

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 153 = 198.

 

Input 2  :   500

                 150

Output 2:  Armstrong Numbers in the Given Range is 153 + 370 + 371 + 407 = 1301.

Explanation:

Armstrong Numbers in the Range of 150 to 500 is 153, 370, 371, 407.

153 + 370 + 371 + 407 = 1301.

 

Input 3  :    8208

                  93084

Output 3:    Armstrong Numbers in the Given Range is 8208 + 9474 + 54748 + 92727 + 93084 = 258241.

Explanation:

Armstrong Numbers in the Range of 8208 to 93084 is 8208, 9474, 54748, 92727, 93084.

8208 + 9474 + 54748 + 92727 + 93084 = 258241.


'''

n = int(input())
n1 = int(input())
if n==0 or n1==0:
    print("Invalid Inputs")
# if n<0 or n1<0:
#     n = abs(n)
#     n1 = abs(n1)
else:
    if n<0 or n1<0:
        n = abs(n)
        n1 = abs(n1)
    
    if n>n1:
        n, n1 = n1,n
        
    def arm(n):
        t = n
        c = 0
        while n > 0:
            r = n%10
            c+=1
            n//=10
            
        v = t
        total = 0
        while t>0:
            r = t%10
            total+=r**c
            t//=10
        return total == v
    total = 0
    c=0
    for i in range(n, n1+1):
        if arm(i):
            total+=i
            c+=1
            if c == 1:
                print("Armstrong Numbers in the Given Range is", end=" ")
            if c>1:
                print(" + ", end="")
            print(i, end="")
    if c>0:
        print(f" = {total}.")
    else:
        print("No Armstrong Numbers in a Given Range.")


'''Description:
Write a program to print the Armstrong Numbers between the Given two values.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the All Armstrong Numbers.

Constraints  :- Either of the Given Inputs is Equal to Zero then Print "Invalid Inputs".

                      If there are No Armstrong Numbers Between the Given Values then print "No Armstrong Numbers Between Given Values".

                      If Either of the Given Inputs is Negative then Convert into Positive and then Print the Armstrong Numbers.


Example:
Input 1  :    1 

                  200

Output 1:    Armstrong Numbers between the Given Values is 2, 3, 4, 5, 6, 7, 8, 9, 153.

 

Input 2  :   500

                 150

Output 2:  Armstrong Numbers between the Given Values is 153, 370, 371, 407.

 

Input 3  :    8208

                  93084

Output 3:    Armstrong Numbers between the Given Values is 9474, 54748, 92727.

 


Explanation:
Input 1  :    1 

                  200

Output 1:    Armstrong Numbers between the Given Values is 2, 3, 4, 5, 6, 7, 8, 9, 153.

Explanation:

Armstrong Numbers between the 1 to 200 is 2, 3, 4, 5, 6, 7, 8, 9, 153.

 

Input 2  :   500

                 150

Output 2:  Armstrong Numbers between the Given Values is 153, 370, 371, 407.

Explanation:

Armstrong Numbers between the 150 to 500 is 153, 370, 371, 407.

 

Input 3  :    8208

                  93084

Output 3:    Armstrong Numbers between the Given Values is 9474, 54748, 92727.

Explanation:

Armstrong Numbers between the 8208 to 93084 is 9474, 54748, 92727.'''

n = int(input())
n1 = int(input())
if n ==0 or n1 == 0:
    print("Invalid Inputs")
else:
    if n<0 or n1<0:
        n = abs(n)
        n1 = abs(n1)
    if n>n1:
        n, n1 = n1, n
        
    def arm(n):
        t = n
        c = 0
        while n>0:
            r = n%10
            c+=1
            n//=10
        
        v = t
        total = 0
        while t>0:
            r = t%10
            total = total + r**c
            t//=10
        return v == total
    
    c=0
    for i in range(n+1 , n1):
        if arm(i):
            c+=1
            if c== 1:
                print("Armstrong Numbers between the Given Values is ", end="")
            if c>1:
                print(",",end=" ")
            print(i, end="")
    if c==0:
        print("No Armstrong Numbers Between Given Values")
    else:
        print(".")

'''Description:
Write a program to Calculate Power of a Number. (With Pre Defined Method)


Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Base Value ).

                     Second Line of Input Consists of One Integer Value ( Exponent Value ).

Output        :- Print the Power Value.

Constraints  :- Given Inputs is Must be Greater than Zero or else Print "Invalid Inputs".

 


Example:
Input 1  :    2

                  5

Output 1:    2 Power 5 value is 32.

 

Input 2  :   6

                 3

Output 2:    6 Power 3 value is 216.


Explanation:
Input 1  :    2

                  5

Output 1:    2 Power 5 value is 32.

Explanation : 

25 = 2 * 2 * 2 * 2 * 2 = 32

Input 2  :   6

                 3

Output 2:    6 Power 3 value is 216.

Explanation : 

63= 6 * 6 * 6 = 216'''

n = int(input())
n1 = int(input())
# v = n**n1
if n<=0 or n1<=0:
    print("Invalid Inputs")
else: 
# if n>0 and n1>0:
#     if n>n1 or n<n1:
    v = n**n1
    print(f"{n} Power {n1} value is {v}.")
# else:
#     print("Invalid Inputs")

'''Description:
Write a program to print the Alternative Armstrong Numbers between the Given Values?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the All Alternative Armstrong Numbers.

Constraints  :- Either of the Given Inputs is Equal to Zero then Print "Invalid Inputs".

                      If there is No Armstrong Numbers Between the Given Values then print "No Armstrong Numbers Between Given Values.".

                      If Either of the Given Inputs is Negative then Convert into Positive and then Print the Alternative Armstrong Numbers.


Example:
Input 1  :    1 

                  200

Output 1:    Alternative Armstrong Numbers between the Given Values is 2, 4, 6, 8, 153.

 

Input 2  :   500

                 150

Output 2:  Alternative Armstrong Numbers between the Given Values is 153, 371.

 

Input 3  :    8208

                  93084

Output 3:    Alternative Armstrong Numbers between the Given Values is 9474, 92727.

 


Explanation:
Input 1  :    1 

                  200

Output 1:    Alternative Armstrong Numbers between the Given Values is 2, 4, 6, 8, 153.

Explanation:

Armstrong Numbers between the 1 to 200 is 2, 3, 4, 5, 6, 7, 8, 9, 153.

Alternative Armstrong Numbers between the Given Values is 2, 4, 6, 8, 153.

 

Input 2  :   500

                 150

Output 2:  Alternative Armstrong Numbers between the Given Values is 153, 371.

Explanation:

Armstrong Numbers between the 150 to 500 is 153, 370, 371, 407.

Alternative Armstrong Numbers between the Given Values is 153, 371.

 

Input 3  :    8208

                  93084

Output 3:    Alternative Armstrong Numbers between the Given Values is 9474, 92727.

Explanation:

Armstrong Numbers between the 8208 to 93084 is 9474, 54748, 92727.

Alternative Armstrong Numbers between the Given Values is 9474, 92727.'''

n = int(input())
n1 = int(input())
if n == 0 or n1 == 0:
    print("Invalid Inputs")
else:
    # if n>n1:
    #     n, n1 = n1, n
    if n<0 or n1<0:
        n = abs(n)
        n1 = abs(n1)
    
    if n>n1:
        n,n1 = n1, n
    
    def alt_arm(n):
        t = n
        c = 0
        while n>0:
            r = n%10
            c+=1
            n//=10
        
        v = t
        total = 0
        while t>0:
            r = t%10
            total = total+r**c
            t//=10
        return v==total
        
    c = 0
    for i in range(n+1, n1):
        if alt_arm(i):
            c+=1
            if c== 1:
                print("Alternative Armstrong Numbers between the Given Values is ", end="")
            if c%2==1:
                if c>1:
                    print(",",end=" ")
                print(i,end="")
    if c==0:
        print("No Armstrong Numbers Between Given Values.")
    else:
        print(".")


'''Description:
Write a program to check if the Given Number is Armstrong or not?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Armstrong Number or Not a Armstrong Number.

Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input".

 


Example:
Input 1  :    253

Output 1:    Not a Armstrong Number

 

Input 2  :   153

Output 2:   Armstrong Number


Explanation:
Input 1  :    253

Output 1:    Not a Armstrong Number

Explanation:

253

23  + 53 + 33

=8 + 125 + 27

=160

Here,The given number(253) does not equal the sum of the cubes of its digits (160). Therefore, it is not an Armstrong number.

 

Input 2  :   153

Output 2:   Armstrong Number

Explanation:

153

13 + 53 + 33

=1 + 125 + 27

=153

Here, Given Number(153) and Sum of the Cubes of the Digits in Given Number(153) are same So It is a Armstrong Number.


'''

n = int(input())
if n<=0:
    print("Invalid Input")
else:
    t = n
    c = 0
    while n>0:
        r = n%10
        c+=1
        n//=10
    
    v = t
    total = 0
    while t>0:
        r = t%10
        total = total+r**c
        t//=10
    if v == total:
        print("Armstrong Number")
    else:
        print("Not a Armstrong Number")

'''Description:
Write a program to check Whether the Given Number(any number of digits) is Armstrong or Not.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print if the number is an Armstrong Number or Not a Armstrong Number.

Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input".

 


Example:
Input 1  :    253

Output 1:    253 is Not a Armstrong Number.

 

Input 2  :   153

Output 2:   153 is a Armstrong Number.

 

Input 3  :    8208

Output 3:    8208 is a Armstrong Number.

 

Input 4  :   548834

Output 4:   548834 is a Armstrong Number.


Explanation:
Input 1  :    253

Output 1:    253 is Not a Armstrong Number.

Explanation:

253

23  + 53 + 33

=8 + 125 + 27

=160

Here Given Number(253) and Sum of the Cubes of the Digits in Given Number(160) are not same. So It is Not a Armstrong Number.

 

Input 2  :   153

Output 2:   153 is a Armstrong Number.

Explanation:

153

13 + 53 + 33

=1 + 125 + 27

=153

Here Given Number(153) and Sum of the Cubes of the Digits in Given Number(153) are same. So It is a Armstrong Number.

 

Input 3  :    8208

Output 3:    8208 is a Armstrong Number.

Explanation:

8208

 

84 + 24 + 04 + 84

=4096 + 16 + 0 + 4096

=8208

Here Given Number(8208) and Sum of the Powers(No of Digits in Given Number) of the Digits in Given Number(8208) are same. So It is a Armstrong Number.

 

Input 4  :   548834

Output 4:   548834 is a Armstrong Number.

Explanation:

548834

 

56 + 46 + 86 + 86 + 36 + 46

=15625 + 4096 + 262144 + 262144 + 729 + 4096

=548834

Here Given Number(548834) and Sum of the Powers(No of Digits in Given Number) of the Digits in Given Number(548834) are same. So It is a Armstrong Number.


'''

n = int(input())
if n<=0:
    print("Invalid Input")
else:
    t = n
    c = 0
    while n>0:
        r = n%10
        c+=1
        n//=10
    
    v = t
    total = 0
    while t>0:
        r = t%10
        total+=r**c
        t//=10
    # if c ==0:
    #     print("")
    if total == v:
        print(f"{total} is a Armstrong Number.")
    else:
        print(f"{v} is Not a Armstrong Number.")


'''Description:
Write a program to print the Armstrong Numbers in the Given Range.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the All Armstrong Numbers.

Constraints  :- Given Inputs is Must be Greater than Zero or else Print "Invalid Inputs".

                      If there are No Armstrong Numbers Between the Given Range then print, "No Armstrong Numbers".

                     If starting range is greater than ending range, swap both the values and print the armstrong numbers.

 


Example:
Input 1  :    1 

                  200

Output 1:    Armstrong Numbers in the Given Range is 1, 2, 3, 4, 5, 6, 7, 8, 9, 153.

 

Input 2  :   500

                 150

Output 2:  Armstrong Numbers in the Given Range is 153, 370, 371, 407.

 

Input 3  :    8208

                  93084

Output 3:    Armstrong Numbers in the Given Range is 8208, 9474, 54748, 92727, 93084.

 


Explanation:
Input 1  :    1 

                  200

Output 1:    Armstrong Numbers in the Given Range is 1, 2, 3, 4, 5, 6, 7, 8, 9, 153.

Explanation:

Armstrong Numbers in the Range of 1 to 200 is 1, 2, 3, 4, 5, 6, 7, 8, 9, 153.

 

Input 2  :   500

                 150

Output 2:  Armstrong Numbers in the Given Range is 153, 370, 371, 407.

Explanation:

Armstrong Numbers in the Range of 150 to 500 is 153, 370, 371, 407.

 

Input 3  :    8208

                  93084

Output 3:    Armstrong Numbers in the Given Range is 8208, 9474, 54748, 92727, 93084.

Explanation:

Armstrong Numbers in the Range of 8208 to 93084 is 8208, 9474, 54748, 92727, 93084.'''

n = int(input())
n1 = int(input())
if n>n1:
    n,n1 = n1,n
if n<=0 or n1<=0:
    print("Invalid Inputs")
else:
    def arm(n):
        t = n
        c = 0
        while n>0:
            r = n%10
            c+=1
            n//=10
        
        v = t
        total = 0
        while t>0:
            r = t%10
            total = total+r**c
            t//=10
        return v == total

    c = 0
    for i in range(n, n1+1):
        if arm(i):
            c+=1
            if c== 1:
                print("Armstrong Numbers in the Given Range is ", end="")
            if c>1:
                print(",",end=" ")
            print(i, end="")
    if c==0:
        print("No Armstrong Numbers")
    else:
        print(".")