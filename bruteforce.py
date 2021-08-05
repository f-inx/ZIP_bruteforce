#!/bin/python3

from zipfile import zipfile
import argparse

#usage
parser = argparse.ArgumentParser(description:"\nUsage: python zipbrute.py -z <zipfile.azip> -p <passwordfile.txt>
#password protected archive
parser.add_argument("-z",dest="ziparchive",help="Zip archive file")
#wordlist for the zip cracker
parser.add_argument("-p",dest="passfile",help="Password file")
parser_args = parser.parse_args()

#error handling part (exit program in a clean way)
try:
	ziparchive=(Zipfile(parsed_args.ziparchive)
	passfile=parsed_args.passfile
	#if the password found
	foundpass=""
	
except:
	print(parser.decription)
	exit(0)
	
#password bruteforcing part
with open(passfile, "r") as f:
	for line in f:
		password = line.strip("\n")
		password = password.encode("utf-8")
	
	try:
		foundpass = ziparchive.extractall(pwd= password)
		if foundpass == None:
			print("\nFound password: ", password.decode())
	except RuntimeError:
		pass
		
	if foundpass == " ":
		print("\nPassword not found. Try a bigger password list)
```
