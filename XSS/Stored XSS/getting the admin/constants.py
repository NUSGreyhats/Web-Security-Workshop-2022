import os

# Update the subdomain here (The only domain that the site can visit)
FLAG = os.getenv("CTF_FLAG", "ExampleFlag{This is a test flag}")
COOKIE = {"flag": FLAG}
BANNED = ["script", "style", "body", "div", "span", "img"]
WEB_LOCATION = "http://127.0.0.1:2776"
