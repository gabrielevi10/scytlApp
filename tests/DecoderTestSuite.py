import unittest
from src.decoder import Decoder

class DecoderTest(unittest.TestCase):
    def setUp(self):
        self.decoder = Decoder()

    def test_divisor(self):
        d = []
        d.append('56d755295c')
        d.append('a7955a569e')
        self.assertEqual(
            self.decoder.divide([b'56', b'd7', b'55', b'29', b'5c', b'6b', b'c6', b'a7', b'95', b'5a', b'56', b'9e', b'21']), d)

    def test_transform(self):
        self.assertEqual(self.decoder.transform('5754955e9e'), '01001111010000010100101100100000')
        self.assertEqual(self.decoder.transform('551755529e'), '01000010010100110100001000100000')

    def test_decode(self):
        self.assertEqual(
            self.decoder.decode(
                self.decoder.transform('5754955e9e') +
                self.decoder.transform('551755529e')), 'OAK BSB')
