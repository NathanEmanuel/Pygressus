from dataclasses import dataclass


@dataclass()
class ElasticMember:
    _score: int = None
    id: int = None
    value: object = None
    name: object = None
    username: str = None
    type: object = None
    email: str = None
    phone_mobile: str = None
    phone_home: str = None
    address: str = None
    zip: str = None
    city: str = None
    province: str = None
    country_id: int = None
    country: str = None
    membership_start: str = None
    membership_end: str = None
    current_member_status_name: str = None
    current_member_status_id: int = None
    manager_uri: object = None
