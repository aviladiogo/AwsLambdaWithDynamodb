import boto3

def sendToDynamoDB(event):
    client_dynamo = boto3.resource("dynamodb")
    table = client_dynamo.Table("UsersDataLinkedin")
    try:
        response = table.put_item(Item=event)
        return "Done"
    except:
        raise


def getFromDynamoDB(id):
    client_dynamo = boto3.resource("dynamodb")
    table = client_dynamo.Table("rasa-chatbot-store")
    try:
        response = table.get_item(Key={"sender_id": id}, ProjectionExpression='events')
        return response
    except:
        raise

