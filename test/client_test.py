from unittest import TestCase

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
