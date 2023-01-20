#Начало строки с En вывод True, если en то False
#09_01_23
starship = "Enterprise"
f=starship.startswith("En")
print(f)

d="Привет"
a=d.startswith('пр')
print(a)

Qw='БуДте здоровы'
w=Qw.startswith('Буд')
print(w)
print(Qw.endswith('вы'))
name = "Picard"
name = name.upper()
print(name.upper())
print(name)
starship = "Enterprise"

k = "Animals".lower()
print(k)
s ="Badger".lower()
print(s)
l ="Honey Bee"
kp="DFFS"
print(l.lower(),kp.lower())
print(k.upper(), s.upper(), l.upper())

string1 = "     Filet Mignon"
string2 = "Brisket    "
stringЗ = "   Cheeseburger  "
print(string1.lstrip(), string2.rstrip(),stringЗ.strip())


string4 = "Becomes"
string5 = "becomes"
string6 = "BEAR"
string7 = " bEautiful"
print(string5.lower().startswith('be'))
print(string4.startswith('be'),string5.startswith('be'),string6.startswith('be'),string7.startswith('be'))
strin = "Becomes".lower()
strin1 = "becomes".lower()
strin2 = "BEAR".lower()
strin3 = " bEautiful".lower()
strq=strin3.lstrip()
print(strin.startswith('be'),strin1.startswith('be'),strin2.startswith('be'),strq.startswith('be'))
