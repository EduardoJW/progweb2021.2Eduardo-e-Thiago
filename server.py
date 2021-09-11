from sys import argv, stderr
from socket import gethostbyaddr 
from posix import abort

def main():

	fileTxt = open('simple.txt','r')
	file_content = fileTxt.read()
	print(file_content)
	
	return
	
if __name__ == '__main__':
	main()
