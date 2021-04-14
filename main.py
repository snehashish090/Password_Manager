import json
from encrypt import encrypt, decrypt
from manager import main

with open("data.json") as file:
	data = json.load(file)

def signup():
	usernames = []
	print("--------------SIGNUP------------------")
	username = encrypt(input("create your username: "), key = 4)
	password = encrypt(input("create your password: "), key = 4)

	for i in data:

		usernames.append(i["name"])

	if username not in usernames:

		with open("data.json", "w") as file:
			data.append({"name": username, "password": password})
			json.dump(data, file)

		print("added!")
		login()
	else:
		print("user already exists!")


def login():

	if data != []:

		while True:
			print("--------------LOGIN------------------")
			username = encrypt(input("enter your username: "), key = 4)
			password = encrypt(input("enter your password: "), key = 4)

			if data[0]["name"] == username and data[0]["password"] == password:
				print("logged in\n")

				main()
			else:
				print("invalid credentials")
	else:
		signup()

# def start():
# 	if login():
# 		main()
# start()
login()