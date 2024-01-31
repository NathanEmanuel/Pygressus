from dataclasses import dataclass
from typing import Optional


@dataclass()
class MemberStatus:
    name: str

    id: Optional[int] = None
    description: Optional[str] = None
    archived: Optional[bool] = None
    hidden: Optional[bool] = None
    deceased: Optional[bool] = None
    order: Optional[int] = None
