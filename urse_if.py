import sys, os, time, getpass, threading

if sys.platform == "ios":
	import console
else:
	from colorama import Fore, Style

def raw_input2(value="", end="", u=False, c=False):
	sys.stdout.write(value)
	data = getpass.getpass("")
	if c:
		if sys.platform == "ios":
			console.set_color()
		else:
			sys.stdout.write(Style.RESET_ALL)
	if u:
		sys.stdout.write(data.upper())
	else:
		sys.stdout.write(data)
	sys.stdout.write(end)
	return data

def urse_out2(pos1,pos2):
	pos1,pos2 = str(pos1),str(pos2)
	if sys.platform == "ios":
		console.set_color(1,0,0)
		sys.stdout.write("[ ")
		console.set_color()
		sys.stdout.write(pos1)
		console.set_color(1,0,0)
		sys.stdout.write(" ][ ")
		console.set_color()
		sys.stdout.write(pos2)
		console.set_color(1,0,0)
		sys.stdout.write(" ]\n")
		console.set_color()
	else:
		print Fore.RED+"[ " + Style.RESET_ALL + pos1 + Fore.RED + " ][ "+ Style.RESET_ALL + Fore.RED + " ]"

class iOS():
	
	def __init__(self, user="urse"):
		self.header = user
		self._go = True
	
	def ultra(self,end=False):
		if not end:
			threading.Thread(target = self.animate).start()
	
	def animate(self):
		run = "[ %s ] "%self.header
		runu = run.upper()
		for a in range(1):
			for x in range(len(run)):
				s = "\r"+run[0:x]+runu[x]+run[x+1:]
				sys.stdout.write(s)
				sys.stdout.flush()
				time.sleep(0.1)
		console.set_color()
	
	def input(self, type=2, over=False):
		if type == 1:
			console.set_color(1,0,0)
			sys.stdout.write("[ ")
			console.set_color()
			if over:
				sys.stdout.write(over.upper())
			else:
				sys.stdout.write(self.header.upper())
			console.set_color(1,0,0)
			sys.stdout.write(" ]")
			console.set_color(1,0,0)
			sys.stdout.write("[ ")
			console.set_color()
			data = raw_input2(u=True)
			console.set_color(1,0,0)
			sys.stdout.write(" ]\n")
			console.set_color()
			return data
		if type == 2:
			console.set_color(1,0,0)
			self.ultra()
			data = raw_input()
			self.ultra(True)
			console.set_color()
			return data

class notiOS():
	
	def __init__(self, user="urse"):
		self.header = user
		self._go = False
	
	def ultra(self,end=False):
		self._go = not self._go
		if not end:
			threading.Thread(target = self.animate).start()
	
	def animate(self):
		run = "[ %s ] "%self.header
		runu = run.upper()
		for a in range(1):
			for x in range(len(run)):
				s = "\r"+run[0:x]+runu[x]+run[x+1:]
				if not self._go:
					break
				sys.stdout.write(s)
				sys.stdout.flush()
				time.sleep(0.1)
		sys.stdout.write(Style.RESET_ALL)
	
	def input(self, type=2, over=False):
		if type == 1:
			sys.stdout.write(Fore.RED+"[ ")
			sys.stdout.write(Style.RESET_ALL)
			if over:
				sys.stdout.write(over.upper())
			else:
				sys.stdout.write(self.header)
			sys.stdout.write(Fore.RED+" ][ ")
			sys.stdout.write(Style.RESET_ALL)
			data = raw_input2(u=True)
			sys.stdout.write(Fore.RED)
			sys.stdout.write(" ]\n")
			sys.stdout.write(Style.RESET_ALL)
			return data
		if type == 2:
			sys.stdout.write(Fore.RED)
			self.ultra()
			data = raw_input()
			self.ultra(True)
			sys.stdout.write(Style.RESET_ALL)
			return data
