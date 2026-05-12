# Simple Stock Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 320
}

total_investment = 0

print("=== STOCK TRACKER ===")

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

# Store results
results = []

for i in range(n):
    stock = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        results.append(f"{stock} - Qty: {quantity} - Value: ${investment}")

        print(f"{stock} price = ${price}")
        print(f"Investment = ${investment}")

    else:
        print("Stock not found!")

# Display total investment
print("\n=== TOTAL INVESTMENT ===")
print("Total Value = $", total_investment)

# Optional: Save to file
save = input("\nDo you want to save results to a file? (yes/no): ").lower()

if save == "yes":
    file = open("stock_report.txt", "w")

    file.write("STOCK INVESTMENT REPORT\n\n")

    for item in results:
        file.write(item + "\n")

    file.write(f"\nTotal Investment = ${total_investment}")

    file.close()

    print("Report saved as stock_report.txt")