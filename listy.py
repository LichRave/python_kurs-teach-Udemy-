empty_list = list()
print(empty_list)

# %%
techs = ["python", "java", "c++", "go", "sql"]
print(techs)
techs[0] = "python 3.7"
print(techs)
techs += ["javascript"]
print(techs)
# %%
numbers = [3, 4, 5, 6, 71, 23]
print(numbers)
print(type(numbers))

# %%
nowa_lista = []
nested = [[1, 2, 3, 5], ["java", "c++", "go"]]
# zagnieżdżanie

# %%
first = ["mleko", "ziemniaki", "nakaron"]
second = ["woda", "jajka"]
bucked = [first, second]
len(bucked)

# %%
first + second + ["salo"]

# %%
# ZADANIA

numbers = [1, 4, 2, 5]
letters = ["d", "s", "t"]

combined_list = numbers + letters

print(combined_list)

# %%
fruits = [["apple", "banana"], ["cherry", "orange"], ["kiwi", "melon"]]

first = fruits[1]
print("Nested list:", fruits)
print("First item of second nested list:", first[0])
# or
print("First item of second nested list:", fruits[1][0])


# %%
print("!!!")
