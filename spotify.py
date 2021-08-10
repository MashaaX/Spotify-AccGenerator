import requests as r, random, os, json
from datetime import datetime

class CreateAcc:
	def __init__(self, username, password):
		self.user = username
		self.pasw = password
		self.date = datetime.now().strftime("%d-%m").split("-")

	def random(self):
		rand = list("abcdefghijklmnopqrstuvwxyz1234567890")
		acak = [random.choice(rand) for _ in range(10)]
		return "".join(acak)

	def create(self):
		randomMail = self.random()+"@gmail.com"
		self.data = {
			"iagree":"true", "birth_day":self.date[0],
			"platform":"Android-ARM", "creation_point":"client_mobile",
			"password":self.pasw,
			"key":"142b583129b2df829de3656f9eb484e6", "birth_year":"2000",
			"email": randomMail,
			"gender":"male", "app_version":"849800892",
			"birth_month":self.date[1], "password_repeat":self.pasw
		}
		try:
			self.run = r.post("https://spclient.wg.spotify.com:443/signup/public/v1/account/", data=self.data).json()
			if self.run["status"] == 1:
				print("[✓] success created")
				print("[-] email: "+randomMail)
				print("[-] passw: "+self.pasw)
				print("[-] username: "+self.run["username"])
			else:
				exit("[×] failed created")
		except:
			exit("[×] failed created")


os.system("clear")
print("""

 ___ _ __   ___ | |_(_)/ _|_   _
/ __| '_ \ / _ \| __| | |_| | | |
\__ \ |_) | (_) | |_| |  _| |_| |
|___/ .__/ \___/ \__|_|_|  \__, | V0.1
    |_|                    |___/

     * Author : Mashaa
""")
user = input("[+] username: ")
pasw = input("[+] password: ")
run = CreateAcc(user, pasw)
run.create()
