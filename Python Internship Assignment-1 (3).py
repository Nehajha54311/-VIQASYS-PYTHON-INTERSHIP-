#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 
# In the below elements, identify which of them are values or expressions. Values can be integers or strings, while expressions will be mathematical operators or combinations thereof.
# 'hello', 
# -87., ), o, lu, alu, ssion)'(Value))str" (Value)

# ___
# 
# <a href='https://viqasys.com/wp-content/uploads/2021/07/ns1.png'><img src='https://viqasys.com/wp-content/uploads/2021/07/ns1.png'/></a>
# ___
# <center><em>Content Copyright VIQASYS INNOVATIONS PVT LTD.</em></center>
# 
# # Assignment 1

# In[ ]:


ANSWER

'hello' - Value (String)

-87. - Value (Floating-point Number)

) - Expression (Closing Parenthesis)

o - Value (Variable or Identifier)

lu - Value (Variable or Identifier)

alu - Value (Variable or Identifier)

ssion) - Value (String)

' - Expression (Opening Quotation Mark)

(Value) - Expression (Grouping)

str - Value (Variable or Identifier)

" - Expression (Closing Quotation Mark)


# ## Question 2
# 
# Explain the difference between a string and a variable.
# 

# 

# In[ ]:


## Answer


String:

A string is a data type used to represent textual data, such as words, sentences, or even entire documents.
It is essentially a sequence of characters enclosed within quotation marks (either single or double) in most programming languages.
Example: "Hello, World!" or 'This is a string'.
Strings can be manipulated, searched, and modified in various ways depending on the programming language.

Variable:

A variable is a symbolic name that represents a value stored in the computer's memory.
It serves as a placeholder for data that can change during the execution of a program.
Variables can store different types of data, including strings, numbers, and more complex data structures.
Unlike strings, which specifically represent textual data, variables can hold various types of data depending on how they are declared and defined.
Example: message = "Hello, World!" Here, message is the variable name, and "Hello, World!" is the string value assigned to it.
Variables are used to store and manipulate data in a program, making it dynamic and adaptable to different situations.


# ## Question 3
# Describe three different data types commonly used in programming

# In[ ]:


Integer (int):

Integers represent whole numbers without any fractional part. They can be positive, negative, or zero.
Integers are commonly used for counting and indexing operations, as well as for representing numerical quantities that don't require decimal precision.

Example: 42, -10, 0.
Operations on integers typically include arithmetic operations such as addition, subtraction, multiplication, and division.

String (str):

Strings represent sequences of characters, typically used to store textual data such as words, sentences, or even entire documents.
Strings are enclosed within quotation marks (either single or double) in most programming languages.

Example: "Hello, World!", 'Python is awesome'.
Operations on strings include concatenation (joining two strings together), slicing (extracting a portion of the string), and searching for substrings.

Floating-point Number (float):

Floating-point numbers represent real numbers with fractional parts. They are used when numerical data requires decimal precision.
Floats are often used for mathematical calculations involving numbers with fractional components.
Example: 3.14, -0.001, 2.71828.

Operations on floating-point numbers include arithmetic operations (addition, subtraction, multiplication, division) as well as more complex mathematical functions like trigonometric functions and exponentiation.


# ## Question 4
# What is an expression made up of? What is the general purpose of expressions?
# 

# In[ ]:


An expression in programming is made up of one or more operands and operators, combined in a manner that represents a computation or a value. Here's what constitutes an expression:


Operands: These are the values or variables involved in the expression. Operands can be literals (like numbers or strings) or variables (representing values stored in memory).

Operators: These are symbols that represent specific computations to be performed on the operands. Operators define the relationship and actions between the operands.

Expressions can also contain other elements such as parentheses for grouping, function calls, and method invocations.

EXAPMLE:
20+45-20, (20*4)/2 etc.

The general purpose of expressions in programming is to perform computations, manipulate data, and evaluate to a value. Expressions are integral to nearly every aspect of programming, from simple arithmetic calculations to complex logical operations and function evaluations.


# ## Question 5
# 
# Explain the difference between an expression and a statement, using examples if necessary.

# In[ ]:


In programming, expressions and statements are both fundamental concepts, but they serve different purposes:

Expression:

An expression is a combination of operands (values or variables) and operators that evaluates to a single value.
Expressions can be simple, like 2 + 3, or more complex, involving function calls, method invocations, or conditional expressions.
They can be used anywhere in a program where a value is expected, such as assigning a value to a variable, passing arguments to a function, or defining conditions in control structures.

Examples of expressions:

2 + 3 (evaluates to 5)

x * y (evaluates to the product of variables x and y)

len("Hello") (evaluates to the length of the string "Hello")

Statement:

A statement is a complete line of code that performs an action, such as declaring a variable, assigning a value, calling a function, or controlling the flow of execution.
Unlike expressions, statements do not necessarily produce a value.
Statements are typically terminated by a semicolon (;) in languages like C, C++, Java, and JavaScript, while in languages like Python, statements are often terminated by newlines.

Examples of statements:
Variable declaration: int x;

Assignment statement: x = 5;

Conditional statement: if (x > 0) { ... }

Loop statement: for (int i = 0; i < 10; i++) { ... }

Difference:

The key difference between expressions and statements is that expressions always produce a value, while statements may or may not produce a value but perform an action.
Expressions are often used within statements, for example, the expression x * y can be used in an assignment statement like result = x * y.


# ## Question 6
# After running the following code, what does the variable "bacon" contain?
# 
# bacon = 22 <br>
# 
# bacon + 1

# In[ ]:


## Answer

