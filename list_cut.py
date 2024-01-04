# %%
lista = [32, 34, 56, 6454, 75]

lista[0]
lista[1]

lista[-1]
lista[-3]

lista[1:5]
cut_stp = lista[-5:-1]
print(cut_stp)

# %%
# zadania
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

print("List:", fruits)
print("Slice 1:", fruits[1:3])
print("Slice 2:", fruits[:3])
print("Slice 3:", fruits[3:])
print("Slice 4:", fruits[1::2])

# %%

fruits = [
    ["apple", "banana", "cherry"],
    ["orange", "kiwi", "melon"],
    ["grape", "pear", "plum"],
]

print("Last item of first nested list:", fruits[0][-1])
print("First two items of second nested list:", fruits[1][:2])
print("Last two items of third nested list:", fruits[2][1:])
