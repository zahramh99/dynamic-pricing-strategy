import numpy as np
from model_training import train_model
import joblib

class PricePredictor:
    def __init__(self, model_path=None):
        """Initialize the price predictor with optional saved model path"""
        try:
            if model_path:
                self.model = joblib.load(model_path)
            else:
                self.model = train_model()
        except Exception as e:
            print(f"Model loading error: {str(e)}")
            raise

    def predict_price(self, number_of_riders, number_of_drivers, vehicle_type, expected_duration):
        """
        Predict ride price based on input parameters
        
        Args:
            number_of_riders: int - Current number of riders in area
            number_of_drivers: int - Current number of available drivers
            vehicle_type: str - "Premium" or "Economy"
            expected_duration: float - Expected ride duration in minutes
            
        Returns:
            float: Predicted price or None if error occurs
        """
        try:
            # Validate and normalize vehicle type
            vehicle_type = vehicle_type.lower()
            if vehicle_type not in ["premium", "economy"]:
                raise ValueError("Vehicle type must be 'Premium' or 'Economy'")
            
            # Validate numerical inputs
            for param, name in [(number_of_riders, "number_of_riders"),
                               (number_of_drivers, "number_of_drivers"),
                               (expected_duration, "expected_duration")]:
                if not isinstance(param, (int, float)) or param < 0:
                    raise ValueError(f"{name} must be a positive number")
            
            # Convert to numeric features
            vehicle_type_numeric = 1 if vehicle_type == "premium" else 0
            input_data = np.array([[number_of_riders, number_of_drivers, 
                                  vehicle_type_numeric, expected_duration]])
            
            # Make prediction
            return float(self.model.predict(input_data)[0])
            
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            return None

if __name__ == "__main__":
    try:
        # Initialize predictor
        predictor = PricePredictor()
        
        # Example prediction
        predicted_price = predictor.predict_price(
            number_of_riders=50,
            number_of_drivers=25,
            vehicle_type="Economy",
            expected_duration=30
        )
        
        if predicted_price is not None:
            print(f"Predicted price: ${predicted_price:.2f}")
        else:
            print("Failed to generate prediction")
            
    except Exception as e:
        print(f"Application error: {str(e)}")