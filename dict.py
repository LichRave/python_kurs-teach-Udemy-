# empty dict

empty_dict = dict()
print(empty_dict)

d = {}
print(type(d))


# %%
pol_to_eng = {"jeden": "one", "Dwa": "two", "trzy": "three"}
name_to_digit = {"jeden": 1, "Dwa": 2, "trzy": 3}

# %%

name_to_digit = {0: 1, 1: 2, 2: 3}
# DICT = {"KEY1":"value", "key2":"valuje"}
len(name_to_digit)
# %%
pol_to_eng["cztery"] = "four"


# %%

pol_to_eng_copied = pol_to_eng.copy()

# %%
print("keys; ", "MOŻNA .LIST")
print(pol_to_eng.keys())
print("values; ", "MOŻNA .LIST")
print(pol_to_eng.values())
print("items; ", "MOŻNA .LIST")
print(pol_to_eng.items())

# %%
pol_to_eng["jeden"]
pol_to_eng.get("zero", "NIE MA TAKIEGO")
pol_to_eng.pop("two")

# %%
pol_to_eng


# %%
# zadania
key1 = 1
key2 = 2
key3 = 3
key4 = 4
key5 = 5
squares_of_numbers = {
    key1: key1**2,
    key2: key2**2,
    key3: key3**2,
    key4: key4**2,
    key5: key5**2,
}
print(squares_of_numbers)

# %%
countries_capitals = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Czechy": "Praga",
}

countries_capitals["Włochy"] = "Rzym"

countries_capitals_list = list(countries_capitals.values())
print(sorted(countries_capitals_list))

# %%

fruits = {"apple": 2, "banana": 3, "cherry": 5, "orange": 1}

# 1
print("Dictionary:", fruits)
# 2
fruits["kiwi"] = 4
print("After adding:", fruits)
# 3
fruits.pop("orange")
print("After deleting:", fruits)
# 4
print("Keys:", fruits.keys())
# 5
print("Values:", fruits.values())


# %%

fruits = {"apple": 2, "banana": 3}
fruits_added = {"orange": 3, "peach": 2}
# 1
print("Dictionary before update:", fruits)

# 2
fruits.update({"apple": 4})
print("Dictionary after update:", fruits)

# 3
fruits["kiwi"] = 1
print("Dictionary after adding:", fruits)

# 4
fruits_merged = fruits | fruits_added
print("Dictionary after merging:", fruits_merged)

# or

fruits = {"apple": 2, "banana": 3}
print("Dictionary before update:", fruits)

fruits.update({"apple": 4})
print("Dictionary after update:", fruits)

fruits.update({"kiwi": 1})
print("Dictionary after adding:", fruits)

fruits.update({"orange": 3, "peach": 2})
print("Dictionary after merging:", fruits)


# %%

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# 1
dict_merg = dict1 | dict2
print(dict_merg)

# or

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)

# %%

people = {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}

# 1
print(people.pop("Bob"))

# 2
print(people)

# %%

people = {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}

# 1
people["Emma"] = 20
print("20")

# 2
print(people)


# correct decision

people = {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}

age_of_emma = people.setdefault("Emma", 20)
print(age_of_emma)
print(people)

# %%
