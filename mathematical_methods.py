'''Description:
Write a Program to Print first 'n' Numbers by taking input of 1st term(a), common difference(d) and no of terms(n) in the Harmonic progression series?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Difference (d)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print the Harmonic Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'd' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "Invalid Input".


Example:
Input 1 :   1

                1

                6

Output 1 : 1.00, 0.50, 0.33, 0.25, 0.20, 0.17

 

Input 2 :   6

                -1

                6

Output 2 : 0.16, 0.20, 0.25, 0.33, 0.50, 1.00

 

Input 3 :   7

                2

                -5

Output 3 : Invalid Input


Explanation:
Harmonic series is inverse of a arithmetic progression.

In general, the terms in a harmonic progression can be denoted as 1/a, 1/(a + d), 1/(a + 2d), 1/(a + 3d) …. 1/(a + nd).
As Nth term of AP is given as ( a + (n – 1)d).

Hence, Nth term of harmonic progression is reciprocal of Nth term of AP, which is 1/(a + (n – 1)d), where “a” is the 1st term of AP and “d” is a common difference.
'''
a = int(input())
d = int(input())
n = int(input())
if n<=0:
    print("Invalid Input")
else:
    c=0
    for i in range(n):
        c+=1
        if c>1:
            print(",", end=" ")
        print(f"{1/(a+i*d):.2f}",end= "")

'''Description:
Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common difference(d) and No of terms(n) in the Arithmetic progression series? 


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Difference (d)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print Sum of the Arithmetic Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'd' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "Invalid input".


Example:
Input 1  :    2

                  4

                  8

Output 1:    2 + 6 + 10 + 14 + 18 + 22 + 26 + 30 = 128.

 

Input 2  :   -11

                 6

                 11

Output 2:   -11 + -5 + 1 + 7 + 13 + 19 + 25 + 31 + 37 + 43 + 49 = 209.

 

Input 3  :    5

                  9

                  -2

Output 3:    Invalid input.


Explanation:
NA'''

a = int(input())
d = int(input())
n = int(input())
if n<=0:
    print("Invalid input.")
else:
    
    c=0
    sum = 0
    for i in range(n):
        c+=1
        if c>1:
            print(" + ", end="")
        # print(a, end= "")
        # sum+=a
        # a+=d
        sum+=(a+i*d)
        print(a+i*d, end="")
        
    
    print(f" = {sum}.")

'''Description:
Write a Program to Print first 'n' Numbers by taking input of 
 term(a), common difference(d) and no of terms(n) in the Arithmetic progression series?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (
 Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Difference (d)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print the Arithmetic Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'd' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "Invalid Input".


Example:
Input 1  :    2

                  4

                  8

Output 1:    2, 6, 10, 14, 18, 22, 26, 30.

 

Input 2  :   -11

                 6

                 11

Output 2:   -11, -5, 1, 7, 13, 19, 25, 31, 37, 43, 49.

 

Input 3  :    5

                  9

                  -2

Output 3:    Invalid Input.


Explanation:
Arithmetic progression ->  a, a+d, a+2d, a+3d, ................., a+(n-1)d.
'''

a = int(input())
d = int(input())
n = int(input())
if n<=0:
    print("Invalid Input.")
else:
    c=0
    for i in range(n):
        c+=1
        if c>1:
            print(",", end=" ")
        print(a, end="")
        a+=d
    print(".")

'''Description:
Write a program to print the LCM of given three numbers.


Constraints:
Input          :- First Line of Input Consists of One Integer Value (n1).

                     Second Line of Input Consists of One Integer Value (n2).

                     Third Line of Input Consists of One Integer Value (n3).

Output        :- Print the LCM of given three values.

Constraints  :-

                     'n1' Value is Must be Greater than zero or else Print "InvalId First Input".

                     'n2' Value is Must be Greater than zero or else Print "Invalid Second Input".

                     'n3' Value is Must be Greater than zero or else Print "InvaliD ThirD Input".

                     In the Given Three Inputs if any of two or three values are less than or equal to zero then Print "Sorry Invalid Inputs!".


Example:
Input 1  :    2

                  5

                  6

Output 1:    30

 

Input 2  :   12

                 -2

                  4

Output 2:    Invalid Second Input


Explanation:
NA'''

