from flask import Flask, request, jsonify, abort
import json, requests

app = Flask(__name__)

@app.route('/updateClient', methods=['POST'])


def updateClient():    
	updateData = json.loads(request.data)
	client_id = request.json['client_id']

	url = 'https://api.freshbooks.com/accounting/account/6GeAy/users/clients/' +  client_id

	headers = { 'Authorization': 'Bearer 753f5126ac8eb75cb5f6bbfe159170b8b7d648cbdf1d0e31f3cc636c5b17b163', 'Api-Version': 'alpha', 'Content-Type': 'application/json' }
	payload = {'client': { 
			            'email': updateData['email'],
			            'fname': updateData['fname'],
			            'lname': updateData['lname'],
			            'organization': updateData['organization'],
			            'home_phone': updateData['home_phone'],
			            'p_street': updateData['p_street'],
			            'p_city': updateData['p_city'],
			            'p_province': updateData['p_province'],
			            'p_code': updateData['p_code'],
			            'p_country': updateData['p_country']
		            	} 
	          }
	res = requests.put(url, data=json.dumps(payload), headers=headers)

	jsonData = res.json()



	# generate new token

	getNewTokenUrl = "https://api.freshbooks.com/auth/oauth/token"
	getNewTokenHeaders = {'Api-Version': 'alpha', 'Content-Type': 'application/json'}
	getNewTokenPayload = {
							'grant_type': 'refresh_token', 
							'client_secret': '32008ab5251bd243a192c9575e4a6962bb2aca0a4a66bc3e727503b06d62e6f8',
							'refresh_token': '4a8970efbf9134eaf68a8635a73dbff573ffe893df66f3e39f96ec497a198173', 
							'client_id': '3ed1514a2d8bd26bcb17dcd531c5c81469f7723a14dc864f541fc32466874772', 
							'redirect_uri': 'https://localhost:8080'
						}

	getNewTokenResponse = requests.post(getNewTokenUrl, data=json.dumps(getNewTokenPayload), headers=getNewTokenHeaders)

	getNewTokenData = getNewTokenResponse.json()


	return jsonify({'refreshToken': getNewTokenData['refresh_token']}, jsonData)	

if __name__ == '__main__':
    app.run(debug=True)