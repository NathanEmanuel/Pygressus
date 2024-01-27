class ElasticMember:
    def __init__(self, **kwargs) -> None:
        self._score = kwargs['_score']
        self.id = kwargs['id']
        self.value = kwargs['value']
        self.name = kwargs['name']
