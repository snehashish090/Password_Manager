import json
from encrypt import encrypt, decrypt


with open("cred.json") as file:
		data = json.load(file)

def add():
	site = encrypt(input("enter the site name: "), 5)
	username = encrypt(input("enter the username or email address used : "), 5)
	password = encrypt(input("enter thepassword you wish to save: "), 5)
	sites = []
	user = ""
	if data != []:
		for i in data :
			sites.append(i["site"])
			user = i["username"]

	if site not in sites:
		with open("cred.json", "w") as file:
			data.append(
				{
				"site": site,
				"username":username,
				"password":password
				})
			json.dump(data, file)

		print("Done!")
	elif site in sites and username != user:
		with open("cred.json", "w") as file:
			data.append(
				{
				"site": site,
				"username":username,
				"password":password
				})
			json.dump(data, file)

		print("Done!")
	else:
		print("site with the user already exists")

def update():
	site = encrypt(input("enter the site: "), 5)
	password = encrypt(input("enter the new password: "), 5)
	for i in data:
		if site == i["site"]:
			i["password"] = password
			with open("cred.json", "w") as file:
				json.dump(cred.data, file)
			print("dump")

def search():
	sites = []
	site = encrypt(input("enter the site name: "), 5)
	for i in data:
		if i["site"] == site:
			sites.append(i)

	for j in sites:
		print("-----------------------------------------------")
		print("site: "+ decrypt(j["site"], 5)+" | "+decrypt(j["username"], 5)+" | "+decrypt(j["password"], 5))
		print("-----------------------------------------------")


def list_all():
	for j in data:
		print("-----------------------------------------------")
		print(decrypt(j["site"], 5)+" | "+decrypt(j["username"], 5)+" | "+decrypt(j["password"], 5))
		print("-----------------------------------------------")



def main():
	while True:
		co = input(">>>")
		comands = {"exit":exit, "add": add, "update": update, "list all": list_all, "search": search}
		for i,j in comands.items():
			if i in co:
				j()
