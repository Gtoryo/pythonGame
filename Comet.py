import pygame
import random
from Monster import Mummy
from Monster import Alien

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):

        super().__init__()
        self.comet_event = comet_event
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.speed = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = -random.randint(0, 800)

    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')
         # on verifie si le nombre de comets est egale à 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre de cometes à 0
            self.comet_event.reset_percent()
            # faire réapparaitre les deux premiers monstres
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)



    def fall(self):

        self.rect.y +=  self.speed  

        if self.rect.y >= 500:
          self.remove()

          # si il n'y a plus de boule de feu
          if len(self.comet_event.all_comets) == 0:
            # remettre la jauge au départ
            self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            self.remove()
            self.comet_event.game.sound_manager.play('cris')
            self.comet_event.game.player.damage(5)
            
            