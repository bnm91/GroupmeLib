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


def getUserFavoritedBy(groupId, userId, msgs=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    groupUserDictionary = getAllGroupUsers(groupId, msgs)

    favoritedByCounts = {}
    for message in msgs:
        if message['user_id'] == userId:
            for favoriter in message['favorited_by']:
                if(groupUserDictionary[favoriter] not in favoritedByCounts.keys()):
                    favoritedByCounts[groupUserDictionary[favoriter]] = 0
                favoritedByCounts[groupUserDictionary[favoriter]] += 1
    return favoritedByCounts


def getAllUsersFavoritedByCount(groupId, msgs=None, groupUserDictionary=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    if(groupUserDictionary is None):
        groupUserDictionary = getAllGroupUsers(groupId, msgs)

    favoritedByCounts = {}
    for user in groupUserDictionary:
        favoritedByCounts[groupUserDictionary[user]] = getUserFavoritedBy(groupId, user, msgs)
    return favoritedByCounts


def getAllGroupUsers(groupId, msgs=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    userDictionary = {}
    for message in reversed(msgs):
        if(message['user_id'] not in userDictionary.keys()):
            userDictionary[message['user_id']] = message['name']
    return userDictionary


def getAllGroupUsersReverse(groupId, msgs=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    userDictionary = {}
    for message in msgs:
        if(message['user_id'] not in userDictionary.keys()):
            userDictionary[message['user_id']] = message['name']
    return userDictionary



#TODO: investigate why with group 4501211 there are users in this result that aren't in the groupUserDictionary
# the issue is that Doug, Nixon, and possibly others had their first message labeled as "groupme" so it they don't have a unique name even if they do have a unique user id's
def getMessageCountPerUser(groupId, msgs=None, groupUserDictionary=None):
    if(msgs is None):
        msgs = messages.getAllGroupMessages(groupId)
    if(groupUserDictionary is None):
        groupUserDictionary = getAllGroupUsers(groupId, msgs)
        
    messageCounts = {}
    for message in msgs:
        if(message['user_id'] not in messageCounts.keys()):
            messageCounts[message['user_id']] = 0
        messageCounts[message['user_id']] += 1

    messageCountsByName = {}
    for key in messageCounts.keys():
        messageCountsByName[groupUserDictionary[key]] = messageCounts[key]

    return messageCountsByName




msgs = messages.getAllGroupMessages(5954413)
#users = getAllGroupUsersReverse(4501211, msgs)
print getFavoritedCountByUser(5954413, msgs)#, users)

#(13104384) SPORTS
#(30425709) Brewgaloo
#(5954413) WPFL
#(4501211) Cary Krewe (OG)
#(18020667) Blue's Krewe


#('17421009') chapla user id