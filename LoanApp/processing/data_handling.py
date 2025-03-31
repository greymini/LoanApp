# import os
# import sys
# import pandas as pd
# import joblib

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# from LoanApp.config import config

# #loading the dataset
# def load_dataset(file_name):
#     filepath = os.path.join(config.BASE_DIR, file_name)
#     _data = pd.read_csv(file_name)
#     return _data

# def save_pipeline(pipeline_to_save):
#     save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
#     joblib.dump(pipeline_to_save, 'loanmodel.pkl')
#     print("The model has been saved under the name of {config.MODEL_NAME}")

# def load_pipeline(pipeline_to_load):
#     save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
#     model_loaded = joblib.load(save_path)
#     print("Model has been loaded")
#     return model_loaded
    



import os
import sys
import pandas as pd
import joblib

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from LoanApp.config import config

# loading the dataset
def load_dataset(file_name):
    filepath = os.path.join(config.BASE_DIR, file_name)
    _data = pd.read_csv(filepath)  # Changed from file_name to filepath
    return _data

def save_pipeline(pipeline_to_save):
    # Make sure the directory exists
    os.makedirs(config.SAVE_MODEL_PATH, exist_ok=True)
    
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)  # Save to the correct path
    print(f"The model has been saved under the name of {config.MODEL_NAME}")  # Fixed f-string

def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH, pipeline_to_load)  # Use the parameter passed
    
    try:
        model_loaded = joblib.load(save_path)
        print("Model has been loaded")
        return model_loaded
    except FileNotFoundError:
        print(f"Model file not found at {save_path}")
        raise