bacon = 22: This line assigns the value 22 to the variable bacon.

bacon + 1: This expression evaluates to 22 + 1, which equals 23.

So, after running the code, the variable bacon still contains the original value, 22. However, the expression bacon + 1 evaluates to 23, but this value isn't assigned back to bacon, so bacon remains 22


# ## Question 7
# Determine the values of the following two terms:<br>
# 'spam' + 'spamspam'<br>
# 'spam' * 3
# 
# 

# In[2]:


'spam' + 'spamspam'
'spam' * 3


# ## Question 8
# 
# Why is "eggs" a valid variable name while "100" is invalid?

# In[ ]:


## Answer

In most programming languages, including Python, variable names must adhere to certain rules. Here's why "eggs" is a valid variable name while "100" is invalid:

Starting Character:

Variable names typically cannot start with a number.

"eggs" starts with a letter, which is allowed.

"100" starts with a number, which is generally not allowed.

Characters Allowed:

Variable names can contain letters (both uppercase and lowercase), digits (but not as the starting character), and underscores.

"eggs" contains only letters, which are valid characters for variable names.

"100" contains only digits, which are not allowed as the starting character for variable names.


# ## Question 9
# 
# List three functions that can be used to obtain the integer, floating-point number, or string version of a value.

# In[ ]:


# Answer

In Python, there are several functions that can be used to obtain the integer, floating-point number, or string version of a value. Here are three commonly used functions for each purpose:

Integer Conversion:

int(): This function converts a value to an integer. If the value is a string, it can represent an integer, such as "10", "42", etc. If the value is a floating-point number, it truncates the decimal part.

value = 10.5

integer_value = int(value)

print(integer_value)  # Output: 10


Floating-Point Number Conversion:

float(): This function converts a value to a floating-point number. It can convert integer values or strings representing floating-point numbers.

value = "3.14"

float_value = float(value)

print(float_value)  # Output: 3.14


String Conversion:

str(): This function converts a value to a string. It can convert integers, floating-point numbers, or other data types to their string representations.

value = 42

string_value = str(value)

print(string_value)  # Output: "42"


# ## Question 10 
# Explain why the following expression causes an error and suggest how to fix it:<br>
# 'I have eaten ' + 99 + ' burritos.'
# 
# 

# In[ ]:


# Answer

The error in the expression 'I have eaten ' + 99 + ' burritos.' occurs because we're trying to concatenate a string ('I have eaten ') with an integer (99) without converting the integer to a string first. In Python, you can only concatenate strings with other strings, not with integers or other data types.

To fix this error, you need to ensure that all parts being concatenated are of the same data type (strings). 

Here's how you can fix it:

'I have eaten ' + str(99) + ' burritos.'

In this corrected expression, str(99) converts the integer 99 to its string representation, allowing it to be concatenated with the other strings. Now, the expression will result in the string 'I have eaten 99 burritos.


# ## Question 11
# Write a Python program to calculate the sum of two numbers and print the result.
# gative, or zero.

# In[3]:


num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
result = num1+num2
print("sum of two number is :", result) 


# ## Question 12
# Create a Python program that takes the user's name as input and prints a greeting message.
# 
# 

# In[4]:


name = input("Enter your name")
greet="welcome to the program"
print("Hello" ,name +" " + greet)


# ## Question 13
# Write a Python program to calculate the area of a rectangle given its length and width. (Assume length and width are provided as inputs.)
# 
# 

# In[5]:


length=float(input("Enter the length"))
width =float(input("Enter the width"))
area_rectangle =length*width
print("Area of rectangle is :",area_rectangle)


# ## Question 14
# Create a Python program that asks the user for their age and prints out a message saying whether they are a child, teenager, or adult based on their age.
# 
# 

# In[6]:


age =int(input("Enter your age"))
if age<13 :
     print(" you are a child")
elif age<20 :
     print("you are teenager")
else :
     print("you are adult")          
     # if age =20 the it print "you are adult"


# ## Question 15
# Write a Python program to convert temperature from Celsius to Fahrenheit. (Assume Celsius temperature is provided as input.)
# 
# 

# In[7]:


celcius = float(input("Enter temperature in celcius"))
fahrenheit =   (1.8*celcius) + 32
print("Temperature in fahrenheit is :", fahrenheit)   

# if celcius =5 then it prints 41 in fahrenheit


# ## Question 16
# Create a Python program that takes the radius of a circle as input and calculates its area. (Assume the value of pi is 3.14.)
# 
# 

# In[8]:


rad = int(input(" Enter radius"))
area = 3.14*rad*rad
print("Area of cicle is :", area)

# if radius is 5 the area of circle is 78.5


# ## Question 17
# Write a Python program to find the maximum of two numbers entered by the user.
# 
# 

# In[9]:


n1 = int(input("Enter the first number"))
n2 = int(input("Enter second number"))
if n1 > n2 :
    print( n1 ,"is max number")   
else:
    print(n2 , " is max number")    


# ## Question 18
# Create a Python program that asks the user to enter two numbers and prints out their product.
# 
# 

# In[10]:


num1= int(input("Enter first number"))
num2= int(input(" Enter second number"))
product = num1*num2
print("product of two number is : ", product)
# if num 1 is 20 and num2 is 30 then product is 600


# ## Question 19
# Write a Python program that prompts the user to enter a number and then prints whether the number is positive, negative, or zero.

# In[11]:


num= int(input("Enter first number"))
if num <0 :
    print(" Number is negative")
elif num >0:
    print( " Number is positive")
else :
    print(" Number is zero")    


# In[ ]:




