from dataclasses import dataclass


@dataclass
class GroupMembership:
    member_id: int
    start: str
    group_id: int

    id: int = None
    end: str = None
    function: str = None
    may_edit_profile: bool = None
    may_manage_memberships: bool = None
    may_manage_storage_objects: bool = None
    is_self_enroll: bool = None
    order_type: str = None
    order: int = None
    group: object = None
