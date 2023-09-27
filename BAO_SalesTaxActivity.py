TAX = .06
total_Price = float(input("Enter Purchase amount:"))

total_TAX = TAX * total_Price

print("You have a total TAX of:", round(total_TAX,2))

Tax_Price = total_Price + total_TAX

print("your total bill with tax is:", round(Tax_Price,2))