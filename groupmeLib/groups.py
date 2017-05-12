import json
import requests
from config import config



def getGroupMembers(groupId):
	group = getGroup(groupId)
	members = group['members']
	return members


def getGroupMembersNameList(groupId):
	members = getGroupMembers(groupId)
	membersList = []
	for member in members:
		membersList.append(member['nickname'])
	
	return membersList


def getGroup(groupId):
	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '?token=' + config['accessToken'])
	group = r.json()['response']
	return group







def getGroupsDictionary(max=None):
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


def getGroups(max=None):
	if(max is not None):
		parameters = {'per_page' : max}
	else:
		parameters = {'per_page' : 100}
	r = requests.get('https://api.groupme.com/v3/groups?token=' + config['accessToken'], params=parameters)
	groups = r.json()['response']
	return groups



print getGroupMembersNameList(30425709)