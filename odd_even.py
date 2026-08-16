'''Description:
Write a program to check whether Given Number is Even or Odd. (Without  % , / , + )


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Even or Odd.

Constraints  :- Given Input is less than or equal to Zero then Print "InvaliD InpuT".


Example:
Input 1  :    9

Output 1:    Odd

 

Input 2  :   112

Output 2:   Even


Explanation:
NA'''

n = int(input())
if n<=0:
    print("IncaliD InpuT")
else:
    if n & 1 == 1:
        print("Odd")
    else:
        print("Even")


'''Description:
Write a program to check whether given number is even or odd. (Without  % , / , + ,* )


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Given Number is Even or Odd.

Constraints  :- Given Input is less than or equal to Zero then Print "Invalid Input".


Example:
Input 1  :    92

Output 1:    Even

 

Input 2  :   11

Output 2:   Odd


Explanation:
Na'''

n = int(input())
if n<=0:
    print("Invalid Input")
else:
    if n & 1==1:
        print("Odd")
    else:
        print("Even")

'''Description:
Write a program to check whether given number is even or odd. (Without dividing by 2)


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Given Number is Even or Odd.

Constraints  :- Given Input is less than or equal to Zero then Print "Invalid Input".


Example:
Input 1  :    92

Output 1:    Even

 

Input 2  :   11

Output 2:   Odd


Explanation:
NA
'''

n = int(input())
if n<=0:
    print("Invalid Input")
else:
    if n & 1 == 1:
        print("Odd")
    else:
        print("Even")

'''Description:
Write a Program to Print the numbers in the following format  -   
,...........64,27,8,1.   


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Following Format.

Constraints  :- Given Input is equal to Zero then Print "Invalid Input.".


Example:
Input 1  :    9

Output 1:    729, 512, 343, 216, 125, 64, 27, 8, 1.

 

Input 2  :   -11

Output 2:    1331, 1000, 729, 512, 343, 216, 125, 64, 27, 8, 1.

 

Input 3  :    5

Output 3:    125, 64, 27, 8, 1.


Explanation:
Print following Output for respective input.'''

n = int(input())
n = abs(n)

if n==0:
    print("Invalid Input.")
else:
    c=0
    for i in range(n,0,-1):
        c+=1
        if c>1:
            print(",", end=" ")
        print(i**3, end="")
    print(".")


'''Description:
Write a Program to Find the result of the following expression -  
 + ........... 16 + 9 + 4 + 1=?  


Constraints:
Input          :- First Line of Input Consists of One Integer Value.

Output        :- Print the Following Format.

Constraints  :- Given Input is equal to Zero then Print "Invalid Input".


Example:
Input 1  :    9

Output 1:    81 + 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 285

 

Input 2  :   -11

Output 2:   121 + 100 + 81 + 64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 506

 

Input 3  :    5

Output 3:    25 + 16 + 9 + 4 + 1 = 55.


Explanation:
----'''

n = int(input())
n = abs(n)
if n==0:
    print("Invalid Input")
else:
    c=0
    sum = 0
    for i in range(n,0,-1):
        c+=1
        if c>1:
            print(" +", end=" ")
        print(i**2, end="")
        sum+=i**2
    print(" =",sum)