import telnetlib , socket
import time


class TELNET(object):

    def __init__(self):
        self.tn = None
        self.username = "root"
        self.password = b'cisco'
        self.cons_password = "12345678"
        self.enable_password = "cisco"
        self.host = "10.1.2.1"
        self.port = 23
        self.timeout = 6
        self.login_prompt = b"login: "
        self.password_prompt = b"Password: "
        self.router_prompt = b"R1>"

    def connect(self):
        try :
            self.tn = telnetlib.Telnet(self.host)
            print("Connection success")
        except socket.timeout :
            print("TELNET.connect() socket.timeout")

        self.tn.read_very_eager()
        self.tn.write(self.password+ b"\n")
        time.sleep(2)

    def write(self,msg):
        self.tn.write(msg.encode('ascii') + b"\n")
        time.sleep(1)
        print("Test: " +msg+" Command written")
        return True


    def read_very_eager(self):
        try :
            op=self.tn.read_very_eager().decode('ascii')
            print(op)
            return op
        except socket.timeout :
            print("read_all socket.timeout")
            return False

    def close(self):
        self.tn.close()
        return True

    def initialize(self):
        self.__init__()
        self.connect()        

    def command(self,msg):
        if self.write(msg) == True :
            resp = self.read_very_eager()
            return resp
        else :
            return False



telnet = TELNET()
telnet.initialize()


#call request function 
cmd = 'term len 0 \n sh ip int brief'
resp = telnet.command(cmd) # let's see if this works
time.sleep(2)

cmd2 = 'enable' 
resp = telnet.command('enable')

telnet.command('cisco')
time.sleep(1)

cmd3 = 'conf t \n hostname YAHOOOOO \n' 
resp3 = telnet.command(cmd3)
time.sleep(1)

cmd3 = 'int fa0/0 \n ip address 10.1.3.1 255.255.255.0 \n no shut \n' 
resp3 = telnet.command(cmd3)
time.sleep(1)



'''

cmd3 = 'conf t'
resp2 = telnet.command()
time.sleep(2)
cmd


if telnet.write('cisco') == True:
    print("Into enable prompt, lets go to config mode ")
    if telnet.write('conf t') == True:
        print("You are now in config mode.")
    else:
        print("Unable to go to config")
else:
    print("Unable to go to config mode")

cmd3 = 'hostname YAHOOOOO'
resp3 = telnet.request(cmd3)

telnet.close()




    def read_all(self):
        try :
            op = self.tn.read_all().decode('ascii')
            print(op)
            return op
        except socket.timeout :
            print("read_all socket.timeout")
            return False

'''