a = int(input())
b = int(input())
e = int(input())
if (a<=0 and b<=0 and e<=0) or (a<=0 and b<=0) or (b<=0 and e<=0) or (e<=0 and a<=0): 
    print("Sorry Invalid Inputs!")
elif b<=0:
    print("Invalid Second Input")
elif e<=0:
    print("InvaliD ThirD Input")
    
elif a<=0 and b>0 and e>0:
    print("InvalId First Input")

elif a<=0 and b<=0 and e<=0:
    print("Sorry Invalid Inputs!")
else:
    c=1
    while True:
        if c%a==0 and c%b==0 and c%e==0:
            print(c)
            break
        c+=1


'''Description:
Find and Print the 
 term value in the Arithmetic progression series by taking input of 1st term(a), common difference(d) and 
 term ?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Difference (d)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print the 
 term value of Arithmetic Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'd' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "InValid Input".


Example:
Input 1  :    2

                  4

                  8

Output 1:    Last term value is : 30.

 

Input 2  :   -11

                 6

                 11

Output 2:  Last term value is : 49.

 

Input 3  :    5

                  9

                  -2

Output 3:    InValid Input.


Explanation:
NA'''

a = int(input())
d = int(input())
n = int(input())
if n<=0:
    print("InValid Input.")
else:
    print(f"Last term value is : {a+(n-1)*d}.")

'''Description:
Write a program to print the LCM of given two numbers


Constraints:
Input          :- First Line of Input Consists of One Integer Value (n1).

                     Second Line of Input Consists of One Integer Value (n2).

Output        :- Print the LCM of given two values.

Constraints  :-

                     Both the values 'n1' & 'n2' must be Greater than zero or else Print "Invalid Inputs.".

                     'n1' Value is Must be Greater than zero or else Print "Invalid First Input".

                     'n2' Value is Must be Greater than zero or else Print "InValid Second Input".

 


Example:
Input 1  :    2

                  4

Output 1:    4

 

Input 2  :   12

                 -2

Output 2:  Invalid Second Input


Explanation:
NA'''

n1 = int(input())
n2 = int(input())
if n1<=0 and n2<=0:
    print("Invalid Inputs.")
elif n1<=0 and n2>0:
    print("Invalid First Input")
elif n1>0 and n2<=0:
    print("InValid Second Input")
else:
    c=1
    while True:
        if c%n1==0 and c%n2==0:
            print(c)
            break
        c+=1

'''Description:
Write a Program to Print first 'n' Numbers by taking input of 1st term(a), common Ratio(r) and No of terms(n) in the geometric progression series ?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Ratio (r)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print the Geometric Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'r' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "Invalid Input".


Example:
Input 1  :    2

                  4

                  8

Output 1:    2, 8, 32, 128, 512, 2048, 8192, 32768.

 

Input 2  :   -11

                 -2

                 11

Output 2:   -11, 22, -44, 88, -176, 352, -704, 1408, -2816, 5632, -11264.

 

Input 3  :    5

                  9

                  -2

Output 3:    Invalid Input.


Explanation:
NA'''

a = int(input())
r = int(input())
n = int(input())
if n<=0:
    print("Invalid Input.")
else:
    
    c=0
    for i in range(n):
        c+=1
        if c>1:
            print(",", end=" ")
        print(a,end="")
        a*=r
    print(".")

'''Description:
Write a program to print the GCD of given two numbers?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (n1).

                     Second Line of Input Consists of One Integer Value (n2).

Output        :- Print the GCD of given two values.

Constraints  :-

                     Both the values 'n1' & 'n2' must be Greater than zero or else Print "Invalid Inputs".

                     'n1' Value is Must be Greater than zero or else Print "Invalid First Input".

                     'n2' Value is Must be Greater than zero or else Print "Invalid Second Input.".

 


Example:
Input 1  :    12

                  3

Output 1:    3

 

Input 2  :   12

                 16

Output 2:    4


Explanation:
NA
'''

n = int(input())
n1 = int(input())
if n<=0 and n1<=0:
    print("Invalid Inputs")
elif n<=0:
    print("Invalid First Input")
elif n1<=0:
    print("Invalid Second Input.")
else:
    min = n if n<n1 else n1
    for i in range(min,0,-1):
        if n%i==0 and n1%i==0:
            print(i)
            break

