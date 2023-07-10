from unittest.mock import patch

from painkiller.tables import ConditionBase
from painkiller.repository.condition import ConditionRepository


def test_get_by_name():
    with patch('painkiller.repository.condition.Repository.get_by') as get_by:
        get_by.return_value = ConditionBase(name="teste")
        condition: ConditionBase = ConditionRepository.get_by_name("teste")
        assert condition.name == "teste"


def test_get_all():
    condition_list = ConditionRepository.get_all()
    assert isinstance(condition_list, list)