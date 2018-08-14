# coding: utf-8
# Domain Name System (DNS)
import asyncio
from contextlib import suppress

ip_map = {
    b'facebook.com.': '173.252.120.6',
    b'yougov.com.': '213.52.133.246',
    b'wipo.int.': '193.5.93.80'
}


def lookup_dns(data):
    domain = b''
    pointer, part_length = 13, data[12]
    while part_length:
        domain += data[pointer:pointer+part_length] + b'.'
        pointer += part_length + 1
        part_length = data[pointer - 1]
    # 5. look up the IP
    ip = ip_map.get(domain, '127.0.0.1')
    return domain, ip


def create_response(data, ip):
    ba = bytearray
    # 6. parse the packet
    packet = ba(data[:2]) + ba([129, 128]) + data[4:6] * 2
    packet += ba(4) + data[12:]
    packet += ba([192, 12, 0, 1, 0, 1, 0, 0, 0, 60, 0, 4])
    for x in ip.split('.'):
        packet.append(int(x))
    return packet


class DNSProtocol(asyncio.DatagramProtocol):
    # 1. protocol defines methods to call when relevant events happen
    # 2. DNS runs on top of User Datagram Protocol (UDP), so subclass DatagramProtocol
    def connection_made(self, transport):
        # 3. store transport for future use
        self.transport = transport

    def datagram_received(self, data, addr):
        # 4. parsed and respond to recieved datagram
        print(f"Received request from{addr[0]}")
        domain, ip = lookup_dns(data)
        print(f"Sending IP {domain.decode()} for {ip} to {addr[0]}")
        # 7. send resulting packet to requesting client using sendto method
        self.transport.sendto(create_response(data, ip), addr)


loop = asyncio.get_event_loop()
# 8. transport represents a communication stream,
#   abstracts away all the sending, recieving data on a UDP socket on an event loop
# 11. socket init takes some time,
#   coroutine loop.create_datagram_endpoint is wrapped in loop.run_until_complete
# 12. the event loop manages the future, returns inited transport and protocol object
transport, protocol = loop.run_until_complete(
    # 9. transport is constructed by loop's create_datagram_endpoint coroutine,
    #   starts listen on it
    loop.create_datagram_endpoint(
        # 10. our protocol class instructs transport what to call when data is recieved
        DNSProtocol, local_addr=('127.0.0.1', 4343)
    )
)
print("DNS Server running")

with suppress(KeyboardInterrupt):
    # 13. transport set up a task on event loop listening for incoming UDP connections,
    #   we start the loop with run_forever()
    #   so that task can process packets
    # 14. when packets arrive, they are processed on the protocol
    loop.run_forever()
# closes are not required in this simple case,
#   but they are when constructing on the fly or in error handling
transport.close()
loop.close()
