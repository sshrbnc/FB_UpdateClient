import json
import requests

# account_id => 6GeAy

bearer = open('bearerToken.txt', "r")
bearerContent = bearer.read() #stores the bearer token to this variable

tokenRefresh = open('refreshToken.txt', "r")
tokenRefreshContent = tokenRefresh.read() #stores the refresh token to this variable


refTokenInput = raw_input('Enter your refreshToken: ')

flag = False

if(refTokenInput == tokenRefreshContent):
	flag = True
else:
	print 'Unauthorized refresh token!'


# generate new refresh token

def getNewRefreshToken():
	tokenPass = tokenRefreshContent

	getNewTokenUrl = "https://api.freshbooks.com/auth/oauth/token"
	getNewTokenHeaders = {'Api-Version': 'alpha', 'Content-Type': 'application/json'}
	getNewTokenPayload = {
							'grant_type': 'refresh_token', 
							'client_secret': '32008ab5251bd243a192c9575e4a6962bb2aca0a4a66bc3e727503b06d62e6f8',
							'refresh_token': tokenPass, 
							'client_id': '3ed1514a2d8bd26bcb17dcd531c5c81469f7723a14dc864f541fc32466874772', 
							'redirect_uri': 'https://localhost:8080'
						}

	getNewTokenResponse = requests.post(getNewTokenUrl, data=json.dumps(getNewTokenPayload), headers=getNewTokenHeaders)

	# print (getNewTokenPayload)
	jsonData = getNewTokenResponse.json()

	# parseData = ast.literal_eval(json.dumps(jsonData))

	print jsonData

	# store new bearer token

	bearer = open("bearerToken.txt", "w+")
	data = jsonData['access_token']
	bearer.write(data)
	bearer.close()

	# store new refresh token

	tokenRefresh = open("refreshToken.txt", "w+")
	data = jsonData['refresh_token']
	tokenRefresh.write(data)
	tokenRefresh.close()

	print 'Your new refresh token is: ' + jsonData['refresh_token']

def updateClient(clientID):
	client_id = clientID
	bearerPass = bearerContent

	email = raw_input('Email: ')
	fname = raw_input('Firstname: ')
	lname = raw_input('Lastname: ')
	organization = raw_input('Organization: ')
	home_phone = raw_input('Phone Number: ')
	p_street = raw_input('Street: ')
	p_city = raw_input('City: ')
	p_code = raw_input('Zip Code: ')
	p_country = raw_input('Country: ')

	url = "https://api.freshbooks.com/accounting/account/6GeAy/users/clients/" + client_id
	headers = {'Authorization': 'Bearer ' + bearerPass, 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
	payload = {'client': 
					{ 
		            'email': email,
		            'fname': fname,
		            'lname': lname,
		            'organization': organization,
		            'home_phone': home_phone,
		            'p_street': p_street,
		            'p_city': p_city,
		            'p_code': p_code,
		            'p_country': p_country
		            } 
	          }
	res = requests.put(url, data=json.dumps(payload), headers=headers)

	jsonData = res.json()
	print jsonData
	print "Updated client data!"

if(flag):
	clientID = raw_input('Enter Client ID: ')
	updateClient(clientID)
	# update(tokenRefreshContent, payload)
	getNewRefreshToken()

