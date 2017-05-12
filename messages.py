import json
import requests
from config import accessToken


#TODO: find a better way to handle access token
#TODO: add handling for no response/bad response etc




def getGroupMessageCount(groupId):
	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + accessToken)
	response = r.json()['response']
	messageCount = response['count']
	return messageCount


#TODO: implement
def getPreviousMessage(messageId):
	return 1


def getAllGroupMessages(groupId):
	parameters = {'limit' : 100}
	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + accessToken, params=parameters)
	response = r.json()['response']
	totalGroupMessageCount = response['count']
	messages = response['messages']
	retrievedMessageCount = len(messages)

	while(retrievedMessageCount <= totalGroupMessageCount):
		before_id = messages[len(messages) -1]['id']
		print before_id
		parameters['before_id'] = before_id
		messages += getGroupMessages(groupId, parameters)
		retrievedMessageCount += len(messages)

	return messages


#TODO refactor to avoid duplication
def getGroupMessages(groupId, inputParameters):
	callParameters = {}

	if('limit' in inputParameters):
		limit = inputParameters['limit']
		callParameters['limit'] = limit
	if('before_id' in inputParameters):
		before_id = inputParameters['before_id']
		callParameters['before_id'] = before_id
	if('since_id' in inputParameters):
		since_id = inputParameters['since_id']
		callParameters['since_id'] = since_id
	if('after_id' in inputParameters):
		after_id = inputParameters['after_id']
		callParameters['after_id'] = after_id
	
	url = 'https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + accessToken
	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + accessToken, params=callParameters)
	response = r.json()['response']
	messages = response['messages']
	return messages




print getAllGroupMessages(30425709)