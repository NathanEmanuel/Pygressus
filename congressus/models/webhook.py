from dataclasses import dataclass
from enum import StrEnum


class Signal(StrEnum):
    MEMBER = "member"
    MEMBER_ADDED = "member_added"
    MEMBER_UPDATED = "member_updated"
    MEMBER_DELETED = "member_deleted"
    EVENT = "event"
    EVENT_ADDED = "event_added"
    EVENT_UPDATED = "event_updated"
    EVENT_DELETED = "event_deleted"
    EVENT_PARTICIPATION = "event_participation"
    EVENT_PARTICIPATION_ADDED = "event_participation_added"
    EVENT_PARTICIPATION_UPDATED = "event_participation_updated"
    EVENT_PARTICIPATION_DELETED = "event_participation_deleted"
    SALE_INVOICE = "sale_invoice"
    SALE_INVOICE_ADDED = "sale_invoice_added"
    SALE_INVOICE_UPDATED = "sale_invoice_updated"
    SALE_INVOICE_DELETED = "sale_invoice_deleted"


@dataclass()
class ConceptualWebhook:
    url: str
    headers: object
    signal: StrEnum
    technical_contact_email: str
    http_basic_auth_enabled: bool


@dataclass()
class Webhook(ConceptualWebhook):
    id: int
    version: str
    http_basic_auth_key: str
