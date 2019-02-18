import unittest
from src.connection import Connection

class ConnectionTest(unittest.TestCase):
    def setUp(self):
        self.connection = Connection()

    def tearDown(self):
        self.connection.disconnect()

    def test_connection(self):
        self.assertEqual(self.connection.connect("189.6.76.118", 50046), 'ok')

    def test_receive(self):
        self.connection.connect("189.6.76.118", 50046)
        self.assertGreater(len(self.connection.receive()), 0)


if __name__ == '__main__':
    unittest.main()