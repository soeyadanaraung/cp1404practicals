total_price = 0
items = int(input("Number of items: "))

while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
for i in range(items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price - (total_price * 0.1)
print(f"Total price for {items} items is ${total_price:.2f}")