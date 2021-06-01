from sys import *


def open_file(filename):
	data = open(filename, "r").read()
	return data

def lex(filecontents):
	tok = ""
	said = False
	inputted = False
	state = False
	say = ""
	inputs = ""
	filecontents = list(filecontents)
	for char in filecontents:
		tok += char
		if " " in tok or tok == "<EOF>" or tok == "\n":
			tok = ""
		if tok == "say" or tok == "Say":
			tok = ""
			said = True
		if tok == "input" or tok == "Input" or tok == "ask" or tok == "Ask" or tok == "get" or tok == "Get":
			tok = ""
			inputted = True
		if '"' in tok:
			tok = ""
			state = not state
		if said and state:
			say += char
		if inputted and state:
			inputs += char
		if state == False:
			say = say[1:]
			inputs = inputs[1:]
			if not say == '':
				print(say)
				say = ""
				said = False
			if not inputs == '':
				input(inputs)
				inputs = ""
				inputted = False

def run():
	data = open_file(argv[1])
	lex(data)

run()