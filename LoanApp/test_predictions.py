# import pytest

# from pathlib import Path
# import os
# import sys

# PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
# sys.path.append(str(PACKAGE_ROOT))
# from .config import config
# from LoanApp.config import config
# from LoanApp.processing.data_handling import load_dataset
# from LoanApp.predict import generate_predictions



# @pytest.fixture
# def single_prediction():
#     test_dataset = load_dataset(config.TEST_FILE)
#     single_row = test_dataset[0:1]
#     result = generate_predictions(single_row)
#     return result

# def test_single_pred_not_none(single_prediction):      
#     assert single_prediction is not None

# def test_single_pred_str_type(single_prediction):        
#     assert isinstance(single_prediction.get('prediction')[0],str)

# def test_single_pred_validate(single_prediction):
#     assert single_prediction.get('prediction')[0] == 'Y'



import pytest
from pathlib import Path
import os
import sys

# Add the parent directory to the system path to make the LoanApp package importable
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# Use only one style of import, not both
from LoanApp.config import config
from LoanApp.processing.data_handling import load_dataset
from LoanApp.predict import generate_predictions


@pytest.fixture
def single_prediction():
    """
    Fixture to generate a prediction for a single row of test data.
    """
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[0:1]
    result = generate_predictions(single_row)
    return result


def test_single_pred_not_none(single_prediction):
    """Test that the prediction is not None."""
    assert single_prediction is not None


def test_single_pred_str_type(single_prediction):
    """Test that the prediction is of string type."""
    assert isinstance(single_prediction.get('prediction')[0], str)


def test_single_pred_validate(single_prediction):
    """Test that the prediction matches the expected value 'Y'."""
    assert single_prediction.get('prediction')[0] == 'Y'