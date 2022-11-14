import env
import json
import boto3
import requests

token = env.getToken()

def getData():
    base_url = f'https://api.linkedin.com/v2/me?oauth2_access_token={token}'
    request = requests.get(base_url)
    return request.json()

def getEmail():
    base_url = f'https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))&oauth2_access_token={token}'
    request = requests.get(base_url)
    return request.json()

def sendToDynamoDB(event):
    client_dynamo=boto3.resource('dynamodb')
    table=client_dynamo.Table('UsersDataLinkedin')
    try:
        response=table.put_item(Item=event)
        return "Done"
    except:
        raise

def lambda_handler(event, context):
    data = {}
    data['ID'] = getData()['id']
    data['Name'] = getData()['localizedFirstName']
    data['LastName'] = getData()['localizedLastName']
    data['Email'] = getEmail()['elements'][0]['handle~']['emailAddress']

    sendToDynamoDB(data) # decoding to utf8 and sending to dynamoDB