import pandas as pd
from pathlib import Path

def load_raw_data(file_path):

    column_dtypes = {
        'Citizenship': 'object',
        # 'CapitalOutstanding': 'float64',  ← REMOVE THIS
        'Converted': 'object'
    }

    df = pd.read_csv(
        file_path,
        sep='|',
        na_values=[' ', ''],
        skipinitialspace=True,
        dtype=column_dtypes,     # CapitalOutstanding now read as object
        low_memory=False,
        decimal=','              # this now works properly
    )

    return df


def preprocess_data(df):
    """Cleans and prepares the DataFrame for analysis."""
    # ... (rest of the function)
    # The explicit TotalPremium/TotalClaims conversion is still good practice, 
    # but the decimal=',' should now handle these during the read_csv step.
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    
    # Ensure TotalPremium and TotalClaims are numeric (this should now succeed thanks to 'decimal=')
    df['TotalPremium'] = pd.to_numeric(df['TotalPremium'], errors='coerce')
    df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')
    
    # Simple cleanup of the Citizenship column which appears to have a lot of empty strings
    df['Citizenship'] = df['Citizenship'].fillna('Not specified').str.strip()

    return df

# ... (rest of the script)

def save_processed_data(df, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Processed data saved to: {output_path}")

if __name__ == "__main__":
    # Define file paths
    raw_file_path = Path("src/data/MachineLearningRating_v3.txt")
    processed_file_path = Path("src/data/processed/insurance_data.parquet")

    # Execute the pipeline
    if raw_file_path.exists():
        print("Starting data processing...")
        data_raw = load_raw_data(raw_file_path)
        data_processed = preprocess_data(data_raw)
        save_processed_data(data_processed, processed_file_path)
        print("Data processing complete.")
    else:
        print(f"Error: Raw data file not found at {raw_file_path}")