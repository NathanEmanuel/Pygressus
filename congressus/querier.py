import requests

from base_client import BaseClient
from response import PaginatedResponse
from models.elastic_member import ElasticMember
from models.group_membership import GroupMembership


class Querier:
    """
    Intended as a base class for queriers. Can be instatiated but this
    generally should be limited to development- and testing environments.
    """

    def __init__(self, client: BaseClient) -> None:
        """
        Requires the client to be injected so the querier can obtain the API domain and -key.
        """
        self.domain = client.get_domain()
        self.auth_header = {"Authorization": f"Bearer {client.get_key()}"}

    def authorized_request(self, path: str, params: dict = dict(), headers: dict = dict()) -> dict:
        """
        Returns the response to an HTTP request.
        Throws error on bad status code.
        Path must start with a /
        """
        url = self.domain + path
        headers.update(self.auth_header)

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return response.json()


class MemberQuerier(Querier):
    def list(self, page=None, page_size=None, order=None) -> PaginatedResponse:
        path = "/v30/members"
        params = {'page': page, 'page_size': page_size, 'order': order}
        return PaginatedResponse(**self.authorized_request(path))

    def create():
        pass

    def retrieve():
        pass

    def update():
        pass

    def delete():
        pass

    def search(self, term, page=None, page_size=None, order=None):
        path = "/v30/members/search"
        params = {'term': term, 'page': page, 'page_size': page_size, 'order': order}
        return PaginatedResponse(**self.authorized_request(path, params=params))

class GroupMembershipQuerier(Querier):
    BASE_PATH = '/v30/groups/memberships'

    def list(self)-> PaginatedResponse:
        return PaginatedResponse(**self.authorized_request(self.BASE_PATH))
    
    def create(self, gms: GroupMembership):
        pass

    def retrieve(self, id: int):
        pass

    def update(self, id: int, gms: GroupMembership):
        pass

    def delete(self, id: int):
        pass
