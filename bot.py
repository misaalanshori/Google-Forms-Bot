from bs4 import BeautifulSoup
import requests

target = "https://docs.google.com/forms/d/e/1FAIpQLSdDMrTY__l-SieCzWZX0XUJgYFLNUdXRvqiFcnBXEkOEHQ37g/"
payloads = [
    {
        "entry.1440537076": "abc",
        "entry.528347400": "def",
        "fvv" : "1",
        "partialResponse": "[null,null,\"fbzx\"]",
        "pageHistory": "0",
        "fbzx": "fbzx",
        "continue": "1"
    },
    {
        "entry.2075281704": "gross",
        "entry.685161618": "Maybe",
        "entry.685161618_sentinel": "",
        "fvv" : "1",
        "partialResponse": "[[[null,1440537076,[\"abc\"],0],[null,528347400,[\"def\"],0]],null,\"fbzx\"]",
        "pageHistory": "0,1",
        "fbzx": "fbzx"
    }
]

for i in range(200):
    req = requests.get(target + "viewform").text
    soup = BeautifulSoup(req, "html.parser")
    fbzx = soup.find_all("input")[-1]["value"]
    for i in payloads:
        payload = i 
        payload["partialResponse"] = payload["partialResponse"].replace("fbzx", fbzx)
        payload["fbzx"] = payload["fbzx"].replace("fbzx", fbzx)
        response = requests.post(target+"formResponse", payload, headers={"Content-Type":"application/x-www-form-urlencoded", "referer": target + "viewform?fbzx=" + fbzx})

