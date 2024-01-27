import os

from dotenv import load_dotenv

from base_client import BaseClient
from querier import MemberQuerier


class Client(BaseClient):
    DOMAIN = "https://api.congressus.nl"

    def __init__(self, key) -> None:
        self.key = key
        self.member = MemberQuerier(self)

    def get_domain(self) -> str:
        return self.DOMAIN

    def get_key(self) -> str:
        return self.key


if __name__ == "__main__":
    load_dotenv()
    client = Client(os.getenv("KEY"))
    print(client.member.list().total)
    print(client.member.search("Nathan Djojomoenawie").total)
