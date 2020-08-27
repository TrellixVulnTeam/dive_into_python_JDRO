import asyncio


database = {}


def process_data(data):
	print(data)
	try:
		command, other = data.split(' ', 1)
	except ValueError:
		return 'error\nwrong command\n\n'

	if command == 'put':
		try:
			metric, value, timestamp = [i.strip() for i in other.split()]
			value = float(value)
			timestamp = int(timestamp)
		except ValueError:
			return 'error\nwrong command\n\n'

		index = -1
		for ind, i in enumerate(database.get(metric, [])):
			if i[0] == timestamp:
				index = ind
		if index == -1:
			database.setdefault(metric, []).append((timestamp, value))
		else:
			database[metric][index] = (timestamp, value)
		

		return 'ok\n\n'

	elif command == 'get' and len(other.split()) == 1:
		if other == '*\n':
			datas = '\n'.join([f'{metric} {value} {timestamp}'	for metric in database 
											for timestamp, value in database[metric]])
			res = 'ok\n' + datas + '\n' + ('\n' if datas else '')
			return res
		elif other.strip() in database:
			metric = other.strip()
			datas = '\n'.join([f'{metric} {value} {timestamp}' 
										for timestamp, value in database[metric]])
			res = 'ok\n' + datas + '\n\n'
			return res
		else:
			return 'ok\n\n'
	else:
		return 'error\nwrong command\n\n'

class ClientServerProtocol(asyncio.Protocol):
	# database = {}
	# def __init__(self):
	# 	print('-' * 33)
	# 	self.database = {}

    def connection_made(self, transport):
    	# print('-' * 33)
    	# self.data = {}
    	print(f'transport = {transport}')
    	self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        print('resp =', resp)
        self.transport.write(resp.encode())
        # print(database)

        # print(f'data = {data}')




def run_server(host, port):
	loop = asyncio.get_event_loop()
	coro = loop.create_server(
    	ClientServerProtocol,
    	host, port
	)

	server = loop.run_until_complete(coro)
	
	try:
	    loop.run_forever()
	except KeyboardInterrupt:
	    pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()



if __name__ == '__main__':
	run_server('127.0.0.1', 8888)

# loop = asyncio.get_event_loop()
# coro = loop.create_server(
#     ClientServerProtocol,
#     '127.0.0.1', 8181
# )

# server = loop.run_until_complete(coro)

# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass

# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()