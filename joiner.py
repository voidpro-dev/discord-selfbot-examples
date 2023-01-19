import requests, random, time, base64, threading, traceback

invite = "https://discord.gg/ovérlay"
key = "nopecha_key"

proxies = open("proxies.txt", "r").read().split("\n")
tokens = open("alltoken.txt", "r").read().split("\n")
invite = invite.split("discord.gg/")[1]
decoded_superproperty = '{"os":"%s","browser":"Discord Client","release_channel":"stable","client_version":"0.0.264","os_version":"15.6.0","os_arch":"x64","system_locale":"en-US","client_build_number":108924,"client_event_source":null}' % ("Windows")
message_bytes = decoded_superproperty.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
x_super_property = base64_bytes.decode('ascii')
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"

def get_proxy():
	return "{}".format(random.choice(proxies))

def solver(session, sitekey, url):
	while True:
		try:
			print("Solving...")
			#proxydata = proxy["http"].split("@")
			#proxyauth = proxydata[0].split(":")
			#proxyaddr = proxydata[1].split(":")
			id = session.post('https://api.nopecha.com/token', json={
				'type': 'hcaptcha',
				'sitekey': sitekey,
				'url': url,
				#"proxy":{
			    #    'scheme': 'http',
			    #    'host': proxyaddr[0],
			    #    'port': proxyaddr[1],
			    #    'username': proxyauth[0],
			    #    'password': proxyauth[1],
			    #},
				'key': key}).json()
			id = id['data']
			data = session.get(f"https://api.nopecha.com/token?key={key}&id={id}").json()
			data = data["data"]
			print("Solved")
			return data
		except Exception as e:
			print("Failed to solve")
			time.sleep(0.5)
			pass

def joiner(token):
	session = requests.Session()
	proxy = {"http": get_proxy()}
	fingerprint = session.get("https://discord.com/api/v9/experiments").json()["fingerprint"]
	headers = {"authorization":token, "content-type":"application/json","x-fingerprint": fingerprint,"X-Super-Properties": x_super_property}
	data = session.get("https://discord.com/api/v9/users/@me", headers={"authorization":token}).json()
	if "code" in data:
		code = data["code"]
		if code == 0:
			print("invalid token")
			return
		if code == 40002:
			print("locked")
			return
	data = session.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers).json()
	if not "captcha_key" in data:
		if "code" in data:
			code = data["code"]
			if code == 40002:
				print("locked")
			else:
				print("Already Joined")
		else:
			print(data)
		return
	print("captcha detected")
	captcha_key = solver(session, data["captcha_sitekey"], f"https://discord.com/api/v9/invites/{invite}")
	data = session.post(f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={"captcha_key":captcha_key}, proxies=proxy).json()
	print(data)
	if "code" in data:
		print("Joined")

for token in tokens:
	joiner(token)
	time.sleep(1) #slowly joining to bypassing official anti-raid
