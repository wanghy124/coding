import requests
import re

url = "https://52.130.67.198/jsonrpc"

payload = "{\n\"id\":1,\n\"method\":\"exec\",\n\"params\":[\n{\n\"data\":{\n\"passwd\":\"Welcome01\",\n\"user\":" \
          "\"fmgapiuser2\"\n },\n\"url\":\"/sys/login/user\"\n }\n]\n}"
headers = {'Content-Type':'text/plain'}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

# print(response.text.encode('utf8'))


session_id = re.findall('.*"session":\s"(.*)"\s}',response.text)
print(session_id[0])
