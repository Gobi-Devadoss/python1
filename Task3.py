'''Section 1 : Loop Basics (1-10)'''

#Task 1

for i in range(51):
    print(i)

#Task 2


for i in range(1, 101):
    if (i % 2 == 0):
        print(i)

#Task 3

for i in range(1, 101):
    if (i % 2 != 0):
        print(i)

#Task 4

for i in range (1,11):
    print(i, "x", "7", "=", i*7)

#Task 5

total = 0
for i in range (1, 101):
    total += i
    
print("Sum:", total)

#Task 6

for i in range (50,0,-1):
    print(i)

#Task 7

count = 0

for i in range (1,101):
    if (i%3==0):
        count += 1
print("Numbers divisible by 3:", count)

#Task 8

for i in range(1,11):
    print(i ** 2)


#Task 9

for i in range(1,11):
    print(i ** 3)


#Task 10

n = int(input("Enter any number:-"))

for i in range(1,n+1):
    print(i)


'''Section 2 While loop (11-15)'''

#Task11

count = 1
while count<=20:
    print(count)
    count += 1


#Task12

num = int(input("Enter Any Number:-"))

factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i += 1

print(("Factorial is", factorial))


#Task13
num = int(input("Enter Any Number:-"))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num// 10
print("reverse number: ", reverse)


#Task14


num = 56874

count = 0

while num != 0:
    num = num // 10
    count += 1
print("number of digits:", count)


#Task15

alpha = ""

while True:
    alpha= input("Enter Any Alphabet, or type stop to end :-")
    if alpha == "stop":
        break
print(alpha)


'''Section 3 Nested loop'''

#Task 16

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

#Task 17


for i in range(1, 6):
    for j in range(i):
        print(j, end="")
    print()


#Task 18
for i in range (1, 6):
    print("table", i)
    for j in range (1, 11):
        print(i,"x",j, "=", i*j)
    


#Task 19

for i in range(3):
    print("A B C", end="\n")
    print()


#Task 20

for i in range(3):
    print("1 2 3", end="\n")
    print()


'''Section 4 string basics(21-25)'''

#Task 21

str = input("Enter any text:-")

print(len(str))

#Task 22

text = input("Enter any text:-")

count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:- ",count)

#Task 23

text = input("Enter any text:-")

count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char not in vowels:
        count += 1
print("Number of consonent:- ",count)

#Task 24

str = input("enter any text:-")
str1 = ""

for char in str:
    str1= char + str1
print(str1)
    
#Task 25

str = input("enter any text:-")
str1 = ""

for char in str:
    str1= char + str1

if str1 == str:
    print("palindrome")
else:
    print("Not palindrome")



'''Section 5 String Slicing (26-30)'''

#Task 26

str = input("Enter Any Text with 8 letters:-")

print(str[ : 5])


#Task 27

str = input("Enter Any Text with 8 letters:-")

print(str[ -4: -1])

#Task 28

str = input("Enter Any Text with 8 letters:-")

print(str[ : : -1])


#Task 29

str = input("Enter Any Text with 8 letters:-")

print((str[0 : : 2]))

#Task 30

str = input("Enter Any Text with 8 letters:-")

str1 = str[1:-1]

print(str1)

'''Section 6 list basics(31-35)'''


#Task 31

numbers = [10, 15, 20, 25, 30]
print(sum(numbers))


#Task 32

numbers = [10,20,50,45,32,27]

max_num = max(numbers)

print("Maximum number :-",max_num)


#Task 33

numbers = [10,20,50,45,32,27]

min_num = min(numbers)

print("Minimum number :-",min_num)

#Task 34

numbers = [ 5, 6, 7, 8, 9, 10]
len(numbers)


#Task 35

numbers = [10,20,30,40,50,60]

element = int(input("Enter any number to search:"))

found = False

for num in numbers:
    if num == element:
        found = True
        break

if found:
    print("number found in list")
else:
    print("number not found")

'''Section 7 list operations(36-40)'''


#Task 36

list1 = ["apple", "orange", "Banana"]

list1.append("jackfruit")
list1.append("mango")
list1.append("guava")

print(list1)


#Task 37

list1 = ["apple", "orange", "Banana"]

list1.insert(2, "watermelon")

print(list1)


#Task 38

list1 = ["apple", "orange", "Banana", "mango", "watermelon"]

list1.remove("mango")
print(list1)


#Task 39


list1 = ["apple", "orange", "Banana", "mango", "watermelon"]

print(list1[ : :-1])

#Task 40

list1 = ["apple", "orange", "banana", "mango", "watermelon"]

sorted_list = sorted(list1)

print(sorted_list)