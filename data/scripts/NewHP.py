import bs
from bsSpaz import Spaz
import random

Spaz._old_init = Spaz.__init__
def _new_init(self, color=(1,1,1), highlight=(0.5, 0.5, 0.5),
              character="Spaz", sourcePlayer=None, startInvincible=True,
              canAcceptPowerups=True, powerupsExpire=False, demoMode=False):
    self._old_init(color,highlight,character,sourcePlayer,
                   startInvincible,canAcceptPowerups,
                   powerupsExpire,demoMode)
    def _new_hp():
        if self.node is None and not self.node.exists():
            return
        hp = bs.newNode('math',
                        owner=self.node,
                        attrs={
                            'input1': (
                                0, 1.14, 0) if self.sourcePlayer.exists(
                                ) else (0, 1.14, 0),
                            'operation': 'add'
                        })
        self.node.connectAttr('torsoPosition', hp, 'input2')
        self.hp = bs.newNode('text',
                             owner=self.node,
                             attrs={
                                'text': '',
                                'inWorld': True,
                                'shadow': 1,
                                'flatness': 0.9,
                                'scale': 0.1,
                                'hAlign': 'center',
                             })
        hp.connectAttr('output', self.hp, 'position')
        bs.animate(self.hp, 'scale', {0: 0.0, 1200: 0.01})
        bs.animate(self.hp,'opacity',{0:1.0})
        
        def _update():
            if not self.hp.exists():
                return
            if self.shield is not None and self.shield.exists():
                hptext = int(
                    (self.shieldHitPoints/self.shieldHitPointsMax)*100)
            else:
                hptext = int(self.hitPoints*0.1)
            if hptext >= 75:
                color = (1,1,1)
            elif hptext >= 50:
                color = (1,1,1)
            elif hptext >= 25:
                color = (1,1,1)
            else:
                color = (1,0,0)
            self.hp.text = 'HP : ' + str(hptext) + '%'
            self.hp.color = (1,1,1) if self.shield else color
        bs.gameTimer(50, _update, repeat=True)
    _new_hp()
    # app = _ba.app
    # cfg = app.config
    # new_hp = cfg.get('New HP', True)
    # if new_hp:
    #     _new_hp()

Spaz.__init__ = _new_init
