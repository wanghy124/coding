import requests

url = "https://52.130.67.198/jsonrpc"

payload = "{\n\"id\":1,\n\"jsonrpc\":\"1.0\",\n\"method\":\"exec\",\n\"params\":[\n{\n\n\"url\":\"/sys/logout\"\n}\n],\n" \
          "\"session\": \"fuRcSs\/iEILt7ozcEbNI90ZhPoNwo\/+lgNLxb5ANgojOHD0rfNpLKdW1JfZiCmg8kkjLx1vGeAggB3flAx7GBA==\",\n" \
          "\"verbose\":1\n}"
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
