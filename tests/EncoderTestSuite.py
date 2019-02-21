import unittest
from src.encoder import Encoder


class EncoderTest(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()

    def test_turnAscToByte(self):
        self.assertEqual(self.encoder.turnAscToByte("BsB_KaO"), '4273425f4b614f5f')

    def test_encode(self):
        self.assertEqual(
            self.encoder.encode('4273425f4b614f5f'),
            ['551f55517d', '55dc95757d'])

    def test_xor(self):
        self.assertEqual(self.encoder.xor(b'55', b'13'), b'46')

    def test_makePacket(self):
        self.assertEqual(
            self.encoder.makePacket(['551f55517d', '55dc95757d']),
            b'\xc6F\x0cFBnk\xc6F\xcf\x86fn!')
