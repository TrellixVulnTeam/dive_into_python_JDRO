import socket
import time


class ClientError(Exception):
	pass


class Client:
	def __init__(self, host, port, timeout=None):
		self.host = host
		self.port = port
		self.timeout = timeout

		self.sock = socket.create_connection((host, port))


	def put(self, metrica, value, timestamp=None):
		timestamp = timestamp or int(time.time())
		self.sock.sendall(
				f'put {metrica} {value} {timestamp}\n'.encode("utf8")
		)
		data = self.sock.recv(1024) # server send 'ok'
		data = data.decode('utf8')
		data = data.split()

		if data[0] == 'error':
			raise ClientError(Exception)

	def get(self, metrica):
		self.sock.sendall(
				f'get {metrica}\n'.encode("utf8")
		)
		data = self.sock.recv(1024)

		# if not data:
		# 	break

		data = data.decode('utf8')
		data = data.split('\n')
		res = {}

		if data[0] == 'error':
			raise ClientError(Exception)

		# print(data)
		for i in range(1, len(data) - 2):
			# print(data[i])
			try:
				name, value, timestamp = data[i].split()
				value = float(value)
				timestamp = int(timestamp)
				res.setdefault(name, []).append((timestamp, value))
			except Exception:
				raise ClientError(Exception)
		if res:
			for metric in res:
				res[metric].sort()

		# print(res)
		return res

		



		










	# def __del__(self):
	# 	self.sock.close()


if __name__ == '__main__':

	client = Client("127.0.0.1", 8888, timeout=15)

	client.put("palm.cpu", 0.5, timestamp=1150864247)
	client.put("palm.cpu", 2.0, timestamp=1150864248)
	client.put("palm.cpu", 0.5, timestamp=1150864248)
	client.put("eardrum.cpu", 3, timestamp=1150864250)
	client.put("eardrum.cpu", 4, timestamp=1150864251)
	client.put("eardrum.memory", 4200000)

	print(client.get("*"))
	# sock = socket.create_connection(("127.0.0.1", 10001))
	# sock.sendall("ping".encode("utf8"))
	# sock.close()

