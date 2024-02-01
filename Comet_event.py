import pygame
from Comet import Comet

# On crée un classs qui va permet de gérer l'évenement comet
class CometEvent():

    # lors du chargement -> on crée un compteur
    def __init__(self, game):

        self.fall_mode = False
        self.game = game
        self.percent = 0
        self.percent_speed = 10
        self.all_comets = pygame.sprite.Group()

    def add_pourcent(self):

        self.percent += self.percent_speed / 100


    def is_full_loaded(self):

        # on verifie si la jauge est remplie
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        
        # on boucle pour générer plus d'une comete
        for i in  range(1, 10):
             self.all_comets.add(Comet(self))  

    def attempt_fall(self):

        # action à faire si la jauge est remplie

        if self.is_full_loaded() and len(self.game.all_monsters) == 0:

            self.meteor_fall()  
            self.fall_mode = True # activer l'evenement de cometes

    # definitionn de la barre
    def update_bar(self, surface):

        self.add_pourcent()

        pygame.draw.rect(surface, (0, 0, 0), [
            0, 
            surface.get_height() - 20,
            surface.get_width(),
            10 # epaisseur
        ])

        pygame.draw.rect(surface, (187, 11, 11), [
            0, 
            surface.get_height() - 20,
            (surface.get_width() / 100) * self.percent,
            10 # epaisseur
        ])