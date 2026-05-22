stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 200,
    "AMZN": 150
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock_name = input("Enter Stock Name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))

        investment = stocks[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Stock not available.")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to file
file = open("portfolio.txt", "w")
file.write(f"Total Investment Value: ${total_investment}")
file.close()

print("Portfolio saved to portfolio.txt")