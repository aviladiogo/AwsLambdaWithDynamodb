from linkedin_api import Linkedin
import env

user = env.getUser()
password = env.getPassword()

api = Linkedin(user, password)

# GET a profile
# profile = api.get_profile('aviladiogo')
def getProfile():
    return api.get_profile('aviladiogo')

# GET a profiles contact info
def getContact():
    return api.get_profile_contact_info('aviladiogo')

# GET 1st degree connections of a given profile
# connections = api.get_profile_connections('aviladiogo')
def getConnections():
    return api.get_profile_connections('aviladiogo')

if __name__ == '__main__':
    answer = 0
    while(answer != '3'):
        print('0- Get a profile')
        print('1- Get a profiles contact info')
        print('2- GET 1st degree connections of a given profile')
        print('3- Exit')
        answer = input("What's you want find ? \n")

        # print(getContact()['email_address'])
        match answer:
            case "0":
                print('searching profile...')
                print(getProfile())

            case "1":
                print('searching contact info...')
                print('Email = ' +getContact()['email_address'])
                print('Websites = ' +getContact()['websites'][0]['url'])
                print(f'Twitter = {getContact()["twitter"]}')

            case "2":
                print('searching connections...')
                print(getConnections())

            case "3":
                print("Bye bye")

            case _:
                print("whats is that ?")
