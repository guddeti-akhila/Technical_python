'''Description:
Write a program to Print the Reverse of a Given Number?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Reverse of a Given Number.

Constraints  :- Given Input Must be Greater than Zero or else Print, "InValid Input".


Example:
Input 1  :    1698

Output 1:    8961

 

Input 2  :   1004

Output 2:   4001


Explanation:
Printing the Reverse of  A Given Number'''

num = int(input())
if num<=0:
    print("InValid Input")
else:
    rev = 0
    while num>0:
        r = num%10
        rev = rev*10+r
        num//=10
        # print(r, end ="")
        
    print(rev)


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


num = int(input())
num1 = int(input())
num, num1 = num1, num
print(num)
print(num1)

'''Description:
Write a program to print all Palindrome Numbers between the Given Numbers?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the All Palindromes Between the Given Numbers.

Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "InvaliD InputS".

                     If there are no Palindrome values between the Given Numbers then, Print "No Palindrome Values".

                     If starting range is greater than ending range, swap the inputs and print all palindromes in the range.


Example:
Input 1  :    100

                  200

Output 1:   

101

111

121

131

141

151

161

171

181

191 

 

Input 2  :   -20

                  20

Output 2:    InvaliD InputS


Explanation:
Input 1  :    100

                  200

Output 1:   

101

111

121

131

141

151

161

171

181

191 

Explanation : 

Palindrome Numbers Between 100 and 200 are 101 111 121 131 141 151 161 171 181 191

 

Input 2  :   -20

                  20

Output 2:    InvaliD InputS

Explanation : 

The Given Numbers are not Positive So print InvaliD InputS.'''

num = int(input())
num1 = int(input())
# if num<0 or num1<num:
#     print("InvaliD InputS")
# else:
#     c=0
#     for i in range(num+1, num1):
#         if str(i)==(str(i)[::-1]):
#             print(i)
#             c+=1
#     if c==0:
#         print("No Palindrome Values")
if num>num1:
    num, num1= num1, num
if num<=0 or num1<=0:
    print("InvaliD InputS")
else:
    def pal(n):
        rev = 0
        t = n
        while n>0:
            r = n%10
            rev = rev*10+r
            n//=10
        if t == rev:
            return True
    c=0
    for i in range(num+1, num1):
        if pal(i):
            print(i)
            c+=1
    if c==0:
        print("No Palindrome Values")

'''Description:
Write a program to check Given Number is Palindrome or Not.


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- If Given Number is a Palindrome then, print "Palindrome" or else print, "Not a Palindrome".

Constraints  :- Given Input Must be Greater than Zero or else Print "InvAlid Input".


Example:
Input 1  :    1698

Output 1:    Not a Palindrome

 

Input 2  :   2112

Output 2:   Palindrome

 


Explanation:
Input 1  :    1698

Output 1:    Not a Palindrome

Explanation : 

If you reverse the Given Number, (1698) then the value is 8961

Now, Check if the Given Number is equal to Reverse of Given Number.

1698 is not Equal to 8961 it means both are not Same, So Print "Not a Palindrome".

 

Input 2  :   2112

Output 2:   Palindrome

Explanation : 

If you reverse the Given Number (2112), then the value is 2112

Now, Check if the Given Number is equal to Reverse of Given Number

2112 is Equal to 2112 it means both are Same, So Print "Palindrome".'''

num1=int(input())
if num1>0:
#     print("InvAlid Input")
# else:
    def palin(num):
    # while num>0:
        rev = 0
        t = num
        while num>0:
            r = num%10
            rev = rev*10+r
            num//=10
        if t == rev:
            # print("Palindrome")
            return True
        # else:
        #     return False
            # print("Not a Palindrome")
            
    
    if palin(num1):
        print("Palindrome")
    else:
        print("Not a Palindrome")
        
else:
    print("InvAlid Input")

'''Description:
Write a program to find Sum of all Palindrome Numbers between the Given Numbers?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Sum of All Palindromes Between the Given Numbers.

Constraints  :- Either of the Given Inputs Must not equal to Zero or else Print "INVALID Inputs".

                    If the starting value is greater than ending value, swap the values and continue the process.

                     If there are no Palindrome values between the Given Numbers then Print "No Palindrome Values".

                     If either input value is negative, convert all negative values to positive.


Example:
Input 1  :    100

                  200

Output 1:   1460

 

Input 2  :   -20

                  25

Output 2:    22


Explanation:
Input 1  :    100

                  200

Output 1:   1460

Explanation :

Palindromes Between 100 and 200 are 101 111 121 131 141 151 161 171 181 191

sum = 101 + 111 + 121 + 131 + 141 + 151 + 161 + 171 + 181 + 191

       = 1460

 

Input 2  :   -20

                  25

Output 2:    22

Explanation :

Palindromic numbers between -20 and 25 include 22.

sum = 22'''

num = int(input())
num1 = int(input())
if num == 0 or num1 == 0:
    print("INVALID Inputs")
    
