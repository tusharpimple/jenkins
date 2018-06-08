import requests
url = "http://13.56.11.237:8080/job/newone/buildwithparameter"
target = "http://13.56.11.237:8080/"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
msg = {
    'token': '9d1e2b6f0cf80d8040f8c9f65bc7a57d',
    'target': [ target ],
}
r = requests.post(url, headers=headers, data=msg)
