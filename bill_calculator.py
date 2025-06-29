product_name = input("Enter product name: ")
quantity = int(input("Enter product quantity: "))
price = float(input("Enter product price: "))

total_amount = price * quantity

print("------------------------")
print("Product   : ", product_name)
print("Quantity  : ", quantity)
print("Price     : ₹{:.2f}".format(price))

if total_amount > 500:
    tax = total_amount * 0.05  # Correct GST: 5%
    print("GST       : ₹{:.2f}".format(tax))
    print("------------------------")
    print("Total     : ₹{:.2f}".format(total_amount + tax))
    print("------------------------")
else:
    print("GST       : -")
    print("------------------------")
    print("Total     : ₹{:.2f}".format(total_amount))
    print("------------------------")
