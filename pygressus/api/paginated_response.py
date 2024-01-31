from typing import Optional


class PaginatedResponse:
    def __init__(
        self,
        total=None,
        has_prev=None,
        prev_num=None,
        has_next=None,
        next_num=None,
        data=None,
    ) -> None:
        self.total: Optional[int] = total
        self.has_prev: Optional[bool] = has_prev
        self.prev_num: Optional[int] = prev_num
        self.has_next: Optional[bool] = has_next
        self.next_num: Optional[int] = next_num
        self.data: Optional[list] = data
