# coding=utf-8
import bs
import math
import random
import pacmanPortalMap
import rymPortalMap
import gfPortalMap
from bsMap import *

class BombermanHomeMap(Map):
    import bmHomeMapDefs as defs
    name = 'Bomberman'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'bombermanMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('bombermanMap')
        data['collideModel'] = bs.getCollideModel('bombermanMapCob')
        data['tex'] = bs.getTexture('bombermanMapColor')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

registerMap(BombermanHomeMap)

class PacmanMap(Map):
    import pacmanMapDefs as defs
    name = 'PAC-MAN'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'pacmanMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('pacmanMap')
        data['collideModel'] = bs.getCollideModel('pacmanMapCob')
        data['tex'] = bs.getTexture('pacmanMapColor')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        g = bs.getSharedObject('globals')
        g.tint = (1.3,1.2,1.0)
        g.ambientColor = (1.3,1.2,1.0)
        g.vignetteOuter = (0.57,0.57,0.57)
        g.vignetteInner = (0.9,0.9,0.9)
        g.vrCameraOffset = (0,-4.2,-1.1)
        g.vrNearClip = 0.5

        pacmanPortalMap.Portal(position1 = (-10.2929, 0.1028, -0.68649),position2 = (10.2929, 0.1028, -0.68649),color = (3,0,9))

registerMap(PacmanMap)

class Mountain(Map):
    import mountainDefs as defs
    name = 'Rampa de Nieve'
    playTypes = ['melee','keepAway','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'mountainPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('mountain')
        data['collideModel'] = bs.getCollideModel('mountainCob')
        data['bgTex'] = bs.getTexture('menuBG')
        data['tex'] = bs.getTexture('mountainColor')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        self.foo = bs.newNode('terrain',
                              attrs={'model':self.preloadData['bgModel'],
                                     'lighting':False,
                                     'background':True,
                                     'colorTexture':self.preloadData['bgTex']})

        g = bs.getSharedObject('globals')
        g.tint = (1,1,1)
        g.ambientColor = (1,1,1)
        g.shadowOrtho = True
        g.vignetteOuter = (0.86,0.86,0.86)
        g.vignetteInner = (0.95,0.95,0.99)

registerMap(Mountain)

class RickMortyMap(Map):
    import rickmortyMapDefs as defs
    name = 'Rick & Morty'
    playTypes = ['melee','keepAway','teamFlag']

    @classmethod
    def getPreviewTextureName(cls):
        return 'rickmortyPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('rickmortymap')
        data['collideModel'] = bs.getCollideModel('rickmortymapCob')
        data['tex'] = bs.getTexture('rickmortymapColor')
        data['bgTex'] = bs.getTexture('rickmortyBGColor')
        data['bgModel'] = bs.getModel('rickmortyBG')
        data['vrFillModel'] = bs.getModel('doomShroomVRFill')
        data['bottomModel'] = bs.getModel('rickmortydown')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        self.foo = bs.newNode('terrain',
                              attrs={'model':self.preloadData['bgModel'],
                                     'lighting':False,
                                     'background':True,
                                     'colorTexture':self.preloadData['bgTex']})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'background':True,
                          'colorTexture':self.preloadData['bgTex']})

        self.bottom = bs.newNode('terrain',
                                 attrs={'model':self.preloadData['bottomModel'],
                                        'lighting':False,
                                        'colorTexture':self.preloadData['tex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.7,0.8,0.8)
        bsGlobals.ambientColor = (0.9,1.3,1.1)
        bsGlobals.shadowOrtho = False
        bsGlobals.vignetteOuter = (0.76,0.76,0.76)
        bsGlobals.vignetteInner = (0.95,0.95,0.99)


        rymPortalMap.Portal(position1 = (0.2929, -2.1028, -1.28649),position2 = (0.5,7,-8) ,color = (3,0,9))

    def _isPointNearEdge(self,p,running=False):
        x = p.x()
        z = p.z()
        xAdj = x*0.125
        zAdj = (z+3.7)*0.2
        if running:
            xAdj *= 1.4
            zAdj *= 1.4
        return (xAdj*xAdj+zAdj*zAdj > 1.0)

registerMap(RickMortyMap)

class TorneoMap(Map):
    import torneoDefs as defs
    name = 'Torneo'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'torneoPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('torneo')
        data['collideModel'] = bs.getCollideModel('torneoCob')
        data['tex'] = bs.getTexture('torneoColor')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1,1.1,1.0)
        bsGlobals.ambientColor = (1.1,1.1,1.0)
        bsGlobals.vignetteOuter = (0.7,0.65,0.75)
        bsGlobals.vignetteInner = (0.95,0.95,0.93)

registerMap(TorneoMap)

class IslaUgandaKnuckles(Map):
    import uknucklesDefs as defs
    name = 'Uganda Knuckles'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'uknucklesPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('uknuckles')
        data['collideModel'] = bs.getCollideModel('uknucklesCob')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['tex'] = bs.getTexture('uknucklesColor')
        data['bgModel'] = bs.getModel('uknucklesBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        self.foo = bs.newNode('terrain',
                              attrs={'model':self.preloadData['bgModel'],
                                     'lighting':False,
                                     'background':True,
                                     'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1,1.1,1.0)
        bsGlobals.ambientColor = (1.1,1.1,1.0)
        bsGlobals.vignetteOuter = (0.7,0.65,0.75)
        bsGlobals.vignetteInner = (0.95,0.95,0.93)

registerMap(IslaUgandaKnuckles)

class CragCastleBigMap(Map):
    import cragCastleBigDefs as defs
    name = 'Crag Castle Big'
    playTypes = ['melee','keepAway','teamFlag','conquest']

    @classmethod
    def getPreviewTextureName(cls):
        return 'cragCastleBigPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('cragCastleLevelBig')
        data['bottomModel'] = bs.getModel('cragCastleLevelBottomBig')
        data['collideModel'] = bs.getCollideModel('cragCastleLevelCollideBig')
        data['tex'] = bs.getTexture('cragCastleLevelColor')
        data['bgTex'] = bs.getTexture('menuBG')
        data['bgModel'] = bs.getModel('thePadBG') # fixme should chop this into vr/non-vr sections
        data['railingCollideModel'] = bs.getCollideModel('cragCastleLevelBumperBig')
        data['vrFillMoundModel'] = bs.getModel('cragCastleVRFillMound')
        data['vrFillMoundTex'] = bs.getTexture('vrFillMound')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        self.bottom = bs.newNode('terrain',
                                 attrs={'model':self.preloadData['bottomModel'],
                                        'lighting':False,
                                        'colorTexture':self.preloadData['tex']})
        self.bg = bs.newNode('terrain',
                             attrs={'model':self.preloadData['bgModel'],
                                    'lighting':False,
                                    'background':True,
                                    'colorTexture':self.preloadData['bgTex']})
        self.railing = bs.newNode('terrain',
                                  attrs={'collideModel':self.preloadData['railingCollideModel'],
                                         'materials':[bs.getSharedObject('railingMaterial')],
                                         'bumper':True})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillMoundModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'color':(0.2,0.25,0.2),
                          'background':True,
                          'colorTexture':self.preloadData['vrFillMoundTex']})
        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.shadowOrtho = True
        bsGlobals.shadowOffset = (0,0,-5.0)
        bsGlobals.tint = (1.15,1.05,0.75)
        bsGlobals.ambientColor = (1.15,1.05,0.75)
        bsGlobals.vignetteOuter = (0.6,0.65,0.6)
        bsGlobals.vignetteInner = (0.95,0.95,0.95)
        bsGlobals.vrNearClip = 1.0

registerMap(CragCastleBigMap)

class StepRightUpMapMod(Map):
    import stepRightUpLevelModDefs as defs
    name = 'Step Right Up Mod'
    playTypes = ['melee','keepAway','teamFlag','conquest']

    @classmethod
    def getPreviewTextureName(cls):
        return 'stepRightUpModPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('stepRightUpLevelMod')
        data['modelBottom'] = bs.getModel('stepRightUpLevelBottomMod')
        data['collideModel'] = bs.getCollideModel('stepRightUpLevelCollideMod')
        data['tex'] = bs.getTexture('stepRightUpLevelColor')
        data['bgTex'] = bs.getTexture('menuBG')
        data['bgModel'] = bs.getModel('thePadBG') # fixme should chop this into vr/non-vr chunks
        data['vrFillMoundModel'] = bs.getModel('stepRightUpVRFillMound')
        data['vrFillMoundTex'] = bs.getTexture('vrFillMound')
        return data

    def __init__(self):
        Map.__init__(self,vrOverlayCenterOffset=(0,-1,2))
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        self.nodeBottom = bs.newNode('terrain',
                                     delegate=self,
                                     attrs={'model':self.preloadData['modelBottom'],
                                            'lighting':False,
                                            'colorTexture':self.preloadData['tex']})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillMoundModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'color':(0.53,0.57,0.5),
                          'background':True,
                          'colorTexture':self.preloadData['vrFillMoundTex']})
        self.bg = bs.newNode('terrain',
                             attrs={'model':self.preloadData['bgModel'],
                                    'lighting':False,
                                    'background':True,
                                    'colorTexture':self.preloadData['bgTex']})
        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.2,1.1,1.0)
        bsGlobals.ambientColor = (1.2,1.1,1.0)
        bsGlobals.vignetteOuter = (0.7,0.65,0.75)
        bsGlobals.vignetteInner = (0.95,0.95,0.93)

