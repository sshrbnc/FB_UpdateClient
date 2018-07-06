import json
import requests


url = "https://api.freshbooks.com/auth/oauth/token"

headers = {'Api-Version': 'alpha', 'Content-Type': 'application/json'}

payload = {'grant_type': 'authorization_code', 'client_secret': '32008ab5251bd243a192c9575e4a6962bb2aca0a4a66bc3e727503b06d62e6f8','code': 'e2d9c9654a8829d875d8838062414a771ba3abe831abf0bcb22e3c1eeef4671c', 'client_id': '3ed1514a2d8bd26bcb17dcd531c5c81469f7723a14dc864f541fc32466874772', 'redirect_uri': 'https://localhost:8080'}

res = requests.post(url, data=json.dumps(payload), headers=headers)

jsonData = res.json()

print jsonData

# store bearer token

f = open("bearerToken.txt", "w+")
data = jsonData['access_token']
f.write(data)
f.close()

# store refresh token
f = open("refreshToken.txt", "w+")
data = jsonData['refresh_token']
f.write(data)
f.close()

# {u'access_token': u'5ebf0040cf94f92fba949ec77435b0d73e32647f94d0b42c91f63a4fb76cd29b', u'created_at': 1530614071, u'expires_in': 43199, u'token_type': u'bearer', u'scope': u'profile:write', u'refresh_token': u'fc7732b2391109fc272f8374d4fbe60fa3d5303986f65fde1023749144ff88be'}