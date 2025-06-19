#Write a program in Python to perform the following


a = int(input("Enter a number:"))

print(a,"here is the input number")  #print function
print(f"here is the input number{a}")   #formated string print



if a % 3 == 0 and a % 5 ==0 :
    print ("BRUDITE-NIRVANA")
elif a % 3 ==0:
    print("SKILLBREW")
elif a % 5 ==0:
    print("BRUDITE")


""""2. Write a program that accepts a string as input from
the user and calculates the number of digits and
letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3
"""
alpha = 0
num = 0

for i in list("Brudite"):
    if i.isalpha():
        alpha += 1
    else:
        num += 1

print(f"total alphabets: {alpha}")
print(f"total nums: {num}")


""""3. Write a Python program to input marks for five
subjects Physics, Chemistry, Biology, Mathematics,
and Computer. Calculate the percentage and grade
according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
"""

physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
biology = float(input("Enter marks for Biology: "))
mathematics = float(input("Enter marks for Mathematics: "))
computer = float(input("Enter marks for Computer: "))


total = physics + chemistry + biology + mathematics + computer
percentage = (total / 500) * 100


if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print(f"\nTotal Marks: {total}/500")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")


""""4.Write a Python program to find the sum of all odd
numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25
"""

i = 1
sum = 0
while (i < 11):
    sum += i
    i += 2

print("sum is :", sum)



""""5. Write a Python program to find the factorial of a
number using a for loop.
"""


num = int(input("Enter a number to find factorial: "))


factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i

    print(f"Factorial of {num} is {factorial}")





    





