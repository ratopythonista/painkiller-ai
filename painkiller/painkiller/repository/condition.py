from painkiller.tables import ConditionBase
from painkiller.repository import Repository

class ConditionRepository(Repository):
    def get_by_name(name: str) -> ConditionBase:       
        return Repository.get_by(ConditionBase, ConditionBase.name == name)
