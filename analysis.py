from groupmeLib import messages

#TODO refactor


def getAllGroupUsers(groupId, msgs=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    userDictionary = {}
    for message in reversed(msgs):
        if(message['user_id'] not in userDictionary.keys()):
            userDictionary[message['user_id']] = message['name']
    return userDictionary


#TODO: implement
def getMessagesByUser(groupId, msgs=None):
    return 1


def getMessageCountPerUser(groupId, msgs=None, groupUserDictionary=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    if(groupUserDictionary is None):
        groupUserDictionary = getAllGroupUsers(groupId, msgs)
        
    messageCounts = {}
    for message in msgs:
        if(groupUserDictionary[message['user_id']] not in messageCounts.keys()):
            messageCounts[groupUserDictionary[message['user_id']]] = 0
        messageCounts[groupUserDictionary[message['user_id']]] += 1
    return messageCounts




msgs = messages.getAllGroupMessages(5954413)
print getMessageCountPerUser(5954413, msgs)

#(13104384) SPORTS
#(30425709) Brewgaloo
#(5954413) WPFL