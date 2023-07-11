from painkiller.repository.measurement import MeasurementRepository


def test_get_all():
    condition_list = MeasurementRepository.get_all()
    assert isinstance(condition_list, list)