from dataclasses import dataclass
from typing import Optional


@dataclass()
class LogEntry:
    type: str
    subject_type: str
    subject_id: int

    id: Optional[int] = None
    text: Optional[str] = None
    author_id: Optional[int] = None
    created: Optional[str] = None
    modified: Optional[str] = None
    author: Optional[object] = None
    subject: Optional[object] = None
