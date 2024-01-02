# -*- coding: utf-8 -*-

imie = "Pawel"
_imie = "Olek"

imie_3 = "Ala"

# %%
a = 8
b = 20

c = a * b
print(c)

# %%
przepracowane_godziny = 8
stawka_godzinowa = 20

dzienna_pensja = przepracowane_godziny * stawka_godzinowa
print(dzienna_pensja)

# %%
# camelCase = 'Python 3.7'
# PascalCase = 'Python 3.7'
# snake_case = 'Python 3.7'
# kebab-case = 'Python 3.7'
# UPPER = 'Python'

# %%
string = "Python"
print(dir(string))

# %%
a = 10
print(dir(a))
type(a)

# %%
text = "Witaj na kursie Pythona.\nPython jest wspaniały!"
print(text.capitalize)
print(text.title())
print(text.count("Python"))
print(text.startswith("kurs"))
print(text.endswith("Ty"))
print(text.find("Python"))
print(text[text.find("Python") :])

# %%
hashtg = "sport#gym"
indx = hashtg.find("#")
print(hashtg[indx:])

# %%
list = ("Table", "Phone", "Mouse", "Libary")
print(list)
print(" #".join(list))

# %%
print("#good#time#mood".replace("#", " "))

# %%
print("       PYthOn      ".strip())
print("       PYthOn      ".rstrip())
print("       PYthOn      ".lstrip())


# %%
print("1,2,3,4,5,6".split(","))
print("12".zfill(5))


# %%
list = ("sport", "python", "free", "time")
print("#".join(list))

# %%
words = ["sport", "python", "free", "time"]
joined_words = "#".join(words)
print(joined_words)


# %%
number_string = "123,785,45,5"
print(number_string.split(","))

# %%
text = " Python "

print("Original text:  ", text)
print("Uppercase text:  ", text.upper())
print("Lowercase text: ", text.lower())
print("Stripped text: ", text.strip())
print("Replaced text:  ", text.replace("P", "C"))

# %%
text = " Python "

uppercase = text.upper()
lowercase = text.lower()
stripped = text.strip()
replaced = text.replace("P", "C")

print("Original text:", text)
print("Uppercase text:", uppercase)
print("Lowercase text:", lowercase)
print("Stripped text:", stripped)
print("Replaced text:", replaced)

# %%
text = "script.py view.jpg README.md main.py"
print("The extension '.py' appears", text.count(".py"), "times in the text.")

# %%
text = "script.py view.jpg README.md main.py"
char = ".py"

count = text.count(char)
print(f"The extension '{char}' appears {count} times in the text.")

# %% TEST
# Jakie jest domyślne zachowanie argumentu end w funkcji print() w języku Python?
# KOńczy wydruk wierszz znakiem nowej linii "\n"

# Jakie jest działanie argumentu file w funkcji print() w języku Python?
# Określa, gdzie zostanie zapisany wydruk funkcji print()

# %%
text=(1, 23, 3432345, 5235)
print(text, sep=",")

# %%
7 // 3.0