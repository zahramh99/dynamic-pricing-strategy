# main.py
from src.data_preprocessing import preprocess_data
from src.dynamic_pricing import calculate_dynamic_pricing
from src.model_training import train_model
import pandas as pd

def main():
    # Load data
    data = pd.read_csv("data/dynamic_pricing.csv")
    
    # Preprocess data
    data = preprocess_data(data)
    
    # Apply dynamic pricing
    data = calculate_dynamic_pricing(data)
    
    # Train and evaluate model
    model = train_model()
    
    print("Dynamic pricing pipeline executed successfully!")
    return data

if __name__ == "__main__":
    main()