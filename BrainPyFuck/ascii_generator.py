# 252
import json

a = {}
printables = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

for printable in printables:
	a[ord(printable)] = printable

with open("a.json", "w") as fh:
	json.dump(a, fh, indent=4)
	
