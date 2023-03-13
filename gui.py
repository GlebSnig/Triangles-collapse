import main
import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from pygame_widgets.combobox import ComboBox
from threading import Thread

def acceptParams():
    global ang, tSize
    ang = 1 if cRotate.getText == "Да" else 0
    tSize = int(eSize.getText())

def task():
    thr = Thread(target=main.collapse(ang, tSize), daemon=True)
    thr.start()

pygame.init()
screen = pygame.display.set_mode((400, 350))
pygame.display.set_caption("Настройки")
screen.fill((255, 255, 255))
done = False
font = pygame.font.SysFont("Calibri", 18)

bStart = Button(screen, 250, 270, 100, 30, text="Запуск", onClick=task)
bAccept = Button(screen, 40, 270, 180, 30, text="Подтвердить параметры", onClick=acceptParams)
eSize = TextBox(screen, 40, 200, 50, 30, borderThickness=1)
lSize = font.render("Размеры треугольников", 1, (0, 0, 0))
screen.blit(lSize, (40, 170))
cRotate = ComboBox(screen, 40, 100, 80, 30, choices=("Да", "Нет"), borderThickness=1)
lRotate = font.render("Вращение треугольников (Да/Нет)", 1, (0, 0, 0))
screen.blit(lRotate, (40, 70))

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    pygame_widgets.update(events)
    pygame.display.flip()
