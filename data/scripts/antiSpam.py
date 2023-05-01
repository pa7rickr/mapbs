import bs
import bsInternal
import bsPowerup
import bsUtils
import random
import getPermissionsHashes as gph
import json
import coinSystem
from threading import Timer
import floater
#byZDARK
#remakeNROFFICIAL 
from settings import *

reply = None
replyColor = None
lol = None

class Custom(object):

    def __init__(self, id, tag):
        self.id = id
        self.tag = tag


def make_custom(id, tag):
    custom = Custom(id, tag)
    return custom


class chatOptions(object):

    def __init__(self):
        self.all = True
        self.tint = None
        return

    def checkDevice(self, clientID, command):
        global commandByCoin
        global commandSuccess
        global costOfCommand
        global reply
        global replyColor
        global lol
        global user
        commandByCoin = None
        commandSuccess = None
	reply = None
	replyColor = None
	lol = None
        client_str = ''
        for i in bsInternal._getForegroundHostSession().players:
            if i.getInputDevice().getClientID() == clientID:
                client_str = i.get_account_id()

        try:
            if client_str in gph.ownerHashes:
                reply = u'\ue043\ue00cWNER C\ue00cMMAND ACCEPTED\ue043'
                replyColor = 0,1,3
		#reply = ''
                return 10
            elif client_str in gph.adminHashes:
                    reply = u'\ue048ADMIN C\ue00cMMAND ACCEPTED\ue048'
                    replyColor = 1,0.5,0
		    #reply = ''
                    return 3
            elif client_str in gph.vipHashes:
                    reply = u'\ue049VIP C\ue00cMMAND ACCEPTED\ue049'
                    replyColor = 1,0.15,0.15
		    #reply = ''
                    return 2
            elif enableCoinSystem and command in availableCommands:
                    costOfCommand = availableCommands[command]
                    haveCoins = coinSystem.getCoins(client_str)
                    if haveCoins >= costOfCommand:
                        commandByCoin = True
                        user = client_str
                        return 3
                    bsInternal._chatMessage('You need ' + bs.getSpecialChar('ticket') + str(costOfCommand) + ' for that. You have ' + bs.getSpecialChar('ticket') + str(haveCoins) + ' only.')
            elif enableTop5commands and client_str in gph.topperslist:
                        lol = 'Top 5 player, COMMAND ACCEPTED'
		        #reply = ''
                        return 1
            return 0

        except:
            pass

        return 0

    def kickByNick(self, nick):
        roster = bsInternal._getGameRoster()
        for i in roster:
            try:
                if i['players'][0]['nameFull'].lower().find(nick.encode('utf-8').lower()) != -1:
                    bsInternal._disconnectClient(int(i['clientID']))
            except:
                pass

    def opt(self, clientID, msg):
        global commandSuccess
        m = msg.split(' ')[0]
        a = msg.split(' ')[1:]
        activity = bsInternal._getForegroundHostActivity()
        with bs.Context(activity):
            '''sender = None
            for i in activity.players:
                if i.getInputDevice().getClientID() == clientID:
                    sender = i.getName()

            try:
                #bs.screenMessage(sender + ':' + msg, color=(0,2.55,2.55))
		pass
            except:
                pass'''

            level = self.checkDevice(clientID, m)
            if m == '':
                bs.screenMessage("Dont Try To Spam Pls", color=(1,0,0))
                
c = chatOptions()


def cmd(msg, clientID):
    c.opt(clientID, msg)
    if commandSuccess:
        if commandByCoin:
            coinSystem.addCoins(user, costOfCommand * -1)
        else:
	  try:
		with bs.Context(bsInternal._getForegroundHostActivity()):
			bs.screenMessage(lol)
            		#bsInternal._chatMessage(reply)
	  except:
		pass
    return