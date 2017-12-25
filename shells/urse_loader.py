import os, sys
shellcodes = {}

md = False
if "shells" in os.listdir("./"):
	md = True
	import urse_if as style
	if sys.platform == "ios":
		inp = style.iOS()
	else:
		inp = style.notiOS()
else:
	execfile("../urse_if.py")
	if sys.platform == "ios":
		inp = iOS()
	else:
		inp = notiOS()
	class style():
		def urse_out2(self,a,b):
			urse_out2(a,b)
	style = style()

s = 0
if md:
	for _ in os.listdir("./shells"):
		if _.endswith(".ultra"):
				shellcodes.update({s:"./shells/"+_})
				s += 1
else:
	for _ in os.listdir("./"):
		if _.endswith(".ultra"):
				shellcodes.update({s:_})
				s += 1

def verbosify(word):
	word = word.upper()
	word = word.replace("RCE","Remote Command Execution")
	word = word.replace("RSE","Remote Shell Execution")
	word = word.replace("RS","Reverse Shell")
	word = word.replace("BSE","Binding Shell Execution")
	word = word.replace("CE","Code Execution")
	word = word.replace("RCI","Remote Command Injection")
	return word

def lister(query):
	if "; " in query:
		q = query.split("; ")
	if ";" in query:
		q = query.split(";")
	elif "-" in query:
		q = query.split("-")
	elif "." in query:
		q = query.split(".")
	elif ", " in query:
		q = query.split(", ")
	elif "," in query:
		q = query.split(",")
	elif " " in query:
		q = query.split()
	else:
		q = [query]
	return q

def show_shells(filter=None, verbose=False,s=False):
	if not s:
		for _ in shellcodes:
			if type(s) == int:
				break
			name = " ".join(shellcodes[_].split("+"))
			if "/" in name:
				name = name.split("/")[len(name.split("/"))-1]
			name = name.split(".ultra")[0].upper()
			if filter:
				for f in lister(filter):
					if f in shellcodes[_] or f in open(shellcodes[_]).read():
						style.urse_out2(_,name)
			if verbose:
				name = verbosify(name)
			if not filter:
				style.urse_out2(_,name)

def process(shell):
	selected = open(shell).read()
	if "%w" in selected:
		selected = selected.replace("%w",raw_input("[*] Wait (Seconds): "))
	if "%d" in selected:
		return selected%(inp.input(1, over="lhost"),int(inp.input(1, over="Lport")))
	if "%s" in selected:
		return selected%inp.input(1, over="Command")
	return selected

def select_shell(verbose=False,s=False):
	show_shells(verbose=verbose,s=s)
	if not s and type(s) != int:
		shell = int(inp.input(1, over="shell"))
	else:
		shell = s
	if shell in shellcodes:
		return shellcodes[shell]
	else:
		print "[-] Invalid Shell Number"
		return ""
