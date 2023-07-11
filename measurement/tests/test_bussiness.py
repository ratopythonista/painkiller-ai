import pytest
from unittest.mock import patch, MagicMock

from fastapi.exceptions import HTTPException

from patient.presentation.schemas import Patient
from measurement.bussiness import MeasurementBussiness


def test_insert_successfully():
    with patch('measurement.bussiness.PatientRepository.insert_measurement') as mock_insert:
        mock_insert.return_value = True
        response = MeasurementBussiness.insert(1, 1, 10.0)
        assert response.request == 'Insert Patient Measurement'
        assert response.response == 'Success'

def test_insert_patient_not_found():
    with pytest.raises(HTTPException) as exc:
        with patch('measurement.bussiness.PatientRepository.insert_measurement') as mock_insert:
            mock_insert.return_value = False
            MeasurementBussiness.insert(999, 1, 10.0)
        assert exc.value.status_code == 404
        assert exc.value.detail == 'Resources not found'

def test_get_all_returns():
    result = MeasurementBussiness.get_all()
    assert isinstance(result, list)