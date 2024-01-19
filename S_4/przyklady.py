# %%
raw_data = "345!23!43253!324525"
print(raw_data.replace("!", ","))

# %%
raw_data = "345!23!43253!324525"
clean_data = ""

for char in raw_data:
    if char != "!":
        clean_data = clean_data + char
    else:
        clean_data = clean_data + ","
print(clean_data)

# %%

suma = 0
for i in range(10):
    suma = suma + i
print(suma)

# %%
saldo = 450

print("Saldo początowe: {}".format(saldo))

for kwota in range(10, 60, 10):
    print("Wypłącona kwota{}".format(kwota))
    saldo -= kwota
    print("Saldo: {}".format(saldo))
print("SAldo doncowe: {}".format(saldo))

# %%

print("Witak=j w systemie logowania")
print("*" * 30)
nick = input("Podaj swój nick: ")
pin = input("podaj swój pin, {}: ".format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in "0123456789":
            print("Podałeś niepoprawny pin")
            break
    else:
        print("Pin wważny.")
else:
    print("Podałeś niepoprawny pin")

# %%
rooms = [
    {
        "number": 101,
        "available_dates": [
            "2023-05-10",
            "2023-05-11",
            "2023-05-12",
        ],
    },
    {
        "number": 102,
        "available_dates": [
            "2023-05-10",
            "2023-05-11",
        ],
    },
    {
        "number": 103,
        "available_dates": [
            "2023-05-11",
            "2023-05-12",
            "2023-05-13",
        ],
    },
    {
        "number": 105,
        "available_dates": [
            "2023-05-10",
            "2023-05-11",
            "2023-05-12",
            "2023-05-13",
        ],
    },
    {
        "number": 107,
        "available_dates": [
            "2023-05-11",
            "2023-05-12",
        ],
    },
    {
        "number": 110,
        "available_dates": [
            "2023-05-10",
            "2023-05-11",
            "2023-05-12",
            "2023-05-13",
        ],
    },
]

start_date = "2023-05-11"
end_date = "2023-05-13"

for room in rooms:
    if (
        start_date not in room["available_dates"]
        or end_date not in room["available_dates"]
    ):
        continue
    print(f"Room number {room['number']} is available.")
