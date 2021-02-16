import requests


r = requests.get("https://serdarkuyuk.netlify.app")
print(r.status_code)

print(r.ok)
