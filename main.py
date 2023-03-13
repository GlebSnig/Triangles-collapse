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
        self.direction = (1, 1)

    def update_position(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

        # Проверка столкновения с границами экрана
        if self.x < 0 or self.x > screen_width - self.size:
            self.direction = (-self.direction[0], self.direction[1])
        if self.y < 0 or self.y > screen_height - self.size:
            self.direction = (self.direction[0], -self.direction[1])

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

    def check_collision(self, other):
        # Проверка пересечения каждой стороны одного треугольника со сторонами другого треугольника
        for i in range(3):
            p1 = self.get_points()[i]
            p2 = self.get_points()[(i + 1) % 3]
            for j in range(3):
                p3 = other.get_points()[j]
                p4 = other.get_points()[(j + 1) % 3]
                if self.do_lines_intersect(p1, p2, p3, p4):
                    triangle1.direction = (-triangle1.direction[0], -triangle1.direction[1])
                    triangle2.direction = (-triangle2.direction[0], -triangle2.direction[1])
                    return True
        return False



triangle1 = Triangle(200, 200, 50, blue)
triangle2 = Triangle(400, 400, 50, green)
triangle1.direction = (1, 1)
triangle2.direction = (-1, -1)
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
    triangle1.update_position()
    triangle2.update_position()
    if triangle1.check_collision(triangle2):
        triangle1.color = red
        triangle2.color = red
    else:
        triangle1.color = blue
        triangle2.color = green

    # Отрисовка треугольников
    screen.fill(white)
    triangle1.draw(screen)
    triangle2.draw(screen)
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)