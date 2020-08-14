# RTR108_2020
Datormācība
## 1.nodarbība
Sava repozitorija izveide un .md faila formatēšanas paņēmieni.
## 2.-4. nodarbība
Tika pastiprinātas un pildveidotas zināšanas izmantojot python programmēšanas valodu. 
Apgūtas iemaņas sava koda izveidē izmantojot:
###### -izteiksmes, lai veiktu praktiskus darbus, piemēram peļņas aprēķins atkarībā no nostrādātajām stundām:
```
rawstr=input('Ievadi stundas:')
x=int(rawstr)
rawstr2=input('Ievadi likmi:')
y=int(rawstr2)
if x<=40:
    print(x*y)
if x>40:
    print((40*y)+(x-40)*y*1.5)
```
    
###### -funkcijas, lai veidotu jaunas funkcijas vai atgrieztu kādu noteiktu izejas rezultātu
```
def greet(lang):
iflang== 'es':
    return'Hola'
eliflang== 'fr':
    return'Bonjour'
else:
    return'Hello'
```
    
###### -mezglus(loops), lai iegūtu sarakstu ar noteiktām iterācijām.
```
for i in[5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')
```
    
###### -virknes(strings), lai iegūtu informāciju par ieejas argumentiem.
```
fruit= 'banana'
print(len(fruit))
```

###### -failu apstrādi, lai iegūtu informāciju par failiem noteiktā direktorijā.
```
fhand= open('mbox.txt')
count= 0
for line in fhand:
    count=count+1
print('Line Count:',count)
```
