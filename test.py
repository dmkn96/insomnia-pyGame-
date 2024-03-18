import pygame
import sys

# Инициализируем Pygame
pygame.init()

# Начальные размеры окна
window_size = (800, 600)

# Минимальные размеры окна
min_width, min_height = 400, 300

# Создаем окно с возможностью изменения размера
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Resizable Window with Min Size")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Проверяем, не стали ли новые размеры меньше минимальных
            new_width = max(event.w, min_width)
            new_height = max(event.h, min_height)

            # Если да, то принудительно устанавливаем минимальные размеры
            if new_width != event.w or new_height != event.h:
                screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
            else:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    screen.fill((0, 0, 0))  # Заполняем экран черным цветом
    pygame.display.flip()

pygame.quit()
sys.exit()
