# List of product prices (duplicates included)
cart_prices = [1200, 2500, 1200, 800, 1500, 2500]

# Step 1: Remove duplicate items
unique_prices = list(set(cart_prices))

# Step 2: Calculate total price
total = sum(unique_prices)

# Step 3: Apply 10% discount if total > 5000
if total > 5000:
    discount = total * 0.10
    total = total - discount
else:
    discount = 0

# Step 4: Add 18% GST
gst = total * 0.18
final_amount = total + gst

# Display results
print("Unique Prices:", unique_prices)
print("Discount Applied:", discount)
print("GST Added:", gst)
print("Final Payable Amount: ₹", round(final_amount, 2))