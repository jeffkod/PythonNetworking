import paramiko

def open_ssh_conn(ip):
    #Change exception message
    try:
        
        username = 'cisco'
        password = 'cisco'
        
        #Logging into device
        session = paramiko.SSHClient()
		
		#For testing purposes, this allows auto-accepting unknown host keys
		#Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
		#Passing the necessary parameters
        session.connect(ip, username = username, password = password)
        
		#Start an interactive shell session on the router
        connection = session.invoke_shell()	
        
        #Setting terminal length for entire output - no pagination
        connection.send("terminal length 0\n sh ip int brief")
        time.sleep(1)

        output = connection.recv(65535)
        print(output)

        session.close()

    except paramiko.AuthenticationException:
        print "* Invalid username or password. \n* Please check the username/password file or the device configuration!"
        print "* Closing program...\n"

ip = '10.1.2.1'
open_ssh_conn(ip)