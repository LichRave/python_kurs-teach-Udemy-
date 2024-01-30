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
