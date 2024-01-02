empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ("Amazon", "USA", "Techology", 1)
google = ("Google", "USA", "Techology", 2)

name_google = google[0]
print(name_google)

# %%
data = (amazon, google)
print(data)
# %%
a = ("Artem", "Monkiewicz")
print(a)

# %%
x, y = (10, 15)
x, y = y, x
print(x, y)

# %%
# ZAADANIA
language = "Python"
version = "3.10"

tuple_data = (language, version)
print(tuple_data)


# %%
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")

tuple3 = tuple1 + tuple2
print("Combined tuple:", tuple3)

# %%

fruits = ("apple", "banana", "cherry", "banana", "banana")
number_of_bananas = fruits.count("banana")
print("Number of bananas:", number_of_bananas)


# %%

fruits = ("apple", "banana", "cherry")
print("Tuple:", fruits)
print("Fruit 1:", fruits[0])
print("Fruit 2:", fruits[1])
print("Fruit 3:", fruits[2])
