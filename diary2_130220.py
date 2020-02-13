Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(32)
<class 'int'>
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>> len('Hello world')
11
>>> int('32')
32
>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159')
3.14159
>>> str(32)
'32'
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> decibels = 10 * math.log10(ratio)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    decibels = 10 * math.log10(ratio)
NameError: name 'ratio' is not defined
>>> 
>>> degrees = 45
>>> 3
3
>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.7071067811865475
>>> radians = 0.7
>>> height = math.sin(radians)
>>> 
>>> 
>>> 
>>> d
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> math.sqrt(2)/2.0
0.7071067811865476
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
0.5238569854614251
0.9686256492029673
0.33171727693048536
0.9278576242320434
0.6972120222999599
0.8951148473111246
0.07157404078805674
0.1470406636507392
0.28922965479211205
0.46999904566183914
>>> random.randint(5, 10)
6
>>> t= [1, 2, 3]
>>> random.choice(t)
2
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
>>> f
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
>>> print_lyrics
<function print_lyrics at 0x7f25d6a85048>
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def repeat_lyrics()
SyntaxError: invalid syntax
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
>>> 
>>> print_twice(bruce)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print_twice(bruce)
NameError: name 'print_twice' is not defined
>>> print_twice(bruce):
	
SyntaxError: invalid syntax
>>> print_twice('Spam')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print_twice('Spam')
NameError: name 'print_twice' is not defined
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(17)
17
17
>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
>>> print_twice('Spam'*4))
SyntaxError: invalid syntax
>>> print_twice('Spam '*4)
Spam Spam Spam Spam 
Spam Spam Spam Spam 
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
Traceback (most recent call last):
  File "/home/user/RTR108_2020/functions.py", line 1, in <module>
    x = math.cos(radians)
NameError: name 'math' is not defined
>>> math.sqrt(5)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    math.sqrt(5)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(5)
2.23606797749979
>>> result = print_twice('Bing')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    result = print_twice('Bing')
NameError: name 'print_twice' is not defined
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
>>> 
================ RESTART: /home/user/RTR108_2020/functions.py ================
8
>>> 
