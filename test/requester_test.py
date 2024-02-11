from unittest import TestCase

from requests.exceptions import HTTPError

from __init__ import (
    pygressus,
)  # purely to avoid a ModuleNotFoundError when __name__ == "__main__"
from pygressus.client import Client
from pygressus.api.requester import (
    HTTPMethod,
    Requester,
    MemberRequester,
    GroupMembershipRequester,
    SaleInvoiceRequester,
    WebhookRequester,
)


class RequesterTest(TestCase):
    """
    This only tests if the request is sent correctly. It doensn't test how the
    answer is handled because that would require either a token or a mock.
    """

    EXCEPTION = HTTPError
    PATTERN = "401 Client Error: UNAUTHORIZED .*"

    def setUp(self):
        self.client = Client("TestToken")
        self.requester = Requester(self.client)

    def test_authorized_request(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.authorized_request(HTTPMethod.GET, "")


class MemberRequesterTest(TestCase):

    EXCEPTION = HTTPError
    PATTERN = "401 Client Error: UNAUTHORIZED .*"

    def setUp(self):
        self.client = Client("TestToken")
        self.requester = MemberRequester(self.client)

    def test_list(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.list()

    def test_create(self):
        pass  # not doing TDD

    def test_retrieve(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.retrieve(0)

    def test_update(self):
        pass  # not doing TDD

    def test_delete(self):
        pass  # not doing TDD

    def test_search(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.search("")

    def test_log_entry_list(self):
        self.requester.log_entry.list(0)

    def test_log_entry_create(self):
        self.requester.log_entry.create(0)

    def test_log_entry_retrieve(self):
        self.requester.log_entry.retrieve(0, 0)

    def test_log_entry_update(self):
        self.requester.log_entry.update(0, 0)

    def test_log_entry_delete(self):
        self.requester.log_entry.delete(0, 0)


class GroupMembershipRequesterTest(TestCase):
    EXCEPTION = HTTPError
    PATTERN = "401 Client Error: UNAUTHORIZED .*"

    def setUp(self):
        self.client = Client("TestToken")
        self.requester = GroupMembershipRequester(self.client)

    def test_list(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.list()

    def test_create(self):
        pass

    def test_retrieve(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass


class SaleInvoiceRequesterTest(TestCase):
    EXCEPTION = HTTPError
    PATTERN = "401 Client Error: UNAUTHORIZED .*"

    def setUp(self):
        self.client = Client("TestToken")
        self.requester = SaleInvoiceRequester(self.client)

    def test_list(self):
        self.requester.list()

    def test_create(self):
        self.requester.create()

    def test_retrieve(self):
        self.requester.retrieve(0)

    def test_update(self):
        self.requester.update(0)

    def test_delete(self):
        self.requester.delete(0)

    def test_send(self):
        self.requester.send(0)

    def test_remind(self):
        self.requester.remind(0)

    def test_mark(self):
        self.requester.mark(0, True)
        self.requester.mark(0, False)

    def test_download(self):
        self.requester.download(0)

    def test_log_entry_list(self):
        self.requester.log_entry.list(0)

    def test_log_entry_create(self):
        self.requester.log_entry.create(0)

    def test_log_entry_retrieve(self):
        self.requester.log_entry.retrieve(0, 0)

    def test_log_entry_update(self):
        self.requester.log_entry.update(0, 0)

    def test_log_entry_delete(self):
        self.requester.log_entry.delete(0, 0)


class WebhookRequesterTest(TestCase):
    EXCEPTION = HTTPError
    PATTERN = "401 Client Error: UNAUTHORIZED .*"

    def setUp(self):
        self.client = Client("TestToken")
        self.requester = WebhookRequester(self.client)

    def test_list(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.list()

    def test_create(self):
        pass

    def test_retrieve(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.delete(0)

    def test_list_calls(self):
        with self.assertRaisesRegex(self.EXCEPTION, self.PATTERN):
            self.requester.list_calls(0)
