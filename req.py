import requests
import os




def inp(a):
	print(a)
	i = input()
	return i


def getText(response):
	tResponse = response.text
	return tResponse


def getContent(response):
	cResponse = response.content
	return cResponse


def getHeader(response, header):
	hResponse = response.headers[header]
	return hResponse

def getHead(response):
	hResponse = response.headers
	return hResponse

def getJson(response):
	jResponse = response.json()
	return jResponse

def getCookies(response):
	cookies = response.cookies
	return cookies



def getSesId(response):
	cookies = response.cookies
	sesId = cookies.get('session_id')
	return sesId




def showRepositories():
	while (i<20):
		repository = jResponse['items'][i]
		print(f'Repository name: {repository["name"]}')
		print(f'Repository name: {repository["description"]}''\n\n')
		i = i+1
		if(f'{repository["name"]}' == 'requests'):
			print('OOOooOOooooOOOOOMMmmmmmMMMaaaaaAAAAaaGGGGGAaaaaaAAAWWWWWWWWWWWddddddDDD')
			break


def switch(ch):
	func=switch.get(ch)
	return func() if func else 'Invalid case'






#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------S T A R T----------------------------------------------------------------------------------------------------------------

url = inp('url   DEF=google')
if(url == ''):
	url = 'https://web.spaggiari.eu/home/app/default/menu_webinfoschool_studenti.php?custcode=' 
print('receiving data from: ')
print(url)
print('\n\n')
ch = inp('\t1)Text\n\t2)Content\n\t3)Header\n\t4)Specific header\n\t5)Json\n\t6)Cookies\n\t7)Session ID\n')
response = requests.get(url)
response.encoding = 'utf-8'
i = 0


switch = {
	'1':getText,
	'2':getContent,
	'3':getHead,
	'4':getHeader,
	'5':getJson,
	'6':getCookies,
	'7':getSesId
}

chosen_function = switch.get(ch)
if chosen_function:
    print(chosen_function(response))
else:
    print('Invalid case')





