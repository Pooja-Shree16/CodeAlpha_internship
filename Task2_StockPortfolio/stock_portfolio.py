portfolio = {}

while True:
    print("\n======================================")
    print("      STOCK PORTFOLIO TRACKER")
    print("======================================")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Delete Stock")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock = input("Enter Stock Name: ").upper()
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price per Share: "))

        if stock in portfolio:
            portfolio[stock]["quantity"] += quantity
            portfolio[stock]["price"] = price
        else:
            portfolio[stock] = {
                "quantity": quantity,
                "price": price
            }

        print("✅ Stock Added Successfully!")

    elif choice == "2":
        print("\n========== YOUR PORTFOLIO ==========")

        if len(portfolio) == 0:
            print("No stocks added yet.")
        else:
            total = 0

            print("Stock\tQuantity\tPrice\tValue")
            print("--------------------------------------------")

            for stock, details in portfolio.items():
                value = details["quantity"] * details["price"]
                total += value

                print(f"{stock}\t{details['quantity']}\t\t₹{details['price']}\t₹{value}")

            print("--------------------------------------------")
            print(f"Total Investment : ₹{total}")

    elif choice == "3":
        stock = input("Enter Stock Name to Delete: ").upper()

        if stock in portfolio:
            del portfolio[stock]
            print("✅ Stock Deleted Successfully!")
        else:
            print("❌ Stock Not Found!")

    elif choice == "4":
        print("\n🙏 Thank You for using Stock Portfolio Tracker!")
        break

    else:
        print("❌ Invalid Choice! Please try again.")