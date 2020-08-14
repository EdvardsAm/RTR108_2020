Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Opening a file
>>> fhand=open('mbox.txt','r')
>>> fhand=open('mbox.txt')
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
>>> 
>>> #The newline character
>>> stuff='Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff='X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> 
>>> #Counting lines in a file
>>> fhand=open('mbox.txt')
>>> count=0
>>> for line in fhand:
	count=count+1
print('Line Count:',count)
SyntaxError: invalid syntax
>>> 	print('Line Count:',count)
SyntaxError: unexpected indent
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_counting_lines_01_20200814.py 
Line Count: 1911
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_counting_lines_01_20200814.py 
Line Count: 48
>>> 
>>> #Reading the whole file
>>> fhand=open('mbox.txt')
>>> inp=fhand.read()
>>> print(len(inp))
2450
>>> print(inp[:20])
From stephen.marquar
>>> 
>>> #Searching trough a file
>>> fhand=open('mbox.txt')
>>> for line in fhand:
	line=line.rstrip()
	if line.startswith('From:'):
		print(line)

		
From: stephen.marquard@uct.ac.za
>>> 
>>> #Using in to select lines
>>> fhand=open('mbox.txt')
>>> for line in fhand:
	line=line.rstrip()
	if not '@uct.ac.za' in line:
		continue
	print(line)

	
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
>>> 
>>> #Prompt for file name
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_prompt_file_01_20200814.py 
Enter the file name:mbox.txt
There were 1 subject lines in mbox.txt
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_prompt_file_02_20200814.py 
Enter the file name:mbox.txt
There were 9 subject lines in mbox.txt
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_prompt_file_02_20200814.py 
Enter the file name:mbox.txt
There were 9 received lines in mbox.txt
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_bad_file_01_20200814.py 
Enter the file name:mbox.txt
There were 9 received lines in mbox.txt
>>> 
 RESTART: /home/side/RTR108_2020/P02_P04_basics/python_bad_file_01_20200814.py 
Enter the file name:fails2
File cannot be opened: fails2
>>> 
