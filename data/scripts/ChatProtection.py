import bs,bsInternal
#import settings
print 'Chat Protection loaded'

def _chatProtect(clientID):
	flag = 1
	for i in bsInternal._getForegroundHostSession().players:
		if i.getInputDevice().getClientID() == clientID:
			flag = 0
			break
	if flag == 1:
			with bs.Context(bsInternal._getForegroundHostActivity()):bs.screenMessage('Join the game first',color=(1,0,0),transient=True, clients=[clientID])
			bsInternal._disconnectClient(clientID)#return False                                                     
                        return False
    	return True
