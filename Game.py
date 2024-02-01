import pygame
from Player import Player
from Monster import Mummy
from Monster import Alien
from Comet_event import CometEvent
from Sounds import SoundManager

class Game:

    def __init__(self):
        
        # definir si notre jeu a commencer ou non
        self.is_playing = False

        # On genere notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        # On génère l'évenement de comet
        self.comet_event = CometEvent(self)

        # On definie un groupe de monstres
        self.all_monsters = pygame.sprite.Group()

        # gerer le son
        self.sound_manager = SoundManager()
        self.font = pygame.font.Font("assets/MyFont.ttf", 25)
        self.score = 0
        self.pressed = {}
    
    def add_score(self, points = 10):

        self.score += points

    def start(self):

        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):

        # remettre le jeu à neuf
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.health_max
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def update(self, screen):

        # afficher le score à l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

         # on affiche la barre de vie du joueur   
        self.player.update_health_bar(screen)

        self.player.update_animation()

        # actualiser la barre d'évenement de jeu
        self.comet_event.update_bar(screen)

        # appliquer l'ensemble des images de mon goupe de cometes
        self.comet_event.all_comets.draw(screen)

        # On recupère les projectiles du joueur un à un
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        # On recupère les monstres  de notre jeu
        for monster in  self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # On recupère les cometes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()   


        # On applique l'ensemble des images de notre groupe de projectiles
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)

        # On vérifie si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and (self.player.rect.x + self.player.rect.width) < screen.get_width():
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left() 

    def spawn_monster(self, monster_class_name):

        self.all_monsters.add(monster_class_name.__call__(self))


    def check_collision(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)