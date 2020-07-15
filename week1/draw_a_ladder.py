import sys

n = int(sys.argv[1])

for i in range(n):
	print(f"{ (i + 1) * '#':>{n}}")
