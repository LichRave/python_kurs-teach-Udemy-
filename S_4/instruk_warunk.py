# %%
version = 3.7

# %%
version > 3
version <= 3

# %%
number = 1200
number > 1000
number == 1200
number == 1000
number != 1200
number != 1000

# %%
# if [warunek]:
#     [instrujkcje]

# %%
if 8 > 10:
    print("Tak")

# %%
a = 8
if a < 10:
    print("a<10")

# %%
b = 15
if b > 10:
    print("b>10")
else:
    print("b<=10")

# %%
age = 18
if age < 18:
    print("nie masz uprawnień")
elif age == 18:
    print("WOW! MASZ 18!! GRATKI!")
else:
    print("Dostęp przyznany!")

# %%
age = int(input("Podaj swój wiek: "))
if age < 18:
    print("Nie masz uprawnień.")
elif age == 18:
    print("WOW! MASZ 18!! GRATKI!")
else:
    print("Dostęp przyznany!")

# %% ZADANIA
number = 10
if number > 0:
    print("The number is greater than zero.")

# %%
number = 5
if number > 0:
    print("The number", 5, "is positive.")
elif number < 0:
    print("The number", 5, "is negative.")
else:
    print("The number", 5, "is equal to zero.")

# %%
number = 7
if number % 2 == 0:
    print("The number", number, "is even.")
else:
    print("The number", number, "is odd.")

# %%
import calendar

year = 2024
if calendar.isleap(year):
    print("The year", year, "is a leap year.")
else:
    print("'The year", year, "is not a leap year.'")

# or

year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year", year, "is a leap year.")
else:
    print("The year", year, "is not a leap year.")

# %%

# %%
print("Hello! Program started...")
print(
    """Włam się do systemu, zgadując dwucyfrowy PIN.
    Numer PIN skłąda się z cyfr: 0, 1, 2.
    """
)
pin = int(input("Wprowadż numer PIN: "))
if pin == 21:
    print("Brawo! Złamałeś system.")
elif pin == 20:
    print("Jesteś blisko!")
else:
    print("Nie zgadłęś, spróbój jeszcze.")

# %% ZADANIA

category = "electronics"
price = 2000

# VAT 23%
Vat_23 = price * 23 / 100
# VAT 21%
Vat_21 = price * 21 / 100
# VAT 8%
Vat_8 = price * 8 / 100

if category == "electronics":
    if price > 1000:
        print("The VAT for a product is", Vat_23, "PLN.")
    elif price < 1000:
        print("The VAT for a product is", Vat_8, "PLN.")
# if category == "cloting":
#     if price > 0:
#         print("The VAT for a product is", Vat_23, "PLN.")
else:
    print("The VAT for a product is", Vat_21, "PLN.")


# or A job done correctly
category = "electronics"
price = 2000

if category == "electronics":
    if price > 1000:
        vat = price * 0.23
    else:
        vat = price * 0.08
elif category == "clothing":
    vat = price * 0.23
else:
    vat = price * 0.21

print(f"The VAT for a product is {vat} PLN.")

# %%

velocity = int(55)
ograniczenie = int(50)

if velocity > ograniczenie:
    print("Slow down!")
else:
    print("Keep it up!")

# %%

category = "crime"
quantity = 5
book_price = 100.0

# category = input(
#     "Hello! please write the category of the book: Crime, Fantasy or Other: "
# )
# quantity = int(input("Okay, now indicate how many books are in stock: "))
# book_price = input("Inicate, how much does one unit of this book cost: ")

if category == "crime":
    if quantity >= 5:
        total_price = book_price - (book_price * 0.2)
    elif quantity >= 3:
        total_price = book_price - (book_price * 0.1)
    else:
        total_price = book_price
if category == "fantasy":
    if quantity >= 10:
        total_price = book_price - (book_price * 0.25)
    elif quantity >= 5:
        total_price = book_price - (book_price * 0.15)
    else:
        total_price = book_price
if category == "other":
    if quantity >= 20:
        total_price = book_price - (book_price * 0.1)
    elif quantity >= 3:
        total_price = book_price - (book_price * 0.05)
    else:
        total_price = book_price

print("The total price after the discount is", total_price, "PLN.")


# OR

category = "crime"
quantity = 5
book_price = 100.0

if category == "crime":
    if quantity >= 5:
        discount = 0.2
    elif quantity >= 3:
        discount = 0.1
    else:
        discount = 0
elif category == "fantasy":
    if quantity >= 10:
        discount = 0.25
    elif quantity >= 5:
        discount = 0.15
    else:
        discount = 0
else:
    if quantity >= 20:
        discount = 0.1
    elif quantity >= 10:
        discount = 0.05
    else:
        discount = 0

final_price = book_price * (1 - discount)
print(f"The total price after the discount is {final_price} PLN.")

# %%
saldo = 10000
klient_zwerifikowany = True

if saldo > 0 and klient_zwerifikowany:
    print("Możesz wypłacic gotówkę.")
else:
    print("Nie możesz wypłacić gotówki.")

# %%
saldo = 10000
klient_zwerifikowany = True

amount = input("Ile chcesz wypłaćić gotówki? ")


if saldo > 0 and klient_zwerifikowany and saldo >= amount:
    print("Możesz wypłacic gotówkę.")
else:
    print("Nie możesz wypłacić gotówki.")

# %% ZADANIA

fact = "Python is easy and enjoyable"
dfack_len = len(fact)

if dfack_len == 28:
    print("There are less than 20 unique characters.")
else:
    print("The number of unique characters is greater than or equal to 20.")

# or`A job done correctly
fact = "Python is easy and enjoyable"
unique_characters = set(fact)
number_of_unique_characters = len(unique_characters)

if number_of_unique_characters < 20:
    print("There are less than 20 unique characters.")
else:
    print("The number of unique characters is greater than " "or equal to 20.")
# %%
# x if [warunek] else y
tech = "sas"
"Dobry wybór" if tech == "python" else "Poszukaj czegos lepszego"

# %% ZADANIA
text = "sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx"

print(
    'The text contains the letter "q".'
    if "q" in text
    else 'The text does not contain the letter "q".'
)

# or

text = "sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx"

print(
    'The text contains the letter "q".'
    if "q" in text
    else 'The text does not contain the letter "q".'
)

# %%

height = 1.85
weight = 85

# BMI = (waga / wzrost)
BMI = float(weight / height**2)
wynik_BMI = round(BMI, 2)

# Zwrot dannych :
print("The patient's BMI is:", wynik_BMI)

# Funkcje
if wynik_BMI < 18.5:
    print("Underweight")
elif wynik_BMI >= 18.5 and wynik_BMI < 25:
    print("Normal weight")
elif wynik_BMI >= 25 and wynik_BMI < 30:
    print("Normal weight")
elif wynik_BMI > 30:
    print("Normal weight")

# or

height = 1.85
weight = 85

bmi = weight / (height**2)
print(f"The patient's BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")


# %%
password = "my_password_123"

if len(password) < 8:
    print("The password is too short.")
elif not any(char.isdigit() for char in password):
    print("The password must contain at least one digit.")
elif not any(char.isupper() for char in password):
    print("The password must contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("The password must contain at least one lowercase letter.")
else:
    print("The password is complex enough.")
