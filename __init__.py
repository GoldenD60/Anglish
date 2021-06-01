from sys import *


def open_file(filename):
	data = open(filename, "r").read()
	return data

def lex(filecontents):
	tok = ""
	said = False
	state = False
	say = ""
	filecontents = list(filecontents)
	for char in filecontents:
		tok += char
		if " " in tok or tok == "<EOF>":
			tok = ""
		if tok == "say" or tok == "Say":
			tok = ""
			said = True
		if '"' in tok:
			tok = ""
			state = not state
		if said and state:
			say += char
	say = say[1:]
	print(say)


def run():
	data = open_file(argv[1])
	lex(data)


run()