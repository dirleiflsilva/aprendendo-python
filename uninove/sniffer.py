# script para Sniffer
import socket
import os
# este eh o IP do meu host, o computador alvo que sera escaneado
host = '192.168.0.55'

# cria o socket
if os.name == 'nt':
    # verifica se o protocolo eh endereco IP ou ICMP
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

# aguarda o host
sniffer.bind((host, 0))
# captura os cabecalhos IP dos pacotes
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == 'nt':
    # para Windows, habilita o modo promiscuo
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# recebe o IP do pacote
print(sniffer.recvfrom(10000))

if os.name == 'nt':
    # para Windows, desabilita o modo promiscuo
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)