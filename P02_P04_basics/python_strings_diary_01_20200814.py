Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#String data type
>>> str1="Hello"
>>> str2='there'
>>> bob=str1+str2
>>> print(bob)
Hellothere
>>> 
>>> x=int(str3)+1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x=int(str3)+1
NameError: name 'str3' is not defined
>>> str3='123'
>>> x=int(str3)+1
>>> print(x)
124
>>> 
>>> #Reading and converting
>>> name=input('Enter:')
Enter:Chuck
>>> print(name)
Chuck
>>> 
>>> apple=input('Enter:')
Enter:100
>>> x=int(apple)-10
>>> print(x)
90
>>> 
>>> #Looking inside strings
>>> fruit='banana'
>>> letter=fruit[1]
>>> print(letter)
a
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>> 
>>> fruit='banana'
>>> print(len(fruit))
6
>>> 
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_looping_strings_01_20200814.py 
0 b
1 a
2 n
3 a
4 n
5 a
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_looping_strings_02_20200814.py 
b
a
n
a
n
a
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_looping_counting_01_20200814.py 
3
>>> 
>>> #Slicing strings
>>> s='Monthy Python'
>>> print(s[0:4])
Mont
>>> print(s[6:7])
 
>>> print(s[7:8])
P
>>> print(s[7:20])
Python
>>> print(s[:2])
Mo
>>> print(s[8:])
ython
>>> print(s[:])
Monthy Python
>>> 
>>> #String Concatenation
>>> a='Hello'
>>> b=a+'There'
>>> print(b)
HelloThere
>>> c=a+''+'There'
>>> print(c)
HelloThere
>>> 
>>> #In as a logical operator
>>> fruit='banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> is 'a' in fruit:
	
SyntaxError: invalid syntax
>>> if 'a' in fruit:
	print('Found it!')
	a

	
Found it!
'Hello'
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py 
Traceback (most recent call last):
  File "/home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py", line 1, in <module>
    if word == 'banana':
NameError: name 'word' is not defined
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py 
Traceback (most recent call last):
  File "/home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py", line 1, in <module>
    if word == 'banana':
NameError: name 'word' is not defined
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py 
Traceback (most recent call last):
  File "/home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py", line 1, in <module>
    if word == 'banana':
NameError: name 'word' is not defined
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py 
your word,you banana,comes after banana.
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py 
your word,you,comes after banana.
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py 
your word,yourself,comes after banana.
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_string comparison_01_20200814.py 
all right, bananas
all right, bananas
>>> 
>>> 
>>> #String library
>>> greet='Hello Bob'
>>> zap=greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
>>> print('Hi There'.lower())
hi there
>>> 
>>> stuff='Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> #Searching a string
>>> fruit='banana'
>>> pos=fruit.find('na')
>>> print(pos)
2
>>> aa=fruit.find('z')
>>> print(aa)
-1
>>> 
>>> 
>>> #Upper case
>>> greet='Hello Bob'
>>> nnn=greet.uppeer()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    nnn=greet.uppeer()
AttributeError: 'str' object has no attribute 'uppeer'
>>> nnn=greet.upper()
>>> print(nnn)
HELLO BOB
>>> www=greet.lower()
>>> print(www)
hello bob
>>> 
>>> 
>>> #Search and replace
>>> greet='Hello Bob'
>>> nstr=greet.replace('Bob','Jane')
>>> print(nstr)
Hello Jane
>>> nstr=greet.replace('o','X')
>>> print(nstr)
HellX BXb
>>> 
>>> #Stripping whitespace
>>> greet='   Hello Bob  '
>>> greet.lstrip()
'Hello Bob  '
>>> greet.rstrip()
'   Hello Bob'
>>> greet.strip()
'Hello Bob'
>>> 
>>> #Prefixes
>>> line='Please have a nice day'
>>> line.startswith('Please')
True
>>> line.startswith('p')
False
>>> 
>>> #Parsing and Extracting
>>> data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos=data.find('@')
>>> print(atpos)
21
>>> sppos=data.find('',atpos)
>>> print(sppos)
21
>>> host=data[atpos+1:sppos]
>>> 
>>> sppos= data.find(' ',atpos)
>>> print(sppos)
31
>>> host= data[atpos+1: sppos]
>>> print(host)
uct.ac.za
>>> 
