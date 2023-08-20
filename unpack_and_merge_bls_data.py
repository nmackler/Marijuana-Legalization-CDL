import os
import pandas as pd

# Path to the folder containing the Excel files
folder_path = 'C:\Users\\natha\OneDrive\Documents\Marijuana\Marijuana-Legalization-CDL\BLS Excels'

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Create a dictionary to store DataFrames
dataframes = {}

# Loop through the files
for file_name in file_list:
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):  # Check if the file is an Excel file
        # Extract year from the file name (necessary becuase the BLS is inconsistent with file naming)
        numbers = ''.join(filter(str.isdigit, file_name))
        
        # Create DataFrame
        df = pd.read_excel(os.path.join(folder_path, file_name))
        
        # Store DataFrame in the dictionary
        dataframes[numbers] = df



