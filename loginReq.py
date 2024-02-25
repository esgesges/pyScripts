import requests
import os


def Input(text):
    print(text)
    return input()


def login(url, username, password):


    session = requests.Session()
    response = session.get(url)
#    csrfToken = response.cookies['csrftoken']
    
    payload = {
#    	'csrfmiddlewaretoken':csrfToken,
        'username':username,
        'password':password,
    }
    

    headers = {
    'referer':url,
#   'X-csrfToken':csrfToken,
    }

    
    lResponse = session.post(url, data=payload)		#headers=headers
    
    
    return lResponse


url = 'https://practicetestautomation.com/practice-test-login/'
username = 'student'
password = 'Password123'

lResponse = login(url, username, password)
lResponse.encoding = 'utf-8'
print(lResponse.headers)
print(lResponse.status_code)
print(lResponse.text)
