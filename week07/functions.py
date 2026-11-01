# Self assessment Qs
# 1. The first bug I spotted was the toal = sale bug. I found it myself.
# 2. apply_discount(price, tier) gives a members tier, and the price they pay based off of their applied discount because of their tier.
# 3. Disclosure comment: I used Claude AI to help me spot bugs in the broken_sales.py file and explain them to me in a simplified way. The AI use did both. It did shortcut it, but it also helped me understand the material.

# Exercise 1

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refractor into a function

discounted = apply_discount(200, "gold") # Used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5
# AI's description did match the bug

# Exercise 6

x = 100 # apple # Global

def double_it():
    # x = 999 # local another apple (not same apple)
    return x * 2

print(x)
print(double_it())
print(x)