import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    """Preprocess the dynamic pricing data"""
    # Identify numeric and categorical features
    numeric_features = data.select_dtypes(include=['float', 'int']).columns
    categorical_features = data.select_dtypes(include=['object']).columns
    
    # Handle missing values
    data[numeric_features] = data[numeric_features].fillna(data[numeric_features].mean())
    
    # Handle outliers
    for feature in numeric_features:
        Q1 = data[feature].quantile(0.25)
        Q3 = data[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        data[feature] = np.where((data[feature] < lower_bound) | (data[feature] > upper_bound),
                                data[feature].mean(), data[feature])
    
    # Handle categorical features
    data[categorical_features] = data[categorical_features].fillna(data[categorical_features].mode().iloc[0])
    
    # Convert vehicle type to numeric
    data["Vehicle_Type"] = data["Vehicle_Type"].map({"Premium": 1, "Economy": 0})
    
    return data