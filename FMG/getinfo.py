import requests

url = "https://52.130.67.198/jsonrpc"

payload = "{\n\"method\":\"get\",\n \"params\":[\n{\n\"meta fields\":[\n\"\"\n],\n\"url\":\"/dvmdb/device\"\n}\n],\n" \
          "\"session\": \"fuRcSs\/iEILt7ozcEbNI90ZhPoNwo\/+lgNLxb5ANgojOHD0rfNpLKdW1JfZiCmg8kkjLx1vGeAggB3flAx7GBA==\"," \
          "\n\"id\":1\n}"

headers = {'Content-Type': 'text/plain'}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text.encode('utf8'))
