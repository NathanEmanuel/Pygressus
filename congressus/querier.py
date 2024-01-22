import requests

from response import CongressusListResponse

class Querier:
    def __init__(self, url, key) -> None:
        self.url = url
        self.key = key
        self.auth_header = {'Authorization': f'Bearer {self.key}'}

class MemberQuerier(Querier):
    ENDPOINT_SUFFIX = '/members'

    def __init__(self, url, key) -> None:
        super().__init__(url + self.ENDPOINT_SUFFIX, key)

    def list(self) -> CongressusListResponse:
        headers = self.auth_header
        params = {}

        response = requests.get(self.url, params=params, headers=headers)
        response.raise_for_status()

        return CongressusListResponse(**response.json())

    @staticmethod
    def create():
        pass

    @staticmethod
    def retrieve():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    @staticmethod
    def search():
        pass