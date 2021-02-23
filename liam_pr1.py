import socket
import os
from datetime import datetime


#Whitman, Luke. CDT 22' A4. Assistance given to the author. 
#Cadet Whitman let me see his code for project 2 and 
#I found it useful in setting up the socket addressing.
#He also gave me some tips in formatting my headers
#So that everything properly displayed. West Point NY.


def createServer():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('liam.thayer.cs484.eecs.net',80))
	print(socket.gethostname())
	serversocket.listen(5)


	rightnow = datetime.now()
	dtg = rightnow.strftime("%m/%d/%Y, %H:%M:%S")

	#<304 stuff>
	with open('moved') as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	mydict = {}
	for i in range(len(content)):
		content[i] = content[i].split(' ')

	for elem in content:
		mydict[elem[0]] = elem[1]
	#</304 stuff>


	while(1):
		clientsocket, address = serversocket.accept()
		req = clientsocket.recv(1024).decode('utf-8')
		print(req)
		stringlist = req.split(' ')
		method = stringlist[0]
		requesting = stringlist[1]
		
		print('client request \n', requesting)
		
		toserv = requesting.split('?')[0]
		toserv = toserv.lstrip('/')
		header = 'HTTP/1.1 200 OK\r\n'
		if(toserv == ''):
			toserv = 'test1.html'
		elif toserv in mydict.keys():
			print('\n\n', toserv, '\n\n')
			toserv = mydict[toserv]
			print('\n\n', toserv, '\n\n')
			header = 'HTTP/1.1 301 Moved\r\nLocation: http://liam.thayer.cs484.eecs.net/' + toserv + '\r\n'

		try:
			file = open(toserv, 'rb')
			response = file.read()
			bytelength = os.path.getsize(toserv)
			if(toserv.endswith('.jpg')):
				mime = 'image/jpg'
			elif(toserv.endswith('.mp4')):
				mime = 'video/mp4'
			else:
				mime = 'text/html'				
			
			header += 'Last-Modified: Sun, 21 Feb 2021 23:59:59 GMT \n'
			header += 'Date: '+ dtg +'\n'
			header += 'Server: Custom\n'
			header += 'Content-Length: ' + str(bytelength) + '\n'
			header += 'Content-Type: ' + mime +'\n'
			header += 'Connection: close\n'
			header += '\n'

		
		except Exception as e:
			print(" \n we got a 404 \n")
			header = 'HTTP/1.1 404 Not Found \n\n'
			response = '<html><body><center><h3>Error 404: File Not Found</h3></center></body></html>'.encode()
		print('THIS IS THE HEADER /n' ,header)
		final_response = header.encode('utf-8')
		final_response += response
		clientsocket.send(final_response)
		
			


		clientsocket.close()
		

createServer()
