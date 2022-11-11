from linkedin_api import Linkedin
import json
import env
# Authenticate using any Linkedin account credentials
user = env.getUser()
password = env.getPassword()

api = Linkedin(user, password)

# # GET a profile
# profile = api.get_profile('aviladiogo')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('aviladiogo')

# # GET 1st degree connections of a given profile
# connections = api.get_profile_connections('aviladiogo')

# print(profile)
print(contact_info)
# print(connections)