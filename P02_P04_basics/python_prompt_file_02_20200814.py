fname=input('Enter the file name:')
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith('Received:'):
        count=count+1
print('There were', count,'received lines in',fname)
