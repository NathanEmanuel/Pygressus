from unittest import TestCase

from __init__ import pygressus  # purely to avoid a ModuleNotFoundError when __name__ == "__main__"
from pygressus.client import Client


class ClientTest(TestCase):
    def test_init(self):
        token = "ExampleToken"
        client = Client(token)

        self.assertEqual("https://api.congressus.nl", client.get_domain())
        self.assertEqual("ExampleToken", client.get_token())
        self.assertIsNotNone(client.member)
        self.assertIsNotNone(client.group_membership)
        self.assertIsNotNone(client.webhook)
