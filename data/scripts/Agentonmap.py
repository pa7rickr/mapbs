# -- coding: utf-8 --
texts = [u'']
import bs
from bsMap import *
import bsMap
from random import randrange
#from settings import *
#count = len(texts)
#made by agent
#inform to use this script 
i=0
            
def __init__(self, vrOverlayCenterOffset=None):
        """
        Instantiate a map.
        """
        import bsInternal
        bs.Actor.__init__(self)
        self.preloadData = self.preload(onDemand=True)
        def text(): 
                import getPermissionsHashes as gph
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue048 Owner: pa7rick\n\ue048 Script by: Vortex & Blitz',
                             
'scale':0.5,
                              'maxWidth':0,
                              'position':(-640,50),
                              'shadow':1,
                              'flatness':0.9,
                              'color':(1,1,1),
                              'hAlign':'left',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0:0.5})
                t = bs.newNode('text',
                       attrs={ 'text':u'Ultimate Server',
                              'scale':0.7,
                              'maxWidth':0,
                              'position':(11,620),
                              'shadow':1.5,
                              'flatness':1.0,
                              'color':(1.92,1.92,1.92),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0:1.0})
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue048JOIN WHATSAPP GROUP FOR FURTHER INFORMATION\nHAPPY PLAY BOMBSQUAD\ue048',
                              'scale':0.4,
                              'maxWidth':0,
                              'position':(11,610),
                              'shadow':0.9,
                              'flatness':1.0,
                              'color':(1.92,1.92,1.92),
                              'hAlign':'center',
                              'vAttach':'bottom'})                                
                bs.animate(t,'opacity',{0:0.7})
                t = bs.newNode('image', 
                       attrs={ 'scale':(300,30),
                               'texture':bs.getTexture('bar'),
                               'position':(0,-80),
                               'attach':'topRight',
                               'color':(0.7,0.1,0)
                      })
                bs.animate(t,'opacity',{0:0.5})
                t = bs.newNode('image', 
                       attrs={ 'scale':(300,30),
                               'texture':bs.getTexture('bar'),
                               'position':(0,-115),
                               'attach':'topRight',
                               'color':(0.6,0.6,0.6)
                      })
                bs.animate(t,'opacity',{0:0.5}) 
                t = bs.newNode('image', 
                       attrs={ 'scale':(300,30),
                               'texture':bs.getTexture('bar'),
                               'position':(0,-150),
                               'attach':'topRight',
                               'color':(0.1,0.3,0.1)
                      })
                bs.animate(t,'opacity',{0:0.5})
                t = bs.newNode('text',
                       attrs={'text':"#1 "+gph.top3Name[0][:10]+"...",
                              'flatness':1.0,
                              'hAlign':'left',
                              'hAttach':'right',
                              'vAttach':'top',
                              'vAlign':'center',
                              'position':(-140,-80),
                              'scale':0.7,
                              'color':(0.7,0.4,0.3)
                       })
                bs.animate(t,'opacity',{0:1.0}) 
                t = bs.newNode('text',
                       attrs={'text':"#2 "+gph.top3Name[1][:10]+"...",
                              'flatness':1.0,
                              'hAlign':'left',
                              'hAttach':'right',
                              'vAttach':'top',
                              'vAlign':'center',
                              'position':(-140,-115),
                              'scale':0.7,
                              'color':(0.8,0.8,0.8)
                       })
                bs.animate(t,'opacity',{0:1.0}) 
                t = bs.newNode('text',
                       attrs={'text':"#3 "+gph.top3Name[2][:10]+"...",
                              'flatness':1.0,
                              'hAlign':'left',
                              'hAttach':'right',
                              'vAttach':'top',
                              'vAlign':'center',
                              'position':(-140,-150),
                              'scale':0.7,
                              'color':(0.2,0.6,0.2)
                       })
                bs.animate(t,'opacity',{0:1.0})
                t = bs.newNode('text',
                       attrs={ 'text':u'[\U0001F451] Ultimate Teams Server \n---------------------------------------------------',
                              'scale':0.5,
                              'maxWidth':0,
                              'position':(-570,90),
                              'shadow':0.9,
                              'flatness':1,
                              'color':(1.92,1.92,1.92),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0:0.5})
	def recurringText():
		global i
		import settings
		if i>len(texts)-2:
			i=0
		else:
			i+=1
                t = bs.newNode('text',
                       attrs={ 'text':random.choice(settings.coinTexts),
                              'scale':0.8,
                              'maxWidth':0,
                              'position':(11,130),
                              'shadow':1.9,
                              'flatness':1.0,
                              'color':(1.92,1.92,1.92,),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t, 'scale', {0: 0.0, 500: 0.7, 4500: 0.7, 5000: 0.0}, loop=False)                     
                multiColor = {0:(1,1,1)}
                bsUtils.animateArray(t,'color',3,multiColor,True)
                bs.gameTimer(7000,t.delete)
	import settings
	if settings.enableCoinSystem:
		texts.append(settings.coinTexts)
	bs.gameTimer(10,bs.Call(text))
	bs.gameTimer(0,bs.Call(recurringText))
	bs.gameTimer(7000,bs.Call(recurringText),repeat = True)
        
        # set some defaults
        bsGlobals = bs.getSharedObject('globals')
        # area-of-interest bounds
        aoiBounds = self.getDefBoundBox("areaOfInterestBounds")
        if aoiBounds is None:
            print 'WARNING: no "aoiBounds" found for map:',self.getName()
            aoiBounds = (-1,-1,-1,1,1,1)
        bsGlobals.areaOfInterestBounds = aoiBounds
        # map bounds
        mapBounds = self.getDefBoundBox("levelBounds")
        if mapBounds is None:
            print 'WARNING: no "levelBounds" found for map:',self.getName()
            mapBounds = (-30,-10,-30,30,100,30)
        bsInternal._setMapBounds(mapBounds)
        # shadow ranges
        try: bsGlobals.shadowRange = [
                self.defs.points[v][1] for v in 
                ['shadowLowerBottom','shadowLowerTop',
                 'shadowUpperBottom','shadowUpperTop']]
        except Exception: pass
        # in vr, set a fixed point in space for the overlay to show up at..
        # by default we use the bounds center but allow the map to override it
        center = ((aoiBounds[0]+aoiBounds[3])*0.5,
                  (aoiBounds[1]+aoiBounds[4])*0.5,
                  (aoiBounds[2]+aoiBounds[5])*0.5)
        if vrOverlayCenterOffset is not None:
            center = (center[0]+vrOverlayCenterOffset[0],
                      center[1]+vrOverlayCenterOffset[1],
                      center[2]+vrOverlayCenterOffset[2])
        bsGlobals.vrOverlayCenter = center
        bsGlobals.vrOverlayCenterEnabled = True
        self.spawnPoints = self.getDefPoints("spawn") or [(0,0,0,0,0,0)]
        self.ffaSpawnPoints = self.getDefPoints("ffaSpawn") or [(0,0,0,0,0,0)]
        self.spawnByFlagPoints = (self.getDefPoints("spawnByFlag")
                                  or [(0,0,0,0,0,0)])
        self.flagPoints = self.getDefPoints("flag") or [(0,0,0)]
        self.flagPoints = [p[:3] for p in self.flagPoints] # just want points
        self.flagPointDefault = self.getDefPoint("flagDefault") or (0,1,0)
        self.powerupSpawnPoints = self.getDefPoints("powerupSpawn") or [(0,0,0)]
        self.powerupSpawnPoints = \
            [p[:3] for p in self.powerupSpawnPoints] # just want points
        self.tntPoints = self.getDefPoints("tnt") or []
        self.tntPoints = [p[:3] for p in self.tntPoints] # just want points
        self.isHockey = False
        self.isFlying = False
        self._nextFFAStartIndex = 0
        
bsMap.Map.__init__ = __init__
