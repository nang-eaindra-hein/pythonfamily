#1.Create a variable age with your age and print its type
x = 20
print (type(x))

#2.Make a variable price with a float value. Add 10 to it and print.
x = 2.5
x +=10
print (x)

#3.Create a complex number z = 4 + 5j and print its real and imaginary parts.
z = 4+5j 
print (z.real , z.imag)

#4.Make a variable is_student = True. Print the opposite using not.
is_student=True

print(not is_student)


#5.Create two boolean variables and test them with and and or.
is_mango =True
is_apple=False
print(is_mango and is_mango)
print(is_apple or is_mango)

#6.Create a string name = "Eaindra Hein" and print the first 4 letters.
x = "Eaindra Hein"
print (x[:4])

#7.Turn the string into lowercase and uppercase.
x= "nang EainDra"
print(x.upper())
print(x.lower())

#8.Reverse a string using slicing.
x = "Nang"
print(x[::-1])

#9.Make a list of 5 fruits.Add one more fruit to the list.Remove the 2nd fruit from the list.Print only the last fruit in the list.
fruits = ["mango","apple","pinapple","orange","grapes"]
fruits.append("cherry")
del fruits[1]
print (fruits[-1])
print(fruits)

#10.Create a tuple of 3 colors.Print the second color in the tuple.Can you change one value in the tuple? Try and see what happens.
colors=('green','yellow','red')
print (colors[1])


#11.Create a set with numbers 1,2,3,3,4. Print it.Add number 5 to the set.Remove number 2 from the set.
numbers = {1,2,3,3,4}
print (numbers)
numbers.add(5)
numbers.discard(2)
print(numbers)


#12.Create a dictionary student = {"name": "Eaindra", "age": 19}.Print only the name from the dictionary.Change the age to 20.Add a new key "country": "Singapore".
student = {"name":"Eaindra", "age":19}
print (student["name"])
student["age"]=20
student["country"]="Singapore"
print(student)

#13.Create a bytes variable with the word "Hello".Convert it into a bytearray and print.
bytes = b"Hello"
ba =bytearray(bytes)
print(ba)

#14.Make a variable x = None. Print whether it is None using is.
x=None
print(x is None)

#15.Create a class Dog with two attributes: name and age.Create an object of Dog called dog1 with your own values.Print your dog’s name and age.
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=Dog("zero",2)
print(dog1.name,dog1.age)

#16.Write a program to check if a number is divisible by both 2 and 3
x = 5
if x % 2 == 0 and x % 3 == 0:
    print ("the number can be divisible by 2 and 3")

else:
    print("the number cannot be divisible by 2 and 3")

# 17.Create a program that takes a score (0–100) and prints the grade:A: 80–100,B: 60–79,C: 40–59,F: below 40

score = 79
if 80 <= score <= 100:
    print ("Grade : A ")
elif 60 <= score <= 79:
    print ("Grade : B")
elif 40 <= score <= 59:
    print ( "Grade : C")
else :
    print ("Grade : F")

#18. Check whether a year is a leap year. (Leap years are divisible by 4 but not by 100, except if divisible by 400.)
year = 2025

if year % 4 == 0:
    print ("it is a leap year divided by 4")

elif year % 100 == 0:
    print ("it is not a leap year divided by 100")

elif year % 400 == 0:
    print( "it is a leap year divided by 400")
else:
    print("it is not a leap year ")

#19.Take three numbers and print the largest among them.
numbers = (1,2,3)
print ("largest number is ", max(numbers))

#20.Write the grading system in school.A-marks above 80,B-marks betw 60 and 80, C- marks betw 40 and 60,
# F-marks under 40,error when marks minus or above 100
 
marks = 0

if 100 >= marks > 80:
    print("Grade A")
elif 60 <= marks <= 80:
    print ("Grade B")
elif 40 <= marks <= 60:
    print("Grade C")
elif  0 > marks or marks> 100:
    print ("Erorr")
else:
    print ("Grade F")

#21 Input a number and check if it is positive, negative, or zero.
x = -7
if x > 0:
    print("posotive")
elif x < 0:
    print("negative")
else:
    print("zero")

#22.Write a program to check if someone is eligible to vote (age ≥ 18).
age = 10
if age >=18:
    print ("eligible to vote")
else:
    print("not eligible to vote")

#23.Given three angles of a triangle, check if it forms a valid triangle (sum = 180).
x, y ,z = 35 ,30 ,115
sum = x + y + z
if sum == 180 and (x > 0 ,y > 0, z >0 ):
    print(sum ,"and it is triangle")
else:
    print(sum ,"and it is not triangle")

#24.if (fruit == "apple"){if (color == "red"){price = 5.00}} change nested condition into single condition
fruit = "apple"
color ="red"
price = 5.00

