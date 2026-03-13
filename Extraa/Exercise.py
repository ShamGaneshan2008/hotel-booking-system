# class Instructor:
#     def __init__(self, name, address, course):
#         self.name = name
#         self.address = address
#         self.course = course
#
# ins_1 = Instructor("Sham", "Aussie", "CS")
# print(ins_1.name)
# ins_2 = Instructor("Ram", "Dubai", "ME")
# print(ins_2.course)
# ins_3 = Instructor("Zack", "US", "Civil")
# print(ins_3.name)
# ins_4 = Instructor("Amanda", "Denmark", "EEE")
# print(ins_4)


# class Dog:
#     sound = "Bark"
#     behaviour = "Friendly"
#     breed = "GDS"
#     height = "Normal"
#
# dog_1 = Dog()
# print(dog_1.sound)
#
# dog_2 = Dog()
# print(dog_2.behaviour)
#
# dog_3 = Dog()
# print(dog_2.breed)
#
# dog_4 = Dog()
# print(dog_2.height)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# stu_1 = Student("Sham", 23)
# print(stu_1.name)
# print(stu_1.age)
#
# stu_2 = Student("Ram", 12)
# print(stu_2.name)
# print(stu_2.age)


# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
# car_1 = Car("BMW", 550000)
# print(car_1.brand)
#
# car_2 = Car("Maruti", 10000)
# print(car_2.price)

# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def greet(self):
#         print("Hello, my name is", self.name)
#
# p1 = Person("Sham")
# p1.greet()

# class Rectangle:
#     def __init__(self, length, width):
#         self.len = length
#         self.wid = width
#
#     def area(self):
#         return self.wid * self.len
#
# answer = Rectangle(3,6)
# print("The area of the rectangle is: ", answer.area())
#
# class Mobile:
#     def __init__(self, brand, RAM, price):
#         self.brand = brand
#         self.RAM = RAM
#         self.price = price
#
#     def display(self):
#         print("Brand", self.brand)
#         print("RAM", self.RAM)
#         print("Price", self.price)
#         print("-----------------------")
#
# mobile1 = Mobile("Samsung", 8, 200000)
# mobile2 = Mobile("Realme", 5, 10000)
# mobile3 = Mobile("Vivo", 6, 450000)
#
#
# mobile1.display()
# mobile2.display()
# mobile3.display()


# class Library:
#     def __init__(self, book):
#         self.book = book
#
#     def check_book(self,book_name):
#         if book_name in self.book:
#             print(book_name,"It is available in the library")
#         else:
#             print(book_name,"It not available in the library")
#
# library = Library(["Python", "Java", "C", "C++"])
#
# library.check_book("Java")
# library.check_book("Vengence")
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def are_circle(self):
#         return 3.14 * self.radius * self.radius
#
# c1 = Circle(5)
# print("The area of the circle is: ",c1.are_circle())


# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
# value = Calculator(78,45)
#
# print("The addition for the equation is: ",value.add())
# print("The subtraction for the equation is: ",value.sub())
# print("The multiplication for the equation is: ",value.mul())
# print("The division for the equation is: ",value.div())


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def details(self):
#         print("The title of the book is: ",self.title)
#         print("The author of the book is: ",self.author)
#
# book1 = Book("Python Programming ", "Guido van Rossum")
#
# book1.details()
#




#                          ///////// 4TH SEMESTER  FIRST PROGRAM //////////
# class Date:
#     def __init__(self, day, month, year):
#         self.date_val = day
#         self.month_val = month
#         self.year_val = year
#
#     def day(self):
#         print("Day: ",self.date_val)
#
#     def month(self):
#         print("Month", self.month_val)
#
#     def year(self):
#         print("Year", self.year_val)
#
#     def month_name(self):
#         months = ["Unknown","January", "February", "March", "April", "May", "June",
#             "July", "August", "September", "October", "November", "December"]
#         print("The current month is: ",months[self.month_val])
#
#     def isLeapYear(self):
#         if self.year_val % 400 == 0:
#             print("It is a leap year")
#         elif self.year_val % 4 == 0 and self.year_val % 100 != 0:
#             print("It is a leap year")
#         else:
#             print("It is not a leap year")
#
#
# d1 = Date(23, 1, 2008)
# d1.day()
# d1.month()
# d1.year()
# d1.month_name()
# d1.isLeapYear()




