import bs
import random
import bsUtils
import math
import bsVector

## Thanks BombDash ##
class Portal(bs.Actor):
    def __init__(self,position1 = (0,1,0),position2 = (3,1,0),color = (random.random(),random.random(),random.random())):
        bs.Actor.__init__(self)

        self.radius = 1.1
        self.position1 = position1
        self.position2 = position2
        self.cooldown = False

        self.portal1Material = bs.Material()
        self.portal1Material.addActions(conditions=(('theyHaveMaterial', bs.getSharedObject('playerMaterial'))),actions=(("modifyPartCollision","collide",True),
                                                      ("modifyPartCollision","physical",False),
                                                      ("call","atConnect", self.Portal1)))

        self.portal2Material = bs.Material()
        self.portal2Material.addActions(conditions=(('theyHaveMaterial', bs.getSharedObject('playerMaterial'))),actions=(("modifyPartCollision","collide",True),
                                                      ("modifyPartCollision","physical",False),
                                                      ("call","atConnect", self.Portal2)))

        self.portal1Material.addActions(conditions=(('theyHaveMaterial', bs.getSharedObject('objectMaterial')),'and',('theyDontHaveMaterial', bs.getSharedObject('playerMaterial'))),actions=(("modifyPartCollision","collide",True),
                                                      ("modifyPartCollision","physical",False),
                                                      ("call","atConnect", self.objPortal1)))

        self.portal2Material.addActions(conditions=(('theyHaveMaterial', bs.getSharedObject('objectMaterial')),'and',('theyDontHaveMaterial', bs.getSharedObject('playerMaterial'))),actions=(("modifyPartCollision","collide",True),
                                                      ("modifyPartCollision","physical",False),
                                                      ("call","atConnect", self.objPortal2)))


        self.node1 = bs.newNode('region',
                       attrs={'position':(self.position1[0],self.position1[1],self.position1[2]),
                              'scale':(0.1,0.1,0.1),
                              'type':'sphere',
                              'materials':[self.portal1Material]})
        self.visualRadius = bs.newNode('shield',attrs={'position':self.position1,'color':color,'radius':2.1})
        bsUtils.animate(self.visualRadius,"radius",{0:0,500:self.radius*0})
        bsUtils.animateArray(self.node1,"scale",3,{0:(0,0,0),500:(self.radius*5,self.radius*5,self.radius*5)})


        self.node2 = bs.newNode('region',
                       attrs={'position':(self.position2[0],self.position2[1],self.position2[2]),
                              'scale':(0.1,0.1,0.1),
                              'type':'sphere',
                              'materials':[self.portal2Material]})
        self.visualRadius2 = bs.newNode('shield',attrs={'position':self.position2,'color':color,'radius':0.1})
        bsUtils.animate(self.visualRadius2,"radius",{0:0,500:self.radius*0})
        bsUtils.animateArray(self.node2,"scale",3,{0:(0,0,0),500:(self.radius,self.radius,self.radius)})

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
        return

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
        return
