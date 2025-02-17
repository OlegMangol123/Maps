import os
import requests
import sys
import pygame
import random

pygame.init()
size = w,h = 600, 450
screen = pygame.display.set_mode(size)
url = "https://static-maps.yandex.ru/v1?"
params = {
    'apikey':"4e60121e-3e68-41f0-bd84-eced30775d1c",
    'll':f'{random.randint(-90, 90)},{random.randint(-90, 90)}',
    'z':f'{random.randint(0,21)}'
}

response = requests.get(url=url, params=params)

if not response:
    print(f"{response.status_code}, {response.reason}")
    sys.exit(1)

with open("map.png", mode="wb") as map_file:
    map_file.write(response.content)

running = True
map_im = pygame.image.load("map.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(map_im,(0, 0))
    pygame.display.flip()
os.remove("map.png")
pygame.quit()