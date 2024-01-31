from unittest import TestCase

from requests.exceptions import HTTPError

from __init__ import pygressus  # purely to avoid a ModuleNotFoundError when __name__ == "__main__"
from pygressus.client import Client
from pygressus.api.requester import MemberRequester


class MemberRequesterTest(TestCase):
    """
    This only tests if the request is sent correctly. It doensn't test how the
    answer is handled because that would require either a token or a mock.
    """

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
