import time, random, requests
url = "https://discord.com/api/v9/channels/1060211977957412964/messages"
headers = {"authorization":"token"}

words = ["japanese", "english", "pencil", "mechanical pencil"]


def generate(text):
	data = requests.get("http://metaphorpsum.com/paragraphs/2/4").text
	return data[:random.randint(30,60)]
while True:
	requests.post(url, headers=headers, json={"content":generate(random.choice(words))})
	time.sleep(random.randint(7,10))