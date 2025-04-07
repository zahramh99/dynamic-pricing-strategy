from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
from data_preprocessing import preprocess_data

def train_model():
    # Load and preprocess data
    data = pd.read_csv("../data/dynamic_pricing.csv")
    data = preprocess_data(data)
    
    # Prepare features and target
    X = data[["Number_of_Riders", "Number_of_Drivers", "Vehicle_Type", "Expected_Ride_Duration"]]
    y = data["adjusted_ride_cost"]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
    
    return model

if __name__ == "__main__":
    model = train_model()
    # Save model if needed
    # import joblib
    # joblib.dump(model, 'model.pkl')