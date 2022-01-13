import requests

url = 'https://webaddress/file'
r = requests.get(url, allow_redirects=True)
open('logo.png', 'wb').write(r.content)