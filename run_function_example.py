import Illumio
fw = Illumio.FireWall('file.csv')
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
print(fw.accept_packet('inbound', 'udp', 54, '192.168.1.2'))
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))
print(fw.accept_packet("outbound", "tcp", 102340, "192.168.10.11"))
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.111"))
print(fw.accept_packet('inbound', 'udp', 53, '192.168.1.200'))
print(fw.accept_packet('inbound', 'udp', 53, '192.168.2.200'))
print(fw.accept_packet('inbound', 'udp', 53, '192.168.2.5'))
print(fw.accept_packet('inbound', 'udp', 53, '192.168.1.1'))
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
print(fw.accept_packet('outbound', 'udp', 51, '52.12.48.92'))
print(fw.accept_packet('outbound', 'udp', 51, '52.112.255.200'))