from connection import Connection
from decoder import Decoder
from encoder import Encoder

if __name__ == "__main__":
    client = Connection()
    client.connect("189.6.76.118", 50046)

    decoder = Decoder()
    encoder = Encoder()

    received_packet = client.receive()

    # Decoding the packet
    divided_packet = decoder.divide(received_packet)

    decoded_packet = decoder.decode(divided_packet)

    finalized_decoded_packet = decoder.finalize(decoded_packet)

    # Encoding the reponse packet
    byte_packet = encoder.turnAscToByte(finalized_decoded_packet)

    encoded_packet = encoder.encode(byte_packet)

    final_packet = encoder.makePacket(encoded_packet)

    response = client.send(final_packet)

    print()
    if response == b'c657557a7a9e21':
        print("The server returned OK!!!!!! :D")
    else:
        print("The server returned ERR =( =( =/")
    print()

    client.disconnect()