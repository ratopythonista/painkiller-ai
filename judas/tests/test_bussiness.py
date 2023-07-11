import pytest
from unittest.mock import patch, MagicMock

from fastapi.exceptions import HTTPException

from jonas.bussiness import ModelBussines


def test_returns_binary_model():
    with patch("jonas.services.filesystem.FileSystem.insert") as insert_mock:
        insert_mock.return_value = "123123123"
        ModelBussines.train()
        assert True


def test_valid_model_id():
    with patch("jonas.services.filesystem.FileSystem.get_recall") as get_recall_mock:
        get_recall_mock.return_value = "[1 2 3]"
        assert ModelBussines.get_metrics("123124123") == "[1 2 3]"


# Tests that the method raises an exception when given an invalid model_id
def test_invalid_model_id():
    model_id = 'invalid_model_id'
    predict_data = {'measurement_1': 1, 'measurement_2': 2}
    with pytest.raises(Exception):
        ModelBussines.predict(model_id, predict_data)