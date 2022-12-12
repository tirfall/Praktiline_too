from math import *

print("puu läbimõõdu")
c = float (input("Anna puu ümbermõõdu:"))
d = round (c/pi, 2)
print(f"Puu läbimõõd on: = {d}")


print ("maatüki diagonaal")
N = float(input("Anna N:"))
M = float(input("Anna M:"))
C = round(sqrt(N**2+M**2), 2)
print (f"ristkülikukujulise maatüki diagonaal: = {C}")


aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")


print ("aritmeetilise keskmise")
num1 = int(input("Anna arv number üks:"))
num2 = int(input("Anna arv number kaks:"))
num3 = int(input("Anna arv number kolm:"))
num4 = int(input("Anna arv number neli:"))
num5 = int(input("Anna arv number viis:"))
total = (num1+num2+num3+num4+num5)/5
print (f"aritmeetilise keskmise on: = {total}")


print ("Konn")
print ('   @..@\n  (----)\n ( \__/ )\n ^^ "" ^^')


print("kolmnurga ümbermõõdu")
ak = int(input("Anna a:"))
bk = int(input("Anna b:"))
ck = int(input("Anna c:"))
Umbermood = ak+bk+ck
print (f"Kolmnurga ümbermõõd on: = {Umbermood}")


print("pitsa")
P = int(input("Kui palju sõbrad?"))
Summa = round((12.90*1.1)/P, 2)
print (f"Iga sõbra peab maksma: = {Summa}")


print("Kütusekulu arvutamine")
liiter = float(input("kütuse liitrid:"))
kilomeetr = float(input("läbitud kilomeetrid:"))
kütusekulu = liiter/kilomeetr*100
print(f" kütusekulu 100km kohta keskmiselt: = {kütusekulu}")


print("Rulluisutajad")
minut = float(input("Kui palju minutit?"))
S = 29.9*minut
print (f"Meetrid käinud: = {S}")


print("Ajateisendus")
minutit = int(input("Sisesta aja minutites"))
H=minutit//60 #hour
minutit = minutit%60 #min
print(f"{H}:{minutit}")