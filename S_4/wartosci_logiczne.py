val_1 = False
val_2 = True

# %%

print(val_1)
print(type(val_1))

# %% koniukcja (and)
# True ==
True and True
# False ==
True and False
False and True
False and False

# %% alternatywa (or)
# True ==
True or True
True or False
False or True
# False ==
False or False

# %% negacja (not) przeciwne wartości
# True ==
True
not False
# False ==
False
not True

# %%
# True ==
bool("python")
bool(0.1)
bool("0.0")
bool({"key": "val"})
# False ==
bool(0)
bool(0.0)
bool({})
bool(set())
bool(list())
bool(tuple())

# %% ZADANIA

print(bool(" "))
print(bool(""))
print(bool("1"))
print(bool(["", ""]))

# %%

x = 3
y = 5
z = 0

print(bool((x > y) and (z < y)))
print(bool((x > y) or (z < y)))

# or

result = (x > y) and (z < y)
print(result)

result = (x > y) or (z < y)
print(result)

# %%

a = 5
b = 10

res_1 = (a < b) and b > 0
res_2 = a == b or b != 0
res_3 = not (a >= b)

print(res_1)
print(res_2)
print(res_3)
