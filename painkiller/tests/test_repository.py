from unittest.mock import patch

from painkiller.tables import PatientBase
from painkiller.repository import Repository


def test_insert():
    with patch('painkiller.repository.Session.add') as session_add:
        session_add.return_value = True
        patient = PatientBase(first_name='John', second_name='Doe', age=30, condition_id=1)
        assert Repository.insert(patient) == True


def test_get_by():
    patient: PatientBase = Repository.get_by(PatientBase, PatientBase.patient_id == 1)
    assert patient.patient_id == 1


def test_get_all():
    patient = Repository.get_all(PatientBase)
    assert isinstance(patient, list)