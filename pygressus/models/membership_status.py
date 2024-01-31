from dataclasses import dataclass
from typing import Optional


@dataclass()
class MembershipStatus:
    status_id: int

    id: Optional[int] = None
    name: Optional[str] = None
    member_from: Optional[str] = None
    member_to: Optional[str] = None
    archived: Optional[bool] = None
    deceased: Optional[bool] = None
