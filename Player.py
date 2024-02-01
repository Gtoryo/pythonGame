import pygame
from Projectile import Projectile
import Animation

class Player(Animation.Animation):

    def __init__(self, game):

        super().__init__('player')
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 10
        self.fast = 3
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):

        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        # on dessine nos barres de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.health_max, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def lance_projectile(self):

        self.all_projectiles.add(Projectile(self))

        # on demarre l'animation
        self.start_animation()
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si le joueur n'est pas en collision avec le monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.fast

    def move_left(self):
        self.rect.x -= self.fast