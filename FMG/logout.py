import requests

url = "https://52.130.67.198/jsonrpc"

payload = "{\n\"id\":1,\n\"jsonrpc\":\"1.0\",\n\"method\":\"exec\",\n\"params\":[\n{\n\n\"url\":\"/sys/logout\"\n}\n],\n" \
          "\"session\": \"x6f6QyzHRZ3sh38RVi70zkLMh4V4GDhg5/icSqH4OjjB6hIt3YKgN/iY6F21z2xAS4JUqkR61s2S6l/55M7vjw==\",\n" \
          "\"verbose\":1\n}"
headers= {}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
