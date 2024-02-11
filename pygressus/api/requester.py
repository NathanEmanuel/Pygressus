from enum import Enum

import requests
from requests.auth import AuthBase

from pygressus.api.base_client import BaseClient
from pygressus.api.paginated_response import PaginatedResponse
from pygressus.models.group_membership import GroupMembership
from pygressus.models.member import Member
from pygressus.models.webhook import ConceptualWebhook


class HTTPMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3


class Requester:
    """
    Intended as a base class for requester components. Can be instatiated but this
    generally should be limited to development- and testing environments.
    """

    class BearerAuth(AuthBase):
        def __init__(self, token):
            self.token = token

        def __call__(self, r):
            r.headers["Authorization"] = "Bearer " + self.token
            return r

    def __init__(self, client: BaseClient) -> None:
        """
        Requires the client to be injected so the requester component can obtain the API domain and token.
        """
        self.domain = client.get_domain()
        self.auth = self.BearerAuth(client.get_token())

    def authorized_request(
        self,
        method: HTTPMethod,
        path: str,
        params: dict = dict(),
        headers: dict = dict(),
        payload: dict = dict(),
    ) -> requests.Response:
        """
        Returns the response to an HTTP request.
        Throws error on bad status code.
        Path must start with a /
        """

        base_kwargs = {
            "url": self.domain + path,
            "params": params,
            "headers": headers,
            "auth": self.auth,
        }

        if method is HTTPMethod.GET:
            response = requests.get(**base_kwargs)
        elif method is HTTPMethod.POST:
            response = requests.post(**base_kwargs, json=payload)
        elif method is HTTPMethod.DELETE:
            response = requests.delete(**base_kwargs)
        else:
            raise ValueError("Unsupported HTTP method")

        response.raise_for_status()
        return response


class LogEntryRequester(Requester):
    def __init__(self, client: BaseClient, base_path) -> None:
        super().__init__(client)
        self.BASE_PATH = base_path

    def list(self, id: int):
        path = f"{self.BASE_PATH}/{id}/logs"

    def create(self, id: int):
        path = f"{self.BASE_PATH}/{id}/logs"

    def retrieve(self, id: int, log_id: int):
        path = f"{self.BASE_PATH}/{id}/logs/{log_id}"

    def update(self, id: int, log_id: int):
        path = f"{self.BASE_PATH}/{id}/logs/{log_id}"

    def delete(self, id: int, log_id: int):
        path = f"{self.BASE_PATH}/{id}/logs/{log_id}"


class MemberRequester(Requester):
    BASE_PATH = "/v30/members"

    def __init__(self, client: BaseClient) -> None:
        super().__init__(client)
        self.log_entry = LogEntryRequester(client, self.BASE_PATH)

    def list(self, page=None, page_size=None, order=None) -> PaginatedResponse:
        path = self.BASE_PATH
        params = {"page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(HTTPMethod.GET, path, params=params).json())

    def create(self):
        pass

    def retrieve(self, id: int) -> Member:
        path = self.BASE_PATH + f"/{id}"
        return Member(**self.authorized_request(HTTPMethod.GET, path).json())

    def update(self):
        pass

    def delete(self):
        pass

    def search(self, term, page=None, page_size=None, order=None) -> PaginatedResponse:
        path = self.BASE_PATH + "/search"
        params = {"term": term, "page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(HTTPMethod.GET, path, params=params).json())


class GroupMembershipRequester(Requester):
    BASE_PATH = "/v30/groups/memberships"

    def list(self, page=None, page_size=None, order=None) -> PaginatedResponse:
        params = {"page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(HTTPMethod.GET, self.BASE_PATH, params=params).json())

    def create(self, gms: GroupMembership):
        pass

    def retrieve(self, id: int):
        pass

    def update(self, id: int, gms: GroupMembership):
        pass

    def delete(self, id: int):
        pass


class SaleInvoiceRequester(Requester):
    BASE_PATH = "/v30/sale-invoices"

    def __init__(self, client: BaseClient) -> None:
        super().__init__(client)
        self.log_entry = LogEntryRequester(client, self.BASE_PATH)

    def list(self):
        path = self.BASE_PATH

    def create(self):
        path = self.BASE_PATH

    def retrieve(self, id: int):
        path = f"{self.BASE_PATH}/{id}"

    def update(self, id: int):
        path = f"{self.BASE_PATH}/{id}"

    def delete(self, id: int):
        path = f"{self.BASE_PATH}/{id}"

    def send(self, id: int):
        path = f"{self.BASE_PATH}/{id}/send"

    def remind(self, id: int):
        path = f"{self.BASE_PATH}/{id}/remind"

    def mark(self, id: int, isCollectible: bool):
        path = f"{self.BASE_PATH}/{id}"
        path = f"{path}/mark-collectible" if isCollectible else f"{path}/mark-uncollectible"

    def download(self, id: int):
        path = f"{self.BASE_PATH}/{id}/download"


class WebhookRequester(Requester):
    BASE_PATH = "/v30/webhooks"

    def list(self, page=None, page_size=None, order=None):
        path = self.BASE_PATH
        params = {"page": page, "page_size": page_size, "order": order}
        return PaginatedResponse(**self.authorized_request(HTTPMethod.GET, path, params=params).json())

    def create(self, new: ConceptualWebhook):
        path = self.BASE_PATH
        payload = {
            "url": new.url,
            "headers": new.headers,
            "signal": str(new.signal),
            "technical_contact_email": new.technical_contact_email,
            "http_basic_auth_enabled": new.http_basic_auth_enabled,
        }
        headers = {"Content-Type": "application/json"}
        return self.authorized_request(HTTPMethod.POST, path, payload=payload, headers=headers)

    def retrieve(self):
        pass

    def update(self):
        pass

    def delete(self, id: int):
        path = f"{self.BASE_PATH}/{id}"
        return self.authorized_request(HTTPMethod.DELETE, path)

    def list_calls(self, id: int) -> PaginatedResponse:
        path = f"{self.BASE_PATH}/{id}/calls"
        return PaginatedResponse(**self.authorized_request(HTTPMethod.GET, path).json())
