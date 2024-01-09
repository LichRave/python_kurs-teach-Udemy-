# %%
print("HERE")
name = "sas"
for charakter in name:
    print(charakter)

# %%
names = "python"
index = 0
for charakter in names:
    print(index, charakter)
    index = index + 1

# %%
for index in range(10):
    print(index)


# %%
print("NEW")
for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)

    # %%
for i in range(10):
    print(i)

# %%
print("iter, strt, stp")
for i in range(10, 20):
    print(i)

# %%

print("iter, strt, stp, stp")
for i in range(100, -1, -1):
    print(i)

# %%
print("iter, strt, stp, stp")
for i in range(10, 100, 10):
    print(i)

# %%
print("Java")
tech = "java"
for i in range(len(tech)):
    print(tech[i], i)

# %%
print("Pytch")
string = "Python Course"
for i in string:
    print(i, index)
    index = index + 1

# %%
print("WhoutCUT")
hashtags = "#sport#gym#fitness"
for char in hashtags:
    print(char)

# %%
print("WhCUT#")
hashtags = "#sport#gym#fitness"
for char in hashtags:
    if char == "#":
        print(char)

# %%
hashtags = "#sport#gym#fitness#"
result = ""

for char in hashtags:
    if char != "#":
        result = result + char
    else:
        print(result)
        result = ""


# %%
for char, number in zip("abced", "123126666"):
    print(char, number)

# %%
hashtags = "#sport#gym#fitness"
for char in hashtags:
    print(char)

    # %%
hashtags = "#sport#gym#fitness#"
result = ""

for char in hashtags:
    if char != "#":
        result = result + char
    else:
        print(result)
        result = ""

# %% ZADANIA
for char in range(0, 21):
    print(char)

# %%
hashtags = "#weekend#good#time#"
result = ""

for char in hashtags:
    if char != "#":
        result = result + char
    else:
        print(result)
        result = ""

# or
hashtags = "#weekend#good#time#"
result = ""

for char in hashtags:
    if char != "#":
        result += char
    elif result:
        print(result)
        result = ""


# %%
sum = 0

for i in range(1, 11):
    sum += i

print("The sum of numbers from 1 to 10 is:", sum)

# %%
products = [("T-shirt", 50.00), ("Pants", 100.00), ("Shoes", 150.00)]

for i, value in products:
    cost = value + value

print("The total order amount is: ", cost)


# or
products = [("T-shirt", 50.00), ("Pants", 100.00), ("Shoes", 150.00)]

total = 0.0

for product in products:
    total += product[1]

print("The total order amount is:", total)

# %%
products = [("T-shirt", 50.00), ("Pants", 100.00), ("Shoes", 150.00)]
total = 0.0
discount = 0.1

for i, value in products:
    if value >= 2:
        total += value - (value * discount)

print("The total order amount after applying the discount is:", total)


# or
products = [("T-shirt", 50.00), ("Pants", 100.00), ("Shoes", 150.00)]

total = 0.0

if len(products) > 1:
    discount = 0.1
else:
    discount = 0.0

for product in products:
    total += product[1]

total_after_discount = total - (total * discount)
print(
    "The total order amount after applying the discount is:",
    total_after_discount,
)

# %%
products = [
    ("T-shirt", "Clothing", 50.00),
    ("Pants", "Clothing", 100.00),
    ("Shoes", "Footwear", 150.00),
]

category = "Clothing"

for product in products:
    if product[1] == category:
        print(product[0], product[2])
