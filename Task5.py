'''Task 1 : User Info Manager (Functions and dictionary)'''

def create_user(name, age, role):
    print("name :", name)
    print("age :", age)
    print("role :", role)
    return

users = {
    "user1": ("jack", 25, "Developer"),
    "user2": ("sam", 26, "Devops"),
    "user3": ("john", 24, "HR"),
    "user4": ("mathew", 27, "Data Analyst"),
    "user5": ("sara", 23, "Backend Developer"),
    "user6": ("Alice", 26, "Fullstack"),
}

for key, (name, age, role) in users.items():
    print(key)
    create_user(name, age, role)
    print()


'''Task 2 : Dynamic Calculator(*args)'''

def calculator(*a):
    sum = 0
    for num in a:
        sum += num
    return sum

print(calculator(1, 2, 3, 4))

#Bonus

def calculator(*a):
    sum = 0
    for num in a:
        sum += num
        avg = sum / len(a)
    return avg

print(calculator(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


'''Task 3 : Keyword config system(**kwargs)'''

def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")


'''task 4 : Factorial service (Recursion)'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


'''Task 5 : Memory optiomization(Generators)'''

def square_generator(n):
    for i in range(n):
        yield i ** 2

print(square_generator(10))

def square_normal(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result
print(square_normal(10))
print(type(square_normal(10)))

print(type(square_generator(10)))


'''Task 6 : Exeception handling'''

try :
     numerical = int(input("enter numerical number:-"))
     denominator = int(input("enter denominator number:-"))

     result = numerical / denominator

     print(result)

except ZeroDivisionError:

     print("you cannot divide by zero.")

except ValueError:
     print("give only integer")

finally :

     print("program completed")

'''Task 7 : File handling'''

with open("team_data.txt") as f :
    print(f.read())
    print(f.closed)





