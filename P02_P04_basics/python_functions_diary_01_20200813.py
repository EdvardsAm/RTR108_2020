Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Max function
>>> big=max('Hello world')
>>> print(big)
w
>>> 
>>> #Type Conversions
>>> print(float(99)/100)
0.99
>>> i=42
>>> type(i)
<class 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<class 'float'>
>>> print(1+2*float(3)/4-5)
-2.5
>>> 
>>> #String conversions
>>> sval='123'
>>> type(sval)
<class 'str'>
>>> print(sval+1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(sval+1)
TypeError: must be str, not int
>>> ival=int(sval)
>>> type(ival)
<class 'int'>
>>> print(ival+1)
124
>>> 
>>> #Building functions
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_building_functions_01_20200813.py 
>>> print_lyrics():
	
SyntaxError: invalid syntax
>>> print_lyrics()
Im a lumberjack, and Im okay.
I sleep all night and I work all day.
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_building_functions_02_20200813.py 
Hello
Yo
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
7
>>>
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_parameters_01_20200813.py 
>>> greet('es')
Hola
>>> 
>>> def greet():
	return "Hello"

>>> print(greet(), "Glenn")
Hello Glenn
>>> 
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_return_value_01_20200813.py 
>>> print(greet('es'),'Sally')
Hola Sally
>>> 
>>> #Multiple parameters
>>> x=addtwo(3, 5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x=addtwo(3, 5)
NameError: name 'addtwo' is not defined
>>> def addtwo(a, b):
	added=a +b
	return added

>>> x=addtwo(3, 5)
>>> print(x)
8
>>> 
>>> 