registerMap(StepRightUpMapMod)

class IceMap(Map):
    import iceMapDefs as defs
    name = 'Mapa Helado'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','conquest','race']

    @classmethod
    def getPreviewTextureName(cls):
        return 'iceMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['modelTop'] = bs.getModel('iceMapTop')
        data['collideModelTop'] = bs.getCollideModel('iceMapTopCob')
        data['modelBottom'] = bs.getModel('iceMapBottom')
        data['collideModelBottom'] = bs.getCollideModel('iceMapBottomCob')
        data['modelIce'] = bs.getModel('iceMapIce')
        data['collideModelIce'] = bs.getCollideModel('iceMapIceCob')
        data['tex'] = bs.getTexture('iceMapColor')
        data['bgTex'] = bs.getTexture('natureBackgroundNColor')
        data['bgModel'] = bs.getModel('natureBackground') # fixme should chop this into vr/non-vr sections
        data['vrFillMoundModel'] = bs.getModel('thePadVRFillMound')
        data['vrFillMoundTex'] = bs.getTexture('vrFillMound')
        m = bs.Material()
        m.addActions(actions=('modifyPartCollision','friction',0.01))
        data['iceMaterial'] = m
        return data

    def __init__(self):
        Map.__init__(self)
        self.top = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModelTop'],
                                      'model':self.preloadData['modelTop'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        self.bottom = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModelBottom'],
                                      'model':self.preloadData['modelBottom'],
                                      'lighting':False,
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})
        self.ice = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModelIce'],
                                      'model':self.preloadData['modelIce'],
                                      'reflection':'soft',
                                      'reflectionScale':[0.65],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial'),
                                                    self.preloadData['iceMaterial']]})

        self.bg = bs.newNode('terrain',
                              attrs={'model':self.preloadData['bgModel'],
                                     'lighting':False,
                                     'background':True,
                                     'colorTexture':self.preloadData['bgTex']})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillMoundModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'color':(0.56,0.55,0.47),
                          'background':True,
                          'colorTexture':self.preloadData['vrFillMoundTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

        # def _doEmit():
            # position=(0,12,0)
            # velocity=(10,0,0)
            # bs.emitBGDynamics(position=position,
                              # velocity=velocity,
                              # emitType='stickers',
                              # count=30, spread=0, scale=1.4,
                              # chunkType='ice')
        # bs.gameTimer(500, _doEmit, repeat=True)

registerMap(IceMap)

class Halloween(Map):
    import halloweenDefs as defs
    name = 'Halloween'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'hwMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('hwMap')
        data['collideModel'] = bs.getCollideModel('hwMapCob')
        data['tex'] = bs.getTexture('hwMapColor')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(Halloween)

class WashMap(Map):
    import washMapDefs as defs
    name = 'Wash Map'
    playTypes = ['melee','keepAway','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'washMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('washMap')
        data['collideModel'] = bs.getCollideModel('washMapCob')
        data['modelDeath'] = bs.getModel('washMapDeath')
        data['collideModelDeath'] = bs.getCollideModel('washMapDeathCob')
        data['tex'] = bs.getTexture('washMapColor')
        data['bgModel'] = bs.getModel('washMapBG')
        data['vrFillMoundModel'] = bs.getModel('thePadVRFillMound')
        data['vrFillMoundTex'] = bs.getTexture('vrFillMound')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModelDeath'],
                                      'model':self.preloadData['modelDeath'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial'),
                                                   bs.getSharedObject('deathMaterial')]})

        self.foo = bs.newNode('terrain',
                              attrs={'model':self.preloadData['bgModel'],
                                     'lighting':False,
                                     'background':True,
                                     'colorTexture':self.preloadData['tex']})

        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillMoundModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'color':(0.56,0.55,0.47),
                          'background':True,
                          'colorTexture':self.preloadData['vrFillMoundTex']})
        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1,1.1,1.0)
        bsGlobals.ambientColor = (1.1,1.1,1.0)
        bsGlobals.vignetteOuter = (0.7,0.65,0.75)
        bsGlobals.vignetteInner = (0.95,0.95,0.93)