if fruit == "apple" and color == "red":
    print(price)
else:
    print("")


#25. Take two strings and check if they are equal or not (case-insensitive).
x = "apple"
y = "APPLE"
if x.lower() == y.lower():
    print("it is equal")
else:
    print("not equal")

#26.print list in reverse order using loop ,list1 = [10,20,30,40,50] 
list1 = [10,20,30,40,50]
print(list1[::-1])

#27.find the factorial of given number,the factorial (symbol: !) means multiplying all munbers from chosen number down to 1.
number = 8
fact = 1
for i in range (1,number+1):
    fact = fact*i
print(fact)

#28.Print numbers from 1 to 10 using a for loop.
for i in range (1,11):
    print(i)

#29.Print the square of numbers from 1 to 5.
for i in range (1,6):
    print(i*i)

#30.Print all even numbers between 1 and 20.
for i in range (2,21,2):
    print(i)

#31.Print each character in the string "Python".
x = "Python"
for i in x:
    print (i)

#32. Print all items in a list: ["apple", "mango", "banana", "orange"].
list = ["apple","mango","banana","orange"]
for i in list:
    print(i)

#33.Print numbers from 1 to 10 using a while loop.
i=1
while i<11:
    print(i)
    i += 1


#34.Print numbers from 10 down to 1 using a while loop.
i = 10
while i > 0:
    print(i)
    i -=1
    

#35.Keep asking the user for a number until they enter 0.
number = int(input("enter zero: "))
while number != 0:
    number = int(input("enter zero: "))
print("ok")
    

#36.Print the sum of numbers from 1 to 100 using a while loop.
number = 1
sum = 0
while number <= 100 :
    sum += number
    number +=1
print(sum)


#37.Print the multiplication table of 5 using a while loop.
i = 1
while i <6:
    print (" 5 times", i ,"=" ,5 * i)
    i +=1

#38.Print numbers from 1 to 10, but stop when you reach 6.
for i in range(1,11):
    if i == 7:
        break
    print(i)


#39.Print numbers from 1 to 10, but skip the number 5.
for i in range(1,11):
    if i == 5:
        continue
    print(i)


#40.Search for "mango" in a list, and stop when found.
list = ["apple","mango","orange"]
for i in list:
    if i == "mango":
        print("ok")
        break
    

#41.Print only odd numbers from 1 to 10 using continue.
for i in range (1,11):
    if i % 2 == 0:
        continue
    print(i)
        

#42.Write a program that keeps asking for a password until the user types "1234".
password = input("enter password (1234) ")
while password != "1234":
    password = input("enter password (1234) ")
print("ok")

#43.Write a function that prints Hello, World!.

def x ():
    print("Hello World")
x()

#44.Write a function that takes a name and prints "Hello, <name>".
def z(name):
    print(f"Hello {name}")
z("clara")

#45.Write a function that adds two numbers and returns the result.
def addnum( one , two ):
    y = one + two 
    return y
print(addnum(1,1))

#46.Write a function that checks if a number is even or odd.
def number(u):
    if u % 2 == 0:
        print ("even")
    else:
        print("odd")
    return number
number(5)
number(20)



#47.Write a function that takes a list of numbers and prints each one.
def numbers(list_of_numbers):
    for i in list_of_numbers:
        print(i)
list_of_numbers = [1,2,3,4,5]
numbers(list_of_numbers)

#48.Write a function that calculates the square of a number and returns it.
def calculate(square_numbers):
    return square_numbers ** 2

print(calculate(60))

#49.Write a function that takes a number and returns its factorial.

def factorial(fac):
    fact = 1
    for i in range( 1 , fac+1):
        fact *= i

    return fact
print(factorial(5))

#50.Write a function that returns the largest of three numbers.
def numbers(a,b,c):
    return max(a,b,c)
print(numbers(5,4,2))

#51.Write a function that checks if a word is a palindrome (same forward and backward).
def palindrome(word):
    return word == word[::-1]
print(palindrome("hi"))
print(palindrome("yelllley"))


#52.Write a function that returns the sum of all numbers in a list.

def allNum(sum):
    total = 0
    for i in sum:
        total += i
    return total
print(allNum([3,8,8,7,6766]))

#53.Write a function that takes a grade score (0–100) and returns the letter grade (A, B, C, F). 
def score(marks):
    if 100 >= marks >=80:
        return "A"
    elif 79 >= marks >=60:
        return "B"
    elif 59 >= marks >= 40:
        return "C"
    else:
        return "F"
print(score(50))
print(score(30))


#54. Write a function that checks if a given year is a leap year. 
def year(leap):
    return leap % 400 == 0 or (leap % 4 == 0 and leap % 100 != 0)

print(year(2025))


