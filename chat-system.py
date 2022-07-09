import socket
import os
import objects 

current_node,user_ip_map = objects.create_config()
def send(receiver , message):
    print(user_ip_map[receiver])
    while True:
        try:
            sender_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            sender_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
            sender_socket.connect((user_ip_map[receiver] , 8000))
            sender_socket.send(message.encode())
            check_ack = sender_socket.recv(1024)
            if check_ack.decode() == "GOT_ACK":
                sender_socket.close()
                break
            else:
                continue
        except Exception as e:
            pass

def receive(sender , receiver):
    receiver_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    receiver_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    print(user_ip_map[sender])
    print(user_ip_map[receiver])
    receiver_socket.bind((user_ip_map[receiver] , 8000))
    while True:
        receiver_socket.listen(1)
        connection,address = receiver_socket.accept()
        message = connection.recv(1024)
        if address[0] == user_ip_map[sender]:
            connection.send("GOT_ACK".encode())
            print(sender + " says: " + message.decode())
            connection.close()
            break
        else:
            connection.send("ACK_DENY".encode())

for message_object in objects.MessageObjects:
    if current_node.username == message_object.sender:
        send(message_object.receiver , message_object.data)
    elif current_node.username == message_object.receiver:
        receive(message_object.sender , message_object.receiver)
    else:
        continue

# for node in objects.NodeObjects:
#     print("Username: " + str(node.username))
#     print("IP: " + str(node.ip))
#     print("Port: " + str(node.port))

# for message in objects.MessageObjects:
#     print("Sender: " + str(message.sender))
#     print("Receiver: " + str(message.receiver))
#     print("Message: " + str(message.data))
