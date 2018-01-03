from Crypto.Cipher import AES
import base64, os, zipfile, sys
import urse_if as style
if sys.platform == "ios":
	inp = style.iOS()
else:
	inp = style.notiOS()

cipher = AES.new(secret_key,AES.MODE_ECB,"ultra")

def decrypt(msg):
	return cipher.decrypt(msg)

def encrypt(msg):
	return cipher.encrypt(msg)

def auth(secret_key):
	enkey = encrypt(secret_key).encode("hex")
	try:
		if encrypt(secret_key) == enkey.decode("hex"):
			style.urse_out2("Key   ","Thank You")
			style.urse_out2("System","Installing URSE ULTRA")
			return True
		else:
			int("a")
	except:
		style.urse_out2("Key","Failed")
		return False

def extract_update(key):
	if auth(key):
		setting = open("ultra.config").read().replace("free","ultra").replace("_donotchange = False","_donotchange = True")
		f = open("ultra.config","w")
		f.write(setting)
		f.close()
		setting = None
		denc = decrypt(open("urse.enc").read())
		if "ultra.zip" not in os.listdir("./"):
			f = open("ultra.zip","a")
			f.write("")
			f.close()
		else:
			f = open("ultra.zip","w")
			f.write(denc)
			f.close()
		denc = None
		zip_ref = zipfile.ZipFile("./ultra.zip", "r")
		zip_ref.extractall("./")
		zip_ref.close()
		os.remove("ultra.zip")
		os.remove("urse.enc")

def check4ultra():
	if "__donotchange = True" in open("ultra.config").read():
		c = inp.input("Check For Updates [y/n] ",type=1)
		if c == "y":
			import urllib
			u = urllib.FancyURLopener()
			u.retrieve("https://github.com/RussianOtter/UltimateRSE/blob/master/urse.txt?raw=True","urse.enc")
			key = open("ultra.config").read().split("ultrakey = ")[1].split("\n")[0]
			extract_update(key)
		return True
	elif "ultrakey = None" not in open("ultra.config").read() and "__donotchange = False" in open("ultra.config").read():
		key = open("ultra.config").read().split("ultrakey = ")[1].split("\n")[0]
		extract_update(key)
		return True
	else:
		return False