registerMap(WashMap)

class MarioWorldMap(Map):
    import mbwMapDefs as defs
    name = 'Mario Bros World'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','conquest']

    @classmethod
    def getPreviewTextureName(cls):
        return 'mbwMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('mbw')
        data['collideModel'] = bs.getCollideModel('mbwCob')
        data['tex'] = bs.getTexture('mbwColor')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

    def _isPointNearEdge(self, p, running=False):
        # count anything off our ground level as safe (for our platforms)
        # see if we're within edgeBox
        boxPosition = self.defs.boxes['edgeBox'][0:3]
        boxScale = self.defs.boxes['edgeBox'][6:9]
        x = (p.x() - boxPosition[0])/boxScale[0]
        z = (p.z() - boxPosition[2])/boxScale[2]
        return (x < -0.5 or x > 0.5 or z < -0.5 or z > 0.5)

registerMap(MarioWorldMap)

class GuardianMap(Map):
    import guardianMapDefs as defs
    name = 'Guardian'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'guardianMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('guardianMap')
        data['collideModel'] = bs.getCollideModel('guardianMapCob')
        data['tex'] = bs.getTexture('guardianMapColor')
        data['bgTex'] = bs.getTexture('skyGlassBG')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(GuardianMap)

class MineMap(Map):
    import mineMapDefs as defs
    name = 'Mine'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'mineMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('mineMap')
        data['collideModel'] = bs.getCollideModel('mineMapCob')
        data['tex'] = bs.getTexture('mineMapColor')
        data['bgTex'] = bs.getTexture('natureBackgroundColor')
        data['bgModel'] = bs.getModel('natureBackground')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(MineMap)

class OceanoMap(Map):
    import oceanoMapDefs as defs
    name = 'Oceano'
    playTypes = ['melee', 'keepAway', 'teamFlag', 'conquest', 'kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'oceanoMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('oceanoMap')
        data['collideModel'] = bs.getCollideModel('oceanoMapCob')
        data['tex'] = bs.getTexture('oceanoMapColor')
        data['bgModel'] = bs.getModel('oceanoMapBG')
        data['bgTex'] = bs.getTexture('oceanoMapBG')
        return data

    @classmethod
    def getMusicType(cls):
        return 'Flying'

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        g = bs.getSharedObject('globals')
        g.happyThoughtsMode = True
        g.shadowOffset = (0.0, 8.0, 5.0)
        g.tint = (0.8, 0.9, 1.3)
        g.ambientColor = (0.8, 0.9, 1.3)
        g.vignetteOuter = (0.79, 0.79, 0.69)
        g.vignetteInner = (0.97, 0.97, 0.99)
        g.vrNearClip = 1.0
        self.isFlying = True

        # throw out some tips on flying
        t = bs.newNode('text', attrs={
            'text':bs.Lstr(resource='pressJumpToFlyText'),
            'scale':1.2,
            'maxWidth':800,
            'position':(0,200),
            'shadow':0.5,
            'flatness':0.5,
            'hAlign':'center',
            'vAttach':'bottom'})
        c = bs.newNode('combine', owner=t, attrs={
            'size':4,
            'input0':0.3,
            'input1':0.9,
            'input2':0.0})
        bsUtils.animate(c, 'input3', {3000:0, 4000:1, 9000:1, 10000:0})
        c.connectAttr('output', t, 'color')
        bs.gameTimer(10000, t.delete)

registerMap(OceanoMap)

class SonicMap(Map):
    import sonicMapDefs as defs
    name = 'Sonic World'
    playTypes = ['melee','keepAway','teamFlag']

    @classmethod
    def getPreviewTextureName(cls):
        return 'sonicMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('sonicMap')
        data['collideModel'] = bs.getCollideModel('sonicMapCob')
        data['tex'] = bs.getTexture('sonicMapColor')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

registerMap(SonicMap)

class ObstaclesMapRace(Map):
    import obstaclesMapDefs as defs
    name = 'Obstacles Race'
    playTypes = ['race']

    @classmethod
    def getPreviewTextureName(cls):
        return 'obstaclesMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('obstaclesMap')
        data['collideModel'] = bs.getCollideModel('obstaclesMapCob')
        data['modelIce'] = bs.getModel('obstaclesIce')
        data['collideIceModel'] = bs.getCollideModel('obstaclesIceCob')
        data['modelDeath'] = bs.getModel('obstaclesDeath')
        data['collideDeathModel'] = bs.getCollideModel('obstaclesDeathCob')
        data['collideWallModel'] = bs.getCollideModel('obstaclesWallCob')
        data['tex'] = bs.getTexture('obstaclesMapColor')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['bgModel'] = bs.getModel('thePadBG')

        data['playerWallMaterial'] = bs.Material()
        data['playerWallMaterial'].addActions(actions=(('modifyPartCollision',
                                                        'friction', 0.0)))
        data['collideWithWallMaterial'] = bs.Material()
        data['playerWallMaterial'].addActions(
            conditions=('theyDontHaveMaterial',data['collideWithWallMaterial']),
            actions=(('modifyPartCollision','collide',False)))

        m = bs.Material()
        m.addActions(actions=('modifyPartCollision','friction',0.01))
        data['iceMaterial'] = m
        return data

    def __init__(self):
        Map.__init__(self)
	## Gracias Oore282
	#Cannon 1
	Auto(position1=(2.67889,3.22767,-1.58723),position2=(2.67889,3.22767,-19.58723),time=1000).autoRetain()
    #Cannon 2
	Auto2(position1=(-4.03589,3.22767,-1.58723),position2=(-4.03589,3.22767,-19.58723),time=1000).autoRetain()

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideIceModel'],
            'model':self.preloadData['modelIce'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         self.preloadData['iceMaterial']]})

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideDeathModel'],
            'model':self.preloadData['modelDeath'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         bs.getSharedObject('deathMaterial')]})

        self.playerWall = bs.newNode('terrain', attrs={
            'collideModel':self.preloadData['collideWallModel'],
            'affectBGDynamics':False,
            'materials':[self.preloadData['collideWithWallMaterial']]})

        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        g = bs.getSharedObject('globals')
        g.tint = (1, 1, 1)
        g.ambientColor = (1, 1, 1)
        g.vignetteOuter = (0.86, 0.86, 0.86)
        g.vignetteInner = (0.95, 0.95, 0.99)
        g.vrNearClip = 0.5

registerMap(ObstaclesMapRace)

