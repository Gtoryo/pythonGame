import pygame
import random
import Animation

class Monster(Animation.Animation):

    def __init__(self, game, name, dimension, decalage = 0):
        super().__init__(name, dimension)
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - decalage
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):

        self.default_speed = speed
        self.fast = random.randint(1, 3)

    def after_damage(self):

        self.rect.x += 100
        self.game.sound_manager.play('retour')

    def set_loot_amount(self, amount):

        self.loot_amount = amount

    def damage(self, amount):

        # infliger les degats
        self.health -= amount

        # on verifie ses point de vie est < ou égale à O

        if self.health <= 0:

            # le suprrimer mais en le faisant reapparaitre en tant que nouveau monstre

            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.health_max
            self.fast = random.randint(1, self.default_speed)

            # onajoute le nombre de points
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est charge à so maximum
            if self.game.comet_event.is_full_loaded():
                # retire les joueurs
                self.game.all_monsters.remove(self)

                # appel de la methode pour essayer de declancher la plui de cometes
                self.game.comet_event.attempt_fall()


    def update_animation(self):
        self.animate(loop = True)


    def update_health_bar(self, surface):

        # on dessine nos barres de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.health_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        

    def forward(self):

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.fast

        # si le joueur est en collision avec le monstre
        else:
            self.game.player.damage(self.attack)
            self.game.sound_manager.play('cris')
            self.after_damage()
        
    
# definir une cass pour la momie
            
class Mummy(Monster):

    def __init__(self, game):

        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)


# definir une classe pour l"alien
        
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 200
        self.health_max = 200
        self.set_speed(1)
        self.attack = 2
        self.set_loot_amount(40)