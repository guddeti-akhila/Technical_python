'''Description:
Write a program to print Fibonacci Series in the Given Range.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Fibonacci Series in the Given Range.

Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "Invalid Inputs".

                     If there are no Fibonacci Series values in the Given Range then, Print "No Fibonacci Series Values".


Example:
Input 1  :    13

                  91

Output 1:    13 21 34 55 89

 

Input 2  :    200

                  10

Output 2:    13 21 34 55 89 144 


Explanation:
Input 1  :    13

                  91

Output 1:    13 21 34 55 89

Explanation :

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 .............

In between 13 and 91, the Fibonacci Series Values are 13 21 34 55 89

 

Input 2  :    200

                  10

Output 2:    13 21 34 55 89 144 

Explanation :

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 .............

In between 10 and 200, the Fibonacci Series Values are 13 21 34 55 89 144

 '''


n = int(input())
n1 = int(input())
if n<0 or n1<0:
    print("Invalid Inputs")
else:
    if n>n1:
        n, n1 = n1, n
    
    a = 0
    b = 1
    co = 0
    while a<=n1:
        if a>=n:
            print(a, end=" ")
            co+=1
        c = a+b
        a = b
        b = c
    if co == 0:
        print("No Fibonacci Series Values")

"""Description:
Write a program to find Factorial of a Given Number?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Factorial of a Given Number.

Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "Invalid InPut".


Example:
Input 1  :    6

Output 1:    720

 

Input 2  :   5

Output 2:   120


Explanation:
Input 1  :    6

Output 1:    720

Explanation :

Factorial = 6 * 5 * 4 * 3 * 2 * 1

             = 720

 

Input 2  :   5

Output 2:   120

Explanation :

Factorial = 5 * 4 * 3 * 2 * 1

             = 120

 """


n = int(input())
if n < 0:
    print("Invalid InPut")
else:
    # fac = 1
    # while n>=1:
    #     fac = fac*n
    #     n = n-1
    # print(fac)
    
    a = 1
    for i in range(1,n+1):
        a*=i
    print(a)



'''Description:
Write a program to print the Average of the Fibonacci Series in Between the Given Range?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Average of Fibonacci Series Between the Given Range.

Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "Invalid Inputs".

                     If there is no Fibonacci Series values between the Given Range then Print, "No Fibonacci Series Values".


Example:
Input 1  :    13

                  91

Output 1:    42.40

 

Input 2  :   200

                  10

Output 2:    59.33


Explanation:
Input 1  :    13

                  91

Output 1:    42.40

Explanation :

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 .............

In between the 13 and 91 the Fibonacci Series Values are 13 21 34 55 89

Sum = 13 + 21 + 34 + 55 + 89

        = 212

Average = sum / count

             = 212 / 5

             = 42.40

 

Input 2  :   200

                  10

Output 2:    59.33

Explanation :

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 .............

In between the 200 and 10 the Fibonacci Series Values are 13 21 34 55 89 144

Sum = 13 + 21 + 34 + 55 + 89 + 144

        = 356

Average = sum / count

             = 356 / 6

             = 59.33


'''

n = int(input())
n1 = int(input())
if n<0 or n1<0:
    print("Invalid Inputs")
else:
    if n>n1:
        n, n1 = n1, n
    
    a = 0
    b = 1
    sum = 0
    co = 0
    while a<=n1:
        if a>=n:
            sum+=a
            co+=1
        c = a+b
        a = b
        b = c
    if co>0:
        print(f"{sum/co:.2f}")
    else:
        print("No Fibonacci Series Values")


'''Description:
Write a program to print First N terms of Alternative Fibonacci Series?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the First N terms of Alternative Fibonacci Series.

Constraints  :- Given Input is Equals to Zero then Print "Invalid Input".

                      If the input number is negative, convert it to positive first, then generate and print the Fibonacci series.


Example:
Input 1  :    10

Output 1:    0, 1, 3, 8, 21, 55, 144, 377, 987, 2584

 

Input 2  :    -16

Output 2:     0, 1, 3, 8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368, 121393, 317811,  832040


Explanation:
Input 1  :    10

Output 1:    0, 1, 3, 8, 21, 55, 144, 377, 987, 2584

Explanation:

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181........

Alternative Fibonacci Series : 0 1 3 8 21 55 144 377 987 2584

 

Input 2  :    -16

Output 2:     0, 1, 3, 8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368, 121393, 317811,  832040

Explanation:

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269...........

Alternative Fibonacci Series : 0 1 3 8 21 55 144 377 987 2584 6765 17711 46368 121393 317811 832040'''


n = int(input())
n = abs(n)
if n==0:
    print("Invalid Input")
