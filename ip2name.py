from sys import argv, stderr
from socket import gethostbyaddr 
from posix import abort

def main():
	if len(argv) == 2:
		endereco = argv[1]
	else:
		endereco = input("Entre com o endereço IP: ")
	try:
		(name, aliaslist, addresslist) = gethostbyaddr(endereco)
	except e:
		print("Não encontrei informações sobre %s"% endereco, file = stderr)
		abort()
	print("Nome: %s\nEndereçoIP: %s"% (endereco, name))
	print("Alias:", aliaslist)
	print("Endereços:", addresslist)
	return
	
if __name__ == '__main__':
	main()
