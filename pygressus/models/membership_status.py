from dataclasses import dataclass


@dataclass()
class MembershipStatus:
    status_id: int

    id: int = None
    name: str = None
    member_from: str = None
    member_to: str = None
    archived: bool = None
    deceased: bool = None
