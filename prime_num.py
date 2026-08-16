'''Description:
Write a program to find Sum of all the prime numbers between the Given values.

 


Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .

                     Second Line of Input Consists of One Integer Value ( Maximum Value ) .

Output        :- Print Sum of Prime Numbers Between the Given Values.

Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".


Example:
Input 1  :    25

                  100

Output 1:    960

 

Input 2  :    -6  

                  -200

Output 2:     Invalid Inputs

 

Input 3  :    19

                  61

Output 3:    363


Explanation:
Input 1  :    25

                  100

Output 1:    960

Explanation:

Prime Numbers between 25 and 100 are :   29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

Their sum is = 29 + 31 + 37 + 41 + 43 + 47 + 53 + 59 + 61 + 67 + 71 + 73 + 79 + 83 + 89 + 97

       = 960

 

Input 2  :    -6  

                  -200

Output 2:     Invalid Inputs

Explanation:

Given Numbers are not Positive.

 

Input 3  :    19

                  61

Output 3:    363

Explanation:

Prime Numbers between 19 and 61 are:  23, 29, 31, 37, 41, 43, 47, 53, 59

Their sum is = 23 + 29 + 31 + 37 + 41 + 43 + 47 + 53 + 59 

       =  363'''

num1 = int(input())
num2 = int(input())
if num1<num2 and num1>0:
    def prime(n):
        c=0
        for i in range(1, n+1):
            if n%i==0:
                c+=1
        if c<=2:
            return True
    sum=0
    for i in range(num1+1, num2):
        if prime(i):
            sum+=i
    print(sum)
else:
    print("Invalid Inputs")


'''Description:
Write a program to swap the two given numbers.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Two Numbers after Swapping.


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
Print the Given Numbers After Swapping Numbers'''

num1 = int(input())
num2 = int(input())
t = num1
num1 = num2
num2 = t
print(num1)
print(num2)

'''Description:
Write a program to find the Sum of all Alternative Prime Numbers between The Given Values.


Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .

                     Second Line of Input Consists of One Integer Value ( Maximum Value ) .

Output        :- Print Sum of All Alternate Prime Numbers Between the Given Values.

Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".

                      If there are no Primes Numbers are identified in Between the Given Values then, Print "No Prime Numbers".


Example:
Input 1  :    25

                  100

Output 1:    462

 

Input 2  :    -6  

                  -200

Output 2:     Invalid Inputs

 

Input 3  :    19

                  61

Output 3:    201

 

Input 4  :    90

                  97

Output 4:    No Prime Numbers


Explanation:
Input 1  :    25

                  100

Output 1:    462 

Explanation :

Prime Numbers between 25 and 100 : 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

Alternative Prime Numbers : 29, 37, 43, 53, 61, 71, 79, 89

Sum of Alternative Prime Numbers : 29 + 37 + 43 + 53 + 61 + 71 + 79 + 89

                                                  = 462

 

Input 2  :    -6  

                  -200

Output 2:     Invalid Inputs

Explanation :

Given Numbers are not a Positive Numbers

 

Input 3  :    19

                  61

Output 3:    

Explanation :

Prime Numbers between 19 and 61  : 23, 29, 31, 37, 41, 43, 47, 53, 59

Alternative Prime Numbers : 23, 31, 41, 47, 59

Sum of Alternative Prime Numbers : 23 + 31 + 41 + 47 + 59

                                                  = 201

 

Input 4  :    90

                  97

Output 4:    No Prime Numbers

Explanation :

Prime Numbers : No Prime Numbers between the Given Numbers

Alternative Prime Numbers : No Alternative Prime Numbers between the Given Numbers So Print, "No Prime Numbers".'''

num1 = int(input())
num2 = int(input())
if num1>0 and num1<num2:
    def prime(num):
        c = 0
        for i in range(1, num+1):
            if num%i==0:
                c+=1
        if c<=2:
            return True
    c = 0
    sum=0
    for i in range(num1+1, num2):
        if prime(i):
  
            c+=1
            if c%2==1:
                sum+=i
    if c == 0:
        print("No Prime Numbers")
    else:    
        print(sum)
else:
    print("Invalid Inputs")

'''Description:
Write a program to print all factors of the Given Number.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print All the Factors of the Given Number.

Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".


Example:
Input 1  :    18

Output 1:    1 2 3 6 9 18

 

Input 2  :    -6

Output 2:     Invalid Input


Explanation:
18     -->   1 2 3 6 9 18   If you divide 18 with these numbers(1 2 3 6 9 18) then, you get 0 as remainder.

-6      -->   Invalid Input  ( Given Number is Not Greater than Zero )


'''

num1 = int(input())
if num1>0:
    for i in range(1, num1+1):
        if num1%i==0:
            print(i,end=" ")
else:
    print("Invalid Input")

