products = [
    ("T-shirt", "Clothing", 50.00),
    ("Pants", "Clothing", 100.00),
    ("Shoes", "Footwear", 150.00),
]

category = "Clothing"

for product in products:
    if product[1] == category:
        print(product[0], product[2])
