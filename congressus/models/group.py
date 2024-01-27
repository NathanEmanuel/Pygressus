from dataclasses import dataclass


@dataclass()
class Group:
    id: int
    slug: str
    start: str

    folder_id: int = None
    folder: object = None
    name: str = None
    address: object = None
    postal_adress: object = None
    description: str = None
    description_short: str = None
    email: str = None
    url: str = None
    logo: object = None
    path: str = None
    published: bool = None
    end: str = None
    memo: str = None
