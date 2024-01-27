from dataclasses import dataclass


@dataclass()
class MemberStatus:
    name: str

    id: int = None
    description: str = None
    archived: bool = None
    hidden: bool = None
    deceased: bool = None
    order: int = None
