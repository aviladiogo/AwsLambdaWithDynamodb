import database.dynamo as dynamo
import database.mongo as mongo
import api.linkedin as linkedin
from json import loads

def lambda_handler(event, context):
    """

    First we will insert into dynamoDB the user data from linkedin

    """
    data = {}
    data['ID'] = linkedin.getData()['id']
    data['Name'] = linkedin.getData()['localizedFirstName']
    data['LastName'] = linkedin.getData()['localizedLastName']
    data['Email'] = linkedin.getEmail()['elements'][0]['handle~']['emailAddress']

    dynamo.sendToDynamoDB(data)

    """
    
    active chatbot
    
    """
    
    """
    get events from chatbot (into dynamoDB) and convert the string to dictionary 
    """

    chatbotData = dynamo.getFromDynamoDB(3243243)
    chatbotEventsString = chatbotData['Item']['events']
    chatbotEventsToDictionary = loads(chatbotEventsString)
    
    """
    send infos to gupy (MongoDB for now)
    """
    dbname = mongo.acessMongodb()
    collection_name = dbname["Linkedin_users"]
    infos ={
        "_id": data['ID'],
        "Name": data['Name'],
        "LastName": data['LastName'],
        "Email": data['Email'],
        "Answer_1": chatbotEventsToDictionary[13]['M']['text']['S'],
        "Answer_2": chatbotEventsToDictionary[18]['M']['text']['S'],
        "Answer_3": chatbotEventsToDictionary[23]['M']['text']['S'],
        "Answer_4": chatbotEventsToDictionary[28]['M']['text']['S']
    }
    collection_name.insert_one(infos)
