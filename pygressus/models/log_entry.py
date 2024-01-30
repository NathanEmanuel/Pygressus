from dataclasses import dataclass


@dataclass()
class LogEntry:
    type: str
    subject_type: str
    subject_id: int

    id: int = None
    text: str = None
    author_id: int = None
    created: str = None
    modified: str = None
    author: object = None
    subject: object = None
