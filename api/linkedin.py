import os
import requests

def getData():
    base_url = os.environ.get("URL_Linkedin_id")
    request = requests.get(base_url)
    return request.json()


def getEmail():
    base_url = os.environ.get("URL_Linkedin_email")
    request = requests.get(base_url)
    return request.json()