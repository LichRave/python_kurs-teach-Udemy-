# instrukcja

# for element in sequence:
#     if condition:
#         break

# Kod do wykonania dla każdego elementu

for i in "0123456789":
    i = int(i)
    print(i)
    if i == 6:
        break

# %%
sample = "Python Course"
for char in sample:
    if char == " ":
        break
    print(char)

# %%
for char in "kowalskygmail.com":
    if char == "@":
        print("Adres e-mail zweryfikowany")
        break
else:
    print("Adres e-mail nie jest poprawny")

print("Koniec")

# %% ZaDANIA

products = [
    ("Shoes", "Footwear", 150.00),
    ("T-shirt", "Clothing", 50.00),
    ("Pants", "Clothing", 100.00),
]
category = "Clothing"
for product in products:
    if product[1] == category:
        print(f"The first product is {product[0]}.")
        break

# %%
cars = [
    {"model": "Tesla", "mileage": 15000, "battery_level": 100},
    {"model": "Nissan", "mileage": 30000, "battery_level": 75},
    {"model": "BMW", "mileage": 5000, "battery_level": 100},
    {"model": "Ford", "mileage": 20000, "battery_level": 50},
]


for car in cars:
    if car["battery_level"] == 100:
        print("The first car with a full charge is:", car["model"])
        break

# %%
panels = [
    {"id": 1, "output_power": 200},
    {"id": 2, "output_power": 150},
    {"id": 3, "output_power": 250},
    {"id": 4, "output_power": 180},
]

for panel in panels:
    if panel["output_power"] > 200:
        print("The first panel with an output power greater than 200 is:", panel["id"])
        break