else:
    
    a = 0
    b = 1
    co=0
    for i in range(2*n):
        co+=1
        if co%2==1:
            if co>1:
                print(",", end=" ")
            print(a,end="")
        c=a+b
        a = b
        b = c



'''Description:
Write a program to find sum of Factorials upto N Numbers like 0! + 1! + 2! + 3! + 4! + 5! +....upto n!?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Sum of Factorials upto N Numbers.

Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "INvalid INput".


Example:
Input 1  :    6

Output 1:    1+1+2+6+24+120+720=874

 

Input 2  :   5

Output 2:   1+1+2+6+24+120=154


Explanation:
Input 1  :    6

Output 1:    874

Explanation :

Factorial = 0! + 1! + 2! + 3! + 4! + 5! + 6!

             = 1 + 1 + 2 + 6 + 24 + 120 + 720

             = 874

 

Input 2  :   5

Output 2:   120

Explanation :

Factorial = 0! + 1! + 2! + 3! + 4! + 5!

             = 1 + 1 + 2 + 6 + 24 + 120

             = 154'''

n = int(input())
if n < 0:
    print("INvalid INput")
else:
    # a = 1
    c = 0
    # st = 0
    sum = 0
    a = 1
    for i in range(n+1):
        # a = 1
        if i == 0:
            i = 1
        c+=1
        if c>1:
            print("+", end = "")
        # a = i*a
        print(i*a, end="")
        a=i*a
        sum+=a
    print(f"={sum}")
        
        
'''Description:
Write a program to print the Sum of the Fibonacci Series of first N terms.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Sum of the First N terms of Fibonacci Series.

Constraints  :- Given Input is Must be Greater than Zero or else Print "Invalid Input".


Example:
Input 1  :    10

Output 1:    88

 

Input 2  :    -16

Output 2:    Invalid Input


Explanation:
Input 1  :    10

Output 1:    88

Explanation:

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144.........................

sum = 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34

       = 88

 

Input 2  :    -16

Output 2:    Invalid Input

Explanation:

                 Given Input is Not Greater than 0 So Print, "Invalid Input" ( Check the Constraints ).'''


n = int(input())
if n<=0:
    print("Invalid Input")
else:
    
    sum = 0
    a = 0
    b = 1
    for i in range(n):
        sum+=a
        c = a+b
        a = b
        b = c
    print(sum)


'''Description:
Write a program to print First N terms in the Fibonacci Series?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the First N terms of Fibonacci Series.

Constraints  :- Given Input is Equals to Zero then Print "Invalid Input".

                      If the input number is negative, convert it to positive first, then generate and print the Fibonacci series.


Example:
Input 1  :    10

Output 1:    0 1 1 2 3 5 8 13 21 34

 

Input 2  :    -16

Output 2:    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610


Explanation:
Input 1  :    10

Output 1:    0 1 1 2 3 5 8 13 21 34

 

Input 2  :    -16

Output 2:    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

 

Explanation:

Fibonacci Series: The Fibonacci series starts with 0 and 1. Each next number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...'''

n = int(input())
n = abs(n)
if n == 0:
    print("Invalid Input")
else:
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a+b
        a = b
        b = c


'''Description:
Write a program to print the Average of the Alternative Fibonacci Series in the Given Range?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Average of Fibonacci Series in the Given Range.

Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "Invalid Inputs".

                     If there are no Fibonacci Series values in the Given Range then Print, "No Fibonacci Series Values".


Example:
Input 1  :    13

                  91

Output 1:    45.33

 

Input 2  :   200

                  5

Output 2:    35.25


Explanation:
Input 1  :    13

                  91

Output 1:    45.33

Explanation :

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 .............

In between 13 and 91, the Fibonacci Series Values are 13 21 34 55 89

In between the 13 and 91, the Alternative Fibonacci Series Values are 13 34 89

Sum = 13 + 34 + 89

        = 136

Average = sum / count

             = 136 / 3

             = 45.33

 

Input 2  :   200

                  5

Output 2:    35.25

Explanation :

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 .............

In between the 200 and 5, the Fibonacci Series Values are 13 21 34 55 89 144

In between the 200 and 5, the Fibonacci Series Values are 5 13 34 89 

Sum = 5 + 13 + 34 + 89

        = 141

Average = sum / count

             = 141 / 4

             = 35.25'''


n = int(input())
n1 = int(input())
if n<0 or n1<0:
    print("Invalid Inputs")
else:
    if n>n1:
        n, n1 = n1, n
        
    a = 0
    b = 1
    alt = 0
    count = 0
    sum = 0
    while a<=n1:
        if a>=n:
            alt+=1
            if alt%2==1:
                sum+=a
                count+=1
        c = a+b
        a = b
        b = c
    if sum>0:
        print(f"{sum/count:.2f}")
    else:
        print("No Fibonacci Series Values")