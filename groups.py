import json
import requests
from config import config



def getGroupsDictionary(accessToken, max=None):
	if(max is not None):
		parameters = {'per_page' : max}
	else:
		parameters = {'per_page' : 100}
	r = requests.get('https://api.groupme.com/v3/groups?token=' + config['accessToken'], params=parameters)
	groups = r.json()['response']
	groupList = {}
	for group in groups:
		groupList[group['name']] = group['id']
	return groupList


def getGroups(accessToken, max=None):
	if(max is not None):
		parameters = {'per_page' : max}
	else:
		parameters = {'per_page' : 100}
	r = requests.get('https://api.groupme.com/v3/groups?token=' + config['accessToken'], params=parameters)
	groups = r.json()['response']
	return groups


def getGroup(accessToken, id):
	r = requests.get('https://api.groupme.com/v3/groups/' + str(id) + '?token=' + config['accessToken'])
	group = r.json()['response']
	return group

print getGroup(config['accessToken'], 30425709)