#%% Wyjatki
a = 3
    b = [1, 0, 2]
    for elem in b:
        wynik = a / elem
        print(f"Wynik to: {wynik}")

#%% AssertionError, który wystąpi, gdy warunek podany po słowie kluczowym assert będzie fałszywy:
a = 2
b = 1
assert a == b

#%% AttributeError, który wystąpi, gdy spróbujemy odwołać się do atrybutu lub metody obiektu, które dla niego nie istnieją:
x = 10
x.append(8)\

#%% FileNotFoundError, który sygnalizuje błąd operacji wejścia/wyjścia i pojawi się w sytuacji próby dostępu do pliku, który nie istnieje:
f = open("plik_tekstowy.txt")
print(f.read())

#%% IndexError, który wystąpi przy próbie dostępu do elementu listy po indeksie, który nie istnieje:
lst = [1, 2, 3, 4]
print(lst[6])

#%% ImportError, który pojawi się, gdy wystąpi błąd z importowaniem modułu, np. gdy spróbujemy zaimportować nieistniejącą funkcję z modułu:
from utils import calculate_diff

#%% ModuleNotFound, który pojawi się, gdy spróbujemy zaimportować niezainstalowany moduł:
import sklearn

#%% KeyError, który wystąpi przy próbie dostępu do elementu słownika po kluczu, który nie istnieje:
people = {
"Adam": 109,
"Monika": 230,
"Grzegorz": 1551
}

print(people["Monika"])
print(people["Beata"])

#%% NameError, który pojawi się, gdy spróbujemy użyć zmiennej, która nie została zainicjalizowana:
a = 10
c = a + b
print(c)

#%% ValueError, który wystąpi np. gdy do funkcji przekażemy argument niewłaściwego typu:
a = "Ala ma kota"
b = int(a)
print(a, b)

#%% ZeroDivisionError, który, jak już widzieliśmy, zostanie rzucony w przypadku próby dzielenia przez zero.

#%% Obsługa wyjątków
# Słowami kluczowymi związanymi z obsługą wyjątków są: try, except, finally, raise.

#%%
class MyError(Exception):
    pass

if __name__ == '__main__':
    a = 5
    b = 0
    try:
        if b == 0:
            raise MyError('b nie może być zerem!')

        result = a / b
        print(f'result {result}')
    except MyError:
        print('Nie dziel przez zero!')
    finally:
        print('FINALLY')

print('KONIEC')

#%% 
if __name__ == "main":
    a = 5
    b = 0
    try:
        result = a / b
        print(f"result{result}")
    except ValueError:
        print("nie dziel pprzez zero!")
    finally:
        print("FINALLY")

print("Koniec")

#%% Klasa ze wszystkimi blendami

class MyError(Exception):
    pass 