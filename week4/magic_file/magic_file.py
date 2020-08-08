import tempfile
import os.path
import time

class File:
	count = -1

	def __init__(self, path):
		self.path = path
		if not os.path.exists(path):
			open(path, 'w').close()

	def read(self):
		with open(self.path) as file:
			return file.read()

	def write(self, text_data):
		with open(self.path, 'w') as file:
			return file.write(text_data)

	def __add__(self, other_file):
		File.count += 1
		new_file = File(os.path.join(tempfile.gettempdir(), f'bruh{File.count}'))
		new_file.write(self.read() + other_file.read())
		return new_file

	def __str__(self):
		return self.path

	def __iter__(self):
		self.file = open(self.path)
		return self
	
	def __next__(self):
		res = self.file.readline()
		if res == '':
			self.file.close()
			raise StopIteration
		return res


# path_to_file = 'some_filename'

# print(os.path.exists(path_to_file))

# file_obj = File(path_to_file)

# print(os.path.exists(path_to_file))

# print(file_obj.read())

# print(file_obj.write('some text'))

# print(file_obj.read())

# print(file_obj.write('other text'))

# print(file_obj.read())

# file_obj_1 = File(path_to_file + '_1')

# file_obj_2 = File(path_to_file + '_2')

# print(file_obj_1.write('line 1\n'))

# print(file_obj_2.write('line 2\n'))

# new_file_obj = file_obj_1 + file_obj_2

# print(isinstance(new_file_obj, File))

# print(new_file_obj)

# for line in new_file_obj:
# 	print(ascii(line))
