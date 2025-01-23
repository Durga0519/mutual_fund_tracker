import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

def load_data(file_path):
    """
    Load the data from an Excel file (xlsx).
    Assumes there is only one sheet or manually selected sheets.
    """
    xls = pd.ExcelFile(file_path)
    data = {}

    # Print all sheet names to verify the format
    print(f"Available sheets in {file_path}: {xls.sheet_names}")
    
    # Load the data from the sheet 'ZN250', skipping unnamed columns
    df = pd.read_excel(xls, sheet_name='ZN250', header=3)
    
    # Drop any rows that are not needed (first few rows are metadata)
    df = df.dropna(how='all')  # Drop rows where all values are NaN

    # Drop the unnamed columns that are not relevant
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    print(f"Columns in sheet ZN250 of {file_path}: {df.columns.tolist()}")  # Print column names for debugging
    data['ZN250'] = df

    return data

def track_changes_across_months(data_nov, data_sep, fund_name):
    """
    Track changes in fund allocations for a specific fund between two months.
    """
    print(f"Tracking changes for fund '{fund_name}' between September and November")
    
    # Filter data for the specified fund in both datasets
    filtered_nov = data_nov['ZN250'][data_nov['ZN250']['Name of the Instrument'] == fund_name]
    filtered_sep = data_sep['ZN250'][data_sep['ZN250']['Name of the Instrument'] == fund_name]
    
    if filtered_nov.empty or filtered_sep.empty:
        return {}

    # Prepare a dictionary to store changes by month
    changes = {}

    # Get data for November (latest data)
    if not filtered_nov.empty:
        changes['November'] = {
            'Quantity': filtered_nov['Quantity'].values[0],
            'Market Value (in Lakhs)': filtered_nov['Market value\n(Rs. in Lakhs)'].values[0],
            'NAV': filtered_nov['% to NAV'].values[0],
            'YTM': filtered_nov['YTM %'].values[0] if pd.notna(filtered_nov['YTM %'].values[0]) else 'N/A'
        }

    # Get data for September (previous month)
    if not filtered_sep.empty:
        changes['September'] = {
            'Quantity': filtered_sep['Quantity'].values[0],
            'Market Value (in Lakhs)': filtered_sep['Market value\n(Rs. in Lakhs)'].values[0],
            'NAV': filtered_sep['% to NAV'].values[0],
            'YTM': filtered_sep['YTM %'].values[0] if pd.notna(filtered_sep['YTM %'].values[0]) else 'N/A'
        }

    return changes

def display_changes(changes):
    """
    Display changes by fund for each month.
    """
    if changes:
        for month, details in changes.items():
            print(f"Changes for {month}:")
            for key, value in details.items():
                print(f"  {key}: {value}")
    else:
        print("No changes found for the specified fund in the selected months.")

def main():
    # File paths for the September and November datasets
    file_nov = 'data/ZN250 - Monthly Portfolio November 2024.xlsx'  # Path to November file
    file_sep = 'data/ZN250 - Monthly Portfolio September 2024.xlsx'  # Path to September file

    fund_name = input("Enter Fund Name: ")  # The mutual fund you're tracking (e.g., 'Macrotech Developers Limited')
    
    # Step 1: Load Data from both November and September files
    data_nov = load_data(file_nov)
    data_sep = load_data(file_sep)

    # Step 2: Track Changes for the specified fund between September and November
    changes = track_changes_across_months(data_nov, data_sep, fund_name)

    # Step 3: Display the changes
    display_changes(changes)

if __name__ == "__main__":
    main()