'''Description:
Write a program to print the GCD of given three numbers?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (n1).

                     Second Line of Input Consists of One Integer Value (n2).

                     Third Line of Input Consists of One Integer Value (n3).

Output        :- Print the GCD of given three values.

Constraints  :-

                     'n1' Value is Must be Greater than zero or else Print "Invalid First Input".

                     'n2' Value is Must be Greater than zero or else Print "Invalid Second Input".

                     'n3' Value is Must be Greater than zero or else Print "Invalid Third Input".

                     In the Given Three Inputs if any of two or three values are less than or Equal to zero then Print "Invalid Inputs".

 


Example:
Input 1  :    24

                  34

                  44

Output 1:    2

 

Input 2  :   12

                 16

                 48

Output 2:   4


Explanation:
NA'''

n = int(input())
n1 = int(input())
n2 = int(input())
if (n<=0 and n1<=0) or (n1<=0 and n2<=0) or (n<=0 and n2<=0) or (n<=0 and n1<=0 and n2<=0):
    print("Invalid Inputs")
elif n<=0:
    print("Invalid First Input")
elif n1<=0:
    print("Invalid Second Input")
elif n2<=0:
    print("Invalid Third Input")
else:
    min = n if n<n1 and n<n2 else n1 if n1<n and n1<n2 else n2
    for i in range(min,0,-1):
        if n%i == 0 and n1%i==0 and n2%i==0:
            print(i)
            break

'''Description:
Find the nth term value in the Harmonic progression series by taking input of 1st term(a), common difference(d) and nth term ?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Difference (d)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print the nth term value of Harmonic Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'd' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "InvaliD InPut".


Example:
Input 1 :   1

                1

                6

Output 1 : 0.17

 

Input 2 :   6

                -1

                6

Output 2 : 1.00

 

Input 3 :   7

                2

                -5

Output 3 : InvaliD InPut
Explanation:
NA
'''

a = int(input())
d = int(input())
n = int(input())
if n<=0:
    print("InvaliD InPut")
else:
    print(f'{1/(a+(n-1)*d):.2f}')


'''Description:
Find the nth term value in the geometric progression series by taking input of 1st term(a), common Ratio(r) and nth term ?


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Ratio (r)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print the nth term value of Geomentric Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'r' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "InValid Input".


Example:
Input 1  :    2

                  4

                  8

Output 1:    Last term value is : 32768.

 

Input 2  :   -11

                 6

                 7

Output 2:  Last term value is : -513216.

 

Input 3  :    5

                  9

                  -2

Output 3:    InValid Input.


Explanation:
NA'''

a = int(input())
r = int(input())
n = int(input())
if n<=0:
    print("InValid Input.")
else:
    print(f"Last term value is : {a*r**(n-1)}.")


'''Description:
Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common difference(d) and No of terms(n) in the Harmonic progression series? 


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Difference (d)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print the sum of the Harmonic Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'd' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "Invalid Input.".


Example:
Input 1 :   1

                1

                6

Output 1 : 2.45

Input 2 :   6

                -1

                5

Output 2 : 1.45

Input 3 :   7

                2

                -5

Output 3 : Invalid Input


Explanation:
First add the values and print the sum value in ".2f" format


'''

a = int(input())
d = int(input())
n = int(input())
if n<=0:
    print("Invalid Input.")
else:
    sum = 0
    for i in range(n):
        sum+=1/(a+i*d)
    print(f'{sum:.2f}')


'''Description:
Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common ratio(r) and No of terms(n) in the Geometric progression series? 


Constraints:
Input          :- First Line of Input Consists of One Integer Value (1st Term (a)).

                     Second Line of Input Consists of One Integer Value (Common Ratio (r)).

                     Third Line of Input Consists of One Integer Value (No of Terms (n)).

Output        :- Print Sum of the Geometric Progression Values.

Constraints  :-

                     'a' Value is an any Integer Value.

                     'r' Value is an any Integer Value.

                     'n' Value is Must be Greater than zero or else Print "Invalid Input".


Example:
Input 1  :    2

                  4

                  8

Output 1:    43690

 

Input 2  :   -11

                 -2

                 11

Output 2:   -7513

 

Input 3  :    5

                  9

                  -2

Output 3:    Invalid Input


Explanation:
NA


'''

a = int(input())
r = int(input())
n = int(input())
if n<=0:
    print("Invalid Input")
else:
    print(int(a*(1-r**n)/(1-r)))