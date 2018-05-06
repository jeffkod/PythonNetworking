from netmiko import ConnectHandler
class Router:
    # Def= Define, below line is defining attribute and in attribute netmeko dictionay defining router details.
    def __init__(self,ip,username='cisco',password='cisco',secret='cisco'):
        self.ip = ip
        self.netmiko_init_dict = {
            'device_type':'cisco_ios',
            'username':username,
            'password':password,
            'secret':secret,
            'ip':self.ip
        }
        self.conn = None
    # Below line is defining method for connecting to device.   
    def connect_to_device(self):
        self.conn = ConnectHandler(**self.netmiko_init_dict)
        self.conn.enable()
   
     # Below line is defining method 
    def get_first_cdp_nei_ip(self):
        if not self.conn:
            print("Not connected. Connecting now!")
            self.connect_to_device()
        cdp_nei_cmd = 'sh cdp nei det'
        cdp_nei_det_op=self.conn.send_command(cdp_nei_cmd).splitlines()
        return cdp_nei_det_op[3].split(":")[1].strip()
    def show_int_desc(self):
        """
        Returns the interface descriptions splited by lines as a list
        """
        if not self.conn:
            print("Not connected. Connecting now!")
            self.connect_to_device()
        int_desc_commmand = 'sh int desc'
        return self.conn.send_command(int_desc_commmand).splitlines()
    
    def get_hostname_from_dev(self):
        if not self.conn:
            print("Not connected. Connecting now!")
            self.connect_to_device()
        cmd = 'sh run | inc hostname'
        return self.conn.send_command(cmd).replace("hostname ","")
        