class Auto(bs.Actor):
    def __init__(self,position1=(0,0,0),position2=(0,0,0),time=5000):
        bs.Actor.__init__(self)
        self.node = bs.newNode('prop',
                               delegate=self,
                               attrs={'position':position1,
                                      'velocity':(0,0,0),
                                      'model':bs.getModel('cannon'), # Modelo de la plataforma
                                      #'modelScale':2,      # Si necesitas el objeto mas grande, activa esta linea de codigo
                                      'bodyScale':3,        # Si necesitas cambiar el tamanio de la COLISION del objeto, acyiva esta linea
									  'density':999999999999999999999, # Esto es importante, impide que se caiga el objeto
									  'damping':999999999999999999999, # Tambien este
                                      'gravityScale':0, # Y este otro
                                      'body':'sphere', # dependiendo de la forma de tu plataforma deberas cambiar esto (sphere,crate,box o landMine)
                                      'reflection':'powerup', #Este es el tipo de brillo
                                      'reflectionScale':[0.3], #este es el brillo del objeto
                                      'colorTexture':bs.getTexture('bg'),  # Aqui va el nombre de la textura de la plataforma (puedes compartir
								      # la misma textura, tanto para el mapa como para la plataforma)
                                      'materials':[bs.getSharedObject('footingMaterial')]})  #Material del que estara compuesto la plataforma...
									  # Si quieres que la plataforma realice cierta accion al estar en contacto con un mugador deberas agregarle
									  # otro material, aunque eso es mas complejo...
        #Ahora el codigo que mueve la plataforma
        bsUtils.animateArray(self.node,'position',3,{0:position1,time:position2},loop=True)

class Auto2(bs.Actor):
    def __init__(self,position1=(0,0,0),position2=(0,0,0),time=5000):
        bs.Actor.__init__(self)
        self.node = bs.newNode('prop',
                               delegate=self,
                               attrs={'position':position1,
                                      'velocity':(0,0,0),
                                      'model':bs.getModel('cannon'), # Modelo de la plataforma
                                      #'modelScale':2,      # Si necesitas el objeto mas grande, activa esta linea de codigo
                                      'bodyScale':3,        # Si necesitas cambiar el tamanio de la COLISION del objeto, acyiva esta linea
									  'density':999999999999999999999, # Esto es importante, impide que se caiga el objeto
									  'damping':999999999999999999999, # Tambien este
                                      'gravityScale':0, # Y este otro
                                      'body':'sphere', # dependiendo de la forma de tu plataforma deberas cambiar esto (sphere,crate,box o landMine)
                                      'reflection':'powerup', #Este es el tipo de brillo
                                      'reflectionScale':[0.1], #este es el brillo del objeto
                                      'colorTexture':bs.getTexture('bg'),  # Aqui va el nombre de la textura de la plataforma (puedes compartir
								      # la misma textura, tanto para el mapa como para la plataforma)
                                      'materials':[bs.getSharedObject('footingMaterial')]})  #Material del que estara compuesto la plataforma...
									  # Si quieres que la plataforma realice cierta accion al estar en contacto con un mugador deberas agregarle
									  # otro material, aunque eso es mas complejo...
        #Ahora el codigo que mueve la plataforma
        bsUtils.animateArray(self.node,'position',3,{0:position1,time:position2},loop=True)

class ObstaclesMap(Map):
    import obstaclesMapDefs as defs
    name = 'Obstacles'
    playTypes = ['melee', 'keepAway', 'teamFlag']

    @classmethod
    def getPreviewTextureName(cls):
        return 'obstaclesMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('obstaclesMap')
        data['collideModel'] = bs.getCollideModel('obstaclesMapCob')
        data['modelIce'] = bs.getModel('obstaclesIce')
        data['collideIceModel'] = bs.getCollideModel('obstaclesIceCob')
        data['modelDeath'] = bs.getModel('obstaclesDeath')
        data['collideDeathModel'] = bs.getCollideModel('obstaclesDeathCob')
        data['tex'] = bs.getTexture('obstaclesMapColor')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['bgModel'] = bs.getModel('thePadBG')

        m = bs.Material()
        m.addActions(actions=('modifyPartCollision','friction',0.01))
        data['iceMaterial'] = m
        return data

    def __init__(self):
        Map.__init__(self)
	#Cannon 1
	Auto(position1=(2.67889,3.22767,-1.58723),position2=(2.67889,3.22767,-19.58723),time=1000).autoRetain()
    #Cannon 2
	Auto2(position1=(-4.03589,3.22767,-1.58723),position2=(-4.03589,3.22767,-19.58723),time=1000).autoRetain()

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideIceModel'],
            'model':self.preloadData['modelIce'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         self.preloadData['iceMaterial']]})

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideDeathModel'],
            'model':self.preloadData['modelDeath'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         bs.getSharedObject('deathMaterial')]})

        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        g = bs.getSharedObject('globals')
        g.tint = (1, 1, 1)
        g.ambientColor = (1, 1, 1)
        g.vignetteOuter = (0.86, 0.86, 0.86)
        g.vignetteInner = (0.95, 0.95, 0.99)
        g.vrNearClip = 0.5

registerMap(ObstaclesMap)

class WaterMap(Map):
    import watherMapDefs as defs
    name = 'Water'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'waterMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('waterMap')
        data['collideModel'] = bs.getCollideModel('waterMapCob')
        data['modelW'] = bs.getModel('waterWMap')
        data['tex'] = bs.getTexture('waterMapColor')
        data['bgTex'] = bs.getTexture('menuBG')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.bottom = bs.newNode('terrain', attrs={
            'model':self.preloadData['modelW'],
            'lighting':False,
            'colorTexture':self.preloadData['tex']})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(WaterMap)

class GravityFallsMap(Map):
    import gravityFallsMapDefs as defs
    name = 'GravityFallsMap'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'gravityFallsMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('gravityFallsMap')
        data['collideModel'] = bs.getCollideModel('gravityFallsMapCob')
        data['modeld'] = bs.getModel('gravityFallsMapD')
        data['tex'] = bs.getTexture('gravityFallsMapColor')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modeld'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         bs.getSharedObject('deathMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

        gfPortalMap.Portal(position1 = (7.5929, -10.1028, -1.68649),position2 = (5.2929, 11.1028, -2.78649),color = (3,0,9))

registerMap(GravityFallsMap)

class CourageMap(Map):
    import courageMapDefs as defs
    name = 'CourageMap'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'courageMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('courageMap')
        data['collideModel'] = bs.getCollideModel('courageMapCob')
        data['tex'] = bs.getTexture('courageMapColor')
        data['bgTex'] = bs.getTexture('courageBGColor')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

    def _isPointNearEdge(self, p, running=False):
        # count anything off our ground level as safe (for our platforms)
        # see if we're within edgeBox
        boxPosition = self.defs.boxes['edgeBox'][0:3]
        boxScale = self.defs.boxes['edgeBox'][6:9]
        x = (p.x() - boxPosition[0])/boxScale[0]
        z = (p.z() - boxPosition[2])/boxScale[2]
        return (x < -0.5 or x > 0.5 or z < -0.5 or z > 0.5)

