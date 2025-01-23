
## Fund Allocation Tracker

### Introduction
This tool allows users to track changes in fund allocations between two Excel datasets representing different months (for example, comparing September and November). The data is extracted from the Excel files containing portfolio details, and users can enter a specific fund name to see how its allocations (quantity, market value, NAV, and YTM) have changed across the selected months.

### Features:
- Load data from two different Excel files (e.g., September and November).
- Track changes in fund allocations for a specific fund between the two months.
- Display changes in fund data, including:
  - **Quantity**: Number of units of the fund.
  - **Market Value (in Lakhs)**: The total market value of the fund in lakhs.
  - **NAV**: Net Asset Value of the fund.
  - **YTM**: Yield to Maturity percentage (if available).
  
### Prerequisites
To use this tool, ensure that the following are installed:
- Python 3.x
- Pandas library (`pip install pandas`)
- Dateutil library (`pip install python-dateutil`)

Additionally, you need two Excel files:
1. `ZN250 - Monthly Portfolio September 2024.xlsx`
2. `ZN250 - Monthly Portfolio November 2024.xlsx`

Ensure these files contain data in the same format as the example.

### How to Use the Tool

1. **Clone or Download the Repository**:
   Clone this repository or download the files to your local machine.
   
   ```
   git clone https://github.com/yourusername/fund-allocation-tracker.git
   ```

2. **Place Your Excel Files**:
   Place your `ZN250 - Monthly Portfolio September 2024.xlsx` and `ZN250 - Monthly Portfolio November 2024.xlsx` files in the same directory as the script.

3. **Run the Script**:
   Open a terminal and run the Python script:

   ```
   python framework.py
   ```

4. **Input Your Fund Details**:
   You will be prompted to enter the fund name you want to track and the number of months you want to analyze (in this case, only two months are considered, but you can modify it to compare more months).
   
   Example:
   ```
   Enter Fund Name: Macrotech Developers Limited
   Enter number of months (e.g., 5 for last 5 months): 5
   ```

5. **View the Results**:
   After inputting the details, the script will display the changes in the fund’s allocation across the two months (September and November).

### Sample Output

```
Enter Fund Name: Macrotech Developers Limited
Available sheets in ZN250 - Monthly Portfolio November 2024.xlsx: ['ZN250']
Columns in sheet ZN250 of ZN250 - Monthly Portfolio November 2024.xlsx: ['Name of the Instrument', 'ISIN', 'Rating / Industry^', 'Quantity', 'Market value\n(Rs. in Lakhs)', '% to NAV', 'YTM %']
Available sheets in ZN250 - Monthly Portfolio September 2024.xlsx: ['ZN250']
Columns in sheet ZN250 of ZN250 - Monthly Portfolio September 2024.xlsx: ['Name of the Instrument', 'ISIN', 'Rating / Industry^', 'Quantity', 'Market value\n(Rs. in Lakhs)', '% to NAV', 'YTM %']
Tracking changes for fund 'Macrotech Developers Limited' between September and November

Changes for November:
  Quantity: 9600.0
  Market Value (in Lakhs): 94.20
  NAV: 0.001330
  YTM: 0.05

Changes for September:
  Quantity: 9550.0
  Market Value (in Lakhs): 93.50
  NAV: 0.001325
  YTM: N/A
```
