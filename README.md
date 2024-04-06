import requests
 
string = "The sun shines bright on the meadow's path"
url = "http://ping.skarj.pl/rhyme"
payload = {"string": string}

response = requests.post(url, json=payload)
if response.status_code == 200:
    rhyming_line = response.json()["output"]
    print(rhyming_line)
else:
    print(f"Error: {response.status_code}")