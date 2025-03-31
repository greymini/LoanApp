import os 
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATAPATH = os.path.join(BASE_DIR, "datasets")


TRAIN_FILE = os.path.join(DATAPATH, "train_loan.csv")
TEST_FILE = os.path.join(DATAPATH, "test_loan.csv")


SAVE_MODEL_PATH = os.path.join(BASE_DIR, "trained_models")
MODEL_NAME = "loanmodel.pkl"


TARGET = 'Loan_Status'

FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 
            'Self_Employed','ApplicantIncome', 
            'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term', 
            'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome','LoanAmount','Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 
                'Education', 'Self_Employed', 'Credit_History', 
                'Property_Area']

FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 
                'Education', 'Self_Employed', 'Credit_History', 
                'Property_Area']

FEATURES_TO_MODIFY = 'ApplicantIncome'
FEATURES_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome']

LOG_FEATURES = ['ApplicantIncome','LoanAmount']