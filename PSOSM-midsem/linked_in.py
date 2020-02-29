import urllib
import requests
import json
from linkedin_api import Linkedin

if __name__ == '__main__':

	api = Linkedin('aditya.bhadoo@gmail.com', 'DelhiBelly11#Snatch00')
	profile = api.get_profile('venkata-ratnadeep-suri')
	contact_info = api.get_profile_contact_info('venkata-ratnadeep-suri')
	connections = api.get_profile_connections('venkata-ratnadeep-suri')

	

	with open('venkata-ratnadeep-suri.txt', 'w') as p:
	    json.dump(profile, p)

	with open('venkata-ratnadeep-suri','w') as c:
		json.dump(contact_info,c)

	with open('venkata-ratnadeep-suri','w') as connect:
		json.dump(connections,connect)
    