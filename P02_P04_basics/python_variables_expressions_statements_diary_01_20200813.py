Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> 
>>> 
>>> hours=35.0
>>> rate=12.50
>>> pay=hours*rate
>>> print(pay)
437.5
>>> 
>>> 
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> 
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> 
>>> yy=440*12
>>> print(yy)
5280
>>> 
>>> zz=yy/1000
>>> print(zz)
5.28
>>> 
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> 
>>> 
>>> print(4**3)
64
>>> 
>>> 
>>> x=1+2**3/4*5
>>> print(x)
11.0
>>> 
>>> 
>>> ddd=1+4
>>> print(ddd)
5
>>> 
>>> eee='hello'+'there'
>>> print(eee)
hellothere
>>> 
>>> eee='hello' + 'there'
>>> type(eee)
<class 'str'>
>>> type(1)
<class 'int'>
>>> 
>>> xx=1
>>> type(xx)
<class 'int'>
>>> temp=98.6
>>> type(temp)
<class 'float'>
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> 
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<class 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<class 'float'>
>>> 
>>> 
>>> print(10/2)
5.0
>>> print(9/2)
4.5
>>> print(99/100)
0.99
>>> print(10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> 
>>> 
>>> sval='123'
>>> type(sval)
<class 'str'>
>>> ival=int(sval)
>>> type(ival)
<class 'int'>
>>> print(ival+1)
124
>>> nsv='hello bob'
>>> niv=int(nsv)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> 
=========== RESTART: /home/side/RTR108_2020/P02_P04_basics/test.py ===========
123
>>> nam=input('Who are you?')
Who are you?
>>> 
>>> nam=input('Who are you?')	print('Welcome',nam)
SyntaxError: invalid syntax
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_userinput_01_20200813.py 
Who are you?Edvards
Welcome Edvards
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_userinput_02_20200813.py 
Europe floor?2
US floor 3
>>> 
>>> #print(4/2)
>>> hours=35
>>> rate=2.75
>>> pay=hours*rate
>>> print(pay)
96.25
>>> 
