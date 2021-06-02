from sys import *

variables = {}

def open_file(filename):
	data = open(filename, "r").read()
	return data

def lex(filecontents):
	tok = ""
	said = False
	inputted = False
	state = False
	var = False
	to = False
	varName = ""
	hasInputtedBefore = False
	lastInputValue = ""
	say = ""
	inputs = ""
	filecontents = list(filecontents)
	for char in filecontents:
		tok += char
		if '"' in tok:
			tok = ""
			state = not state
			continue
		if " " in tok or tok == "<EOF>" or tok == "\n":
			tok = ""
		if tok == "say" or tok == "Say" or tok == "tell" or tok == "Tell" and state == False:
			tok = ""
			said = True
		if tok == "input" or tok == "Input" or tok == "ask" or tok == "Ask" and state == False:
			tok = ""
			inputted = True
		if tok == "to" or tok == "To" or tok == "into" or tok == "Into" and state == False:
			var = False
			to = True
		if said and state:
			say += char
		if inputted and state:
			inputs += char
		if to and state:
			varName += char
		if state == False:
			if not say == '':
				print(say)
				say = ""
				said = False
			if not inputs == '':
				lastInputValue = input(inputs)
				inputs = ""
				inputted = False
				hasInputtedBefore = True
			if not varName == '':
				# print(f"A new variable has been created called '{varName}', with a value of {lastInputValue}")
				variables.update({f"{varName}": f"{lastInputValue}"})
				# print(variables[f"{varName}"])
		# print(tok)

def run():
	lex(open_file(argv[1]))

run()