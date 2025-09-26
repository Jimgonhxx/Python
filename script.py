
print("Tabliczka mnożenia")
liczba = int(input("Podaj liczbę: "))
for i in range(1, 11):
    print(f"{liczba} x {i} = {liczba * i}")
print()


print("Lista zakupów")
zakupy = []
while True:
    produkt = input("Dodaj produkt (Enter = koniec): ")
    if produkt == "":
        break
    zakupy.append(produkt)
print("Twoja lista zakupów:", zakupy)
print()


print("Suma, różnica, iloczyn, iloraz")
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
print("Suma:", a + b)
print("Różnica:", a - b)
print("Iloczyn:", a * b)
if b != 0:
    print("Iloraz:", a / b)
else:
    print("Zero nie jest podzielne")

print()

print("km/h - mph")
kmh = float(input("Podaj prędkość w km/h: "))
mph = kmh / 1.61
print(f"{kmh} km/h to około {mph:.2f} mph")
print()


print("Czy liczba jest podzielna?")
liczba = int(input("Podaj liczbę dzieloną: "))
dzielnik = int(input("Podaj dzielnik: "))
if liczba % dzielnik == 0:
    print(f"{liczba} jest podzielna przez {dzielnik}")
else:
    print(f"{liczba} nie jest podzielna przez {dzielnik}")
print()


import random
print(" Zgadnij liczbę 1-10 (5 prób :P)")
tajna = random.randint(1, 10)
proby = 5



for i in range(proby):
    strzal = int(input(f"Próba {i+1}/{proby}. Podaj liczbę: "))
    if strzal == tajna:
        print(" Zgadłeś!")
        break
    elif strzal < tajna:
        print("Nuh uh za niska!")
    else:
        print("Nuh uh za wysoka!")
else:
    print(f"game over {tajna}.")
print()
print()