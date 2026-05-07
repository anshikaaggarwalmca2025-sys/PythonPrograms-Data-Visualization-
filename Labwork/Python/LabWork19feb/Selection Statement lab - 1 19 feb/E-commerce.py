cart_value = float(input("Enter total cart value: "))
membership = input("Enter membership level (Silver/Gold/Platinum): ").lower()
is_festival = input("Is it festival season? (yes/no): ").lower() == "yes"
cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum/None): ")
festival = input("Is it festival season? (yes/no): ")

discounts = []

# Cart discount
if cart_value >= 10000:
    discounts.append(20)
elif cart_value >= 5000:
    discounts.append(10)

# Membership discount
if membership.lower() == "silver":
    discounts.append(5)
elif membership.lower() == "gold":
    discounts.append(10)
elif membership.lower() == "platinum":
    discounts.append(15)

# Festival discount
if festival.lower() == "yes":
    discounts.append(12)

# Apply highest discount
if discounts:
    max_discount = max(discounts)
else:
    max_discount = 0

final_amount = cart_value - (cart_value * max_discount / 100)

print("Highest Discount Applied:", max_discount, "%")
print("Final Payable Amount: ₹", final_amount)
