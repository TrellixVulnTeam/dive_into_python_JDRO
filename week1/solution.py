import sys

digit_string = sys.argv[1]

s = 0

for letter in digit_string:
	s += int(letter)

print(s)
