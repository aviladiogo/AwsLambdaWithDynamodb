from linkedin_api import Linkedin
import env

user = env.getUser()
password = env.getPassword()

api = Linkedin(user, password)

# GET a profiles contact info
def getContact(target):
    return api.get_profile_contact_info(target)

if __name__ == '__main__':
    arq = open("usuarios.txt")
    linhas = arq.readlines()
    for linha in linhas:
        for target in linha.split(', '):
            print(f'searching contact info from {target}...')
            print(f'Email = {getContact(target)["email_address"]}')
            print(f'Websites = {getContact(target)["websites"]}')
            print(f'Twitter = {getContact(target)["twitter"]}')