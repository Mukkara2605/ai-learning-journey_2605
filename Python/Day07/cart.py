# Shopping cart (cart.py): use a dictionary of item to price, such as {"pen": 10, "book": 150, "bag": 600}. Print each item with its price, the total, and the most expensive item.
cart = {"pen": 10, "book": 150, "bag": 600}
total_price = 0
expensive_item = ""
maximum_price = 0
for item,price in cart.items():
    print(f"{item}: {price}")
    total_price += price
    if price > maximum_price:
        maximum_price = price
        expensive_item = item

print(f"Total price: {total_price}")
print(f"Most expensive item: {expensive_item} ({maximum_price})")