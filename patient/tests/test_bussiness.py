import pytest
from unittest.mock import patch, MagicMock

from fastapi.exceptions import HTTPException

from patient.presentation.schemas import Patient
from patient.bussiness import PatientBussiness, PatientRepository, ConditionBussiness


def test_insert_patient_successfully():
    patient = Patient(first_name='John', second_name='Doe', age=30, condition_id=1)
    with patch('patient.bussiness.PatientRepository.insert') as mock_insert:
        mock_insert.return_value = True
        response = PatientBussiness.insert(patient)
        assert response.request == 'Insert Patient'
        assert response.response == 'Success'

def test_retrieve_patient_by_id_success():
    with patch('patient.bussiness.PatientRepository.get_by_id') as mock_get:
        patient_id = 42
        mock_get.return_value = Patient(first_name='John', second_name='Doe', age=30, condition_id=1)

        retrieved_patient = PatientBussiness.get_by_id(patient_id)

        assert retrieved_patient.first_name == 'John'
        assert retrieved_patient.second_name == 'Doe'
        assert retrieved_patient.age == 30

def test_get_all_returns_list():
    conditions = ConditionBussiness.get_all()
    assert isinstance(conditions, list)


def test_insert_patient_failure():
    patient = Patient(first_name='John', second_name='Doe', age=30, condition_id=1)
    with pytest.raises(HTTPException):
        PatientRepository.insert = MagicMock(return_value=False)
        PatientBussiness.insert(patient)

def test_retrieve_patient_by_id_failure():
    with pytest.raises(HTTPException):
        PatientRepository.get_by_id = MagicMock(return_value=None)
        PatientBussiness.get_by_id(1)