# if num ==0 and num1==0:
#     print("INVALID Inputs")
else:
    num = abs(num)
    num1= abs(num1)
        
    if num>num1:
        num, num1 = num1, num
        
    # if num1<0 and num<0:
    #     num = abs(num)
    #     num1 = abs(num1)
    
    def pal(n):
        rev = 0
        t = n
        while n>0:
            r = n%10
            rev = rev*10+r
            n//=10
        if t == rev:
            return True
    total = 0
    c=0
    for i in range(num+1, num1):
        if pal(i):
            total+=i
            c+=1
    if c==0:
        print("No Palindrome Values")
    
    # print(total)
    else:
        print(total)

'''Description:
Write a program to the check if the Given Number is a Palindrome or not and if it is a palindrome then Print PALINDROME, else Print the Reverse Value of a Given Number ?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Palindrome or Reverse value.

Constraints  :- Given Input is Must be Greater than or equal to Zero or else Print "Invalid Input".

                     If the Given Number is Zero then Print "Zero".


Example:
Input 1  :    1698

Output 1:    Reverse of a Given Number is 8961

 

Input 2  :   2112

Output 2:   Given Number is Palindrome

 


Explanation:
Input 1  :    1698

Output 1:    Reverse of a Given Number is 8961

Explanation : 

If you reverse the Given Number (1698) then the value is 8961.

Now Check if the Given Number is equal to Reverse of Given Number.

1698 is not Equal to 8961 it means both are not Same, So Print "Reverse value of the Given Number --> 8961".

 

Input 2  :   2112

Output 2:   Given Number is Palindrome

Explanation : 

If you reverse the Given Number (2112), then the value is 2112

Now Check if the Given Number is equal to Reverse of Given Number

2112 is Equal to 2112 it means both are Same, So Print "Given Number is Palindrome".''' 
num = int(input())

if num <0:
    print("Invalid Input")
else:
    if num==0:
        print("Zero")
    if num>0:
        rev = 0
        t= num
        while num>0:
            r = num%10
            rev = rev*10+r
            num//=10
            
        if rev == t:
            print("Given Number is Palindrome")
        else:
            print("Reverse of a Given Number is",rev)

'''Description:
Write a program to find Average of all Palindrome Numbers in the Range?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Average of All Palindromes In the Given Range.

Constraints  :- Either of the Given Inputs Must not equal to Zero or else Print "INVALID Inputs".

                     If there are no Palindrome values in the Given Range then, Print "No Palindrome Values".

                     If Either of the Given Inputs is Negative then convert all the Negative Values to Positive Values.

                     If the First Input is Greater then Second Input then, Print "Given Inputs are Swapped".


Example:
Input 1  :    100

                  120

Output 1:    106.00

 

Input 2  :   -20

                  45

Output 2:    33.00


Explanation:
Input 1  :    100

                  120

Output 1:    106.00

Explanation :

Palindromes in range 100 and 120 are 101 111

sum = 101 + 111

       = 212

Average = sum / count

            = 212 / 2

            = 106.00

 

Input 2  :   -20

                  45

Output 2:    33.00

Explanation :

Palindromes in the range -20 and 45 are 22 33 44

sum = 22 + 33 + 44

       = 99

Average = sum / count

            = 99 / 3

            = 33.00


'''


num1=int(input())
num2 = int(input())
num1=abs(num1)
num2=abs(num2)

if num1==0 or num2==0:
    print("INVALID Inputs")
    
# if num1 ==0 and num2==0:
#     print("INVALID Inputs")

# else:
#     num1 = abs(num1)
#     num2 = abs(num2)
    
    # if num2<0:
    #     num2 = abs(num2)
    # if num1<0 and num2<0:
    #     num1 = abs(num1)
    #     num2 = abs(num2)

elif num1>num2:
    print("Given Inputs are Swapped")
  # print("Given Inputs are Swapped")
  
    # num1 = abs(num1)
    # num2 = abs(num2)
   
else:        
    def avg_pal(n):
        rev = 0
        t = n
        while n>0:
            r = n%10
            rev = rev*10+r
            n//=10
        if rev == t:
            return True
        # return False
        
    if num1<num2:
        total=0
        c=0
        for i in range(num1, num2+1):
            if avg_pal(i):
                total+=i
                c+=1
        if c==0:
            print("No Palindrome Values")
        else:
            print(f"{total/c:.2f}")