'''Description:
Write a program to print all Prime Factors of a Given Number?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print All the Prime Factors of a Given Number.

Constraints  :- Given Input is Equals to Zero then Print "Invalid Input".

                      If no Primes Factors are identified of a Given Number then, Print "No Prime Factors".

                      If the Given Input is Negative, then convert that number into Positive and Find Prime Factors.


Example:
Input 1  :    18

Output 1:    2 3

 

Input 2  :    -10

Output 2:     2 5


Explanation:
Input 1  :    18

Output 1:    2 3

Explanation:

Factors :   1 2 3 6 9 18

Prime Factors : 2 3

 

Input 2  :    -10

Output 2:     2 5

Explanation:

Given Number is Negative so, Convert that Number to Positive and then Find its Factors

Factors  : 1 2 5 10

Prime Factors : 2 5'''
n = int(input())
if n==0:
    print("Invalid Input")
elif n<0:
    n = -(n)
# if n>0:
#     c=0
#     for i in range(1, n+1):
#         if n%i==0:
#             c=0
#             for j in range(1, i+1):
#                 if i%j==0:
#                     c+=1
#             if c==0:
#                 print("No Prime Factors")
#             else:
#                 if c==2:
#                     print(j, end=" ")
   
def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    return False
if n>0:
    c=0
    for i in range(1,n+1):
        if n%i==0:
            if isprime(i):
                c+=1
                print(i,end=" ")
    if c==0:
        print("No Prime Factors")



'''Description:
Write a program to find Average of all Alternative Prime Numbers between The Given Values.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print Average of all Alternative Prime Numbers Between the Given Values.

Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".

                         If starting range is greater than ending range swap the both values and findout the average

                      If no Primes Numbers are identified in Between the Given Values then, Print "No Prime Numbers".


Example:
Input 1  :    25

                  100

Output 1:    57.750

 

Input 2  :    -23  

                  -133

Output 2:     Invalid Inputs

 

Input 3  :    61

                  19

Output 3:    40.200

 

Input 4  :    90

                  97

Output 4:    No Prime Numbers


Explanation:
Input 1  :    25

                  100

Output 1:    57.750

Explanation :

Prime Numbers between 25 and 100 are : 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

Alternative Prime Numbers : 29, 37, 43, 53, 61, 71, 79, 89

Sum of Alternative Prime Numbers : 29 + 37 + 43 + 53 + 61 + 71 + 79 + 89

                                                  = 462

Average of Alternative Prime Numbers : 462 /8

                                                        =57.750

 

Input 2  :    -23  

                  -133

Output 2:     Invalid Inputs

Explanation :

Given Numbers are not Positive.

 

Input 3  :    61

                  19

Output 3:    40.200

Explanation :

Prime Numbers between 19 and 61 : 23, 29, 31, 37, 41, 43, 47, 53, 59

Alternative Prime Numbers : 23, 31, 41, 47, 59

Sum of Alternative Prime Numbers : 23 + 31 + 41 + 47 + 59

                                                  = 201

Average of Alternative Prime Numbers : 201 / 5

                                                        =40.200

 

Input 4  :    90

                  97

Output 4:    No Prime Numbers

Explanation :

Prime Numbers : No Prime Numbers between the Given Numbers

Alternative Prime Numbers : No Alternative Prime Numbers between the Given Numbers So Print, "No Prime Numbers".'''

num1 = int(input())
num2 = int(input())
if num1>num2:
    num1, num2= num2, num1
if num1>0 and num1<num2:
    def prime_factor(n):
        c= 0
        for i in range(1, n+1):
            if n%i ==0:
                c+=1
        if c==2:
            return True
    c=0
    total = 0
    alt = 0
    for i in range(num1+1, num2):
       if prime_factor(i):
           alt+=1
           if alt%2==1:
               c+=i
               total+=1
    if c==0:
        print("No Prime Numbers")
    else:
        print(f"{c/total:.3f}")
else:
    print("Invalid Inputs")


'''Description:
Write a program to find Average of all the Prime Numbers between the Given Values. (Print the value upto 3 digits after Decimal Point)


Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .

                     Second Line of Input Consists of One Integer Value ( Maximum Value ) .

Output        :- Print All the Prime Number Between the Given Values.

Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".


Example:
Input 1  :    25

                  100

Output 1:    60.000

 

Input 2  :    -10  

                  -90

Output 2:     Invalid Inputs

 

Input 3  :    19

                  61

Output 3:    40.333


Explanation:
Input 1  :    25

                  100

Output 1:    60.000

Explanation:

Prime Numbers between 25 and 100 are :   29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

Their sum = 29 + 31 + 37 + 41 + 43 + 47 + 53 + 59 + 61 + 67 + 71 + 73 + 79 + 83 + 89 + 97

       = 960

Average = Sum of all the Primes / Number of Primes

              = 960 / 16

             = 60.000

 

Input 2  :    -10  

                  -90

Output 2:     Invalid Inputs

Explanation:

Given Numbers are not Positive.

 

Input 3  :    19

                  61

Output 3:    40.333

Explanation:

Prime Numbers between 19 and 61:  23, 29, 31, 37, 41, 43, 47, 53, 59

Their sum = 23 + 29 + 31 + 37 + 41 + 43 + 47 + 53 + 59 

       =  363 

Average = Sum of all the Primes / Number of Primes

             = 363 / 9

             = 40.333333333

             = 40.333'''

