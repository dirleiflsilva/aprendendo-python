# Sniffer simples para Windows e Linux
import socket

host = '192.168.0.55'
# considerando soh o protocolo IP
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

sniffer.bind((host, 0))
# captura o cabecalho IP dos cabecalhos
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
# para Windows
sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while True:
    # recebe o IP do pacote
    dados = sniffer.recvfrom(10000)
    print(dados)