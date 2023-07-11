from unittest.mock import patch

from painkiller.repository.patient import PatientRepository
from painkiller.tables import PatientBase, PatientMeasurementBase


def test_get_by_id():
    with patch('painkiller.repository.patient.Repository.get_by') as get_by:
        get_by.return_value = PatientBase(patient_id=42)
        patient: PatientBase = PatientRepository.get_by_id(42)
        assert patient.patient_id == 42


def test_insert_patient():
    patient = PatientBase(first_name='John', second_name='Doe', age=30, condition_id=1)
    with patch('painkiller.repository.patient.Repository.insert') as mock_insert:
        mock_insert.return_value = True
        response = PatientRepository.insert(patient)
        assert response


def test_insert_patient_mesurement():
    patient_mesurement = PatientMeasurementBase(patient=42, measurement=42, value=42)
    with patch('painkiller.repository.patient.Repository.insert') as mock_insert:
        mock_insert.return_value = True
        response = PatientRepository.insert_measurement(patient_mesurement)
        assert response