num1 = int(input())
num2 = int(input())
if num1>0 and num2>0:
    def avg_prime(num):
        c=0
        for i in range(1, num+1):
            if num%i==0:
                c+=1
        if c==2:
            return True

    c=0
    total=0
    for i in range(num1+1, num2):
    
        if avg_prime(i):
            c+=i
            total+=1
    if total ==0:
        print("Invalid Inputs")
    else:
        print(f"{(c/total):.3f}")
else:
    print("Invalid Inputs")

'''Description:
Write a program to print Alternative Prime Numbers in the Given Range.


Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .

                     Second Line of Input Consists of One Integer Value ( Maximum Value ) .

Output        :- Print Alternate Prime Numbers in the Given Range.

Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".


Example:
Input 1  :    25

                  100

Output 1:    29, 37, 43, 53, 61, 71, 79, 89 

 

Input 2  :    -6  

                  -200

Output 2:     Invalid Inputs

 

Input 3  :    19

                  61

Output 3:    19, 29, 37, 43, 53, 61


Explanation:
Input 1  :    25

                  100

Output 1:    29, 37, 43, 53, 61, 71, 79, 89 

Explanation :

Prime Numbers in between 25 and 100 are : 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

Alternative Prime Numbers : 29, 37, 43, 53, 61, 71, 79, 89

 

Input 2  :    -6  

                  -200

Output 2:     Invalid Inputs

Explanation :

Given Numbers are not Positive.

 

Input 3  :    19

                  61

Output 3:    19, 29, 37, 43, 53, 61

Explanation :

Prime Numbers in between 19 and 61 are : 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61

Alternative Prime Numbers : 19, 29, 37, 43, 53, 61


'''

num1 = int(input())
num2 = int(input())
if num1>0 and num1<num2:
    def prime(num):
        c = 0
        for i in range(1,num+1):
            if num%i ==0:
                c+=1
        if c <= 2:
            return True
        else:
            return False
    
    fc = 0
    c = 0
    for i in range(num1, num2+1):
      
        if prime(i):
            fc+=1
            if fc%2==1:
                c+=1
                if c>1:
                    print(",",end=" ")
                print(i, end="")
else:
    print("Invalid Inputs")

'''Description:
Write a program to check if the given number is a prime number or not.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :-  If the given number is a Prime Number, print "Prime Number", and if the given number is not a Prime Number then, print "Not a Prime Number" .

Constraints  :- Given Input Must be Greater than Zero or else Print "Invalid Input".


Example:
Input 1  :    83

Output 1:    Prime Number

 

Input 2  :    -6

Output 2:     Invalid Input

 

Input 3  :    182

Output 3:    Not a Prime Number


Explanation:
If the Given Input is greater than Zero, then check if the Given Number is a Prime Number or not.'''

num1 = int(input())
if num1>0:
    c = 0
    for i in range(1, num1+1):
        if num1%i == 0:
            c+=1
    if c<=2:
        print("Prime Number")
    else:
        print("Not a Prime Number")
        
else:
    print("Invalid Input")

'''Description:
Write a program to print All the Prime Numbers in the Given Range.


Constraints:
Input          :- First Line of Input Consists of One Integer Value ( Minimum Value ) .

                     Second Line of Input Consists of One Integer Value ( Maximum Value ) .

Output        :- Print All the Prime Numbers in the Given Range.

Constraints  :- Given Inputs Must be Greater than Zero or else Print "Invalid Inputs".


Example:
Input 1  :    25

                  100

Output 1:    29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

 

Input 2  :    -6  

                  -200

Output 2:     Invalid Inputs

 

Input 3  :    19

                  61

Output 3:    19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61


Explanation:
If the Given Inputs are greater than Zero, then Print All the Prime Numbers in the Given Range.'''

num1 = int(input())
num2 = int(input())

if num1>0 and num2>0:
    def prime(num):
        fc = 0
        for i in range(1, num+1):
            if num%i==0: 
                fc+=1
        if fc==2:
            return True
    c=0      
    for i in range(num1, num2+1):
       if prime(i):
           c+=1
           if c>1:
               print(",",end=" ")
           print(i, end="")       
else:
    print("Invalid Inputs")