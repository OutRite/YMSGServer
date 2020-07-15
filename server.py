yahoo_port = 5050

import socketserver

class YahooHandler(socketserver.BaseRequestHandler):
	def handle(self):
		print("RECEIVED CONNECTION FROM {}".format(self.client_address[0]))
		self.data = self.request.recv(1024)
		#print("Received:")
		#print(self.data)
		self.request.sendall(self.data)
		self.data = self.request.recv(1024)
		#print("Received:")
		#print(self.data)
		for i in range(0,len(self.data)):
			if self.data[i] == ord('\xc0') and self.data[i+1] == ord('\x80'):
				user_offset = i+2
				#print('uo: {}'.format(user_offset))
				break
		username = ''
		for i in range(user_offset, len(self.data)):
			if self.data[i] == ord('\xc0'):
				break
			else:
				username += chr(self.data[i])
				#print(username)
		print("Trying to log in with username {}...".format(username))



if __name__ == '__main__':
	HOST = '66.196.114.97' # replace this with whatever ip yahoo messenger contacts that you've bound to loopback
	with socketserver.TCPServer((HOST, yahoo_port), YahooHandler) as server:
		server.serve_forever()
