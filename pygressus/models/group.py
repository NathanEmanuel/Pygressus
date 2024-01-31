from dataclasses import dataclass
from typing import Optional


@dataclass()
class Group:
    id: int
    slug: str
    start: str

    folder_id: Optional[int] = None
    folder: Optional[object] = None
    name: Optional[str] = None
    address: Optional[object] = None
    postal_adress: Optional[object] = None
    description: Optional[str] = None
    description_short: Optional[str] = None
    email: Optional[str] = None
    url: Optional[str] = None
    logo: Optional[object] = None
    path: Optional[str] = None
    published: Optional[bool] = None
    end: Optional[str] = None
    memo: Optional[str] = None
