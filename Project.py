import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Add Sprites")
clock = pygame.time.Clock()

class Box(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

p1 = Box((0, 0, 255), 100, 180)
p2 = Box((255, 0, 0), 320, 180)

sprites = pygame.sprite.Group(p1, p2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p1.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        p1.rect.x += 5
    if keys[pygame.K_UP]:
        p1.rect.y -= 5
    if keys[pygame.K_DOWN]:
        p1.rect.y += 5

    screen.fill((255, 255, 255))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