#55. Write a function that checks if someone is eligible to vote (age ≥ 18). 
def vote(age):
    return age >= 18
print(vote(15))
print(vote(50))

#56. Write a function that counts how many vowels are in a string.
def count(vowels):
    count_vowels = 0
    vow_char = "aeiouAEIOU"
    for i in vowels:
        if i in vow_char:
            count_vowels += 1
    return count_vowels 
print(count("nang"))
        

#57.Write a function to reverse a string. 
def rev(str1):
    return str1[::-1]
print (rev("james"))

# 58.Write a function to generate the Fibonacci sequence up to n terms. 

# 59.Write a function that accepts a string and returns it in uppercase and lowercase.
def words(str2):
    return str2.upper() , str2.lower()
print(words("Hello"))


# 60. Write a function that takes a list and returns only the even numbers.
def even(li):
    result = []
    for i in li:
        if i % 2 == 0:
            result.append (i)
    return result

print (even([5,8,7,30]))

# 61. Write a function that calculates the average of numbers in a list.
def cal(li3):
    total = 0
    for i in li3:
        total += i
    return total / len(li3)
    
print(cal([5,6,9,2]))

#62.Create a class Person with attributes name and age.
# Add a method introduce() that prints "My name is <name> and I am <age> years old." Create 2 objects and call the method.
class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"my name is  {self.name}  and i am  {self.age}  years old.")

p1 = Person("nang",20)
p2 = Person("Eaindra",18)

p1.intro()
p2.intro()

#63.Create a class Car with attributes brand and color. 
# Add a method drive() that prints "The <color> <brand> is driving." Create 2 cars and test.
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def drive(self):
        print(f"{self.brand}{ self.color} is driving")

Car1 = Car("Toyota", "red")
Car2 = Car("BMW", "Black")

Car1.drive()
Car2.drive()

#64. Create a class Dog with attributes name and breed. Add a method bark() that prints "<name> is barking!".
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} is barking")
dog1 = Dog("shine","golden")
dog1.bark()

#65.Create a class Rectangle with attributes length and width. Add methods area() and perimeter().
#  Create an object and print its area and perimeter.
class rect:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width

obj1 = rect(50,40)
print ("perimeter is ",obj1.perimeter())
print("area is ", obj1.area())

#66. Create a class Circle with attribute radius. Add a method area() that returns the circle’s area. (Hint: use 3.14 * radius ** 2).
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
circle_area =circle(7)
print ("area ",circle_area.area())

#67. Create a class BankAccount with attributes owner and balance. Add methods deposit(amount) and withdraw(amount).
#  Make sure withdraw cannot go below 0.
class BankAcc:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return f"{self.owner} deposit {amount} .Now new balance is {self.balance}"

    def withdraw(self,amount):

        if self.balance < amount:
            return f"{self.owner} has not enough amount to withdraw.your balance is {self.balance}"
        else:
            self.balance -= amount

            return f"{self.owner} withdraw {amount}.Now new balance is {self.balance}"
     
mybank = BankAcc("may",0)
mybank1 = BankAcc("su",30)
print(mybank.deposit(200))
print(mybank.withdraw(200))

print(mybank1.deposit(200))
print(mybank1.withdraw(600))


#68.Create a class Student with attributes name and a list of grades. Add a method average() that returns the average grade.
'''class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def avrg(self):
        return sum(self.grade) / len(self.grade)
    
st1 = Student("mali", [7.5,1,46,5.5])
print (f" student {st1.name} got the average grade of {st1.avrg()}")     '''

#69.Create a class Book with attributes title and author. 
# Add a method info() that prints "Title: <title>, Author: <author>". Create a list of 3 books and print their info.
class book:
    totalbooks = 0
    def __init__(self,title,author,):
        self.title = title
        self.author = author
        book.totalbooks += 1
        

    def info(self):
        return f"Author: {self.author}, Title: {self.title}"
    
info1 = book("Python basic for beginner","James")
info2 = book("Python basic for beginner","charles")
info3 = book("Python basic for beginner","molly")

print(info1.info())
print(info2.info())
print(info3.info())
print ("total books: ", book.totalbooks)

#70.Create a class Employee with attributes name and salary. Add a method give_raise(amount) that increases the salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount_salary):
        self.salary += amount_salary
        return f"{self.name} has a raise salary amount of {amount_salary} ,new salary balance {self.salary}"
    
emp1 = Employee("ma ma ",300)
print(emp1.give_raise(90))


#71.Create a class Calculator with methods add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
#  Create one object and call all methods.
class calcu:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        return self.a / self.b
method1 =calcu(3,9)
print("add" ,method1.add())
print("subtract" ,method1.subtract())
print("multiply" ,method1.multiply())
print("divide" ,method1.divide())

        
