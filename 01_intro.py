# -*- coding: utf-8 -*-
# %%
commit_name = "training from scratch, day _ (dd.mm.rr)"
print(commit_name)

# %%
print(5 + 5)

# %%
print(5 * 5)

# %%
print(10 / 3)
print(4 / 2)

# %%
print(4 // 9)
# %%
print(1 % 8)
# %%
a = 10
b = 20
c = "xa"
d = a * c
# %%
print("love python")


# %%
print("C:\path\to\something\new")
print("C:\path\\to\something\\new")
print(r"C:\path\to\something\new")

# %%
# Import biblio
import os

# %%
print(
    """Instrukcja uruchamiana pliku przykład.py
      
      --file [nazwa pliku]
         zapisuje output do piku
      --quiet
         wycisza logi w konsoli
      
Koniec."""
)

# %%
text = "I love Python. "
print("Py" "thon")

# %%

url = "https://www.udemy.com/course/programowanie-w-jezyku-python/learn/lecture/15714542#questions"
url_2 = (
    "https://www.udemy.com/course/programowanie-w-jezyku-python/learn/"
    "lecture/15714542#questions"
)

# %%
name = "python"
print(name + " 3.7")
print(name, "3.7")

# %%
age = 27
imie = "Artem"
print(imie + " " + str(age))
print(imie, age)
print("{} ma {} lat.".format(imie, age))
# index
print("{0} ma {1} lat.".format(imie, age))
print("{1} ma {0} lat.".format(imie, age))

# %%

# Utworzenie zmiennej o nazwie name
name = "Python"
# Wydrukowanie 'Czesć, Python' do konsoli
# v1 Moja
print("Cześć,", name)
# v2
print("Cześć, {}".format(name))
# v3
print(f"Cześć, {name}")

# %%
# Podane są poniższe zmienne:

name = "John"
age = 25
height = 180.5

# Wykorzystując funkcję print() oraz podane zmienne wydrukuj poniższy tekst do konsoli.
# My name is John and I'm 25 years old.
# My height is 180.5 cm.

# v1 Moja
print("My name is", name, "and I'm", age, "years old.")
print("My height is", height, "cm.")

# v2 Moja
print(f"My name is {name} and I'm {age} years old.")
print(f"My height is {height} cm.")

# %%

# Podane są poniższe zmienne:

name = "Alice"
age = 30
height = 165.5

# Wykorzystując funkcję print() oraz podane zmienne wydrukuj poniższy tekst do konsoli.
# Alice|30|165.5

# v1 Moja
print(f"{name}|{age}|{height}")
# v2 Moja
print(name, "|", age, "|", height, sep="")
# v3
print(name, age, height, sep="|")

# %%
saldo = 40
print(saldo)


# 17 Punkt
