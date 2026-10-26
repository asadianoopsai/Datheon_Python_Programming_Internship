Stock Portfolio Performance Tracker
 Project Overview
The Stock Portfolio Performance Tracker is a Python-based application that helps users calculate and monitor the performance of their stock investments. Users can enter stock ticker symbols, purchase prices, quantities, and current stock prices to calculate their portfolio's profit or loss.

 Objectives
- Record stock investment details.
- Calculate the total invested capital.
- Calculate the current portfolio value.
- Determine profit or loss for each stock.
- Calculate the percentage return on investment.
- Export the portfolio report to a CSV file.

 Technologies Used
- **Python 3**
- **CSV module** — to read and write CSV files.
- **Pathlib module** — to manage file paths.

 Project Structure
```text
Project-2-Stock-Portfolio/
├── portfolio.py
├── constituents.csv
├── portfolio_summary.csv  # Generated automatically
└── README.md
```

 Features
1. **Stock Validation:** Checks ticker symbols against the supplied S&P 500 company dataset.
2. **Investment Calculation:** Calculates the amount invested in each stock.
3. **Current Portfolio Value:** Calculates the current value using the entered current price.
4. **Profit or Loss:** Determines whether each stock has gained or lost value.
5. **Return Percentage:** Calculates the percentage gain or loss.
6. **CSV Export:** Automatically generates `portfolio_summary.csv` containing the results.
7. **Input Validation:** Rejects invalid numbers and non-positive prices or quantities.
8. **Portfolio Summary:** Displays the total investment, current value, overall profit or loss, and overall return.

 How to Run

 Step 1: Install Python
Install Python 3 if it is not already installed.

 Step 2: Check the Files
Ensure that `portfolio.py` and `constituents.csv` are in the same folder.

Step 3: Open the Terminal
Open the terminal in the `Project-2-Stock-Portfolio` folder.

 Step 4: Run the Program
Execute:

```bash
python portfolio.py
```

 Step 5: Enter Stock Details
Enter a valid ticker symbol, purchase price per share, number of shares, and current price per share.

Repeat for additional stocks. When finished, type:

```text
DONE
```

 Step 6: View the Report
The program automatically creates `portfolio_summary.csv` in the same folder. Open it using Excel, Google Sheets, or a text editor.

 Calculation Formulas

**Invested Capital**
```text
Purchase Price × Number of Shares
```

**Current Value**
```text
Current Price × Number of Shares
```

**Profit or Loss**
```text
Current Value − Invested Capital
```

**Return Percentage**
```text
(Profit or Loss ÷ Invested Capital) × 100
```

A positive result indicates a profit, while a negative result indicates a loss.

 Example

Suppose a user enters:
- Stock ticker: `AAPL`
- Purchase price: `150`
- Number of shares: `10`
- Current price: `120`

The results will be:

| Metric | Result |
|---|---:|
| Invested Capital | 1500 |
| Current Value | 1200 |
| Profit/Loss | -300 |
| Return Percentage | -20% |

*This is an illustrative example, not a live stock price.*

 Output File
The generated `portfolio_summary.csv` contains:
- Stock ticker
- Purchase price
- Quantity
- Current price
- Invested capital
- Current value
- Profit or loss
- Return percentage

**Note:** The program generates the report after at least one stock has been entered and the user types `DONE`. Running the program again overwrites the previous report.

 Limitations
- Stock prices are entered manually; the program does not retrieve live market prices.
- Valid ticker symbols are checked against the supplied S&P 500 dataset.
- This project is for educational purposes and is not financial advice.

 Author
Developed as part of the **Datheon Python Programming Internship**.

 License
This project was created for educational and internship purposes.