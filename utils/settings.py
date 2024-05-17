import pygame

pygame.init()

res_y = 900
res_x = res_y + 200
framerate = 60

canvas_width = 16
canvas_height = 16

scale = int(canvas_width / 2 + 1)

pixel_size = 6 * scale

draw_grid_lines = False

font = pygame.font.Font('assets/spacewarfont/spacewarfont.ttf', 27)

hex_allowed_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

