# %%

text = []
print(text)

text.append("python")
text.append("python")
print(text)


# %%

text.extend(["java", "go"])


# %%
text.insert(2, "go")

# %%
text.pop()
text.remove("go")
# %%
print(text)
# %%
text.index("python")
# %%
text.count("java")
# %%
text.sort(reverse=False)
print(text)
# %%
text[0] = "c++"
print(text)


# zadania

fruits = ["apple", "banana", "cherry"]
fruits += ["orange"]

print("List with 'orange':", fruits)


# %%
list_1 = [4, 5, 3, 3]
list_2 = [9, 7]

list_1.extend(list_2)
print(list_1)

# or

list_1 = [4, 5, 3, 3]
list_2 = [9, 7]

list_1 += list_2
print(list_1)

# %%

IT_corps = ["Apple", "Microsoft", "Samsung", "Netflix", "Uber"]
IT_corps.extend(["Amazon", "Google"])

print(IT_corps)

# Rozwiązanie I:

companies = ["Apple", "Microsoft", "Samsung", "Netflix", "Uber"]
companies.append("Amazon")
companies.append("Google")

print(companies)


# Rozwiązanie II:

companies = ["Apple", "Microsoft", "Samsung", "Netflix", "Uber"]
new_companies = ["Amazon", "Google"]
companies.extend(new_companies)

print(companies)
