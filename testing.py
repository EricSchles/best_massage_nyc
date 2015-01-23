import requests

r = requests.get("https://www.google.com")
with open("filez.txt","w") as f:
	f.write(r.text)
