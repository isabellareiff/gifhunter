import socket
import os
from datetime import datetime

# I had trouble with getting the date to work so I searched online about the datetime module, and came across these links which helped me realize I had to use "from datetime import datetime": https://stackoverflow.com/questions/42771909/difference-between-import-datetime-and-from-datetime-import-datetime-which, https://www.codecademy.com/forum_questions/555ec051937676658b0007d2

#Thayer, Liam. CDT 22' A4. Assistance given to the author, Verbal Discussion. I was having serious issues with getting my virtual machine to work, and CDT Thayer helped me understand which firewall I had to take down in order for it to work, because I was focused on the wrong thing. CDT Thayer helped explain proper usage of the socket module, specifically socket addressing to me, as I was having a  lot of trouble with it. CDT Thayer also helped me understand that the header encoding had to be UTF-8, which although I knew, I didn't realize had to be explicitly stated. 21 February 2021. West Point, NY.

#Jones, Colin. CDT 22' D2. Assistance given to the author, Teams Chat. CDT Jones helped me with some of the formatting of my responseCode headers as I was having trouble getting the exact foramtting text correct. 21 February 2021.West Point, NY.

# https://emalsha.wordpress.com/2016/11/22/how-create-http-server-using-python-socket/ and https://emalsha.wordpress.com/2016/11/24/how-create-http-server-using-python-socket-part-ii/. These websites were helpful for knowing which specific methods to use when I got stuck trying to figure things out, like AFINET and SOCK_STREAM.
def makeServ():
	realsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	realsocket.bind(('isabella.reiff.cs484.eecs.net',80))
	realsocket.listen(5)

	print(socket.gethostname())

	time = datetime.now()
	fulltime = time.strftime("%m/%d/%Y, %H:%M:%S")
	with open('moved') as file:
		fileRead = file.readlines()
	fileRead = [type.strip() for type in fileRead]
	book = {}
	for i in range(len(fileRead)):
		fileRead[i] = fileRead[i].split(' ')
	for j in fileRead:
		book[j[0]] = j[1]

	while(1):
		client, address = realsocket.accept()
		request = client.recv(1024).decode('utf-8')
		print(request)
		strsplit = request.split(' ')
		em = strsplit[0]
		streReq = strsplit[1]
		serve = streReq.split('?')[0]
		serve = serve.lstrip('/')
		header = 'HTTP/1.1 200 OK\r\n'
		if(serve == ''):
			serve = 'test1.html'
		elif serve in book.keys():
			print('\n\n', serve, '\n\n')
			serve = book[serve]
			print('\n\n', serve, '\n\n')
			header = 'HTTP/1.1 301 Moved\r\nLocation: http://isabella.reiff.cs484.eecs.net/'+serve+'\r\n'
		try:
			file = open(serve, 'rb')
			responseCode = file.read()
			bytes = os.path.getsize(serve)
			if(serve.endswith('.mp4')):
				ft = 'video/mp4'
			elif(serve.endswith('.jpg')):
				ft = 'image/jpg'
			else:
				ft = 'text/html'
			header += 'Last-Modified: Mon, 22 Feb 2021 23:59:59 GMT \n'
			header += 'Date: '+ fulltime +'\n'
			header += 'Server: Custom\n'
			header += 'Content-Length: ' + str(bytes) + '\n'
			header += 'Content-Type: ' + ft +'\n'
			header += 'Connection: close\n\n'
		except Exception as e:
			header = 'HTTP/1.1 404 Not Found \n\n'
			responseCode = '<html><body><center><h3>Error 404: File Not Found</h3></center></body></html>'.encode()
		rC = header.encode('utf-8')
		rC += responseCode
		client.send(rC)
		client.close()
makeServ()
