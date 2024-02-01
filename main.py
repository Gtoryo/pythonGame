import pygame 
from Game import Game
import math

#  intitialisation de pygame
pygame.init()

# definir une clock pour gerer la vitesse du jeu selon le processeur
clock = pygame.time.Clock()
FPS = 60

# Generer la fenetre de notre jeu 

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720)) # ma surface 

font = pygame.image.load('assets/bg.jpg')

# importation de notre bannière

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# mise en place de notre bouton pour le lancement du jeu

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33) 
play_button_rect.y = math.ceil(screen.get_height() / 2)

game = Game()
#Maintenir notre fenetre ouverte

running = True

# La boucle de jeu

while running:

    # Ajout de l'mage à notre écran

    screen.blit(font, (0, -200))

    
    # on verifie si notre jeu a commencer ou non

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
            

    # On met à jour notre écran

    pygame.display.flip()

    # On recupere l'evenement

    for event in pygame.event.get():

        # On verifie si l'evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:

            running = False
            pygame.quit()

        # On detecte si un joueur tape sur les touches du clavier

        elif event.type == pygame.KEYDOWN: # touche enfoncée
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.lance_projectile()
                else:
                    # mettre le jeu en mode "lancé"
                    game.  start()

                    # jouer le son click
                    game.sound_manager.play('click')


        elif event.type == pygame.KEYUP: # touche realchée
            game.pressed[event.key] = False
            

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verificetion si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.  start()

                # jouer le son click
                game.sound_manager.play('click')

    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)

