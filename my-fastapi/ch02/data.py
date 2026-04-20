from ch02.model import Champion, RoleEnum
from typing import List

champions = [
    Champion(id=1, name="브라이어", release_date="2023-09-14", role=RoleEnum.FIGHTER),
    Champion(id=2, name="모데카이저", release_date="2010-02-24", role=RoleEnum.MAGE)
]

def get_champion() -> List[Champion]:
    return champions