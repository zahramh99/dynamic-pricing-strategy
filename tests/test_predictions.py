import unittest
from src.predict import PricePredictor

class TestPredictions(unittest.TestCase):
    def setUp(self):
        self.predictor = PricePredictor()
        
    def test_prediction(self):
        price = self.predictor.predict_price(50, 25, "Economy", 30)
        self.assertIsInstance(price, float)
        
if __name__ == "__main__":
    unittest.main()