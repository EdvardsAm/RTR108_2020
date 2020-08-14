rawstr=input('Enter hours:')
x=int(rawstr)
rawstr2=input('Enter rate:')
y=int(rawstr2)
if x<=40:
    print(x*y)
if x>40:
    print((40*y)+(x-40)*y*1.5)

