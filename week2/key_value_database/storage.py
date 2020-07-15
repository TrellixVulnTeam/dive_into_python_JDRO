#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# my solution !!!

import os
import argparse
import json
import tempfile

parser = argparse.ArgumentParser(description='key-value or just key')
parser.add_argument(
    '--key',
    type=str,
    help='key!!!! must be'
)
parser.add_argument(
    '--value',
    type=str,
    default=None,
    help='value can be and not be'
)

args = parser.parse_args()

data = {}

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


if not os.path.exists(storage_path):
	with open(storage_path, 'w') as f:
		f.write('{}')

with open(storage_path, 'r') as f:
	data = json.load(f)


if args.value == None:
	if args.key not in data:
		print(None)
	else:
		print(*(data[args.key]), sep=', ')
else:
	if args.key not in data:
		data[args.key] = []
	data[args.key].append(args.value)

	with open(storage_path, 'w') as f:
		json.dump(data, f, indent=2)
