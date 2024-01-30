from api.base_client import BaseClient
from api.requester import MemberRequester, GroupMembershipRequester, WebhookRequester


class Client(BaseClient):
    DOMAIN = "https://api.congressus.nl"

    def __init__(self, key) -> None:
        self.key = key
        self.member = MemberRequester(self)
        self.group_membership = GroupMembershipRequester(self)
        self.webhook = WebhookRequester(self)

    def get_domain(self) -> str:
        return self.DOMAIN

    def get_key(self) -> str:
        return self.key
