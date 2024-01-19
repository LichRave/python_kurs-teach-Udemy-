# %%
file = open("simple.txt", "r")

for line in file:
    print(line, end="")

file.close()

# %%
with open("simple.txt", "r") as file:
    for line in file:
        print(line, end="")

# %%

with open("simple.txt", "r") as file:
    for linia in file:
        print(linia, end="")

# %%

with open("data.txt", "r") as file:
    for linia in file:
        print(linia, end="")

# %%

with open("simple.txt", "r") as plik:
    spis_tresci = plik.readlines()
    for line in spis_tresci:
        print(line, end="")

# %%

with open("simple.txt", "r") as plik:
    linja = plik.readline()
    while linja:
        print(linja, end="")
        linja = plik.readline()
# %%

with open("simple.txt", "r") as file:
    lines = file.read()
    print(lines)

# %% ZADANIA
with open("simple.txt", "r") as file:
    all_lines = file.readlines()
    print(all_lines)

# %%
with open("simple.txt", "r") as file:
    all_lines = file.readlines

lines = lines[1:]

products = []
for line in lines:
    cols = line.strip()

# %%
products = []

with open("products.txt", "r") as file:
    for line in file:
        name, price, quantity = line.strip().split(",")
        products.append(
            {"name": name, "price": float(price), "quantity": int(quantity)}
        )

for product in products:
    print(product)
