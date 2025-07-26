import pandas as pd
import os
import glob

def extract_max_p_from_csv(file_path):
    """
    Extract the maximum p value where x == 0 from a CSV file.
    Returns a dictionary with f, d, n, x, y, p values.
    """
    try:
        # Read CSV file
        df = pd.read_csv(file_path)
        
        # Filter rows where x == 0.0
        x_zero_rows = df[df['x'] == 0.0]
        
        if x_zero_rows.empty:
            print(f"Warning: No rows with x == 0.0 found in {file_path}")
            return None
        
        # Find the row with maximum p value
        max_p_row = x_zero_rows.loc[x_zero_rows['p'].idxmax()]
        
        # Extract required values with rounding
        result = {
            'f': round(max_p_row['F'], 2),  # F column maps to f, rounded to 2 digits
            'd': round(max_p_row['d'], 4),  # d rounded to 4 digits
            'n': max_p_row['N'],  # N column maps to n
            'x': max_p_row['x'],
            'y': max_p_row['y'],
            'p': max_p_row['p']
        }
        
        return result
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def process_files(pattern, output_filename):
    """
    Process all CSV files matching a pattern and create output CSV.
    """
    files = glob.glob(pattern)
    files.sort()  # Sort for consistent ordering
    
    results = []
    
    for file_path in files:
        print(f"Processing {file_path}...")
        result = extract_max_p_from_csv(file_path)
        if result:
            results.append(result)
    
    if results:
        # Create DataFrame and ensure column order is f, d, n, x, y, p
        output_df = pd.DataFrame(results)
        output_df = output_df[['f', 'd', 'n', 'x', 'y', 'p']]
        
        # Sort by f first, then by n
        output_df = output_df.sort_values(['f', 'n'])
        
        # Reset index after sorting
        output_df = output_df.reset_index(drop=True)
        
        output_df.to_csv(output_filename, index=False)
        print(f"Created {output_filename} with {len(results)} entries")
    else:
        print(f"No valid results found for pattern {pattern}")

def main():
    """
    Main function to process all file categories and create output CSV files.
    """
    print("Starting to process CSV files...")
    
    # Process W_*.csv files from data/scaled
    print("\n1. Processing W_*.csv files from data/scaled...")
    process_files("data/scaled/W_*.csv", "scaled_w_max_p.csv")
    
    # Process W_*.csv files from data/unscaled
    print("\n2. Processing W_*.csv files from data/unscaled...")
    process_files("data/unscaled/W_*.csv", "unscaled_w_max_p.csv")
    
    # Process DRPINN_*.csv files from data/unscaled
    print("\n3. Processing DRPINN_*.csv files from data/unscaled...")
    process_files("data/unscaled/DRPINN_*.csv", "unscaled_drpinn_max_p.csv")
    
    print("\nAll processing complete!")
    
    # Verify the output files
    print("\nVerifying output files:")
    for filename in ["scaled_w_max_p.csv", "unscaled_w_max_p.csv", "unscaled_drpinn_max_p.csv"]:
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            print(f"{filename}: {len(df)} entries")
            print(f"  Columns: {list(df.columns)}")
            print(f"  Sample row: {df.iloc[0].to_dict()}")
            print(f"  f values range: {df['f'].min()} to {df['f'].max()}")
        else:
            print(f"{filename}: File not found")

if __name__ == "__main__":
    main()
