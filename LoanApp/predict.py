# import pandas as pd
# import joblib
# import numpy as np

# from config import config
# from processing.data_handling import load_dataset, load_pipeline

# _model = load_pipeline(config.MODEL_NAME)

# def generate_predictions():
#     test_data = load_dataset(config.TEST_FILE)
#     pred = _model.predict(test_data[config.FEATURES])
#     result = {"Predictions": pred}
#     return result

# if __name__ == "__main__":
#     generate_predictions()

import pandas as pd
import joblib
import numpy as np
import os

from config import config
from processing.data_handling import load_dataset, load_pipeline

try:
    _model = load_pipeline(config.MODEL_NAME)
except FileNotFoundError:
    print("Model file not found. Please train the model first or check if the file path is correct.")
    exit(1)

def generate_predictions():
    test_data = load_dataset(config.TEST_FILE)
    pred = _model.predict(test_data[config.FEATURES])
    result = {"Predictions": pred}
    print(f"Generated predictions for {len(pred)} samples")
    return result

if __name__ == "__main__":
    print(generate_predictions())