# 30DAYSOFPYTHON

This is an open-source project guide for learning Python Programming Language .

Fork it and create separate branches/folders for each day. 

## Topics Breakdown

### Day 1: Python Basics
Start by installing Python and a text editor. Learn the basics of Python, such as: 
 variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

#### Exercise
Advanced Calculator Program: Simple Calculator
Create a simple calculator program that performs basic arithmetic operations based on user input.
Display a menu with the following options:
a. Addition (+)
b. Subtraction (-)
c. Multiplication (*)
d. Division (/)
e. Exit
Prompt the user to choose an option by entering the corresponding letter (a, b, c, d, or e).
If the user chooses an arithmetic operation (a, b, c, or d), prompt the user to enter two numbers.
Perform the selected arithmetic operation on the entered numbers and display the result.
If the user chooses "Exit" (e), end the program.
If the user enters an invalid option, display an error message and return to the menu.
Repeat steps 2-6 until the user chooses to exit.


### Day 2: Python Control Flow - IF Statements, Logical and Comparator Operations

Learn how to use control flow statements like if-else statements, Switch-Case Statement,Logical Operators (and, OR), Boolean operators and comparisonooperations such as <, >, !==, ==, etc

#### Exercise

You are building a program to help a user decide what to wear based on the current weather conditions. Write a Python program that prompts the user to enter the current temperature in Fahrenheit and whether it is currently raining or not (as a boolean value), and then suggests an appropriate outfit based on the following criteria:

If the temperature is less than 50 degrees Fahrenheit, suggest wearing a coat, hat, scarf, and gloves. If the temperature is between 50 and 70 degrees Fahrenheit and it is not raining, suggest wearing a sweater or light jacket. If the temperature is between 50 and 70 degrees Fahrenheit and it is raining, suggest wearing a rain jacket and boots. If the temperature is above 70 degrees Fahrenheit and it is not raining, suggest wearing a t-shirt and shorts. If the temperature is above 70 degrees Fahrenheit and it is raining, suggest wearing a light jacket and rain boots.

### Day 3: Loops and Iteration in Python 

Understand how to apply Loops and iteration in python programs. *** While loops:With boolean values, do-while loop too *** For Loops: Using Indexing,using range(), Using items, looping over sequential data (sets, dictionaries, lists, tuples) *** For-Else statements *** Break and Continue Statements

Exercise
Fibonacci: Write a program that prompts the user to enter a positive integer n, and then prints the first n Fibonacci numbers. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.


### Day 4: Functions In Python 

Understand the concept of functions in Python. A function is a block of organized code that is used to perform a single task. They provide better modularity for your application and reuse-ability. A function can take arguments and return values:

Exercise:

1.write a function in python that takes a list of numbers and returns the sum of the given numbers. 

2. write a function in python that takes a list of numbers and returns the second-largest item in the list of the given numbers. 

 3. write a function in python that takes 3 parameters: name, age, and occupation and prints this sentence as output: "My name is {name}, I am {age} years old and I work as a {occupation}". 

### Day 5: Strings and String Manipulations 

Understand how to create strings in python, how to format and how to manipulate. https://www.programiz.com/python-programming/methods/string https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings https://www.pythoncheatsheet.org/cheatsheet/string-formatting

Exercise:
1. Write a Python program to count the number of characters    (character frequency) in a string. Sample String : google.com' Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Sample String : 'w3resource' Expected Result : 'w3ce' Sample String : 'w3' Expected Result : 'w3w3' Sample String : ' w' Expected Result : Empty String

3. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'

### Day 6: LISTS in Python

Understand LISTS and how to manipulate lists in python. Understand CRUD Operations in Lists using Python. https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples https://www.programiz.com/python-programming/list

Exercise
1. Write a Python program to remove duplicates from a list.

2. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

3. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False. Sample Data: ([0, 3, 4, 7, 9]) -> False ([3, 5, 7, 13]) -> True ([1, 5, 3]) -> False


### Day 7: Dictionaries in Python 


Understand the concept of dictionaries in Python Understand CRUD Operations and manipulation of dictionaries

https://www.programiz.com/python-programming/dictionary https://www.pythoncheatsheet.org/cheatsheet/dictionaries

