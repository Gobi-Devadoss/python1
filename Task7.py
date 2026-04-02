from functools import reduce

'''Task 1: use super'''
class User:

    def __init__(self,name,id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self,name,id,dept,fees):
        super().__init__(name,id)
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary


class Tempfaculty(User):
    def __init__(self,name,id,salary,duration):
        super().__init__(name,id,)
        self.salary = salary
        self.duration = duration

s1= Student("John","S01","ARTIFICIAL INTELLIGENCE",100000)
print(f'Name: {s1.name}, Id: {s1.id}, Dept: {s1.dept}, Fees: {s1.fees}')

f1= Faculty("ram","F01",30000)
print(f'Name: {f1.name}, Id: {f1.id}, Salary: {f1.salary}')

tf1= Tempfaculty("mano","TF01",20000,"12 month")
print(f'Name: {tf1.name}, Id: {tf1.id}, Salary: {tf1.salary}, Duration: {tf1.duration}')


'''Task 2 : Abstraction'''

from abc import ABC,abstractmethod


class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class User:

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def get_details(self):
        return f'Name: {self.name}, ID: {self.id}'

class Student(User):
    def __init__(self,name,id,dept,fees):
        super().__init__(name,id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f'{self.name}, Id: {self.id}, Dept: {self.dept}, Fees: {self.fees}'

class Faculty(User):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
    
    def get_details(self):
        return f"{self.name}, {self.id}, Salary: {self.salary}"
    

class Tempfaculty(User):
    def __init__(self,name,id,salary,duration):
        super().__init__(name,id,)
        self.salary = salary
        self.duration = duration
    
    def get_details(self):
        return f"Name:{self.name}, Id:{self.id}, Salary: {self.salary}, Duration:{self.duration}"
    

#list for sort,map,filter,reduce
students = [
    Student("John", 1, "CSE", 60000),
    Student("Alice", 2, "ECE", 45000),
    Student("Sara", 3, "IT", 70000),
    Student("Sam", 4, "CSE", 30000)
]

faculty = [
    Faculty("Smith", 101, 40000),
    Faculty("Joseph", 102, 25000),
    Tempfaculty("Ravi", 103, 35000, "6 months"),
    Tempfaculty("Anish", 104, 28000, "3 months")
]

'''Task 3 : Sorting '''
sorted_student = sorted(students, key=lambda x: x.fees)
for s in sorted_student:
    print(s.get_details())

sorted_faculty = sorted(faculty, key=lambda x: x.salary)
for f in sorted_faculty:
    print(f.get_details())


'''Task 4 : using Map'''
student_names = list(map(lambda s:s.name,students))
print(student_names)

faculty_names = list(map(lambda s:s.name,faculty))
print(faculty_names)

'''Task 5 : Using filter'''
high_students_fees = list(filter(lambda s: s.fees>50000,students))
for s in high_students_fees:
    print(s.get_details())

high_faculty_salary = list(filter(lambda f: f.salary>50000,faculty))
for f in high_faculty_salary:
    print(f.get_details())



'''Task 6 : using Reduce'''
total_fees_collected = reduce(lambda acc, s: acc+int(s.fees),students,0)
print("Total fees collected : ", total_fees_collected)

total_salary = reduce(lambda acc, f: acc+int(f.salary),faculty,0)
print("Total salary : ", total_salary)


'''Task 7 : higher order function'''

def process_users(users, func):
    return list(map(func, users))

upper_names = process_users(students, lambda s: s.name.upper())
print(upper_names)


'''Final challenge'''

print("------Final Challenge------")

for user in students + faculty:
    print(user.get_details())

for s in sorted(students, key=lambda x: x.fees):
    print(f"{s.name} -> {s.fees}")

for s in filter(lambda s: s.fees > 50000, students):
    print(f"{s.name} -> {s.fees}")


print("Total fees collected : ", reduce(lambda acc, s: acc+int(s.fees),students,0))


print("Total salary : ", reduce(lambda acc, f: acc+int(f.salary),faculty,0))

print("------Combining 3 concepts------")

total= list(
    map(
        lambda s:s.get_details(),
        filter(lambda s:s.fees>50000,students)
    )
)
for t in total:
    print(t)
