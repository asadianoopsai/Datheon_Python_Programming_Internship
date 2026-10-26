
import csv
from pathlib import Path


def load_tickers():
    """Load valid ticker symbols from the company CSV."""
    file_path = Path(__file__).parent / "constituents.csv"
    tickers = set()

    try:
        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                symbol = row.get("Symbol", "").strip().upper()
                if symbol:
                    tickers.add(symbol)

    except FileNotFoundError:
        print("Error: constituents.csv was not found.")
        return None

    return tickers


def get_positive_number(prompt):
    """Ask for a number greater than zero."""
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    valid_tickers = load_tickers()

    if valid_tickers is None:
        return

    portfolio = []

    print("=== Stock Portfolio Performance Tracker ===")
    print("Enter stock details. Type DONE as the ticker when finished.\n")

    while True:
        ticker = input("Stock ticker: ").strip().upper()

        if ticker == "DONE":
            break

        if ticker not in valid_tickers:
            print("Ticker not found in the supplied S&P 500 dataset.")
            print("Please enter a valid ticker symbol.\n")
            continue

        purchase_price = get_positive_number("Purchase price per share: ")
        quantity = get_positive_number("Number of shares: ")
        current_price = get_positive_number("Current price per share: ")

        invested = purchase_price * quantity
        current_value = current_price * quantity
        profit_loss = current_value - invested
        return_percentage = (profit_loss / invested) * 100

        portfolio.append({
            "Ticker": ticker,
            "Purchase Price": round(purchase_price, 2),
            "Quantity": quantity,
            "Current Price": round(current_price, 2),
            "Invested Capital": round(invested, 2),
            "Current Value": round(current_value, 2),
            "Profit/Loss": round(profit_loss, 2),
            "Return Percentage": round(return_percentage, 2)
        })

        print(f"\nAdded {ticker} successfully!\n")

    if not portfolio:
        print("No stocks were entered. Nothing to export.")
        return

    output_file = Path(__file__).parent / "portfolio_summary.csv"

    fieldnames = list(portfolio[0].keys())

    with open(output_file, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(portfolio)

    total_invested = sum(stock["Invested Capital"] for stock in portfolio)
    total_value = sum(stock["Current Value"] for stock in portfolio)
    total_profit_loss = total_value - total_invested
    total_return = (total_profit_loss / total_invested) * 100

    print("\n=== Portfolio Summary ===")
    print(f"Total invested:       {total_invested:.2f}")
    print(f"Current value:        {total_value:.2f}")
    print(f"Total profit/loss:    {total_profit_loss:.2f}")
    print(f"Overall return:       {total_return:.2f}%")
    print(f"\nReport saved to: {output_file.name}")


if __name__ == "__main__":
    main()
