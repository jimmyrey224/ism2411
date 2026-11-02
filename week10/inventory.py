# inventory.py
# Name: Jimmy Reyes
# ISM2411 — Module 10 Lab: Inventory List Manager
#
# Reflection
# 1. Most surprising thing about Python lists:
#    The most surprising thing about Python lists is that the indexing starts at 0, not 1. Also, that negative indexes grab form the end. It took a little bit to get used to.
#
# 2. A business situation where a list would beat doing it in Excel:
#    Apllying the same disocunt or price change to a long list of items. it would be much more efficient rather than doing it in Excel.

print("--- Exercise 1: Build the list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2: Index Practice ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2
print(inventory[middle]) # middle item

print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item

print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope")

print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average List of Sales ---")
sales = [100,250,75,480,200]
total = sum(sales)
count = len(sales)
average = total/count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

## Exam question explanation
best = sales[0]
worst = sales[0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best (manual): {best}")
print(f"Worst (manual): {worst}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * .9,2)) # 10% discount

print ("Original prices:", prices)
print("Discounts:", discounted)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340,127,589,204,467,88,731,315,62,490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