registerMap(CourageMap)

class GotchaMap(Map):
    import gotchaMapDefs as defs
    name = 'GotchaMap'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'gotchaMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('gotchaMap')
        data['modelBG'] = bs.getModel('gotchaMapBG')
        data['collideModel'] = bs.getCollideModel('gotchaMapCob')
        data['tex'] = bs.getTexture('gotchaMapColor')
        data['collideRailing'] = bs.getCollideModel('gotchaMapRailing')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modelBG'],
            'colorTexture':self.preloadData['tex'],
            'lighting':False,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.railing = bs.newNode('terrain', attrs={
            'collideModel':self.preloadData['collideRailing'],
            'materials':[bs.getSharedObject('railingMaterial')],
            'bumper':True})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(GotchaMap)

class Cangremovil(bs.Actor):
    def __init__(self,position1=(0,0,0),position2=(0,0,0),time=5000):
        bs.Actor.__init__(self)
        self.node = bs.newNode('prop',
                               delegate=self,
                               attrs={'position':position1,
                                      'velocity':(0,0,0),
                                      'model':bs.getModel('cangremovilModel'), # Modelo de la plataforma
                                      #'modelScale':2,      # Si necesitas el objeto mas grande, activa esta linea de codigo
                                      'bodyScale':3,        # Si necesitas cambiar el tamanio de la COLISION del objeto, acyiva esta linea
									  'density':999999999999999999999, # Esto es importante, impide que se caiga el objeto
									  'damping':999999999999999999999, # Tambien este
                                      'gravityScale':0, # Y este otro
                                      'body':'crate', # dependiendo de la forma de tu plataforma deberas cambiar esto (sphere,crate,box o landMine)
                                      'reflection':'powerup', #Este es el tipo de brillo
                                      'reflectionScale':[0.3], #este es el brillo del objeto
                                      'colorTexture':bs.getTexture('cangremovilColor'),  # Aqui va el nombre de la textura de la plataforma (puedes compartir
								      # la misma textura, tanto para el mapa como para la plataforma)
                                      'materials':[bs.getSharedObject('footingMaterial')]})  #Material del que estara compuesto la plataforma...
									  # Si quieres que la plataforma realice cierta accion al estar en contacto con un mugador deberas agregarle
									  # otro material, aunque eso es mas complejo...
        #Ahora el codigo que mueve la plataforma
        bsUtils.animateArray(self.node,'position',3,{0:position1,time:position2},loop=True)

class BikiniBottomMap(Map):
    import bikiniBottomDefs as defs
    name = 'Bikini Bottom'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'bikiniBottomPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('bikiniBottomMap')
        data['modelBG'] = bs.getModel('bikiniBottomMapBG')
        data['collideModel'] = bs.getCollideModel('bikiniBottomMapCob')
        data['tex'] = bs.getTexture('bikiniBottomMapColor')
        data['texBG'] = bs.getTexture('bikiniBottomMapBGColor')
        return data

    def __init__(self):
        Map.__init__(self)
	#Cangremovil
	Cangremovil(position1=(-30.10481, 0.81866, 3.05734),position2=(30.10481, 0.81866, 3.05734),time=3000).autoRetain()
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modelBG'],
            'colorTexture':self.preloadData['texBG'],
            'lighting':False,
            'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

registerMap(BikiniBottomMap)

class PiramideMap(Map):
    import piramideMapDefs as defs
    name = 'Piramide'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','race']

    @classmethod
    def getPreviewTextureName(cls):
        return 'piramideMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('piramideMap')
        data['collideModel'] = bs.getCollideModel('piramideMapCob')
        data['tex'] = bs.getTexture('piramideMapColor')
        data['bgTex'] = bs.getTexture('menuBG')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.8, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(PiramideMap)

class KrustyKrabMap(Map):
    import krustyKrabMapDefs as defs
    name = 'Krusty Krab'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','race']

    @classmethod
    def getPreviewTextureName(cls):
        return 'krustyKrabMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('krustyKrabMap')
        data['collideModel'] = bs.getCollideModel('krustyKrabMapCob')
        data['tex'] = bs.getTexture('krustyKrabMapColor')
        data['bgTex'] = bs.getTexture('krustyKrabBGMapColor')
        data['bgModel'] = bs.getModel('krustyKrabBGMap')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.15, 1.11, 1.03)
        bsGlobals.ambientColor = (1.2, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.73, 0.7)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.95)

registerMap(KrustyKrabMap)

class TorneoFuerzaFly(Map):
    import torneoFuerzaFlyDefs as defs
    name = 'Torneo de Poder Fly'
    playTypes = ['melee','keepAway','teamFlag','conquest','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'torneoFuerzaFlyPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('torneoFuerzaFly')
        data['bgModel'] = bs.getModel('alwaysLandBG')
        data['collideModel'] = bs.getCollideModel('torneoFuerzaFlyCob')
        data['tex'] = bs.getTexture('torneoFuerza')
        data['bgTex'] = bs.getTexture('torneoFuerzaBG')
        data['vrFillMoundModel'] = bs.getModel('alwaysLandVRFillMound')
        data['vrFillMoundTex'] = bs.getTexture('vrFillMound')
        return data

    @classmethod
    def getMusicType(cls):
        return 'Flying'

    def __init__(self):
        Map.__init__(self,vrOverlayCenterOffset=(0,-3.7,2.5))
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain',
                              attrs={'model':self.preloadData['bgModel'],
                                     'lighting':False,
                                     'background':True,
                                     'colorTexture':self.preloadData['bgTex']})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillMoundModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'color':(0.2,0.25,0.2),
                          'background':True,
                          'colorTexture':self.preloadData['vrFillMoundTex']})
        g = bs.getSharedObject('globals')
        g.happyThoughtsMode = True
        g.shadowOffset = (0.0,8.0,5.0)
        g.tint = (1.0,1.05,1.1)
        g.ambientColor = (0.9,1.3,1.1)
        g.vignetteOuter = (0.64,0.59,0.69)
        g.vignetteInner = (0.95,0.95,0.93)
        g.vrNearClip = 1.0
        self.isFlying = True

        # throw out some tips on flying
        t = bs.newNode('text',
                       attrs={'text':bs.Lstr(resource='pressJumpToFlyText'),
                              'scale':1.2,
                              'maxWidth':800,
                              'position':(0,200),
                              'shadow':0.5,
                              'flatness':0.5,
                              'hAlign':'center',
                              'vAttach':'bottom'})
        c = bs.newNode('combine',owner=t,attrs={'size':4,'input0':0.3,'input1':0.9,'input2':0.0})
        bsUtils.animate(c,'input3',{3000:0,4000:1,9000:1,10000:0})
        c.connectAttr('output',t,'color')
        bs.gameTimer(10000,t.delete)

