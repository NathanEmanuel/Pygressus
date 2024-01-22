from querier import MemberQuerier


class Client:
    DOMAIN = 'https://api.congressus.nl'

    def __init__(self, key, version='v30') -> None:
        self.key = key
        self.version: str = version
        self.url = f'{self.DOMAIN}/{self.version}'
        self.member = MemberQuerier(self.url, self.key)


if __name__ == "__main__":
    key = 0
    client = Client(key)
    response = client.member.list()
    print(response.data)
