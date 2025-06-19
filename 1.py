
""""6.Write a Python program to check if a given number
is a perfect number.
A Perfect number is a positive integer that is equal to the
sum of its proper divisors. For instance, 6 has divisors 1, 2,
and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
Input: 5
Output: No
"""
num = int(input("Enter a number: "))

sum_divisors = 0


for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num and num != 0:
    print("Yes, it's a Perfect Number")
else:
    print("No, it's not a Perfect Number")


""""7.Write a Python program to check if a string is an
anagram of another string.
string1 = "listen", string2 = "silent"
Output: True
"""
a = input("Enter first string: ")
b = input("Enter second string: ")

if sorted(a) == sorted(b):
    print("True")
else:
    print("False")



""" 8.Write a Python program to calculate the LCM (Least
 Common Multiple) of two numbers."""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    big = x
else:
    big = y

while True:
    if big % x == 0 and big % y == 0:
        print("LCM is:", big)
        break
    big += 1



    """9.Write a Python program to count the frequency of
 each element in a list."""

lst = [1, 2, 3, 2, 4, 1, 2, 4, 5]
freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)



""" 10. Write a Python program to reverse the order of
 words in a given sentence."""

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print(result)




"""11. Write a Python program to calculate the sum of
 digits of a given number until the sum becomes a
 single-digit number."""


num = int(input("Enter a number: "))


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  
        n = n // 10       
    return total


while num >= 10:
    print("Intermediate sum:", num)
    num = sum_of_digits(num)


print("Final Output:", num)


"""12. Write a Python program to reverse a number using
 a while loop."""

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10   
    rev = rev * 10 + digit
    num //= 10

print("Reversed number is:", rev) 
