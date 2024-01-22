class CongressusListResponse():
    def __init__(self, total, has_prev, prev_num, has_next, next_num, data) -> None:
        self.total: int = total
        self.has_prev: bool = has_prev
        self.prev_num: int = prev_num
        self.has_next: bool = has_next
        self.next_num: int = next_num
        self.data: list = data
