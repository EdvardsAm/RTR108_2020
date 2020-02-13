Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 8
x is a positive single-digit number.
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 6
x is a positive single-digit number.
>>> 5 == 5
True
>>> 5 == 5
True
>>> 5 == 6
False
>>> type(True)
<class 'bool'>
>>> 17 and True
True
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 2
x is positive
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 0
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 2
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: -2
>>> x = 3
>>> if x < 10:
	print('Small')

	
Small
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 3
x is odd
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 6
x is even
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 3
Traceback (most recent call last):
  File "/home/user/RTR108_2020/condition_V1.py", line 2, in <module>
    if x < y:
NameError: name 'y' is not defined
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number: 3
Please, enter number: 4
x is less than y
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number x: 6
Please, enter number y: 2
x is greater than y
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number x: 5
Please, enter number y: 3
x is greater than y
Please, enter number : 6
x is positive
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter letter : a
Traceback (most recent call last):
  File "/home/user/RTR108_2020/condition_V1.py", line 1, in <module>
    x=int(input('Please, enter letter : '))
ValueError: invalid literal for int() with base 10: 'a'
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter letter : 'a'
Traceback (most recent call last):
  File "/home/user/RTR108_2020/condition_V1.py", line 1, in <module>
    x=int(input('Please, enter letter : '))
ValueError: invalid literal for int() with base 10: "'a'"
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter letter : 2
Traceback (most recent call last):
  File "/home/user/RTR108_2020/condition_V1.py", line 2, in <module>
    if choice == 1:
NameError: name 'choice' is not defined
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter letter : a
Traceback (most recent call last):
  File "/home/user/RTR108_2020/condition_V1.py", line 1, in <module>
    a=int(input('Please, enter letter : '))
ValueError: invalid literal for int() with base 10: 'a'
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter letter : 1
Please, enter letter : 1
Please, enter letter : 2
Traceback (most recent call last):
  File "/home/user/RTR108_2020/condition_V1.py", line 4, in <module>
    if choice == 'a':
NameError: name 'choice' is not defined
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number : 4
Traceback (most recent call last):
  File "/home/user/RTR108_2020/condition_V1.py", line 2, in <module>
    if choice == 'a':
NameError: name 'choice' is not defined
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number x : 3
Please, enter number y : 6
x is less than y
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number x : 3
Please, enter number y : 3
x and y are equal
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Please, enter number x : 4
Please, enter number y : 2
x is greater than y
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Enter Fahrenheit Temperature: 5
-15.0
>>> 
============== RESTART: /home/user/RTR108_2020/condition_V1.py ==============
Enter Fahrenheit Temperature:43
6.111111111111111
>>> x=6
>>> y=2
>>> x >=2 and (x/y) > 2
True
>>> x=1
>>> y=0
>>> x>=2 and(x/y) > 2
False
>>> x=6
>>> y=0
>>> x >= 2 and (x/y) > 2
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x >= 2 and (x/y) > 2
ZeroDivisionError: division by zero
>>> x=1
>>> y=0
>>> x>=2 and y != 0 and (x/y) > 2
False
>>> 
