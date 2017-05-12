from groupmeLib import messages

#TODO refactor
#TODO create util module/package
#TODO create util function that takes an output that uses user_id and prints it with Name


def getSelfFavoritedCountByUser(groupId, msgs=None, groupUserDictionary=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    if(groupUserDictionary is None):
        groupUserDictionary = getAllGroupUsers(groupId, msgs)

    selfFavoritesCounts = {}
    for message in msgs:
        for favoriter in message['favorited_by']:
            if(groupUserDictionary[favoriter] not in selfFavoritesCounts.keys()):
                selfFavoritesCounts[groupUserDictionary[favoriter]] = 0
            if(message['user_id'] == favoriter):
                selfFavoritesCounts[groupUserDictionary[favoriter]] += 1
    return selfFavoritesCounts


#TODO: refactor this so is done by user_id instead of Name
def getFavoritedCountByUser(groupId, msgs=None, groupUserDictionary=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    if(groupUserDictionary is None):
        groupUserDictionary = getAllGroupUsers(groupId, msgs)

    favoriteCounts = {}
    for message in msgs:
        if(groupUserDictionary[message['user_id']] not in favoriteCounts.keys()):
            favoriteCounts[groupUserDictionary[message['user_id']]] = 0
        favoriteCounts[groupUserDictionary[message['user_id']]] += len(message['favorited_by'])
    return favoriteCounts


#TODO: refactor this so is done by user_id instead of Name
def getFavoritesGivenCountbyUser(groupId, msgs=None, groupUserDictionary=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    if(groupUserDictionary is None):
        groupUserDictionary = getAllGroupUsers(groupId, msgs)

    favoritesGivenCounts = {}
    for message in msgs:
        for favoriter in message['favorited_by']:
            if(groupUserDictionary[favoriter] not in favoritesGivenCounts.keys()):
                favoritesGivenCounts[groupUserDictionary[favoriter]] = 0
            favoritesGivenCounts[groupUserDictionary[favoriter]] += 1
    return favoritesGivenCounts


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
print getSelfFavoritedCountByUser(5954413, msgs)

#(13104384) SPORTS
#(30425709) Brewgaloo
#(5954413) WPFL