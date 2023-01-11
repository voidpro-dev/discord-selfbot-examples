import requests, json, re

token = ""

channel = input("Channel > ")
command = input("/")
data = requests.get("https://discord.com/api/v9/channels/{}/application-commands/search?type=1&query={}&limit=7&include_applications=false".format(channel, command), headers={"authorization":token}).json()
commands = data["application_commands"]
if len(commands) == 1:
	n = 0
else:
	for n in range(len(commands)):
		print("{}. /{} : {}".format(n+1, commands[n]["name"], commands[n]["description"]))
	n = int(input("> "))-1
options = []
for option in commands[n]["options"]:
	options.append("{\"type\":" + str(option["type"]) + ",\"name\":\"" + option["name"] + "\", \"value\":" + option["name"] + "}")
wara = ("{\"type\":2,\"application_id\":\"" + commands[n]["application_id"] +
"\",\"guild_id\":guild_id,\"channel_id\":\"" + channel + 
"\",\"session_id\":session_id,\"data\":{\"version\":\"" + commands[n]["version"] + 
"\",\"id\":\"" + commands[n]["id"] + 
"\",\"guild_id\":guild_id" + 
",\"name\":\"" + commands[n]["name"] + 
"\",\"type\":" + str(commands[n]["type"]) + 
",\"options\":[" + ','.join(options) + 
"], \"application_command\":" + json.dumps(commands[n]) + 
",\"attachments\":[]}, \"nonce\":str(time.time_ns())}")
wara = re.sub(": null", ": None", wara)
wara = re.sub(": true", ": True", wara)
wara = re.sub(": false", ": False", wara)
print("\n\n")
print(wara)
print("\n\n")