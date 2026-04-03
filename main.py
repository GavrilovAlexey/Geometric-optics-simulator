from numpy import array
import pygame
from simulator.engine import engine

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
pygame.display.set_caption("Geometric optics simulator")
icon = pygame.image.load("icon.ico")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
fps = 60

activated_color = array([255, 255, 255])
deactivated_color = array([155, 155, 155])
background_color = array([55, 55, 55])

def main():
    while True:
        screen.fill((0, 0, 0))
        if engine() == "exit":
            break

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
    pygame.quit()
