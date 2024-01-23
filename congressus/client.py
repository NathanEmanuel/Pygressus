import os

from dotenv import load_dotenv

from querier import MemberQuerier


class Client:
    DOMAIN = 'https://api.congressus.nl'

    def __init__(self, key, version='v30') -> None:
        self.key = key
        self.version: str = version
        self.url = f'{self.DOMAIN}/{self.version}'
        self.member = MemberQuerier(self.url, self.key)


if __name__ == "__main__":
    load_dotenv()
    client = Client(os.getenv('KEY'))
    response = client.member.list()
    print(response.data)
