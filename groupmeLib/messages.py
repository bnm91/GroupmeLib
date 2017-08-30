import json
import requests
from config import config


#TODO: add handling for no response/bad response etc
#TODO: rename this package.  Messages begs to become overloaded when this module is used elsewhere


#TODO implement
def getGroupId(groupName):
	return 1

def getGroupMessageCount(groupId):
	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + config['accessToken'])
	response = r.json()['response']
	messageCount = response['count']
	return messageCount


#TODO: implement
def getPreviousMessage(groupId, messageId):
	return 1


#TODO: implement
def getMessage(groupId, messageId):
	return 1


#TODO implement
def getAllMessagesByUser(userId):
	return 1


#TODO implement
def getAllMessagesInTimeRange(beginTime, endTime):
	return 1


#TODO: add some sort % complete output
def getAllGroupMessages(groupId):
	parameters = {'limit' : 100}
	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + config['accessToken'], params=parameters)
	response = r.json()['response']
	totalGroupMessageCount = response['count']
	print totalGroupMessageCount
	messages = response['messages']
	retrievedMessageCount = len(messages)

	while(retrievedMessageCount < totalGroupMessageCount):
		# if(retrievedMessageCount % 100 != 0): #this is because in some cases groupmes count seems to be wrong.  this prevents it from crashing in the end.  #TODO:rework this 
		# 	break
		before_id = messages[len(messages) -1]['id']
		parameters['before_id'] = before_id
		try:
			retrievedMessages = getGroupMessages(groupId, parameters)
		except:
			break
		messages += retrievedMessages
		retrievedMessageCount += len(retrievedMessages)
		print str(retrievedMessageCount) + ' ' + str(before_id)

	return messages


# #trying out a differnt way
# def getAllGroupMessages(groupId):
# 	parameters = {'limit' : 100}
# 	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + config['accessToken'], params=parameters)
# 	response = r.json()['response']
# 	totalGroupMessageCount = response['count']
# 	messages = response['messages']
# 	retrievedMessageCount = len(messages)
# 	totalRetrievedMessageCount = retrievedMessageCount

# 	while(retrievedMessageCount == 100):
# 		before_id = messages[len(messages) -1]['id']
# 		parameters['before_id'] = before_id
# 		retrievedMessages = getGroupMessages(groupId, parameters)
# 		messages += retrievedMessages
# 		retrievedMessageCount = len(retrievedMessages)
# 		totalRetrievedMessageCount += retrievedMessageCount
# 		print str(totalRetrievedMessageCount) + ' ' + str(before_id)

# 	return messages


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
	
	url = 'https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + config['accessToken']
	r = requests.get('https://api.groupme.com/v3/groups/' + str(groupId) + '/messages?token=' + config['accessToken'], params=callParameters)
	response = r.json()['response']
	messages = response['messages']
	return messages




# print getAllGroupMessages(30425709)