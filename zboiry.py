# -*- coding: utf-8 -*-

empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
text = {"python", "java", "c++", "sql"}
print(text)
print(type(text))
print(len(text))
# %%
print("python" in text)
print("go" in text)

# %%
text.add("sas")
print(text)

# %%
text.remove("sas")
print(text)

# %%

empty_set = set()
print(empty_set)
print(type(empty_set))


# %%
techs = {"python", "java", "c++", "sql"}
print(techs)
print(type(techs))
print(len(techs))

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}
C.issubset(A)
A.intersection(B)
A.symmetric_difference(B)

D = A.copy()
print(D)

# %%
# Zadania
string = "Programowanie w języku Python - od A do Z"
string = string.lower()
string = string.replace("ę", "e")
string = string.replace(" ", "")
string = string.replace("-", "")
print(string)
cel = len(set(string))
print(cel)

# %%
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

print("Union set:", union_set)
print("Intersection set:", intersection_set)
print("Difference set:", difference_set)
print("Symmetric difference set:", symmetric_difference_set)


# %%
# list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# print("List with duplicates:", list1)
# set().union(list1)
# print("List without duplicates:", set)


list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

unique_set = set(list1)
unique_list = list(unique_set)

print("List with duplicates:", list1)
print("List without duplicates:", unique_list)

# %%
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

set3 = set1 | set2
print("Union set without duplicates:", set3)

# 2 sposób
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

union_set = set(list(set1) + list(set2))

print("Union set without duplicates:", union_set)
