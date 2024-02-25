import requests
import os


def Input(text):
    print(text)
    return input()

def loginWebsite(url, user, password):
    creds = {
            'login':user,
            'password':password
            
    }
    response = requests.post(url, data=creds)
    return response






urlMenu = ''
User = Input('Inserisci l\'username: ')
Pass = Input('Inserisci la password: ')
if(User == ''):
    User = 'S8968986P'
if(Pass == ''):
    Pass = 'dkJue82K0-'

lResponse = loginWebsite(urlLogin, User, Pass)
lResponse.encoding = 'utf-8'
print(lResponse.status_code)



print(lResponse.text)


cookies = lResponse.cookies
sesId = cookies.get('\n\n\tPHPSESSID')
print(sesId)