registerMap(TorneoFuerzaFly)

class TorneoDeFuerza(Map):
    import torneoFuerzaDefs as defs
    name = 'Torneo de Poder'
    playTypes = ['melee','keepAway','teamFlag','conquest','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'torneoFuerzaPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('torneoFuerza')
        data['modelNL'] = bs.getModel('torneoFuerzaNL')
        data['bgModel'] = bs.getModel('alwaysLandBG')
        data['collideModel'] = bs.getCollideModel('torneoFuerzaCob')
        data['tex'] = bs.getTexture('torneoFuerza')
        data['bgTex'] = bs.getTexture('torneoFuerzaBG')
        data['vrFillMoundModel'] = bs.getModel('alwaysLandVRFillMound')
        data['vrFillMoundTex'] = bs.getTexture('vrFillMound')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'model':self.preloadData['modelNL'],
                                      'lighting':False,
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain',
                              attrs={'model':self.preloadData['bgModel'],
                                     'lighting':False,
                                     'background':True,
                                     'colorTexture':self.preloadData['bgTex']})
        bs.newNode('terrain',
                   attrs={'model':self.preloadData['vrFillMoundModel'],
                          'lighting':False,
                          'vrOnly':True,
                          'color':(0.2,0.25,0.2),
                          'background':True,
                          'colorTexture':self.preloadData['vrFillMoundTex']})
        g = bs.getSharedObject('globals')
        g.tint = (1.0,1.05,1.1)
        g.ambientColor = (0.9,1.3,1.1)
        g.vignetteOuter = (0.64,0.59,0.69)
        g.vignetteInner = (0.95,0.95,0.93)

registerMap(TorneoDeFuerza)

class DreamlandMap(Map):
    import dreamlandMapDefs as defs
    name = 'Dream Land'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','conquest']

    @classmethod
    def getPreviewTextureName(cls):
        return 'dreamlandMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('dreamlandMap')
        data['collideModel'] = bs.getCollideModel('dreamlandMapCob')
        data['modelB'] = bs.getModel('dreamlandMapBottom')
        data['collideModelB'] = bs.getCollideModel('dreamlandMapBottomCob')
        data['tex'] = bs.getTexture('dreamlandMapColor')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.nodeB = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModelB'],
                                      'model':self.preloadData['modelB'],
                                      'colorTexture':self.preloadData['tex'],
                                      'lighting':False,
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['bgModel'],
            'colorTexture':self.preloadData['bgTex'],
            'lighting':False,
            'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.9, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(DreamlandMap)

class DreamlandMapN(Map):
    import dreamlandMapDefs as defs
    name = 'Dream Land Night'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','conquest']

    @classmethod
    def getPreviewTextureName(cls):
        return 'dreamlandMapNPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('dreamlandMap')
        data['collideModel'] = bs.getCollideModel('dreamlandMapCob')
        data['modelB'] = bs.getModel('dreamlandMapBottom')
        data['collideModelB'] = bs.getCollideModel('dreamlandMapBottomCob')
        data['tex'] = bs.getTexture('dreamlandMapColor')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.nodeB = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModelB'],
                                      'model':self.preloadData['modelB'],
                                      'colorTexture':self.preloadData['tex'],
                                      'lighting':False,
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['bgModel'],
            'colorTexture':self.preloadData['bgTex'],
            'lighting':False,
            'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.0, 0.2, 0.5)
        bsGlobals.ambientColor = (1, 1, 1)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(DreamlandMapN)

