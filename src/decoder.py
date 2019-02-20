import binascii

class Decoder:
    def __init__(self):
        self.start_packet = 'c6'
        self.end_packet = '6b'
        self.end_transmission = '21'

        self.decoder_table = {
            '11110':'0000',
            '01001':'0001',
            '10100':'0010',
            '10101':'0011',
            '01010':'0100',
            '01011':'0101',
            '01110':'0110',
            '01111':'0111',
            '10010':'1000',
            '10011':'1001',
            '10110':'1010',
            '10111':'1011',
            '11010':'1100',
            '11011':'1101',
            '11100':'1110',
            '11101':'1111'
        }

        self.hex_table = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'a': '1010',
            'b': '1011',
            'c': '1100',
            'd': '1101',
            'e': '1110',
            'f': '1111'
        }

        # self.client.connect("189.6.76.118", 50046)


    def divide(self, rcv_bytes):
        strbytes = [x.decode('utf-8') for x in rcv_bytes]
        packet = ''
        packets = []

        for s in strbytes:
            if s == self.end_packet:
                packets.append(packet)

            elif s == self.start_packet:
                packet = ''

            elif s == self.end_transmission:
                packets.append(packet)
                return packets

            else:
                packet += s

    def transform(self, packet):
        bit_str = ''
        converted_str = ''
        c = 0
        for x in packet:
            bit_str += self.hex_table[x]

        str_len = len(bit_str)
        for i in range(int(len(bit_str)/5)):
            converted_str += self.decoder_table[bit_str[:5]]
            bit_str = bit_str[5:].strip()

        return converted_str

    def getKeybyValue(self, dict, value):
        for k, v in dict.items():
            if v == value:
                return k

    def decode(self, bit_str):
        converted_str = ''
        asc_str = ''

        for i in range(int(len(bit_str) / 4)):
            converted_str += self.getKeybyValue(self.hex_table, bit_str[:4])
            bit_str = bit_str[4:].strip()

        for i in range(int(len(converted_str) / 2)):
            asc_str += bytearray.fromhex(converted_str[:2]).decode()
            converted_str = converted_str[2:].strip()

        return asc_str.strip()
