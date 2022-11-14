from linkedin_api import Linkedin
import env
import json
import boto3

user = env.getUser()
password = env.getPassword()

api = Linkedin(user, password)

def getContact(target):
    return api.get_profile_contact_info(target)

def getProfile(target):
    return api.get_profile(target)

def sendToDynamoDB(event):
    client_dynamo=boto3.resource('dynamodb')
    table=client_dynamo.Table('UsersDataLinkedin')
    try:
        response=table.put_item(Item=event)
        return "Done"
    except:
        raise
def lambda_handler(event, context):
    arq = open("usuarios.txt") # open file with users to fetch
    linhas = arq.readlines()
    for linha in linhas:
        for target in linha.split(', '):
            data = {}
            print(f'searching contact info from {target}...')

            data['Email'] = getContact(target)["email_address"]
            data['FirstName'] = getProfile(target)["firstName"]
            data['LastName'] = getProfile(target)["lastName"]
            data['HeadLine'] = getProfile(target)["headline"]
            data['University'] = getProfile(target)["education"][0]["school"]["schoolName"]

            data = json.dumps(data, ensure_ascii=False).encode('utf8') # converting dictoinary to json and encoding to utf8 
            sendToDynamoDB(data.decode()) # decoding to utf8 and sending to dynamoDB