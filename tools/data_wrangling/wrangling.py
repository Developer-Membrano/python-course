# Import necessary libraries
import pandas as pd

# Load your data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Handle missing values
def handle_missing_values(data, strategy="mean"):
    if strategy == "mean":
        data = data.fillna(data.mean())
    elif strategy == "median":
        data = data.fillna(data.median())
    elif strategy == "mode":
        data = data.fillna(data.mode().iloc[0])
    return data

# Normalize the data
def normalize_data(data):
    return (data - data.min()) / (data.max() - data.min())

# Main function to use the tool
def main():
    file_path = r"E:/Users/Angie Villalba/Documents/Kenny/data_set_survey.csv"  # replace with your file path
    data = load_data(file_path)
    print("Data before handling missing values: ")
    print(data.head())
    
    # Handle missing values
    data = handle_missing_values(data, strategy="mean")
    print("Data after handling missing values: ")
    print(data.head())
    
    # Normalize the data
    data = normalize_data(data)
    print("Data after normalization: ")
    print(data.head())

if __name__ == "__main__":
    main()
