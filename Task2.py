'''''Task 1
Bitwise Operators Task (1-8)'''

#1
a = 10
b = 6

Print = (a & b)

#2
x = 12
y = 5

print(x | y)

#3
num = 8

print(~num)

#4
a = 15
b = 9

print(a ^ b)

#5
num = 7

print(num << 2)

#6
num = 20

print(num >> 1)

#7
num1 = int(input("enter any number:-"))
num2 = int(input("enter any number:-"))

print(num1 & num2)

#8
num3 = int(input("enter any number:-"))
num4 = int(input("enter any number:-"))

print(num3 ^ num4)

'''Task 2
string Task(9-14)'''

#9
welcome = "Hi"

print(welcome*4)

#10
text = "Python"

print(text * 3)

#11
first = "Super"
second = "Man"

print(first +" "+ second)

#12
word1 = "Hello"
sep = " "
word2 = "World"

print(word1 + sep + word2)

#13
username = input("Enter Your Name:-")

print(username * 5)

#14
firstname = input("Enter your First name:-")
secondname = input("Enter your Second name:-")

print(firstname + secondname)

'''Task 3
Input & Type casting (15-20)'''

#15
name = input("Enter Your Name:-")

print(type(name))

#16
age = int(input("Enter Your Age:-"))

print(type(age))

#17
number1 = int(input("Enter any number:-"))
number2 = int(input("Enter any number:-"))

print(number1 + number2)

#18
mark1 = int(input("Enter Your Maths Mark:-"))
mark2 = int(input("Enter Your Science Mark:-"))

print((mark1 + mark2)/2)

#19
a = int(input("Enter any number:-"))
b = int(input("Enter any number:-"))

print(3*a*2 + b -2)

#20
num = input("enter any number:-")

print("Before Typecating:",type(num))

numint = int(num)

print("After Typecating:",type(numint))

'''Task4
#unit digit (21-25)'''

#21
num = "12345"

print(num[4])

#22
num = 12345

print(num%10)

#23
num = 123456

print(num//10)

#24
num = 56847

print((num//10)%10)

#25
num = "75849"
print(num[len(num)-1])

'''Task 5
If statement tasks'''

#26
if (10 >= 5):
    print("condition is True")



#27
number = int(input("Enter any number"))

if (number > 50):
    print("given number is greater than 50")


#28
age = int(input("Enter Your Age:-"))

if (age >= 18):
    print("you are eligible")


#29
num=500

if (num>100):
    print("number is greater")


#30
num=10

if (num>=0):
    print("the number is above zero")


'''Task 6
if else statement(31-34)'''

#31
number = int(input("Enter any number"))

if number % 2 == 0:
    print("given number is Even")
else:
    print("given number is odd")

#32
marks = int(input("Enter your mark"))

if marks >= 35:
    print("you are pass")
else:
    print("you are fail")

#33
number = int(input("Enter any number"))

if number > 0:
    print("your number is positive")
else:
    print("your number is negative")

#34
number = int(input("Enter any number"))

if number > 10:
    print("greater than 10")
else:
    print("not greater than 10")

'''Task 7
Nested Statement(35-37)'''

#35
age = int(input("Enter Your Age:-"))
height = int(input("Enter Your Height in cm:-"))
weight = int(input("Enter Your Weight in kg:-"))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("you are eligible")
        else:
            print("you are rejected due to low weight")
    else:
        print("you are rejected due to low height")
else:
    print("you are rejected due to under age")

#36
age = int(input("Enter your age :- "))
marks = int(input("Enter your Mark"))

if age >= 17:
    if marks >= 60:
        print("you secured the college seat")
    else:
        print("you scored low marks")
else:
    print("your age not satisfied")

#37
age = int(input("Enter your age :- "))
height = int(input("Enter Your Height in cm:-"))
weight = int(input("Enter Your Weight in kg:-"))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("you are Selected")
        else:
            print("you are rejected due to low weight")
    else:
        print("you are rejected due to low height")
else:
    print("you are rejected due to under age")

'''Task 8
Match Statement (38-40)'''
#38
day = int(input("Enter today's number:-"))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")


#39
color_num = int(input("Enter number between 1-3:-"))

match color_num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("green")

#40
fruit = int(input("Enter Number Between 1-4:-"))

match fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")