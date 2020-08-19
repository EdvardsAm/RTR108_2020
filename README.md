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
## 5.nodarbība
## 6.nodarbība
Apgūtas iemaņas sava koda izveidē izmantojot objektus(objects) pitona vidē, lai pievienotu objektiem papildus vērtības, aprakstus, iedalījumu.
```
class PartyAnimal:
    x=0

    def __init__(self,z):
        self.name=z
        print(self.name,"constructed")

    def party(self):
        self.x=self.x+1
        print(self.name,"party count",self.x)

s=PartyAnimal("Sally")
j=PartyAnimal("Jim")

s.party()
j.party()
s.party()
```
## 7.nodarība
## 9.nodarbība
Tika iegūtas zināšanas par to kā veidot shēmas izmantojot gschem un kā tās simulēt ngspice vidē lai iegūtu nepieciešamos rezultātus.
## 10.-11.nodarbība
Izmantojot LaTeX vidi, tika apgūti vairāki failu formatēšanas paņēmieni:
- vienādojumu izveide
- bilžu ievietošana, apstrāde
- tabulu izveide, apstrāde
- sarakstu izveide 
- teksta apstrāde
## 12.nodarbība
## 13.nodarbība
Tika atrisināti vingrinājumi un uzdevumi, un iegūtas pamata zināšanas lietojot JavaScript programmēšanas valodu.
