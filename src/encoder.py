import binascii

class Encoder:
    def __init__(self):
        self.start_packet = b'c6'
        self.end_packet = b'6b'
        self.end_transmission = b'21'

        self.encoder_table = {
            '0': '11110',
            '1': '01001',
            '2': '10100',
            '3': '10101',
            '4': '01010',
            '5': '01011',
            '6': '01110',
            '7': '01111',
            '8': '10010',
            '9': '10011',
            'a': '10110',
            'b': '10111',
            'c': '11010',
            'd': '11011',
            'e': '11100',
            'f': '11101'
        }

        self.hex_table = {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'a',
            '1011': 'b',
            '1100': 'c',
            '1101': 'd',
            '1110': 'e',
            '1111': 'f'
        }

    # Converts ASCII to corresponding hexadecimal value
    def turnAscToByte(self, asc_str):
        while len(asc_str) % 4 is not 0:
            asc_str += '_'
        return binascii.hexlify(asc_str.encode()).decode()

    # Encode the message using the protocol X
    def encode(self, msg_byte):
        c = 1
        bit_list = []
        aux = ''
        converted_str = ''
        converted_list = []

        for b in msg_byte:
            # 4 bytes -> 5 bytes
            aux += self.encoder_table[b]
            if c % 8 == 0:
                bit_list.append(aux)
                aux = ''
            c += 1

        for i in bit_list:
            for j in range(int(len(i) / 4)):
                # bin -> hexadecimal
                converted_str += self.hex_table[i[:4]]
                i = i[4:].strip()
            converted_list.append(converted_str)
            converted_str = ''

        return converted_list

    # Does a xor between bytes
    # Found in: https://stackoverflow.com/questions/17404690/how-to-xor-two-hex-strings-so-that-each-byte-is-xored-separately
    def xor(self, b, prime_factor):
        return binascii.hexlify(
            bytes(c1 ^ c2 for c1, c2 in zip(
                binascii.unhexlify(b[-len(prime_factor):]), binascii.unhexlify(prime_factor))))

    # Adds start packet, end packet and end transmission to message
    # Concatenates all bytes into one byte array to send 
    def makePacket(self, converted_list):
        packet = []
        for i in converted_list:
            packet.append(self.start_packet)
            for j in range(int(len(i) / 2)):
                packet.append(self.xor(i[:2], b'13'))
                i = i[2:].strip()
            packet.append(self.end_packet)
        packet.pop()
        packet.append(self.end_transmission)

        bytes_packet = bytes()
        for a in packet:
            bytes_packet += bytearray(binascii.unhexlify(a))

        return(bytes_packet)
