import requests

url="https://139.217.218.31/logincheck"
post_data={'username':"fgtapiuser1","secretkey":"Welcome01"}
# parameters={'wd':"abc"}
#提交get请求
# P_get=request.get(url,params=parameters)
#提交post请求
P_post=requests.post(url,data=post_data,verify=False)
print(P_post.text)

url2="https://139.217.218.31/api/v2/monitor/vpn/ipsec/"
s = requests.session()
response = s.post(url,data=post_data,verify=False)
response = s.get(url2)
print(response.text)

