from pygressus.api.base_client import BaseClient
from pygressus.api.requester import (
    MemberRequester,
    GroupMembershipRequester,
    WebhookRequester,
)


class Client(BaseClient):
    DOMAIN = "https://api.congressus.nl"

    def __init__(self, token) -> None:
        self.token = token
        self.member = MemberRequester(self)
        self.group_membership = GroupMembershipRequester(self)
        self.webhook = WebhookRequester(self)

    def get_domain(self) -> str:
        return self.DOMAIN

    def get_token(self) -> str:
        return self.token
