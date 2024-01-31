from dataclasses import dataclass
from typing import Optional


@dataclass
class GroupMembership:
    member_id: int
    start: str
    group_id: int

    id: Optional[int] = None
    end: Optional[str] = None
    function: Optional[str] = None
    may_edit_profile: Optional[bool] = None
    may_manage_memberships: Optional[bool] = None
    may_manage_storage_objects: Optional[bool] = None
    is_self_enroll: Optional[bool] = None
    order_type: Optional[str] = None
    order: Optional[int] = None
    group: Optional[object] = None
