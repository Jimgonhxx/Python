'''
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
'''

#1
'''
def tabliczka_mnożenia (liczba):
    for i in range(1, 11):
        print(f"{liczba} x {i} = {liczba * i}")
        print()

#2

def read_shoppign():
    while True:
        produkt = input("dodaj produkt, zaczończenie to enter pusty")
        if produkt == "":
            break
        zakupy = []
        zakupy.append(produkt)
    print("twoja lista zakupów", zakupy)


    #3

    def calc(a, b):
        if b != 0: 
            print("suma", a + b)
            print("różnica", a - b)
            print("iloczyn", a * b)
            print("iloraz", a / b)


#4

def kmh_to_mph (kmh):
    mph = kmh / 1.61
    kmh = int(input("Podaj prędkość  w km/h"))
    print("f {kmh} km/h to około {mph.round(2)} mph")


#5 try/expect

def is_divisible(a, b):
    b = int(input("Podaj liczbe"))
    if b == 0 : ValueError("Nie dzielimy przez zero")
    if b % 2:
        print("Liczba jest podzielna")
    else :
        print("Liczba nie jest podzielna")

'''
'''
            #6  
    def guess_game(max_tries=5):
        import random
        liczba = random.randint(1, 10)
        proby = 0
        while proby < max_tries:
            guess = int(input("Podaj liczbe: "))
            if guess == liczba:
                print("Brawo zgadłeś")
                break
            else:
                print("Nie udało się")
                proby += 1
        else:
            print(f"Przegrałeś! Prawidłowa liczba to {liczba}")

                


    #7
def sum_loop(nums):
        suma = 0;
        Licznik =[];
    for i in range(1,6):
        Licznik = int(input("Podaj swoje liczby: "))
        suma = +1;
        print(f"Suma wynosi {suma}")


       



        



# 8
def znajdz_max():
    lista = []
    n = int(input("Ile liczb chcesz podać? "))
    if n <= 0:
        print("Zero się nie liczy")
        return
    for i in range(n):
        liczba = int(input(f"Podaj liczbę {i+1}: "))
        lista.append(liczba)
    najwieksza_liczba = max(lista)
    print(f"Największa liczba to: {najwieksza_liczba}")



    






def kalkulator_z_bledami():
    try:
        
        liczba1_str = input("Podaj pierwszą liczbę: ")
        liczba1 = float(liczba1_str) # Konwersja na liczbę zmiennoprzecinkową

        
        operator = input("Podaj operator (+, -, *, /): ")

       
        liczba2_str = input("Podaj drugą liczbę: ")
        liczba2 = float(liczba2_str) 

        if operator == '+':
            wynik = liczba1 + liczba2
        elif operator == '-':
            wynik = liczba1 - liczba2
        elif operator == '*':
            wynik = liczba1 * liczba2
        elif operator == '/':
            if liczba2 == 0:
               
                print("Błąd: Nie można dzielić przez zero!")
                return 
            else:
                wynik = liczba1 / liczba2
        else:
            
            print("Błąd: Nieznany operator.")
            return 

        
        print(f"Wynik: {wynik}")

    except ValueError:
        
        print("Błąd: Wprowadzono nieprawidłową wartość liczbową.")
    





'''