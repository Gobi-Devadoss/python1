'''Mini Project 1 : Employee Management System'''

# Create an empty list to store employee information


employee_list= []

# Add employee information to the list using dictionaries
employee_list.append({"name": "John", "age": 30, "role": "HR", "salary": 50000})

employee_list.append({"name": "Jack", "age": 25, "role": "Developer", "salary": 60000})

employee_list.append({"name": "ram", "age": 28, "role": "Data Analyst", "salary": 55000})

employee_list.append({"name": "Michael", "age": 35, "role": "Devops Engineer", "salary": 50000})

print(employee_list)

# Updating an employee's information
employee_list[0]["salary"] = 55000

print(employee_list[0])


#adding a new employee to the list
employee_list.append({"name": "Sara", "age": 32, "role": "Sales", "salary": 45000})

print(employee_list)

# Removing an employee from the list
del employee_list[1]

print(employee_list)


'''Mini Project 2 : Student report card '''

#creating dictionary to store student information

student_details = {
    "name": "Alice",
    "subjects": {"Math": 85, "Science": 90, "English": 88},
}
# Calculate total marks using a function
def calculate_total_marks(student):
    total_marks = sum(student["subjects"].values())
    return total_marks

print("Total Marks:", calculate_total_marks(student_details))


# Calculate average marks using a function
def calculate_average_marks(student):
    total_marks = calculate_total_marks(student)
    average_marks = total_marks / len(student["subjects"])
    return average_marks

print("Average Marks:", int(calculate_average_marks(student_details)))

# grade based on average marks using a function
def assign_grade(student):
    average_marks = calculate_average_marks(student)
    if average_marks >= 90:
        return "A"
    elif average_marks >= 80:
        return "B"
    else:
        return "C"

print("Grade:", assign_grade(student_details))

#formatted report card
def generate_report_card(student):
    report_card = "Report card of " + student["name"] + "\n"
    for subject, marks in student["subjects"].items():
        report_card += subject + ": " + str(marks) + "\n"
    report_card += "Total Marks: " + str(calculate_total_marks(student)) + "\n"
    report_card += "Average Marks: " + str(int(calculate_average_marks(student))) + "\n"
    report_card += "Grade: " + assign_grade(student) + "\n"
    return report_card

print(generate_report_card(student_details))


'''Mini project 3 : shopping cart system'''

product = []

product.append({"productname" : "rice", "price" : 62, "quantity" : 5})
product.append({"productname" : "wheat", "price" : 45, "quantity" : 3})
product.append({"productname" : "sugar", "price" : 40, "quantity" : 2})
product.append({"productname" : "salt", "price" : 20, "quantity" : 4})

print(product)

# Calculate total bill

def total_bill(products):
    total=0
    for item in products:
        total += item["price"] * item["quantity"]
    return total
    
print("Total Bill:", total_bill(product))

#removing item from the cart
del product[1]


#displaying the bill in a formatted way


def bill_generated(product):
    bill = "invoice for the purchase " + "\n"
    for item in product:
        bill += item["productname"] + ": " + str(item["price"]) + " x " + str(item["quantity"]) + " = " + str(item["price"] * item["quantity"]) + "\n"
    bill += "Total Bill: " + str(total_bill(product)) + "\n"
    return bill

print(bill_generated(product))


'''Mini project 4 : Login and user validation'''

#storing username and password

users = {
    "admin": "password123",
    "user1": "mypassword"
}

#taking login input

username = input("enter username: ")
password = input("enter password: ")

#validating credentials

if username in users and users[username] == password:
    print("login successful")
else:
    print("invalid username or password")

'''Mini project 5 : unique visitor counter'''

#storing unique visitors in a set

visitors = {"john", "jack", "ram", "michael", "sara"}

#adding duplicate visitor
visitors.add("sara")

print(visitors)

#counting unique visitors
print("Unique visitors count:", len(visitors))

'''Mini project 6 : string formatter tool'''

name_input = input("enter your name: ")
product_input = input("enter product name you purchased: ")


#formattting string 
text = 'Hello {0}, thank you for purchasing {1}!'

print(text.format(name_input, product_input))

#Padding String

print('{0:>20}'.format(name_input))
print('{0:<20}'.format(name_input))
print('{0:^20}'.format(name_input))


'''Mini project 7 : bank account system'''

bank_accounts = {
    "account1": {"name": "John", "balance": 1000},
    "account2": {"name": "Jack", "balance": 1500},
    "account3": {"name": "ram", "balance": 2000},
    "account4": {"name": "Michael", "balance": 2500},
}

def deposit_money(account, amount):
    bank_accounts[account]["balance"] += amount
    return bank_accounts[account]["balance"]

def withdraw_money(account, amount):
    bank_accounts[account]["balance"] -= amount
    return bank_accounts[account]["balance"]

def check_balance(account):
    return bank_accounts[account]["balance"]

print("Balance after deposit:", deposit_money("account1", 500))
print("Balance after withdrawal:", withdraw_money("account1", 200))
print("Current Balance:", check_balance("account1"))


'''Mini project 8 : voting system'''

candidates = {"john": 3000, "jack": 2500, "ram": 2800, "michael": 3500, "sara": 3200}

votes= 0

#counting total votes casted

for candidate, vote_count in candidates.items():
    votes += vote_count
print("Total votes casted:", votes)

#finding the winner

for candidate, vote_count in candidates.items():
    if vote_count == max(candidates.values()):
        print("Winner is:", candidate)

'''Mini project 9 : course enrollment system'''

students = []

students.append({"name": "John", "courses": ["Math", "Science"]})
students.append({"name": "Jack", "courses": ["English", "History"]})
students.append({"name": "ram", "courses": ["Math", "English"]})
students.append({"name": "Michael", "courses": ["Science", "History "]})

#updating courses for a student

students[0]["courses"].append("History")
print(students[0])

#displaying students details
def display_student_details(students):
    details = ""
    for student in students:
        details += "Name: " + student["name"] + "\n"
        details += "Courses: " + ", ".join(student["courses"]) + "\n\n"
    return details 

print(display_student_details(students))

'''Mini project 10 : number utility tool'''

#converting number to binary,octal and hexadecimal

number = int(input("enter a number: "))

print("Binary:", bin(number))
print("Octal:", oct(number))
print("Hexadecimal:", hex(number))

#formatting large numbers with commas

money = 100000000

print("account balance: Rs.{:,}".format(money))


