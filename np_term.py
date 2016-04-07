import socket 
import time 									
import sys 

def connect(ip_value, port_value):

	HOST = str(ip_value)			 			# The remote host IP address
	PORT = int(port_value)       				# The server port number
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	
	time.sleep(0.1) 							#use time.sleep to give delay and netBooter time to process

	timeout_limit = 1
	timeout_count = 0	
	
	while timeout_count < timeout_limit: 		#Wait for user input command
		
		print("\n\r")
		print("--Type command 'exit' to quit terminal--\n\r")
		print("Enter Command:\r")
		usr_cmd = raw_input(">")
		
		if 'exit' in usr_cmd: 					#if command = exit close socket, exit python
			sock.close()
			exit()
		
		
		else:		#Otherwise send input from user to socket connection (sock)
			sock.send('\n\r')
			sock.send(usr_cmd)
			sock.send('\r')
			time.sleep(0.5)
			recv = sock.recv(2048) 				#Receive data from connection
			print(recv) 						#print received data
			
	
  
def main():
	if len(sys.argv) !=5:
		print('Example:> np_term.py -i 192.168.1.100 -p 23\r')
		sys.exit(1)
	
	ip = sys.argv[1]							#For -i option in command line
	ip_value = sys.argv[2]						#IP address value entered
	port = sys.argv[3]							#For -p option in command line
	port_value = sys.argv[4]					#Port number entered
	if ip == '-i' and port == '-p':				#Check that the command line uses both -i and -p for valid connection
		connect(ip_value,port_value)			
	else:
		print('unknown option: ' + ip + port)	#Otherwise show unknown command that was entered.
		sys.exit(1)
		
if __name__ == '__main__':
	main()

	
