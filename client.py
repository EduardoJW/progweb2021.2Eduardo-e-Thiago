from sys import argv, stderr 
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, IPPROTO_TCP, AI_ADDRCONFIG
from posix import abort

def main():
		if len(argv) == 3:
			host = argv[1]
			porta = int(argv[2])
		else:
			host = 'localhost'
			porta = 8752
		enderecoServidor = getEnderecoServidor(host, porta)
		socketfd = criaSocket(enderecoServidor)
		conecta(socketfd, enderecoServidor)
		fazOResto(socketfd)
		socketfd.close()
	
	return
	
if__name__ == '__main__':
	main()
	
def getEnderecoServidor(host, porta):
	try:
		enderecoServidor= getaddrinfo(host, porta, family=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP, flags=AI_ADDRCONFIG)
		
	except as e:
		print("Não obtive informações sobre servidor", file=stderr)
		abort()
			
	return enderecoServidor
