'''Description:
Write a program to print the Sum of all Alternative Palindrome Numbers Between the Given Numbers?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Sum of All Alternative Palindromes Between the Given Numbers.

Constraints  :- If Either of the Given Inputs is equal to Zero then, Print "Invalid Inputs".

                     If there are no Palindrome values between the Given Numbers then, Print "No Palindrome Values".

                     If Either of the Given Inputs is Negative, then convert those Negative Values to Positive Values.


Example:
Input 1  :    100

                  200

Output 1:    Sum of Alternative Palindrome Numbers between the 100 and 200 is 101 + 121 + 141 + 161 + 181 = 705.

 

Input 2  :   -200

                  25

Output 2:    Sum of Alternative Palindrome Numbers between the 25 and 200 is 33 + 55 + 77 + 99 + 111 + 131 + 151 + 171 + 191 = 1019.

 


Explanation:
Input 1  :    100

                  200

Output 1:    Sum of Alternative Palindrome Numbers between the 100 and 200 is 101 + 121 + 141 + 161 + 181 = 705

Explanation :

Palindromes Between 100 and 200 is 101 111 121 131 141 151 161 171 181 191

Alternative Palindromes Between 100 and 200 is 101 121 141 161 181 

Sum = 101 + 121 + 141 + 161 + 181

       = 705

 

Input 2  :   -200

                  25

Output 2:    Sum of Alternative Palindrome Numbers between the 25 and 200 is 33 + 55 + 77 + 99 + 111 + 131 + 151 + 171 + 191 = 1019.

Explanation :

Palindromes Between 25 and 200 is 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191.

Alternative Palindromes Between 25 and 200 is 33 55 77 99 111 131 151 171 191.

Sum = 33 + 55 + 77 + 99 + 111 + 131 + 151 + 171 + 191

       = 1019'''

num = int(input())
num1 = int(input())

num = abs(num)
num1 = abs(num1)


if num == 0 or num1 == 0:
    print("Invalid Inputs")
# elif num == 0 and num1 ==0:
#     print("Invalid Inputs")
# if num>num1:
#     num, num1= num1, num
    
else:
    
    # num = abs(num)
    # num1 = abs(num1)
    
    if num>num1:
        num, num1= num1, num
        
    # if num<0 or num1<0:
    #     num = abs(num)
    #     num1 = abs(num1)
        
    # if num<0 and num1<0:
    #     num = abs(num)
    #     num1 = abs(num1)
        
    # print(f"Sum of Alternative Palindrome Numbers between the {num} and {num1} is ", end="")
    def alt_pal(n):
        rev = 0
        t = n
        while n>0:
            r = n%10
            rev = rev*10+r
            n//=10
        if t == rev:
            return True

    c=0
    total = 0
    plus = 0
    for i in range(num+1, num1):
        if alt_pal(i):
            c+=1
            if c==1:
                print(f"Sum of Alternative Palindrome Numbers between the {num} and {num1} is ",end="")
            if c%2==1:
                plus+=1
                total+=i
                if plus>1:
                    print(" + ", end="")
                print(i, end="")
    if c ==0:
        print("No Palindrome Values")
    else:
        print(f" = {total}.")
    # print(".")

'''Description:
Write a program to print Alternative Palindrome Numbers in the Given Range?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

                     Second Line of Input Consists of One Integer Value.

Output        :- Print the Alternative Palindromes in a Given Range.

Constraints  :- Given Inputs Must be Greater than or equal to Zero or else Print "InvAlid InPUts".

                     If there are no Palindrome values in the Given Range then, Print "No Palindrome Values".


Example:
Input 1  :    100

                  200

Output 1:   

101, 121, 141, 161, 181. 

 

Input 2  :   -33

                  20

Output 2:   InvAlid InPUts


Explanation:
Input 1  :    100

                  200

Output 1:   

101, 121, 141, 161, 181. 

Explanation : 

Palindrome Numbers in the Range of 100 and 200 are 101, 111, 121, 131, 141, 151, 161, 171, 181, 191.

Alternative Palindrome Numbers in the Range of 100 and 200 are 101, 121, 141, 161, 181.

 

Input 2  :   -33

                  20

Output 2:    InvAlid InPUts

Explanation : 

The Given Numbers are not Positive. So print "InvAlid InPUts".'''

num1 = int(input())
num2 = int(input())
if num1<0 or num2<0:
    print("InvAlid InPUts")

else:
    if num1 > num2:
        num1, num2= num2, num1
    def alt_pal(n):
        rev = 0
        t = n
        while n>0:
            r = n%10
            rev = rev*10+r
            n//=10
        if rev == t:
            return True
                
    c=0
    for i in range(num1, num2+1):
        if alt_pal(i):
            c+=1
            if c%2==1:
                if c>1:
                    print(",",end=" ")
               
                print(i, end="")
    # print(".")
    if c==0:
        print("No Palindrome Values")
    else:
        print(".")


'''Description:
Write A Program to check the Given Number is Perfect Square or not?


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Given Number is Perfect Square or not Perfect Square.

Constraints  :-  If the given input is negative convert it into positive

If the Given Input is equal to Zero then Print "Invalid Input".


Example:
Input 1  :    9

Output 1:    Given Number is Perfect Square.

 

Input 2  :   -11

Output 2:   Given Number is Not a Perfect Square.

 

Input 3  :    5

Output 3:    Given Number is Not a Perfect Square.


Explanation:
NA
'''

import math
num = int(input())
if num == 0:
    print("Invalid Input")
else:
    if num<0:
        num = abs(num)
    sq = int(math.sqrt(num))
    ps = sq*sq
    
    if num == ps:
        print("Given Number is Perfect Square.")
    else:
        print("Given Number is Not a Perfect Square.")
# if num < 0:
#     num = abs(num)