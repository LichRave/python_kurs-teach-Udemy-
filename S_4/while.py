# %%
n = 0
while True:
    print(n)
    if n > 10:
        break
    n = n + 1

# %%
while True:
    name = input("Podaj swoje imie: ")
    if len(name) < 3 and name.isalpha():
        print("Podaj poprawne imie, długość min.3!")
        continue
    if len(name) >= 3 and name.isalpha():
        break
print("Cześć, {}!".format(name))


# %%
while True:
    name = input("Podaj swoje imie: ")
    if len(name) >= 3 and name.isalpha():
        break
print("Czesc {}".format(name))

# %%
n = 0

while n < 20:
    n = n + 1
    if n % 2 != 0:
        continue
    print(n)

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
falga = False

idx = 0
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 60

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print("Znaleziono element {}".format(wartosc))


# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 60

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista_do_przeszukania.append(wartosc)


# %%

KOD_PIN = "0000"

pin = input("podaj kod pin: ")

while pin != KOD_PIN:
    pin = input("spróbój jeszcze raz: ")

print("Zalogowany")

# %%

KOD_PIN = "0000"

pin = ""
counter = 0

while pin != KOD_PIN and counter < 3:
    pin = input("Wprowadż kod pin: ")
    if pin == KOD_PIN:
        print("Zalogowany")
        break
    counter + 1
else:
    print("Zbyt dużoprób logowania.")

# %%

KOD_PIN = "0000"

pin = ""
counter = 0

while pin != KOD_PIN and counter < 3:
    pin = input("Wprowadż kod pin: ")
    if pin is KOD_PIN:
        print("Zalogowany")
        break
    counter += 1
else:
    print("Zbyt dużo prób logowania.")

# %% ZADANIA

fuel = 100
fuel_consumption_rate = 10
time = 0

while fuel > 0:
    print(f"Fuel remaining: {fuel} units.")
    fuel -= fuel_consumption_rate
    time += 1

print("End of flight.")

# %%

hour = 8
solar_power = 50
battery_capacity = 500
battery_level = 0

while battery_level < battery_capacity and hour < 15:
    hour += 1
    battery_level += solar_power

print(f"The solar battery charge level is: {battery_level} Watt-hours.")