# import time
# class Stack:
#     def __init__(self):
#         # Initialize an empty stack
#         self.items = []
#
#     def isEmpty(self):
#         # Check if stack is empty
#         return self.items == []
#
#     def push(self, item):
#         # Insert element into stack
#         self.items.append(item)
#
#     def pop(self):
#         # Remove top element from stack
#         if self.isEmpty():
#             print("Stack Underflow")
#             return None
#         return self.items.pop()
#
#     def peek(self):
#         # Return top element without removing
#         if self.isEmpty():
#             print("The list is empty")
#             return None
#         return self.items[-1]
#
#     def size(self):
#         # Return number of elements
#         return len(self.items)
#
#     def display(self):
#         # Display stack elements
#         return self.items
#
# s = Stack()
#
# start = time.time()
#
# print(s.isEmpty())
#
# print("Push Operations")
# s.push(11)
# s.push(12)
# s.push(13)
# print("Size: ",s.size())
#
# print(s.display())
#
# print("Peek: ",s.peek())
# print("Pop Operation")
# print(s.pop())
# print(s.pop())
# print(s.display())
#
# print("Size: ", s.size())
#
# end = time.time()
# print("Runtime of the program is: ",end - start)


# import time # to track the time until the program ends
# def linearsearch(arr,key): # method to the index of the value
#     n = len(arr) # to find the number of value in the array of element
#     for index in range(n): # loop the number of element in the array
#         if arr[index] == key: # if the index = the user inputt
#             return index # return the index
#     return -1
# arr = [12,34,67,90,37,50] # this is the array given by user
#
# start = time.time() # this start the time tracking
# print("The array elements are: ",arr) # prints the array
#
# k = int(input("Enter the key top be searched: ")) # this asks the input to the user
#
# index = linearsearch(arr,k) # Searches for key k in list a and stores the result index in i
# if index == -1: #
#     print("Search Unsuccessful")
# else:
#     print("Search successful key found at location: ",index+1)
# end = time.time() # this ends the time tracking
# print("Runtime of the program is: ", start - end) # prints out the time diff of start and end

# def my_decor(func):
#     def wrapped():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapped
#
# @my_decor
# def say_hello():
#     print("Hello")
#
#
# say_hello()

# def decor(func):
#     def before():
#         print("Before function started")
#         func()
#     return before
#
# @decor
# def after():
#     print("After function ended ")
#
# after()

# def decorator(func):
#     def before():
#         print("Function execution started")
#         func()
#         print("Function execution ended"
#               "")
#     return before
#
# @decorator
# def display():
#     print("Hello World")
#
# display()



# def number(check_number):
#     if check_number % 2 == 0:
#         return True
#     else:
#         return False
#
# print("The even or odd is: ",number(2))

# def number(a, b):
#     sums = a + b
#     return sums
#
# print("The sum of two number is: ",number(2,5))




# def uppercase_decorator(func):
#     def words():
#         capital_letter = func()
#         return capital_letter.upper()
#     return words
#
# @uppercase_decorator
# def greet():
#     return "hola amigos"
#
# print("The greeting in capital letters are: ", greet())




# import time
# def decorator(func):
#     def number():
#         start = time.time()
#         func()
#         end = time.time()
#         print("Exection time: ", end-start, "seconds")
#     return number
#
# @decorator
# def times():
#     for i in range(1,9):
#         print(i)
#         time.sleep(1)
#
# times()


# import time
# def time_decorator(func):
#     def number():
#         start = time.time()
#         func()
#         end = time.time()
#         print("Execution time:", end-start, "seconds")
#     return number
#
# @time_decorator
# def slow_function():
#     time.sleep(2)
#     print("Task completed")
#
#
# slow_function()


# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#
#     def display(self):
#         print("The name of the student: ",self.name)
#         print("The roll_no of the student: ",self.roll_no)
#         print("The marks of the student: ",self.marks)
#
# s1 = Student("Sham", 121, 456)
#
# s1.display()



# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#
#     def display(self):
#         print("The name of the employee is: ", self.name)
#         print("The emp_id of the employee is: ", self.emp_id)
#         print("The salary of the employee is: ", self.salary)
#
# emp1 = Employee("Rachin", 121, 450000)
#
# emp1.display()


# def decorator(func):
#     def wrapped(self): ## Decorators for class methods MUST accept self
#         print("The msg is: Trust the process")
#         func(self)
#     return wrapped
#
# class Student:
#     def __init__(self ,name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#
#     @decorator
#     def display(self):
#         print("Name: ", self.name)
#         print("Roll_no: ", self.roll_no)
#
# s1 = Student("Sham", 121)
#
# s1.display()






