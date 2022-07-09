from faker import Faker
import random

users = int(input("Enter number of users connected: "))
fake = Faker()
fake.text()
username_dict = {}
usernames = []

with open('config.txt' , 'w') as config_file:
    config_file.write(str(users) + "\n")
    for i in range(users):
        mapping = input("Enter username and IP in <username>,<ip> format: ")
        username,ip = mapping.split(',')
        # username_dict[username] = ip
        usernames.append(username)
        config_file.write(username + ":" + ip + "\n")
    for i in range(users*5):
        user_1 = usernames[random.choice(range(users))]
        user_2 = usernames[random.choice(range(users))]
        if user_1 != user_2:
            message_line = "" + user_1 + ">" + user_2 + ">" + fake.text(100)
            config_file.write(message_line + "\n")
    config_file.close()


