import bs
import bsInternal
import bsPowerup
import bsUtils
import random
import getPermissionsHashes as gph
import json
import coinSystem
from threading import Timer

from settings import *

reply = None

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
        global user
        commandByCoin = None
        commandSuccess = None
	reply = None
        client_str = ''
        for i in bsInternal._getForegroundHostSession().players:
            if i.getInputDevice().getClientID() == clientID:
                client_str = i.get_account_id()

        try:
            if client_str in gph.ownerHashes:
                reply = u'\ue043 OWNER COMMAND ACCEPTED \ue043'
		#reply = ':)'
                return 10
            if client_str in gph.coownerHashes:
                reply = u'\ue043 MANAGER COMMAND ACCEPTED \ue043'
		#reply = ':)'
                return 10
            elif client_str in gph.adminHashes:
                    reply = u'\ue048 ADMIN COMMAND ACCEPTED ||\ue048'
		    #reply = ':)'
                    return 3
            elif client_str in gph.vipHashes:
                    reply = u' \ue043 VIP COMMAND ACCEPTED \ue043'
		    #reply = ':)'
                    return 2
            elif enableCoinSystem and command in availableCommands:
                    costOfCommand = availableCommands[command]
                    haveCoins = coinSystem.getCoins(client_str)
                    if haveCoins >= costOfCommand:
                        commandByCoin = True
                        user = client_str
                        return 3
                    bsInternal._chatMessage('You need ' + bs.getSpecialChar('ticket') + str(costOfCommand) + ' for that. You have ' + bs.getSpecialChar('ticket') + str(haveCoins) + ' only. Type /me for detail information about you.')
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
                #bs.screenMessage(sender + ':' + msg, color=(0, 0.4, 0.8))
		pass
            except:
                pass'''

            level = self.checkDevice(clientID, m)
            if m in ('/stats', '/rank', '/myself', '/me'):
                for player in activity.players:
                    if player.getInputDevice().getClientID() == clientID:
                        f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/pStats.json', 'r')
                        pats = json.loads(f.read())
                        accountID = player.get_account_id()
                        #if enableCoinSystem: haveCoins = coinSystem.getCoins(accountID)
                        if accountID in pats:
			    if enableCoinSystem:
			        haveCoins = coinSystem.getCoins(accountID)
			        string = '| ' + player.getName() + ' #' + pats[str(accountID)]['rank'] + ' | ' + bs.getSpecialChar('ticket') + ' ' + str(haveCoins) + ' | Score: ' + pats[str(accountID)]['scores'] + ' | Kills: ' + pats[str(accountID)]['kills'] + ', Deaths: ' + pats[str(accountID)]['deaths'] + ', Games: ' + pats[str(accountID)]['games'] + ' |'
			    else:
			        string = '| ' + player.getName() + ' #' + pats[str(accountID)]['rank'] + ' | ' + ' | Score: ' + pats[str(accountID)]['scores'] + ' | Kills: ' + pats[str(accountID)]['kills'] + ', Deaths: ' + pats[str(accountID)]['deaths'] + ', Games: ' + pats[str(accountID)]['games'] + ' |'
			    bsInternal._chatMessage(string)

                            #bsInternal._chatMessage('|| ' + player.getName() + ' | Wallet:' + bs.getSpecialChar('ticket') + str(haveCoins) + ' | Rank:' + pats[str(accountID)]['rank'] + ' | Games:' + pats[str(accountID)]['games'] + ' | Score:' + pats[str(accountID)]['scores'] + ' | Kills:' + pats[str(accountID)]['kills'] + ' | Deaths:' + pats[str(accountID)]['deaths'] + ' ||')
                        else:
                            bsInternal._chatMessage('The player ' + str(player.getName()) + ' is not yet registered')
                        f.close()
                        break

            elif m == '/donate' and enableCoinSystem:
                try:
                    if len(a) < 2:
                        bs.screenMessage('Usage: /donate amount clientID', transient=True, clients=[clientID])
                    else:
                        transfer = int(a[0])
                        if transfer < 100:
                            bsInternal._chatMessage('You can only transfer more than ' + bs.getSpecialChar('ticket') + '100.')
			    return
                        sendersID = None
                        receiversID = None
                        for player in activity.players:
                            clID = player.getInputDevice().getClientID()
                            aid = player.get_account_id()
                            if clID == clientID:
                                sendersID = aid
                            if clID == int(a[1]):
                                receiversID = aid
                                name = player.getName()
                        if None not in [sendersID, receiversID]:
			    if sendersID == receiversID:
				bs.screenMessage('You can\'t transfer to your own account', color=(1, 0, 0))
                            elif coinSystem.getCoins(sendersID) < transfer:
                                bsInternal._chatMessage('Not enough ' + bs.getSpecialChar('ticket') + ' to perform transaction')
                            else:
                                coinSystem.addCoins(sendersID, int(transfer * -1))
                                coinSystem.addCoins(receiversID, int(transfer))
                                bsInternal._chatMessage('Successfully transfered ' + bs.getSpecialChar('ticket') + a[0] + ' into ' + name + "'s account.")
                        else:
                            bs.screenMessage('Player not Found', color=(1, 0, 0))
                except:
                    bs.screenMessage('Usage: /donate amount clientID', transient=True, clients=[clientID])

            elif m == '/buy' and enableCoinSystem:
                if a == []:
                    bsInternal._chatMessage('Usage: /buy item_name')
                elif a[0] in availableEffects:
                    effect = a[0]
                    client_str = None
                    for i in bsInternal._getForegroundHostActivity().players:
                        if i.getInputDevice().getClientID() == clientID:
                            client_str = i.get_account_id()

                    if client_str is not None:
                        costOfEffect = availableEffects[effect]
                        haveCoins = coinSystem.getCoins(client_str)
                        if haveCoins >= costOfEffect:
                            customers = gph.effectCustomers
                            if client_str not in customers:
                                from datetime import datetime, timedelta
                                expiry = datetime.now() + timedelta(days=1)
                                customers[client_str] = {'effect': effect, 'expiry': expiry.strftime('%d-%m-%Y %H:%M:%S')}
                                with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
                                    s = [ row for row in file ]
                                    s[4] = 'effectCustomers = ' + str(customers) + '\n'
                                    f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py', 'w')
                                    for i in s:
                                        f.write(i)

                                    f.close()
                                coinSystem.addCoins(client_str, costOfEffect * -1)
                                bsInternal._chatMessage('Success! That cost you ' + bs.getSpecialChar('ticket') + str(costOfEffect))
                            else:
                                activeEffect = customers[client_str]['effect']
                                bs.screenMessage('You already have ' + activeEffect + ' effect active', color = (1,0,0))
                        else:
                            bsInternal._chatMessage('You need ' + bs.getSpecialChar('ticket') + str(costOfEffect) + ' for that. You have ' + bs.getSpecialChar('ticket') + str(haveCoins) + ' only.')


            elif m == '/list':
                #string = u'==Name========ClientID====PlayerID==\n'
		string = u'{0:^16}{1:^15}{2:^10}\n------------------------------------------------------------------------------\n'.format('Name','ClientID','PlayerID')
                for s in bsInternal._getForegroundHostSession().players:
                    #string += s.getName()  '========' + str(s.getInputDevice().getClientID()) + '====' + str(bsInternal._getForegroundHostSession().players.index(s)) + '\n'
		    string += u'{0:^16}{1:^15}{2:^10}\n'.format(s.getName(True,True), str(s.getInputDevice().getClientID()), str(bsInternal._getForegroundHostSession().players.index(s)))
                bs.screenMessage(string, transient=True, color=(1, 1, 1), clients=[clientID])
		#print string
		

            elif m == '/shop' and enableCoinSystem:
                string = '[ You can buy following items ]\n'
                if a == []:
                    bs.screenMessage('Usage: /shop commands or /shop effects', transient=True, color=(1, 0.1, 0.1), clients=[clientID])
                elif a[0] == 'effects':
                    for x in availableEffects:
                        string += x + '----' + bs.getSpecialChar('ticket') + str(availableEffects[x]) + '----for 1 day\n'

                    bs.screenMessage(string, transient=True, color=(0, 1, 0), clients=[clientID])
                elif a[0] == 'commands':
		    separator = '          '
                    for x in availableCommands:
                        string += x + '----' + bs.getSpecialChar('ticket') + str(availableCommands[x]) + separator
			if separator == '          ':
				separator = '\n'
			else:
				separator = '          '
                    bs.screenMessage(string, transient=True, color=(0, 1, 0), clients=[clientID])

            elif m == '/......cashtoscore' and enableCoinSystem:
                try:
                    coins = int(a[0])
                    for player in activity.players:
                        if player.getInputDevice().getClientID() == clientID:
                            accountID = player.get_account_id()
			    haveCoins = coinSystem.getCoins(accountID)
			    if haveCoins < coins:
                                bsInternal._chatMessage('Not enough ' + bs.getSpecialChar('ticket') + ' 100000000000000')
			    elif coins < 100:
                                bsInternal._chatMessage('You can only convert more than ' + bs.getSpecialChar('ticket') + '1000000000')
			    else:
                                coinSystem.addCoins(accountID, coins * -1)
                                f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/stats.json', 'r')
				stats = json.loads(f.read())
				f.close()
                                equivalentScore = int(coins * 5 * 0.9)
                                stats[accountID]['scores'] += equivalentScore
				f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/stats.json', 'w')
                                f.write(json.dumps(stats))
                                bs.screenMessage('Transaction Successful', color=(0,1,0))
                                f.close()
                                bsInternal._chatMessage(str(equivalentScore) + 'score added to your account stats. [10% transaction fee deducted]')
                                import mystats
                                mystats.refreshStats()
                            break
				
                except:
                    bs.screenMessage('Usage: /cashtoscore amount_of_cash', transient=True, color=(1,
                                                                                        0.1,
                                                                                        0.1), clients=[clientID])



            elif m == '/scoretocash' and enableCoinSystem:
                try:
                    score = int(a[0])
                    for player in activity.players:
                        if player.getInputDevice().getClientID() == clientID:
                            f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/stats.json', 'r')
                            stats = json.loads(f.read())
                            accountID = player.get_account_id()
                            haveScore = stats[accountID]['scores']
                            f.close()
                            if haveScore < score:
                                bsInternal._chatMessage('Not enough scores to perform the transaction')
                            elif score < 500:
                                bsInternal._chatMessage('You can only convert more than 500scores')
                            else:
                                f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/stats.json', 'w')
                                stats[accountID]['scores'] -= score
                                f.write(json.dumps(stats))
                                equivalentCoins = int(score / 5 * 0.9)
                                coinSystem.addCoins(accountID, equivalentCoins)
                                bs.screenMessage('Transaction Successful', color=(0, 1,
                                                                              0))
                                f.close()
                                bsInternal._chatMessage(bs.getSpecialChar('ticket') + str(equivalentCoins) + ' added to your account. [10% transaction fee deducted]')
                                import mystats
                                mystats.refreshStats()
                            break

                except:
                    bs.screenMessage('Usage: /scoretocash amount_of_score', transient=True, color=(1,
                                                                                        0.1,
                                                                                        0.1), clients=[clientID])

            elif level > 0:
                if m == '/nv':
                    if self.tint is None:
                        self.tint = bs.getSharedObject('globals').tint
                    bs.getSharedObject('globals').tint = (0.5, 0.7, 1) if a == [] or not a[0] == 'off' else self.tint
                    commandSuccess = True
                elif m == '/ooh':
                    if a is not None and len(a) > 0:
                        s = int(a[0])

                        def oohRecurce(c):
                            bs.playSound(bs.getSound('ooh'), volume =2)
                            c -= 1
                            if c > 0:
                                bs.gameTimer(int(a[1]) if len(a) > 1 and a[1] is not None else 1000, bs.Call(oohRecurce, c=c))
                            return

                        oohRecurce(c=s)
                    else:
                        bs.playSound(bs.getSound('ooh'), volume =2)
                    commandSuccess = True
                elif m == '/playSound':
                    if a is not None and len(a) > 1:
                        s = int(a[1])

                        def oohRecurce(c):
                            bs.playSound(bs.getSound(str(a[0])), volume =2)
                            c -= 1
                            if c > 0:
                                bs.gameTimer(int(a[2]) if len(a) > 2 and a[2] is not None else 1000, bs.Call(oohRecurce, c=c))
                            return

                        oohRecurce(c=s)
                    else:
                        bs.playSound(bs.getSound(str(a[0])), volume =2)
                    commandSuccess = True
                elif m in ('/box', '/boxall'):
                    try:
                        if m == '/boxall':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.torsoModel = bs.getModel('tnt')
                                    i.actor.node.colorMaskTexture = bs.getTexture('tnt')
                                    i.actor.node.colorTexture = bs.getTexture('tnt')
                                    i.actor.node.highlight = (1, 1, 1)
                                    i.actor.node.color = (1, 1, 1)
                                    i.actor.node.headModel = None
                                    i.actor.node.style = 'cyborg'
                                except:
                                    print 'error'

                            commandSuccess = True
                        elif a == []:
                            bsInternal._chatMessage('Usage: /boxall or /box player_code')
                        else:
                            try:
                                n = int(a[0])
                                bs.getSession().players[n].actor.node.torsoModel = bs.getModel('tnt')
                                bs.getSession().players[n].actor.node.colorMaskTexture = bs.getTexture('tnt')
                                bs.getSession().players[n].actor.node.colorTexture = bs.getTexture('tnt')
                                bs.getSession().players[n].actor.node.highlight = (1,
                                                                                   1,
                                                                                   1)
                                bs.getSession().players[n].actor.node.color = (1, 1,
                                                                               1)
                                bs.getSession().players[n].actor.node.headModel = None
                                bs.getSession().players[n].actor.node.style = 'cyborg'
                                commandSuccess = True
                            except:
                                bsInternal._chatMessage('Usage: /boxall or /box player_code')

                    except:
                        bs.screenMessage('Error!', color=(1, 0, 0))

                elif m in ('/spaz', '/spazall'):
                    try:
                        if a == []:
                            bsInternal._chatMessage('Usage: /spazall or /spaz number of list')
                        elif m == '/spazall':
                            for i in bs.getSession().players:
                                a.append(a[0])
                                t = i.actor.node
                                try:
			  	  if a[1] in ['ali','neoSpaz','wizard','cyborg','penguin','agent','pixie','bear','bunny']:
                                    t.colorTexture = bs.getTexture(a[1] + 'Color')
                                    t.colorMaskTexture = bs.getTexture(a[1] + 'ColorMask')
                                    t.headModel = bs.getModel(a[1] + 'Head')
                                    t.torsoModel = bs.getModel(a[1] + 'Torso')
                                    t.pelvisModel = bs.getModel(a[1] + 'Pelvis')
                                    t.upperArmModel = bs.getModel(a[1] + 'UpperArm')
                                    t.foreArmModel = bs.getModel(a[1] + 'ForeArm')
                                    t.handModel = bs.getModel(a[1] + 'Hand')
                                    t.upperLegModel = bs.getModel(a[1] + 'UpperLeg')
                                    t.lowerLegModel = bs.getModel(a[1] + 'LowerLeg')
                                    t.toesModel = bs.getModel(a[1] + 'Toes')
                                    t.style = a[1]
                                except:
                                    print 'error'
                                else:
                                    commandSuccess = True

                        else:
                            try:
			      if a[1] in ['ali','neoSpaz','wizard','cyborg','penguin','agent','pixie','bear','bunny']:
                                n = int(a[0])
                                t = bs.getSession().players[n].actor.node
                                t.colorTexture = bs.getTexture(a[1] + 'Color')
                                t.colorMaskTexture = bs.getTexture(a[1] + 'ColorMask')
                                t.headModel = bs.getModel(a[1] + 'Head')
                                t.torsoModel = bs.getModel(a[1] + 'Torso')
                                t.pelvisModel = bs.getModel(a[1] + 'Pelvis')
                                t.upperArmModel = bs.getModel(a[1] + 'UpperArm')
                                t.foreArmModel = bs.getModel(a[1] + 'ForeArm')
                                t.handModel = bs.getModel(a[1] + 'Hand')
                                t.upperLegModel = bs.getModel(a[1] + 'UpperLeg')
                                t.lowerLegModel = bs.getModel(a[1] + 'LowerLeg')
                                t.toesModel = bs.getModel(a[1] + 'Toes')
                                t.style = a[1]
                                commandSuccess = True
                            except:
                                bsInternal._chatMessage('Usage: /spazall or /spaz number of list')

                    except:
                        bs.screenMessage('error', color=(1, 0, 0))

                elif m in ('/inv', '/invall'):
                    try:
                        if m == '/invall':
                            for i in bs.getSession().players:
                                t = i.actor.node
                                t.headModel = None
                                t.torsoModel = None
                                t.pelvisModel = None
                                t.upperArmModel = None
                                t.foreArmModel = None
                                t.handModel = None
                                t.upperLegModel = None
                                t.lowerLegModel = None
                                t.toesModel = None
                                t.style = 'cyborg'

                            commandSuccess = True
                        elif a == []:
                            bsInternal._chatMessage('Usage: /invall or /inv number of list')
                        else:
                            try:
                                n = int(a[0])
                                t = bs.getSession().players[n].actor.node
                                t.headModel = None
                                t.torsoModel = None
                                t.pelvisModel = None
                                t.upperArmModel = None
                                t.foreArmModel = None
                                t.handModel = None
                                t.upperLegModel = None
                                t.lowerLegModel = None
                                t.toesModel = None
                                t.style = 'cyborg'
                                commandSuccess = True
                            except:
                                bsInternal._chatMessage('Usage: /invall or /inv number of list')

                    except:
                        bs.screenMessage('error', color=(1, 0, 0))

                elif m == '/bunnyNOtavailabehere':
                    if a == []:
                        bsInternal._chatMessage('Usage: /bunny count owner(number of list)')
                    import BuddyBunny
                    for i in range(int(a[0])):
                        p = bs.getSession().players[int(a[1])]
                        if 'bunnies' not in p.gameData:
                            p.gameData['bunnies'] = BuddyBunny.BunnyBotSet(p)
                        p.gameData['bunnies'].doBunny()

                elif m in ('/tex', '/texall'):
                    if m == '/texall':
                        for i in bs.getSession().players:
                            try:
                                i.actor.node.colorMaskTexture = bs.getTexture('egg1')
                                i.actor.node.colorTexture = bs.getTexture('egg1')
                            except:
                                print 'error'
                            else:
                                commandSuccess = True

                    elif a == []:
                        bsInternal._chatMessage('Usage: /texall or /tex number of list')
                    else:
                        try:
                            n = int(a[0])
                            bs.getSession().players[n].actor.node.colorMaskTexture = bs.getTexture('egg1')
                            bs.getSession().players[n].actor.node.colorTexture = bs.getTexture('egg1')
                            commandSuccess = True
                        except:
                            bs.screenMessage('Error!', color=(1, 0, 0))


		elif level>1:
                    if m in ('/freeze', '/freezeall'):
                        if m == '/freezeall':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage(bs.FreezeMessage())
                                    commandSuccess = True
                                except:
                                    pass

                        elif a == []:
                            bsInternal._chatMessage('Usage: /freezeall or /freeze number of list')
                        else:
                            try:
                                bs.getSession().players[int(a[0])].actor.node.handleMessage(bs.FreezeMessage())
                                commandSuccess = True
                            except:
                                bsInternal._chatMessage('Usage: /freezeall or /freeze number of list')

                    elif m in ('/thaw', '/thawall'):
                        if m == '/thawall':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage(bs.ThawMessage())
                                except:
                                    pass

                            commandSuccess = True
                        elif a == []:
                            bsInternal._chatMessage('Usage: /thawall or number of list')
                        else:
                            try:
                                bs.getSession().players[int(a[0])].actor.node.handleMessage(bs.ThawMessage())
                                commandSuccess = True
                            except:
                                bsInternal._chatMessage('Usage: /thawall or /thaw number of list')

                    elif m in ('/sleep', '/sleepall'):
                        if m == '/sleepall':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage('knockout', 5000)
                                except:
                                    pass

                            commandSuccess = True
                        elif a == []:
                            bsInternal._chatMessage('Usage: /sleepall or /sleep number of list')
                        else:
                            try:
                                bs.getSession().players[int(a[0])].actor.node.handleMessage('knockout', 5000)
                                commandSuccess = True
                            except:
                                bsInternal._chatMessage('Usage: /sleepall or /sleep number of list')

                    elif m in ('/kill', '/killall'):
                        if m == '/killall':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage(bs.DieMessage())
                                except:
                                    pass

                            commandSuccess = True
                        elif a == []:
                            bsInternal._chatMessage('Usage: /killall or /kill number of list')
                        else:
                            try:
                                bs.getSession().players[int(a[0])].actor.node.handleMessage(bs.DieMessage())
                                commandSuccess = True
                            except:
                                bsInternal._chatMessage('Usage: /killall or /kill number of list')

                    elif m == '/curse':
                        if a == []:
                            bsInternal._chatMessage('Using: /curse all or number of list')
                        elif a[0] == 'all':
                            for i in bs.getSession().players:
                                try:
                                    i.actor.curse()
                                except:
                                    pass

                            commandSuccess = True
                        else:
                            try:
                                bs.getSession().players[int(a[0])].actor.curse()
                                commandSuccess = True
                            except:
                                pass

	            elif m == '/floater' and level > 3:
                        playerlist = bsInternal._getForegroundHostActivity(
                        ).players
                        if not hasattr(bsInternal._getForegroundHostActivity(),
                                       'flo'):
                            import floater
                            bsInternal._getForegroundHostActivity().flo = floater.Floater(bsInternal._getForegroundHostActivity()._mapType())
                        floater = bsInternal._getForegroundHostActivity().flo
                        if floater.controlled:
                            bs.screenMessage(
                                'Floater is already being controlled',
                                color=(1, 0, 0))
                            return
                        for i in playerlist:
                            if i.getInputDevice().getClientID() == clientID:
                                clientID = i.getInputDevice().getClientID()
                                bs.screenMessage(
                                    'You Gained Control Over The Floater!',
                                    clients=[clientID],
                                    transient=True,
                                    color=(0, 1, 1))

                                def dis(i, floater):
                                    i.actor.node.invincible = False
                                    i.resetInput()
                                    i.actor.connectControlsToPlayer()
                                    floater.dis()

                                # bs.gameTimer(15000,bs.Call(dis,i,floater))
                                ps = i.actor.node.position
                                i.actor.node.invincible = True
                                floater.node.position = (ps[0], ps[1] + 1.5,
                                                         ps[2])
                                i.actor.node.holdNode = bs.Node(None)
                                i.actor.node.holdNode = floater.node2
                                i.actor.disconnectControlsFromPlayer()
                                i.resetInput()
                                floater.sourcePlayer = i
                                floater.con()
                                i.assignInputCall('pickUpPress', floater.up)
                                i.assignInputCall('pickUpRelease', floater.upR)
                                i.assignInputCall('jumpPress', floater.down)
                                i.assignInputCall('jumpRelease', floater.downR)
                                i.assignInputCall('bombPress', floater.drop)
                                i.assignInputCall('punchPress',
                                                  bs.Call(dis, i, floater))
                                i.assignInputCall('upDown', floater.updown)
                                i.assignInputCall('leftRight',
                                                  floater.leftright)
                                i.actor.afk_checker = None

                    elif m == '/sm':
                        bs.getSharedObject('globals').slowMotion = bs.getSharedObject('globals').slowMotion == False
                        commandSuccess = True

                    elif m == '/end':
                        try:
                            bsInternal._getForegroundHostActivity().endGame()
                            commandSuccess = True
                        except:
                            pass




                    elif level > 2:
		            if m == '/quit':
		                commandSuccess = True
		                bsInternal.quit()
		            elif m == '/kick':
		                if a == []:
		                    bsInternal._chatMessage('Using: /kick name or number of list')
		                elif len(a[0]) > 3:
		                    self.kickByNick(a[0])
		                    commandSuccess = True
		                else:
		                    try:
		                        s = int(a[0])
		                        bsInternal._disconnectClient(int(a[0]))
		                        commandSuccess = True
		                    except:
		                        self.kickByNick(a[0])
		                        commandSuccess = True

		            elif m == '/admin' and level > 3:
		                clID = int(a[0])
		                updated_admins = gph.adminHashes
		                for client in bsInternal._getGameRoster():
		                    if client['clientID'] == clID:
		                        cl_str = client['displayString']

		                for i in bsInternal._getForegroundHostActivity().players:
		                    if i.getInputDevice().getClientID() == clID:
		                        newadmin = i.get_account_id()
		                        if a[1] == 'add':
		                            if newadmin not in updated_admins:
		                                gph.adminHashes.append(newadmin)
		                                commandSuccess = True
		                                updated_admins = gph.adminHashes
		                                with open(bs.getEnvironment()['systemScriptsDirectory'] + '/membersidlogged.txt', mode='a+') as (fi):
		                                    fi.write(cl_str + ' || ' + newadmin + '\n')
		                                    fi.close()
		                        elif a[1] == 'remove':
		                            if newadmin in updated_admins:
		                                gph.adminHashes.remove(newadmin)
		                                commandSuccess = True
		                                updated_admins = gph.adminHashes

		                if len(a) > 2:
		                    if a[2] == 'permanent' and level > 3:
		                        with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
		                            s = [ row for row in file ]
		                            s[0] = 'adminHashes = ' + str(updated_admins) + '\n'
		                            f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py', 'w')
		                            for i in s:
		                                f.write(i)

		                            f.close()
		            elif m == '/vip' and level > 3:
		                clID = int(a[0])
		                updated_admins = gph.vipHashes
		                for client in bsInternal._getGameRoster():
		                    if client['clientID'] == clID:
		                        cl_str = client['displayString']

		                for i in bsInternal._getForegroundHostActivity().players:
		                    if i.getInputDevice().getClientID() == clID:
		                        newadmin = i.get_account_id()
		                        if a[1] == 'add':
		                            if newadmin not in updated_admins:
		                                gph.vipHashes.append(newadmin)
		                                commandSuccess = True
		                                updated_admins = gph.vipHashes
		                                with open(bs.getEnvironment()['systemScriptsDirectory'] + '/membersidlogged.txt', mode='a+') as (fi):
		                                    fi.write(cl_str + ' || ' + newadmin + '\n')
		                                    fi.close()
		                        elif a[1] == 'remove':
		                            if newadmin in updated_admins:
		                                gph.vipHashes.remove(newadmin)
		                                commandSuccess = True
		                                updated_admins = gph.vipHashes

		                if len(a) > 2:
		                    if a[2] == 'permanent' and level > 3:
		                        with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
		                            s = [ row for row in file ]
		                            s[1] = 'vipHashes = ' + str(updated_admins) + '\n'
		                            f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py', 'w')
		                            for i in s:
		                                f.write(i)

		                            f.close()

		            elif m == '/remove':
		                if a == []:
		                    bsInternal._chatMessage('Using: /remove all or number of list')
		                elif a[0] == 'all':
		                    for i in bs.getSession().players:
		                        try:
		                            i.removeFromGame()
		                        except:
		                            pass

		                    commandSuccess = True
		                else:
		                    bs.getSession().players[int(a[0])].removeFromGame()
		                    commandSuccess = True


		            elif m in ('/hug', '/hugall'):
		                try:
		                    if m == '/hugall':
		                        try:
		                            bsInternal._getForegroundHostActivity().players[0].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[1].actor.node
		                        except:
		                            pass
		                        else:
		                            try:
		                                bsInternal._getForegroundHostActivity().players[1].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[0].actor.node
		                            except:
		                                pass
		                            else:
		                                try:
		                                    bsInternal._getForegroundHostActivity().players[3].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[2].actor.node
		                                except:
		                                    pass
		                                else:
		                                    try:
		                                        bsInternal._getForegroundHostActivity().players[4].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[3].actor.node
		                                    except:
		                                        pass

		                                try:
		                                    bsInternal._getForegroundHostActivity().players[5].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[6].actor.node
		                                except:
		                                    pass

		                            try:
		                                bsInternal._getForegroundHostActivity().players[6].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[7].actor.node
		                            except:
		                                pass

		                        commandSuccess = True
		                    elif a == []:
		                        bsInternal._chatMessage('Usage: /hugall or /hug number of list')
		                    else:
		                        try:
		                            bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[int(a[1])].actor.node
		                            commandSuccess = True
		                        except:
		                            bsInternal._chatMessage('Usage: /hugall or /hug number of list')

		                except:
		                    bs.screenMessage('Error!', color=(1, 0, 0))

		            elif m == '/tint':
		                if a == []:
		                    bsInternal._chatMessage('Using: /tint R G B')
		                    bsInternal._chatMessage('OR')
		                    bsInternal._chatMessage('Using: /tint r bright speed')
		                elif a[0] == 'r':
		                    m = 1.3 if a[1] is None else float(a[1])
		                    s = 1000 if a[2] is None else float(a[2])
		                    bsUtils.animateArray(bs.getSharedObject('globals'), 'tint', 3, {0: (1 * m, 0, 0), s: (0, 1 * m, 0), s * 2: (0, 0, 1 * m), s * 3: (1 * m, 0, 0)}, True)
		                    commandSuccess = True
		                else:
		                    try:
		                        if a[1] is not None:
		                            bs.getSharedObject('globals').tint = (
		                             float(a[0]), float(a[1]), float(a[2]))
		                            commandSuccess = True
		                        else:
		                            bs.screenMessage('Error!', color=(1, 0, 0))
		                    except:
		                        bs.screenMessage('Error!', color=(1, 0, 0))

		            elif m == '/pause':
		                bs.getSharedObject('globals').paused = bs.getSharedObject('globals').paused == False
		                commandSuccess = True
		            elif m == '/cameraMode':
		                try:
		                    if bs.getSharedObject('globals').cameraMode == 'follow':
		                        bs.getSharedObject('globals').cameraMode = 'rotate'
		                    else:
		                        bs.getSharedObject('globals').cameraMode = 'follow'
		                    commandSuccess = True
		                except:
		                    pass

		            elif m == '/lm':
		                arr = []
		                for i in range(100):
		                    try:
		                        arr.append(bsInternal._getChatMessages()[(-1 - i)])
		                    except:
		                        pass

		                arr.reverse()
		                for i in arr:
		                    bsInternal._chatMessage(i)

		                commandSuccess = True
		            elif m == '/gp':
		                if a == []:
		                    bsInternal._chatMessage('Using: /gp number of list')
		                else:
		                    s = bsInternal._getForegroundHostSession()
		                    for i in s.players[int(a[0])].getInputDevice()._getPlayerProfiles():
		                        try:
		                            bsInternal._chatMessage(i)
		                        except:
		                            pass

		                    commandSuccess = True
		            elif m == '/icy':
		                bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node = bsInternal._getForegroundHostActivity().players[int(a[1])].actor.node
		                commandSuccess = True
		            elif m in ('/fly', '/flyall'):
		                if m == '/flyall':
		                    for i in bsInternal._getForegroundHostActivity().players:
		                        i.actor.node.fly = True

		                    commandSuccess = True
		                elif a == []:
		                    bsInternal._chatMessage('Failed!!! Usage: /flyall or /fly number of list')
		                else:
		                    try:
		                        bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.fly = bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.fly == False
		                        commandSuccess = True
		                    except:
		                        bsInternal._chatMessage('Failed!!! Usage: /flyall or /fly number of list')

		            elif m == '/floorReflection':
		                bs.getSharedObject('globals').floorReflection = bs.getSharedObject('globals').floorReflection == False
		            elif m == '/ac':
		                if a == []:
		                    bsInternal._chatMessage('Using: /ac R G B')
		                    bsInternal._chatMessage('OR')
		                    bsInternal._chatMessage('Using: /ac r bright speed')
		                elif a[0] == 'r':
		                    m = 1.3 if a[1] is None else float(a[1])
		                    s = 1000 if a[2] is None else float(a[2])
		                    bsUtils.animateArray(bs.getSharedObject('globals'), 'ambientColor', 3, {0: (1 * m, 0, 0), s: (0, 1 * m, 0), s * 2: (0, 0, 1 * m), s * 3: (1 * m, 0, 0)}, True)
		                else:
		                    try:
		                        if a[1] is not None:
		                            bs.getSharedObject('globals').ambientColor = (
		                             float(a[0]), float(a[1]), float(a[2]))
		                        else:
		                            bs.screenMessage('Error!', color=(1, 0, 0))
		                    except:
		                        bs.screenMessage('Error!', color=(1, 0, 0))

		            elif m == '/iceOff':
		                try:
		                    activity.getMap().node.materials = [
		                     bs.getSharedObject('footingMaterial')]
		                    activity.getMap().isHockey = False
		                except:
		                    pass
		                else:
		                    try:
		                        activity.getMap().floor.materials = [
		                         bs.getSharedObject('footingMaterial')]
		                        activity.getMap().isHockey = False
		                    except:
		                        pass

		                    for i in activity.players:
		                        i.actor.node.hockey = False

		                commandSuccess = True
		            elif m == '/maxPlayers' and level >3:
		                if a == []:
		                    bsInternal._chatMessage('Using: /maxPlayers count of players')
		                else:
		                    try:
		                        bsInternal._getForegroundHostSession()._maxPlayers = int(a[0])
		                        bsInternal._setPublicPartyMaxSize(int(a[0]))
		                        bsInternal._chatMessage('Maximum players set to ' + str(int(a[0])))
		                    except:
		                        bs.screenMessage('Error!', color=(1, 0, 0))

		                    commandSuccess = True
		            elif m in ('/heal', '/healall'):
		                if m == '/healall':
		                    for i in bs.getActivity().players:
		                        try:
		                            if i.actor.exists():
		                                i.actor.node.handleMessage(bs.PowerupMessage(powerupType ='health'))
		                        except Exception:
		                            pass
		                        else:
		                            commandSuccess = True

		                elif a == []:
		                    bsInternal._chatMessage('Usage: /healall or /heal number of list')
		                else:
		                    try:
		                        bs.getActivity().players[int(a[0])].actor.node.handleMessage(bs.PowerupMessage(powerupType ='health'))
		                        commandSuccess = True
		                    except Exception:
		                        bsInternal._chatMessage('Usage: /healall or /heal number of list')

		            elif m == '/gm' and level > 3:
		                try:
		                    if a == []:
		                        for i in range(len(activity.players)):
		                            if activity.players[i].getInputDevice().getClientID() == clientID:
		                                activity.players[i].actor.node.hockey = activity.players[i].actor.node.hockey == False
		                                activity.players[i].actor.node.invincible = activity.players[i].actor.node.invincible == False
		                                activity.players[i].actor._punchPowerScale = 5 if activity.players[i].actor._punchPowerScale == 1.2 else 1.2

		                        commandSuccess = True
		                    else:
		                        activity.players[int(a[0])].actor.node.hockey = activity.players[int(a[0])].actor.node.hockey == False
		                        activity.players[int(a[0])].actor.node.invincible = activity.players[int(a[0])].actor.node.invincible == False
		                        activity.players[int(a[0])].actor._punchPowerScale = 5 if activity.players[int(a[0])].actor._punchPowerScale == 1.2 else 1.2
		                        commandSuccess = True
		                except:
		                    bsInternal._chatMessage('Player Not Found')

		            elif m == '/reflections':
		                if len(a) < 2:
		                    bsInternal._chatMessage('Usage: /reflections type(1/0) scale')
		                else:
		                    rs = [
		                     int(a[1])]
		                    typee = 'soft' if int(a[0]) == 0 else 'powerup'
		                    try:
		                        bsInternal._getForegroundHostActivity().getMap().node.reflection = typee
		                        bsInternal._getForegroundHostActivity().getMap().node.reflectionScale = rs
		                        print 'node'
		                    except:
		                        pass
		                    else:
		                        try:
		                            bsInternal._getForegroundHostActivity().getMap().bg.reflection = typee
		                            bsInternal._getForegroundHostActivity().getMap().bg.reflectionScale = rs
		                            print 'bg'
		                        except:
		                            pass
		                        else:
		                            try:
		                                bsInternal._getForegroundHostActivity().getMap().floor.reflection = typee
		                                bsInternal._getForegroundHostActivity().getMap().floor.reflectionScale = rs
		                                print 'floor'
		                            except:
		                                pass

		                        try:
		                            bsInternal._getForegroundHostActivity().getMap().center.reflection = typee
		                            bsInternal._getForegroundHostActivity().getMap().center.reflectionScale = rs
		                            print 'center'
		                        except:
		                            pass

		                    commandSuccess = True
		            elif m == '/shatter':
		                if a == []:
		                    bsInternal._chatMessage('Using: /shatter all or number of list')
		                elif a[0] == 'all':
		                    for i in bsInternal._getForegroundHostActivity().players:
		                        i.actor.node.shattered = int(a[1])

		                    commandSuccess = True
		                else:
		                    bsInternal._getForegroundHostActivity().players[int(a[0])].actor.node.shattered = int(a[1])
		                    commandSuccess = True
		            elif m == '/cm':
		                if a == []:
		                    time = 8000
		                else:
		                    time = int(a[0])
		                    op = 0.08
		                    std = bs.getSharedObject('globals').vignetteOuter
		                    bsUtils.animateArray(bs.getSharedObject('globals'), 'vignetteOuter', 3, {0: bs.getSharedObject('globals').vignetteOuter, 17000: (0, 1, 0)})
		                try:
		                    bsInternal._getForegroundHostActivity().getMap().node.opacity = op
		                except:
		                    pass
		                else:
		                    try:
		                        bsInternal._getForegroundHostActivity().getMap().bg.opacity = op
		                    except:
		                        pass
		                    else:
		                        try:
		                            bsInternal._getForegroundHostActivity().getMap().bg.node.opacity = op
		                        except:
		                            pass
		                        else:
		                            try:
		                                bsInternal._getForegroundHostActivity().getMap().node1.opacity = op
		                            except:
		                                pass
		                            else:
		                                try:
		                                    bsInternal._getForegroundHostActivity().getMap().node2.opacity = op
		                                except:
		                                    pass

		                                try:
		                                    bsInternal._getForegroundHostActivity().getMap().node3.opacity = op
		                                except:
		                                    pass

		                            try:
		                                bsInternal._getForegroundHostActivity().getMap().steps.opacity = op
		                            except:
		                                pass

		                        try:
		                            bsInternal._getForegroundHostActivity().getMap().floor.opacity = op
		                        except:
		                            pass

		                    try:
		                        bsInternal._getForegroundHostActivity().getMap().center.opacity = op
		                    except:
		                        pass

		                def off():
		                    op = 1
		                    try:
		                        bsInternal._getForegroundHostActivity().getMap().node.opacity = op
		                    except:
		                        pass
		                    else:
		                        try:
		                            bsInternal._getForegroundHostActivity().getMap().bg.opacity = op
		                        except:
		                            pass
		                        else:
		                            try:
		                                bsInternal._getForegroundHostActivity().getMap().bg.node.opacity = op
		                            except:
		                                pass
		                            else:
		                                try:
		                                    bsInternal._getForegroundHostActivity().getMap().node1.opacity = op
		                                except:
		                                    pass
		                                else:
		                                    try:
		                                        bsInternal._getForegroundHostActivity().getMap().node2.opacity = op
		                                    except:
		                                        pass

		                                    try:
		                                        bsInternal._getForegroundHostActivity().getMap().node3.opacity = op
		                                    except:
		                                        pass

		                                try:
		                                    bsInternal._getForegroundHostActivity().getMap().steps.opacity = op
		                                except:
		                                    pass

		                            try:
		                                bsInternal._getForegroundHostActivity().getMap().floor.opacity = op
		                            except:
		                                pass

		                        try:
		                            bsInternal._getForegroundHostActivity().getMap().center.opacity = op
		                        except:
		                            pass

		                    bsUtils.animateArray(bs.getSharedObject('globals'), 'vignetteOuter', 3, {0: bs.getSharedObject('globals').vignetteOuter, 100: std})

		                bs.gameTimer(time, bs.Call(off))
		            elif m == '/help not avilable tooo':
		                bsInternal._chatMessage(bs.Lstr(resource='help1').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help2').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help3').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help4').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help5').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help6').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help7').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help8').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help9').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help10').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help11').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help12').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help13').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help14').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help15').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help16').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help17').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help18').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help19').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help20').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help21').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help22').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help23').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help24').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help25').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help26').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help27').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help28').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help29').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help30').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help31').evaluate())
		                bsInternal._chatMessage(bs.Lstr(resource='help32').evaluate())
		            elif level > 3:
		                if m == '/partyname':
		                    if True:
		                        if a == []:
		                            bsInternal._chatMessage('Usage: /partyname name_party')
		                        else:
		                            #print 'value of a[0] = ' + a[0]
		                            name = a[0].replace('_', ' ')
		                            try:
		                                bsInternal._setPublicPartyName(name)
		                                bsInternal._chatMessage('Party name changed to "' + name + '"')
		                                commandSuccess = True
		                            except:
		                                bs.screenMessage('Failed to change party name!')

		                elif m == '/public':
		                    if True:
		                        if a == []:
		                            bsInternal._chatMessage('Usage: /public 0 or 1')
		                        elif a[0] == '0':
		                            try:
		                                bsInternal._setPublicPartyEnabled(False)
		                                bsInternal._chatMessage('Party is Private')
		                                commandSuccess = True
		                            except:
		                                bs.screenMessage('failed to change')

		                        elif a[0] == '1':
		                            try:
		                                bsInternal._setPublicPartyEnabled(True)
		                                bsInternal._chatMessage('Party is Public')
		                                commandSuccess = True
		                            except:
		                                bs.screenMessage('failed to change')

		                        else:
		                            bsInternal._chatMessage('Usage: /public 0 or 1')
		                elif m == '/id':
		                    if True:
		                        clID = int(a[0])
		                        for i in bsInternal._getForegroundHostActivity().players:
		                            if i.getInputDevice().getClientID() == clID:
		                                bsInternal._chatMessage(i.get_account_id())
		                                commandSuccess = True


		                elif m == '/customtag':
		                    if True:
		                        clID = int(a[0])
		                        for i in bsInternal._getForegroundHostActivity().players:
		                            if i.getInputDevice().getClientID() == clID:
		                                newadmin = i.get_account_id()
		                                if a[1] == 'add':
		                                    gph.customtagHashes.append(newadmin)
		                                    commandSuccess = True
		                                elif a[1] == 'remove':
		                                    if newadmin in gph.dragonHashes:
		                                        gph.customtagHashes.remove(newadmin)
		                                        commandSuccess = True

		                elif m == '/clear':
		                    if True:
		                        gph.customlist = []
		                        gph.customtagHashes = []
		                        gph.dragonHashes = []
		                        gph.adminHashes = []

		                elif m == '/ban':
		                    if a != []:
		                        bannedId = None
					aid = None
		                        try:
		                            clID = int(a[0])
					    for i in bsInternal._getGameRoster():
						if i['clientID'] == clID:
						    aid = i['displayString']
		                            	    for i in bsInternal._getForegroundHostActivity().players:
		                                	if i.getInputDevice().getClientID() == clID:
		                                    	    bannedID = i.get_account_id()
		                                    	    name = i.getName()

		                            if aid is not None:
						gph.banlist[bannedID] = aid
		                                with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
		                                    s = [ row for row in file ]
		                                    s[2] = 'banlist = ' + str(gph.banlist) + '\n'
		                                    f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py', 'w')
		                                    for i in s:
		                                        f.write(i)
		                                    f.close()
		                                bsInternal._chatMessage('banned ' + name)
		                                bsInternal._disconnectClient(clID)
		                                commandSuccess = True
		                        except Exception:
		                            bsInternal._chatMessage('player not found')

		                elif m == '/custom':
		                    try:
		                        attributes = len(a)
		                        clID = int(a[0])
		                        for i in bsInternal._getForegroundHostActivity().players:
		                            if i.getInputDevice().getClientID() == clID:
		                                customer = i.get_account_id()
		                                if a[1] == 'add':
		                                    if customer in gph.customlist:
		                                        gph.customlist.pop(customer)
		                                    try:
		                                        if attributes > 2:
		                                            tag = a[2]
		                                            if '\\' in tag:
		                                                tag = tag.replace('\\d', ('\\ue048').decode('unicode-escape'))
		                                                tag = tag.replace('\\c', ('\\ue043').decode('unicode-escape'))
		                                                tag = tag.replace('\\h', ('\\ue049').decode('unicode-escape'))
		                                                tag = tag.replace('\\s', ('\\ue046').decode('unicode-escape'))
		                                                tag = tag.replace('\\n', ('\\ue04b').decode('unicode-escape'))
		                                                tag = tag.replace('\\f', ('\\ue04f').decode('unicode-escape'))
		                                            gph.customlist[customer] = tag
		                                            if attributes > 3:
		                                                if a[3] == 'permanent' and level > 5:
		                                                    with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
		                                                        s = [ row for row in file ]
		                                                        s[5] = 'customlist = ' + str(gph.customlist) + '\n'
		                                                        f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py', 'w')
		                                                        for i in s:
		                                                            f.write(i)

		                                                        f.close()
		                                    except:
		                                        print 'inside exception but adding into customHashes'
		                                        gph.customtagHashes.append(customer)

		                                    commandSuccess = True
		                                elif a[1] == 'remove':
		                                    if customer in gph.customtagHashes:
		                                        gph.customtagHashes.remove(customer)
		                                        commandSuccess = True
		                                    if customer in gph.customlist:
		                                        gph.customlist.pop(customer)
		                                        commandSuccess = True
		                                    if attributes > 2:
		                                        if a[2] == 'permanent':
		                                            with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
		                                                s = [ row for row in file ]
		                                                s[5] = 'customlist = ' + str(gph.customlist) + '\n'
		                                                f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py', 'w')
		                                                for i in s:
		                                                    f.write(i)

		                                                f.close()

		                    except:
		                        pass

		                elif m == '/whois':
					try:
						clID = int(a[0])
						ID = ''
				                for i in bsInternal._getForegroundHostActivity().players:
				                    if i.getInputDevice().getClientID() == clID:
				                        ID = i.get_account_id()
							name = i.getName(True,True)
						if ID is not '':
						    with open('logPlayers.json','r') as f:
							allPlayers = json.loads(f.read())
							allID = allPlayers[ID]
							string = 'Login ID of %s is:' %name
							for i in allID:
								#bsInternal._chatMessage(i)
								string += '\n' + i
				                        	#commandSuccess = True
							bs.screenMessage(string, transient=True, color=(1, 1, 1))
					except:
						print 'who is exception'
							
		                elif m == '/text':
					from BsTextOnMap import texts
					if a == []:
						bsInternal._chatMessage("Usage: /text showall or /text add [text] or /text del [textnumber]")
					elif a[0] == 'add' and len(a)>1:
						#get whole sentence from argument list
						newText = u''
						for i in range(1,len(a)):
							newText += a[i] + ' '
						#print newText
						texts.append(newText)

						#write to file
		                                with open(bs.getEnvironment()['systemScriptsDirectory'] + '/BsTextOnMap.py') as (file):
		                                    s = [ row for row in file ]
		                                    s[0] = 'texts = ' + str(texts) + '\n'
		                                    f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/BsTextOnMap.py', 'w')
		                                    for i in s:
		                                        f.write(i)
		                                    f.close()
						    commandSuccess=True
					elif a[0] == 'showall':
						for i in range(len(texts)):
							#print texts(i)
							bsInternal._chatMessage(str(i) + '. ' + texts[i])
						commandSuccess=True
					elif a[0] == 'del' and len(a)>1:
					    try:
						if len(texts) > 1:
							texts.pop(int(a[1]))
							#write to file
				                        with open(bs.getEnvironment()['systemScriptsDirectory'] + '/BsTextOnMap.py') as (file):
				                            s = [ row for row in file ]
				                            s[0] = 'texts = ' + str(texts) + '\n'
				                            f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/BsTextOnMap.py', 'w')
				                            for i in s:
				                                f.write(i)
				                            f.close()
							    commandSuccess=True
						else:
							bs.screenMessage("At least one text should be present",(1,0,0))
					    except:
						pass
					else:
						bsInternal._chatMessage("Usage: /text showall or /text add [text] or /text del [textnumber]")
		                elif m == '/whoinqueue':
				        def _onQueueQueryResult(result):
					    #print result, ' is result'
					    inQueue = result['e']
					    #print inQueue, ' is inQueue'
					    string = 'No one '
					    if inQueue != []:
						string = ''
						for queue in inQueue:
							#print queue[3]
							string += queue[3] + ' '
					    bsInternal._chatMessage(string + 'is in the queue')
							
					bsInternal._addTransaction(
						{'type': 'PARTY_QUEUE_QUERY', 'q': "p_S-l150a7a1d-0f12-43de-a3bf-467a7a5bcd72_1029295_13.233.116.32_43210"},
						callback=bs.Call(_onQueueQueryResult))
					bsInternal._runTransactions()					

                else:
                    bs.screenMessage('Failed', color=(1, 0, 0))
        return


c = chatOptions()


def cmd(msg, clientID):
    c.opt(clientID, msg)
    if commandSuccess:
        if commandByCoin:
            coinSystem.addCoins(user, costOfCommand * -1)
            bs.screenMessage('Success! That cost you ' + bs.getSpecialChar('ticket') + str(costOfCommand), color=(1,1,1))
        else:
	  try:
		with bs.Context(bsInternal._getForegroundHostActivity()):
			bs.screenMessage(reply, color=(0.1,1,0.1))
            		#bsInternal._chatMessage(reply)
	  except:
		pass
    return