Exercise:
1. Write a Python program to combine two dictionary by adding values for common keys. d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400} Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

2. Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string. Sample string : 'w3resource' Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

3. Write a Python program to sort Counter by value. Sample data : {'Math':81, 'Physics':83, 'Chemistry':87} Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]


### Day 8: Sets 

Understand what Sets are,& how they work in Python https://www.programiz.com/python-programming/set

Exercises
1. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

2. Write a Python program to return a new set with unique items from both sets by removing duplicates. Given: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} Expected output: {70, 40, 10, 50, 20, 60, 30}

3. Update the first set with items that don’t exist in the second set Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set. Given: set1 = {10, 20, 30} set2 = {20, 40, 50} Expected output: set1 {10, 30}


### Day 9: Tuples 

Understand Tuples and working with Tuples in Python

https://www.programiz.com/python-programming/tuple https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples

Exercise
1. Write a Python program to check whether an element exists within a tuple.
2. Write a Python program to convert a list to a tuple.
3. Attempt this Quiz on Tuples in [Python] (https://pynative.com/python-tuple-quiz/)


### Day 10: Regular Expressions

Understand the basics of Regex and how to apply it in Python Study via: https://www.pythoncheatsheet.org/cheatsheet/regular-expressions https://www.edureka.co/blog/python-regex/ https://programmingwithmosh.com/interviews/interview-questions-in-python-regular-expressions/

Exercise
Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels from the trolls’ comments, neutralizing the threat. Your task is to write a function that takes a string argument and returns a new string with all vowels removed. For example, the string “Hello World!” would become “Hll Wrld”. Note: For this problem, ‘y’ is NOT considered a vowel.

Write a Python program to match if two words from a list of words start with the letter 'P'.

Write a Python program to remove the parenthesis area in a string. Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"] Expected Output: example w3resource github stackoverflow


### Day 11: Object-Oriented Python 
Understand the concept of OOP in Python, covering Classes, Instance Methods, Objects https://www.programiz.com/python-programming/object-oriented-programming

Exercise
Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details. Sample Employee Data: "ADAMS", "E7876", 50000, "ACCOUNTING" "JONES", "E7499", 45000, "RESEARCH" "MARTIN", "E7900", 50000, "SALES" "SMITH", "E7698", 55000, "OPERATIONS" Use 'assign_department' method to change the department of an employee. Use 'print_employee_details' method to print the details of an employee. Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula: overtime = hours_worked - 50 Overtime amount = (overtime * (salary / 50))
Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format


### Day 12: OOP Concepts in Python: Inheritance, Polymorphism, Encapsulation and Abstraction

Advanced OOP in Python https://www.programiz.com/python-programming/inheritance

Exercise
1.Inheritance: Create a class called Animal with a method speak() that prints "The animal makes a sound." Create two subclasses, Dog and Cat, which inherit from the Animal class. Override the speak() method in each subclass to print "The dog barks" and "The cat meows" respectively. Create instances of both subclasses and call their speak() methods.

#Polymorphism : Create a class called Shape with an abstract method area(). Implement two subclasses, Circle and Rectangle, which inherit from the Shape class. Override the area() method in each subclass to calculate and return the area of a circle and rectangle respectively. Create instances of both subclasses and call their area() methods.
Encapsulation: Create a class called BankAccount with private attributes account_number and balance. Implement public methods to access and modify these attributes. Use encapsulation to protect the data from direct access outside the class. Create an instance of the BankAccount class and demonstrate how to access and modify the account number and balance using the public methods.


### Day 13: Working with JSON (Reading and Writing)


Understand how to navigate the directory and acess files How to READ, WRITE and manipulate Files --- Excel files, csv files, text files

Exercise
Create a new file named "output.txt" and write the sentence "Hello, world!" to it using Python.
Given a file named "numbers.txt" containing a list of integers separated by spaces, write a Python function to read the file and return the sum of all the numbers.
3.Write a Python program that reads a CSV file named "students.csv" with columns "Name" and "Age". Create a new file named "young_students.txt" and write the names of all students who are below 18 years old to this file.


### Day 14: Debugging,Error and Exception Handling 




### Day 15: Working with APIs 



### Day 16: Working with SQL Databases and Python 


















