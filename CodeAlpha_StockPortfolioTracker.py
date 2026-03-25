stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

total_investment = 0

print("📈 Stock Portfolio Tracker")

while True:
    stock_name = input("Enter stock name (or 'done'): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stocks:
        print("❌ Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))
    
    total_investment += stocks[stock_name] * quantity

print("\n💰 Total Investment:", total_investment)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: {total_investment}")

print("✅ Saved to portfolio.txt")