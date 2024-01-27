import os

from congressus.api.base_client import BaseClient
from congressus.api.querier import MemberQuerier, GroupMembershipQuerier, WebhookQuerier


class Client(BaseClient):
    DOMAIN = "https://api.congressus.nl"

    def __init__(self, key) -> None:
        self.key = key
        self.member = MemberQuerier(self)
        self.group_membership = GroupMembershipQuerier(self)
        self.webhook = WebhookQuerier(self)

    def get_domain(self) -> str:
        return self.DOMAIN

    def get_key(self) -> str:
        return self.key
