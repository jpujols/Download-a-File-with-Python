url = #

import requests

req = request.get(url)
content = req.content

with open('download.mp3', 'wb') as file:
  file.write(content)