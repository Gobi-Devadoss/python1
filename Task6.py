'''Task 1 : Encapsulation(User class)'''

class User:
    def __init__(self):
        self.__user_name = ""
        self.__password = ""

    def set_user(self,username,password):
        self.__user_name = username
        self.__password = password
    
    def get_user(self):
        return self.__user_name
    
    def register(self):
        print("registering user:" + self.__user_name )

    def login(self):
        print("loging in: " + self.__user_name)


user1 = User()
user1.set_user("ram","12345678")
user1.register()
user1.login()



'''Task 2 : Inheritance (User -> Student, Faculty)'''

class User:

    def register(self):
        print("registering user")

    def login(self):
        print("login successfull")


class Students(User):

    def student_greet(self):
        print("Hello Student")

class Faculty(User):

    def faculty_greet(self):
        print("Hello Faculty")

class Tempfaculty(Faculty):

    def tempfaculty_greet(self):
        print("Hello Temp Faculty")

student1 = Students()
student1.register()
student1.student_greet()

faculty1 = Faculty()
faculty1.login()
faculty1.faculty_greet()

tempfaculty1 = Tempfaculty()

tempfaculty1.tempfaculty_greet()

#Tempfaculty.faculty_greet() #shows Error parent cannot access child method


'''Task 3 : Method overriding'''

class User():

    def greet(self):
        print("Welcome User")

class Students(User):

    def greet(self):
        print("Welcome Student")

class Faculty(User):

    def greet(self):
        print("Welcome Faculty")


student1 = Students()
faculty1 = Faculty()
student1.greet()
faculty1.greet()

'''Task 4 : Method Cleaning'''

class User :

    def register(self) :
        print("regitered")
        return self

    def login(self) :
        print("logined")
        return self
        

    def greet(self) :
        print("enjoy everyone")
        return self
    
user = User()

user.login().greet().register()


'''Task 5 : Combined task - Mini User System'''

class User :

    users_count = 0

    def __init__(self):
        self.__user_name = ""
        self.__password = ""

    def set_user(self,username,password):
        self.__user_name = username
        self.__password = password

        User.users_count += 1


    def get_user(self):
        return self.__user_name
    
    def register(self):
        print("registering user:" + self.__user_name )

    def login(self):
        print("loging in: " + self.__user_name)

    def register(self) :
        print("regitered")
        return self

    def login(self) :
        print("logined")
        return self
        

    def greet(self) :
        print("enjoy everyone")
        return self


class Students(User):

    def student_greet(self):
        print("Hello Student")

    def greet(self):
        print("Welcome Student")
        return self

class Faculty(User):

    def faculty_greet(self):
        print("Hello Faculty")

    def greet(self):
        print("Welcome Faculty")
        return self

    
user1 = User()
user1.set_user("ram","12345678")
user1.register()
user1.login()


student1 = Students()
student1.register()
student1.student_greet()

faculty1 = Faculty()
faculty1.login()
faculty1.faculty_greet()

student1.greet()
faculty1.greet()


user = User()

user.login().greet().register()