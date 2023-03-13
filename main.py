import pygame
import math

# Инициализация Pygame
pygame.init()

# Определение размеров окна
screen_width = 800
screen_height = 600

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Detection Example")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Класс для треугольника
class Triangle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rotation = 0
        self.speed = 2

    def get_points(self):
        x, y = self.x, self.y
        size = self.size
        p1 = (x + size * math.cos(math.radians(self.rotation)),
              y + size * math.sin(math.radians(self.rotation)))
        p2 = (x + size * math.cos(math.radians(self.rotation + 120)),
              y + size * math.sin(math.radians(self.rotation + 120)))
        p3 = (x + size * math.cos(math.radians(self.rotation + 240)),
              y + size * math.sin(math.radians(self.rotation + 240)))
        return [p1, p2, p3]

    def draw(self, surface):
        points = self.get_points()
        pygame.draw.polygon(surface, self.color, points)

    def do_lines_intersect(self, p1, p2, p3, p4):
        # Расчет коэффициентов уравнений прямых, содержащих отрезки
        a1 = p2[1] - p1[1]
        b1 = p1[0] - p2[0]
        c1 = a1 * p1[0] + b1 * p1[1]

        a2 = p4[1] - p3[1]
        b2 = p3[0] - p4[0]
        c2 = a2 * p3[0] + b2 * p3[1]

        # Вычисление точки пересечения прямых
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return False
        else:
            x = (b2 * c1 - b1 * c2) / determinant
            y = (a1 * c2 - a2 * c1) / determinant

            # Проверка, что точка пересечения находится на отрезках
            if (min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and
                    min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]) and
                    min(p3[0], p4[0]) <= x <= max(p3[0], p4[0]) and
                    min(p3[1], p4[1]) <= y <= max(p3[1], p4[1])):
                return True
            else:
                return False

triangle1 = Triangle(200, 200, 50, blue)
triangle2 = Triangle(400, 400, 50, green)
running = True
clock = pygame.time.Clock()
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Обновление состояния треугольников
    triangle1.rotation += 1
    triangle2.rotation += 1

    # Отрисовка треугольников
    screen.fill(white)
    triangle1.draw(screen)
    triangle2.draw(screen)
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)