class MortalKombatMap(Map):
    import mkMapDefs as defs
    name = 'Mortal Kombat'
    playTypes = ['melee', 'keepAway', 'teamFlag']

    @classmethod
    def getPreviewTextureName(cls):
        return 'mapMKPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('mapMK')
        data['collideModel'] = bs.getCollideModel('mapMKCob')
        data['tex'] = bs.getTexture('mapMKColor')
        data['bgTex'] = bs.getTexture('torneoFuerzaBG')
        data['bgModel'] = bs.getModel('alwaysLandBG')
        return data

    def __init__(self):
        Map.__init__(self, vrOverlayCenterOffset=(0,0,2))
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})
        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.9, 0.9, 1.3)
        bsGlobals.ambientColor = (0.8, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

    def _isPointNearEdge(self,p,running=False):
        boxPosition = self.defs.boxes['edgeBox'][0:3]
        boxScale = self.defs.boxes['edgeBox'][6:9]
        x = (p.x() - boxPosition[0])/boxScale[0]
        z = (p.z() - boxPosition[2])/boxScale[2]
        return (x < -0.5 or x > 0.5 or z < -0.5 or z > 0.5)

registerMap(MortalKombatMap)

class PicnicMap(Map):
    import picnicMapDefs as defs
    name = 'Picnic'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'mapPicnicPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('mapPicnic')
        data['collideModel'] = bs.getCollideModel('mapPicnicCob')
        data['modelCopa'] = bs.getModel('mapPicnicTransparent')
        data['collideModelCopa'] = bs.getCollideModel('mapPicnicTransparentCob')
        data['collideModelDeath'] = bs.getCollideModel('mapPicnicDeathCob')
        data['tex'] = bs.getTexture('mapPicnicColor')
        data['bgTex'] = bs.getTexture('menuBG')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModelCopa'],
            'model':self.preloadData['modelCopa'],
            'colorTexture':self.preloadData['tex'],
            'opacity':0.8,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.foo = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        self.bgCollide = bs.newNode('terrain', attrs={
            'collideModel':self.preloadData['collideModelDeath'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         bs.getSharedObject('deathMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

registerMap(PicnicMap)

class TestBotsMap(Map):
    import testBotsMapDefs as defs
    name = 'TestBotsMap'
    playTypes = ['melee']

    @classmethod
    def getPreviewTextureName(cls):
        return 'testBotsMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('testBotsMap')
        data['collideModel'] = bs.getCollideModel('testBotsMapCob')
        data['tex'] = bs.getTexture('testBotsMapColor')
        data['bgTex'] = bs.getTexture('uknucklesBGColor')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain',
                               delegate=self,
                               attrs={'collideModel':self.preloadData['collideModel'],
                                      'model':self.preloadData['model'],
                                      'colorTexture':self.preloadData['tex'],
                                      'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['bgModel'],
            'colorTexture':self.preloadData['bgTex'],
            'lighting':False,
            'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (0.7, 0.9, 1.3)
        bsGlobals.ambientColor = (0.5, 0.9, 1.3)
        bsGlobals.vignetteOuter = (0.79, 0.79, 0.69)
        bsGlobals.vignetteInner = (0.97, 0.97, 0.99)

registerMap(TestBotsMap)

class ArenaMinigore(Map):
    import arenaMinigoreDefs as defs
    name = 'Hardland Arena'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'arenaMinigorePreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('arenaminigoreMap')
        data['collideModel'] = bs.getCollideModel('arenaminigoreMapCob')
        data['tex'] = bs.getTexture('arenaminigoreMapColor')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

        bs.gameTimer(10,self._offMusic)

    def _offMusic(self):
        bs.playMusic(None)
        bs.gameTimer(10,self._newMusic)

    def _newMusic(self):
        gMusic = bs.newNode(type='sound', attrs={
            'sound':bs.getSound('frozenPlainsMusic'),
            'positional':False,
            'music':True,
            'volume':4.0,
            'loop':True})
        bs.playMusic(gMusic)

registerMap(ArenaMinigore)

### MAP RAW
class EliminationRawMap(Map):
    import ecMapDefs as defs
    name = 'Elimination Chamber - Raw'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','wwe']

    @classmethod
    def getPreviewTextureName(cls):
        return 'ecRawMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('ecRawMap')
        data['collideModel'] = bs.getCollideModel('ecMapCob')
        data['modelInv'] = bs.getModel('ecRawInvMap')
        data['modelNL'] = bs.getModel('ecRawNLMap')
        data['modelGlass'] = bs.getModel('ecRawGlassMap')
        data['collideModelGlass'] = bs.getCollideModel('ecGlassMapCob')
        data['modelExt'] = bs.getModel('ecExtMap')
        data['collideModelExt'] = bs.getCollideModel('ecExtMapCob')
        data['tex'] = bs.getTexture('ecMapColor')
        data['bgModel'] = bs.getModel('ecBGMap')
        return data

    def __init__(self):
        Map.__init__(self)
        self.ring = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.ringNL = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modelNL'],
            'colorTexture':self.preloadData['tex'],
            'lighting':False,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.ringInv = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modelInv'],
            'colorTexture':self.preloadData['tex'],
            'opacity':0.05,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.glass = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModelGlass'],
            'model':self.preloadData['modelGlass'],
            'colorTexture':self.preloadData['tex'],
            'lighting':False,
            'opacity':0.2,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.ext = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModelExt'],
            'model':self.preloadData['modelExt'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['tex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

registerMap(EliminationRawMap)

### MAP SMACKDOWN
class EliminationSDMap(Map):
    import ecMapDefs as defs
    name = 'Elimination Chamber - SD'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill','wwe']

    @classmethod
    def getPreviewTextureName(cls):
        return 'ecSDMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('ecSDMap')
        data['collideModel'] = bs.getCollideModel('ecMapCob')
        data['modelInv'] = bs.getModel('ecSDInvMap')
        data['modelNL'] = bs.getModel('ecSDNLMap')
        data['modelGlass'] = bs.getModel('ecSDGlassMap')
        data['collideModelGlass'] = bs.getCollideModel('ecGlassMapCob')
        data['modelExt'] = bs.getModel('ecExtMap')
        data['collideModelExt'] = bs.getCollideModel('ecExtMapCob')
        data['tex'] = bs.getTexture('ecMapColor')
        data['bgModel'] = bs.getModel('ecBGMap')
        return data

    def __init__(self):
        Map.__init__(self)
        self.ring = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.ringNL = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modelNL'],
            'colorTexture':self.preloadData['tex'],
            'lighting':False,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.ringInv = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modelInv'],
            'colorTexture':self.preloadData['tex'],
            'opacity':0.05,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.glass = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModelGlass'],
            'model':self.preloadData['modelGlass'],
            'colorTexture':self.preloadData['tex'],
            'lighting':False,
            'opacity':0.2,
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.ext = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModelExt'],
            'model':self.preloadData['modelExt'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['tex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

registerMap(EliminationSDMap)

class TwoFortMap(Map):
    import twoFortMapDefs as defs
    name = 'Two Fort'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'twoFortMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('twoFortMap')
        data['collideModel'] = bs.getCollideModel('twoFortMapCob')
        data['modelWater'] = bs.getModel('twoFortWaterMap')
        data['collideModelWater'] = bs.getCollideModel('twoFortWaterMapCob')
        data['tex'] = bs.getTexture('twoFortMapColor')
        data['bgTex'] = bs.getTexture('menuBG')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)

        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.water = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModelWater'],
            'model':self.preloadData['modelWater'],
            'lighting':False,
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         bs.getSharedObject('deathMaterial')]})

        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.1, 1.0)
        bsGlobals.ambientColor = (1.1, 1.1, 1.0)
        bsGlobals.vignetteOuter = (0.7, 0.65, 0.75)
        bsGlobals.vignetteInner = (0.95, 0.95, 0.93)

registerMap(TwoFortMap)

class PaperMap(Map):
    import paperMapDefs as defs
    name = 'Paper Map'
    playTypes = ['melee','keepAway','teamFlag','kingOfTheHill']

    @classmethod
    def getPreviewTextureName(cls):
        return 'paperMapPreview'

    @classmethod
    def onPreload(cls):
        data = {}
        data['model'] = bs.getModel('paperMap')
        data['modelNL'] = bs.getModel('paperNLMap')
        data['collideModel'] = bs.getCollideModel('paperMapCob')
        data['collideDeath'] = bs.getCollideModel('paperMapDeath')
        data['tex'] = bs.getTexture('paperMapColor')
        data['bgTex'] = bs.getTexture('menuBG')
        data['bgModel'] = bs.getModel('thePadBG')
        return data

    def __init__(self):
        Map.__init__(self)
        self.node = bs.newNode('terrain', delegate=self, attrs={
            'collideModel':self.preloadData['collideModel'],
            'model':self.preloadData['model'],
            'colorTexture':self.preloadData['tex'],
            'materials':[bs.getSharedObject('footingMaterial')]})

        self.nl = bs.newNode('terrain', delegate=self, attrs={
            'model':self.preloadData['modelNL'],
            'lighting':False,
            'colorTexture':self.preloadData['tex']})

        self.death = bs.newNode('terrain', attrs={
            'collideModel':self.preloadData['collideDeath'],
            'materials':[bs.getSharedObject('footingMaterial'),
                         bs.getSharedObject('deathMaterial')]})

        self.bg = bs.newNode('terrain', attrs={
            'model':self.preloadData['bgModel'],
            'lighting':False,
            'background':True,
            'colorTexture':self.preloadData['bgTex']})

        bsGlobals = bs.getSharedObject('globals')
        bsGlobals.tint = (1.1, 1.2, 1.3)
        bsGlobals.ambientColor = (1.1, 1.2, 1.3)
        bsGlobals.vignetteOuter = (0.65, 0.6, 0.55)
        bsGlobals.vignetteInner = (0.9, 0.9, 0.93)

        PortalPaperMap(pos1=(-8.51902,3.48958,-1.70803),
                       pos2=(-8.49219,1.59328,-6.47048),
                       pos3=(-5.34609,4.06478,-9.69347),
                       pos4=(9.8227,1.72204,5.39438))

    # def _isPointNearEdge(self,p,running=False):
        # # see if we're within edgeBox
        # boxes = self.defs.boxes
        # boxPosition = boxes['b7'][0:3]
        # boxScale = boxes['b7'][6:9]
        # x = (p.x() - boxPosition[0])/boxScale[0]
        # z = (p.z() - boxPosition[2])/boxScale[2]
        # # if we're outside of *both* boxes we're near the edge
        # return (x < -0.5 or x > 0.5 or z < -0.5 or z > 0.5)

registerMap(PaperMap)

class PortalPaperMap(bs.Actor):
    def __init__(self, pos1, pos2, pos3, pos4, color=(1,1,1)):
        bs.Actor.__init__(self)

        self.radius = 1.1
        self.position1 = pos1
        self.position2 = pos2
        self.position3 = pos3
        self.position4 = pos4
        self.cooldown = False

        self.portal1Material = bs.Material()
        self.portal1Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.Portal1)))

        self.portal1Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('objectMaterial')),
                        'and',
                        ('theyDontHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.objPortal1)))

        self.portal2Material = bs.Material()
        self.portal2Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.Portal2)))

        self.portal2Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('objectMaterial')),
                        'and',
                        ('theyDontHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.objPortal2)))

        self.portal3Material = bs.Material()
        self.portal3Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.Portal3)))

        self.portal3Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('objectMaterial')),
                        'and',
                        ('theyDontHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.objPortal3)))

        self.portal4Material = bs.Material()
        self.portal4Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.Portal4)))

        self.portal4Material.addActions(
            conditions=(('theyHaveMaterial',
                        bs.getSharedObject('objectMaterial')),
                        'and',
                        ('theyDontHaveMaterial',
                        bs.getSharedObject('playerMaterial'))),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("call","atConnect", self.objPortal4)))

        self.node1 = bs.newNode('region',
                       attrs={'position':(self.position1[0],
                                          self.position1[1],
                                          self.position1[2]),
                              'scale':(0.1,0.1,0.1),
                              'type':'sphere',
                              'materials':[self.portal1Material]})
        # self.visualRadius = bs.newNode('shield',
                    # attrs={'position':self.position1,
                           # 'color':color,
                           # 'radius':0.1})
        # bsUtils.animate(self.visualRadius,"radius",{0:0,500:self.radius*5})
        bsUtils.animateArray(
            self.node1,"scale",3,{0:(0,0,0),500:(self.radius,
                                                 self.radius,
                                                 self.radius)})

        self.node2 = bs.newNode('region',
                       attrs={'position':(self.position2[0],
                                          self.position2[1],
                                          self.position2[2]),
                              'scale':(0.1,0.1,0.1),
                              'type':'sphere',
                              'materials':[self.portal2Material]})
        # self.visualRadius2 = bs.newNode('shield',
                    # attrs={'position':self.position2,
                           # 'color':color,
                           # 'radius':0.1})
        # bsUtils.animate(self.visualRadius2,"radius",{0:0,500:self.radius*5})
        bsUtils.animateArray(
            self.node2,"scale",3,{0:(0,0,0),500:(self.radius,
                                                 self.radius,
                                                 self.radius)})

        self.node3 = bs.newNode('region',
                       attrs={'position':(self.position3[0],
                                          self.position3[1],
                                          self.position3[2]),
                              'scale':(0.1,0.1,0.1),
                              'type':'sphere',
                              'materials':[self.portal3Material]})
        # self.visualRadius3 = bs.newNode('shield',
                    # attrs={'position':self.position3,
                           # 'color':color,
                           # 'radius':0.1})
        # bsUtils.animate(self.visualRadius3,"radius",{0:0,500:self.radius*5})
        bsUtils.animateArray(
            self.node3,"scale",3,{0:(0,0,0),500:(self.radius,
                                                 self.radius,
                                                 self.radius)})
        self.node4 = bs.newNode('region',
                       attrs={'position':(self.position4[0],
                                          self.position4[1],
                                          self.position4[2]),
                              'scale':(0.1,0.1,0.1),
                              'type':'sphere',
                              'materials':[self.portal4Material]})
        # self.visualRadius4 = bs.newNode('shield',
                    # attrs={'position':self.position4,
                           # 'color':color,
                           # 'radius':0.1})
        # bsUtils.animate(self.visualRadius4,"radius",{0:0,500:self.radius*5})
        bsUtils.animateArray(
            self.node4,"scale",3,{0:(0,0,0),500:(self.radius,
                                                 self.radius,
                                                 self.radius)})

    def cooldown1(self):
        self.cooldown = True
        def off():
            self.cooldown = False
        bs.gameTimer(10,off)

    def Portal1(self):
        sound = bs.getSound('powerup01')
        bs.playSound(sound)
        node = bs.getCollisionInfo('opposingNode')
        node.handleMessage(bs.StandMessage(position = self.node2.position))

    def Portal2(self):
        sound = bs.getSound('powerup01')
        bs.playSound(sound)
        node = bs.getCollisionInfo('opposingNode')
        node.handleMessage(bs.StandMessage(position = self.node1.position))

    def Portal3(self):
        sound = bs.getSound('powerup01')
        bs.playSound(sound)
        node = bs.getCollisionInfo('opposingNode')
        node.handleMessage(bs.StandMessage(position = self.node4.position))

    def Portal4(self):
        sound = bs.getSound('powerup01')
        bs.playSound(sound)
        node = bs.getCollisionInfo('opposingNode')
        node.handleMessage(bs.StandMessage(position = self.node3.position))

    def objPortal1(self):
        node = bs.getCollisionInfo('opposingNode')
        v = node.velocity
        if not self.cooldown:
            node.position = self.position2
            self.cooldown1()
        def vel():
            node.velocity = v
        bs.gameTimer(10,vel)

    def objPortal2(self):
        node = bs.getCollisionInfo('opposingNode')
        v = node.velocity
        if not self.cooldown:
            node.position = self.position1
            self.cooldown1()
        def vel():
            node.velocity = v
        bs.gameTimer(10,vel)

    def objPortal3(self):
        node = bs.getCollisionInfo('opposingNode')
        v = node.velocity
        if not self.cooldown:
            node.position = self.position4
            self.cooldown1()
        def vel():
            node.velocity = v
        bs.gameTimer(10,vel)

    def objPortal4(self):
        node = bs.getCollisionInfo('opposingNode')
        v = node.velocity
        if not self.cooldown:
            node.position = self.position3
            self.cooldown1()
        def vel():
            node.velocity = v
        bs.gameTimer(10,vel)
