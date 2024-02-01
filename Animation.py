import pygame

class Animation(pygame.sprite.Sprite):

    def __init__(self, name, dimension = (200, 200)):

        super().__init__()
        self.dimension = dimension
        self.image = pygame.image.load(f'assets/{name}.png')
        self.image = pygame.transform.scale(self.image, dimension)
        self.current_image = 0 # commencer l'anim à l'image 0
        self.images = animations.get(name)
        self.animation = False

    # definition d'une methode  pour déclancher l'animation
    def start_animation(self):
        self.animation = True

    def animate(self, loop = False):

        # verifier si lanimation est active
        if self.animation:
            self.current_image += 1
            
            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # on actualise l'image à l'écran
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.dimension)
    


def load_animation_image(name):
    # on charge les 24 images de ce sprite deans le dossier correspondant
    images = []

    # on recupère le chemin du dossier de ce sprite
    path = f"assets/{name}/{name}"

    # on boucle sur chaque image dans ce dossier

    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append( pygame.image.load(image_path))

    # renvoie le contenu de la liste d'images
    return images
    
# definir un dictionnaire qui va contenir les images chargées de cahque sprite
animations = {
    'mummy': load_animation_image('mummy'),
    'player': load_animation_image('player'),
    'alien': load_animation_image('alien')
}