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

#16.


