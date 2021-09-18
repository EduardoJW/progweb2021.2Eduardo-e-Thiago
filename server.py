from sys import argv, stderr
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, AI_ADDRCONFIG, AI_PASSIVE
from socket import IPPROTO_TCP, SOL_SOCKET, SO_REUSEADDR
from posix import abort
import time
from pathlib import Path
import myconf
import os

def treatGET(fd):
	print("TREAT GET")
	string = ""
	name = ""
	tipo = -1
	
	data = fd.recv(1024)
	string = string + str(data.decode())
	
	print("EIS A STRING:")
	print(string)
	print("FIM DA STRING")
	print(len(string))
	
	if len(string) != 0:
		if string[4]+string[5] != "/ ":
			i = 5
			while string[i] != " ":
				name = name+string[i]
				i = i + 1
			
			print("NAME: "+ name)
			
			searchList = name.split(".")
			#print(searchList[1])
			name = myconf.PATH + name
			testFileExistence = Path(name)
			if len(searchList) > 1 and testFileExistence.is_file():
				if searchList[1] == "html":
					tipo = 1
				elif searchList[1] == "js":
					tipo = 2
				elif searchList[1] == "jpg":
					tipo = 3
				elif searchList[1] == "png":
					tipo = 4
				elif searchList[1] == "gif":
					tipo = 5
				else:
					tipo = -1
					name = myconf.PATH+myconf.NOTFOUND
			else:
				
				
					
				tipo = -1
				name = myconf.PATH+myconf.NOTFOUND
			#print(string)
			
			print("END TREAT GET")
		else:	
			#print("TESTEEEEEEEEE")
			tipo = 0
			for i in range(5):
				name = ""
				name = myconf.PATH+myconf.DEFAULT_PAGES[i]
				testName = Path(name)
				if testName.is_file():
					tipo = i+1
					#print("CORRECT!")
					break
					
			if tipo == 0:
				name = myconf.PATH+myconf.NOTFOUND
				tipo = -1
	else:
		tipo = -2
		name = None
	
	
	return name, tipo
	
def getEnderecoHost(porta):
	try:
		enderecoHost = getaddrinfo(None,porta,family=AF_INET,type=SOCK_STREAM,proto=IPPROTO_TCP,flags=AI_ADDRCONFIG | AI_PASSIVE)
		
	except:
		print("Nao obtive informacoes sobre o servidor (???)", file=stderr)
		abort()
	return enderecoHost
	
def criaSocket(enderecoServidor):
	fd = socket(enderecoServidor[0][0], enderecoServidor[0][1])
	if not fd:
		print("Nao consegui criar o socket", file=stderr)
		abort()
	return fd
	
def setModo(fd):
	fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	return

def bindaSocket(fd, porta):
	try:
		fd.bind(('', porta))
	except:
		print("Erro ao dar bind no socket do servidor", porta, file=stderr)
		abort()
	return


def escuta(fd):
	try:
		fd.listen(0)
	except:
		print("Erro ao comecar a escutar a porta", file = stderr)
		abort()
	print("Iniciando o servico")
	return
	
def conecta(fd):
	(con, cliente) = fd.accept()
	print("Servidor conectado com", cliente)
	return con
	
def carregaPagina(fd):
	
	
	filename, filetype = treatGET(fd)
	
	if filetype == 1:
		#filename = "test.html"
		f = open(filename, "r")
		
		fd.sendall(str.encode("HTTP/1.1 200 OK\n", 'iso-8859-1'))
		fd.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
		fd.send(str.encode('\r\n'))
		
		for l in f.readlines():
			print('Sent ', repr(l))
			fd.sendall(str.encode(""+l+"", 'iso-8859-1'))
			l = f.read(1024)
		
		f.close()
		
		fd.close()
	elif filetype == 2:
		f = open(filename, "r")
		
		fd.sendall(str.encode("HTTP/1.1 200 OK\n", 'iso-8859-1'))
		fd.sendall(str.encode('Content-Type: text/javascript\n', 'iso-8859-1'))
		fd.send(str.encode('\r\n'))
		
		for l in f.readlines():
			print('Sent ', repr(l))
			fd.sendall(str.encode(""+l+"", 'iso-8859-1'))
			l = f.read(1024)
		
		f.close()
		
		fd.close()
		
		
	elif filetype == 3:
		f = open(filename, "rb")
		
		fd.sendall(str.encode("HTTP/1.1 200 OK\n", 'iso-8859-1'))
		fd.sendall(str.encode('Content-Type: image/jpg\n', 'iso-8859-1'))
		
		fd.send(str.encode('\r\n'))
		
		for data in f:
			fd.sendall(data)
		
		f.close()
	
		fd.close()
	elif filetype == 4:
		f = open(filename, "rb")
		
		fd.sendall(str.encode("HTTP/1.1 200 OK\n", 'iso-8859-1'))
		fd.sendall(str.encode('Content-Type: image/png\n', 'iso-8859-1'))
		
		fd.send(str.encode('\r\n'))
		
		for data in f:
			fd.sendall(data)
		
		f.close()
	
		fd.close()
	elif filetype == 5:
		f = open(filename, "rb")
		
		fd.sendall(str.encode("HTTP/1.1 200 OK\n", 'iso-8859-1'))
		fd.sendall(str.encode('Content-Type: image/gif\n', 'iso-8859-1'))
		
		fd.send(str.encode('\r\n'))
		
		#fd.recv(1000000)
		for data in f:
			fd.sendall(data)
		
		f.close()
	
		fd.close()
		
	elif filetype == -1:
		#filename = "notfound.html"
		f = open(filename, "r")
		
		fd.sendall(str.encode("HTTP/1.1 404 Not Found\n", 'iso-8859-1'))
		fd.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
		fd.send(str.encode('\r\n'))
		
		for l in f.readlines():
			print('Sent ', repr(l))
			fd.sendall(str.encode(""+l+"", 'iso-8859-1'))
			l = f.read(1024)
		
		f.close()
		
		fd.close()
	elif filetype == -2:
		print("Tentativa de acesso não identificada.")
	#elif filetype == -2:
		#print("ARGUMENTO")
		#while True:
			#data = fd.recv(1024)
			#if not data:
			#	break
				
			#print(data.decode())	
		#print("END")
	return
	

	

def main():
	#if len(argv) == 2:
		#porta = int(argv[1])
	#else:
		#porta = 8080
	#if len(argv) == 2:
		#print("TEXTOOOOOOO")
	
	
	porta = myconf.PORT
	enderecoHost = getEnderecoHost(porta)
	fd = criaSocket(enderecoHost)
	setModo(fd)
	bindaSocket(fd,porta)
	newpid = os.fork()
	print("Servidor pronto em", enderecoHost)
	escuta(fd)
	
	while True:
		#time.sleep(16)
		con = conecta(fd)
		if con == -1:
			continue
		print("CON:")
		print(con)
		carregaPagina(con)
	return


if __name__ == '__main__':
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
