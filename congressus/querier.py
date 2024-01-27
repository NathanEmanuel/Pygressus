import requests

from base_client import BaseClient
from response import PaginatedResponse
from models.elastic_member import ElasticMember


class Querier:
    def __init__(self, client: BaseClient) -> None:
        self.domain = client.get_domain()
        self.auth_header = {"Authorization": f"Bearer {client.get_key()}"}

    def authorized_request(self, path: str, params: dict = dict(), headers: dict = dict()) -> dict:
        """Returns the response to an HTTP request.
        Throws error on bad status code.
        Path must start with a /
        """
        url = self.domain + path
        headers.update(self.auth_header)

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return response.json()


class MemberQuerier(Querier):
    def list(self) -> PaginatedResponse:
        path = "/v30/members"
        return PaginatedResponse(**self.authorized_request(path))

    def create():
        pass

    def retrieve():
        pass

    def update():
        pass

    def delete():
        pass

    def search(self, term):
        path = "/v30/members/search"
        params = {"term": term}
        return PaginatedResponse(**self.authorized_request(path, params=params))
