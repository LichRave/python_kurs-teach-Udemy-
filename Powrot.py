# %%
lst = [
    " koala ",
    " cat ",
    " fox ",
    " panda ",
    " chipmunk ",
    " sloth ",
    " penguin ",
    " dolphin ",
]

for animal in lst:
    print(animal)

# %%
st = [" Sam ", " Lisa ", " Micha ", " Dave ", " Wyatt ", " Emma ", " Sage "]

for name in st:
    print(f"Hello,{name}!")

# %%
str = "Civilization"

c = 0
for i in str:
    c += 1

print(c)
print(c == len(str))
# %%
lst1 = [" Phil ", " Oz ", " Seuss ", " Dre "]
lst2 = []

for name in lst1:
    lst2.append(f"Dr.{name}")

print(lst2)
# 2
for name in lst1:
    lst2.append("Dr." + name)

# %%
lst123 = [3, 7, 6, 8, 9, 11, 15, 25]
lst124 = []

for cyfra in lst123:
    lst124.append


# %%
def print_communique():
    print("Pierwsza linijka komunikatu")
    print("Druga linijka komunikatu")
    print("Trzecia linijka komunikatu")


a = 24

if a / 2 == 0:
    b = a / 2
    print_communique()
else:
    b = a / 3

# Gdzieś dalej w kodzie

if b != 1:
    print_communique()


# %%
def sum_up(x, y):
    return x + y


a = sum_up(3, 4)
b = sum_up(2.5, 7.5)
c = sum_up(4, -2)

print(a)
print(b)
print(c)


# %%
class Pies:
    def szczekaj(self):
        print("Hau, hau!")

    def __init__(self, name):
        self.name = name

    def toaleta(self):
        print("Siusiu")


pies1 = Pies("Burek")
pies1.name
pies1.szczekaj()
pies1.toaleta()


class Pies:
    def __init__(self, name, is_hungry):
        self.name = name
        self.is_hungry = is_hungry

    def jedz(self):
        if self.is_hungry == True:
            self.is_hungry = False


# %%
lst1 = [3, 7, 6, 8, 9, 11, 15, 25]
lst2 = []

for i in lst1:
    lst2.append(i**2)

print(lst2)

# %%
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []

for i in lst1:
    if i > 0:
        lst2.append(i)

print(lst2)

# %%
dict = {
    " z1 ": 900,
    " t1 ": 1100,
    " p1 ": 2300,
    " r1 ": 1050,
    " k1 ": 3200,
    " g1 ": 400,
}
lst = []

for value in dict.values():
    if value > 1000:
        lst.append(value - 1000)

print(lst)

# %%
lst1 = [3.14, 66, " Teddy Bear ", True, [], {}]
lst3 = []

for i in lst1:
    lst3.append(type(i))

print(lst3)


# %%
lst1 = [1, 2, 3, 4, 5]
lst2 = [i for i in lst1]

print(lst2)

# %%

rng = [i for i in range(1200, 2001, 130)]


print(rng)


# %% 70
lst1 = [44, 54, 64, 74, 104]
lst2 = [i + 6 for i in lst1]

print(lst2)

# %% 71
print("Zadanie")
lst1 = [2, 4, 6, 8, 10, 12, 14]
lst2 = [i * i for i in lst1 if i * i > 50]


print(lst2)

# or

lst1 = [2, 4, 6, 8, 10, 12, 14]
lst2 = [i**2 for i in lst1 if i**2 > 50]


print(lst2)

# %% 72
dict = {
    " Sedan ": 1500,
    " SUV ": 2000,
    " Pickup ": 2500,
    " Minivan ": 1600,
    " Van ": 2400,
    " Semi ": 13600,
    "Bicycle ": 7,
    " Motorcycle ": 110,
}

lst_car = [key.upper() for key in dict if dict[key] < 5000]
print(lst_car)

# or
lst23 = [key.upper() for key, value in dict.items() if value < 5000]
print(lst23)
