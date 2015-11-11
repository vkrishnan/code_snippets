import sys

lowercase = [chr(i) for i in range(ord('a'), ord('z')+1)]
uppercase = [chr(i) for i in range(ord('A'), ord('Z')+1)]

l = raw_input()
s = raw_input()
k = int(raw_input())

for ch in s:
	if ch.islower():
		index = (lowercase.index(ch) + k) % len(lowercase)
		sys.stdout.write(lowercase[index])
	elif ch.isupper():
		index = (uppercase.index(ch) + k) % len(uppercase)
		sys.stdout.write(uppercase[index])
	else:
		sys.stdout.write(ch)
