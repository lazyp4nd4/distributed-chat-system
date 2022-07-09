class Node:
    def __init__(self, ip, username, port):
        self.ip = ip.strip('\n')
        self.username = username
        self.port = port
    
    # def show(self):
    #     print("Node IP: " + str(self.ip.strip('\n')))
    #     print("Node Username: " + str(self.username))
    #     print("Node Port: " + str(self.port))

class Message: 
    def __init__(self, sender, receiver, data):
        self.sender = sender
        self.receiver = receiver
        self.data = data

    # def show(self):
    #     print("Sender: " + str(self.sender))
    #     print("Receiver: " + str(self.receiver))
    #     print("Message Text: " + str(self.data))

class ID:
    def __init__(self , username , ip):
        self.ip = ip
        self.username = username
    
    # def show(self):
    #     print("My Username: " + self.username)
    #     print("My IP: " + self.ip)

NodeObjects = []
MessageObjects = []
current_node = None
user_ip_map = {}

def create_config():
    my_username = input("Enter this node username: ")
    my_ip = input("Enter this node IP: ") 
    current_node = ID(my_username, my_ip)
    with open('config.txt' , 'r') as config_file:
        lines = []
        for line in config_file:
            lines.append(line)
        
        no_of_user = int(lines[0])
        nodes = lines[1:no_of_user+1]

        for node in nodes:
            user,ip = node.split(':')
            user_ip_map[user] = ip.strip('\n')
            if current_node.ip != ip and current_node.username != user:
                NodeObjects.append(Node(ip,user,8000))
        
        messages = lines[no_of_user+1:]
        for message in messages:
            sender,receiver,text = message.split('>')
            MessageObjects.append(Message(sender,receiver,text))
        
        return current_node,user_ip_map

        # for node in NodeObjects:
        #     node.show()
        
        # for message in MessageObjects:
        #     message.show()


# create_config()





    