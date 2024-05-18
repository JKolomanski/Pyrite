from utils import *
import pygame
from sys import exit

# Clock, icon, display, caption
clock = pygame.time.Clock()
screen = pygame.display.set_mode((res_x, res_y))
screen.fill('#191919')

pygame.display.set_caption('Pyrite')
pygame.display.set_icon(pygame.image.load('assets/logo_small.png'))

toolbarWidth = 200
toolbar_surface = pygame.Surface((toolbarWidth, res_y))
toolbar_surface.fill('#272727')

canvas_background = pygame.transform.scale_by(pygame.image.load('assets/canvas_background.png'), scale)
canvas_background_rect = canvas_background.get_rect(center=(((res_x + toolbarWidth) / 2), (res_y / 2)))

logo = pygame.transform.scale_by(pygame.image.load('assets/logo_white.png'), 6)
logo_rect = canvas_background.get_rect(midtop=(100, 2))

color_text_box = text_box(x=100, y=100, w=174, h=50)

# create the list that contains the individual pixel color data
def init_grid(width, height, color):
    grid = []

    for i in range(width):
        grid.append([])
        for _ in range(height):
            grid[i].append(color)

    return grid


# draw the image and grid lines
def draw_grid(screen, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            # pygame rect class doesn't support transparency
            # instead, check the 3rd value for each pixel to determine whether to draw it
            if pixel[3] == 0:
                pass
            elif pixel[3] == 1:
                pygame.draw.rect(screen, (pixel), (j * pixel_size + canvas_background_rect.left, i * 
                                                   pixel_size + canvas_background_rect.top, pixel_size, pixel_size))

    if draw_grid_lines:
        for i in range(canvas_width):
            pygame.draw.line(screen, 'black', (canvas_background_rect.left, i * pixel_size + canvas_background_rect.top), 
                             (canvas_background_rect.right, i * pixel_size + canvas_background_rect.top))

        for j in range(canvas_height):
            pygame.draw.line(screen, 'black', (j * pixel_size + canvas_background_rect.left, canvas_background_rect.top), 
                             (j * pixel_size + canvas_background_rect.left, canvas_background_rect.bottom))


# Update all the objects on screen
def draw_screen():
    screen.blit(toolbar_surface, (0, 0))
    screen.blit(canvas_background, (canvas_background_rect))

    draw_grid(screen, grid)

    screen.blit(logo, (0, 0))

    color_text_box.draw(screen)


def get_cursor_pos(pos):
    x, y = pos
    row = (y - canvas_background_rect.top) // pixel_size + (canvas_background_rect.top // pixel_size)
    col = x // pixel_size - (canvas_background_rect.left // pixel_size)

    if row >= canvas_width or row < 0 or col >= canvas_height or col < 0:
        raise IndexError

    return row, col

grid = init_grid(canvas_width, canvas_height, (255, 255, 255, 0))

# Main program loop
while True:

    for event in pygame.event.get():
        color_text_box.handle_event(event, hex_allowed_input)
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if pygame.mouse.get_pressed()[0]:
            pos =  pygame.mouse.get_pos()

            try:
                if not len(color_text_box.text) == 6:
                    color_text_box.text = '0000'
                
                else:
                    brush_color = convert(color_text_box.text)
                    row, col = get_cursor_pos(pos)
                    grid[row][col] = (brush_color)

            except IndexError:
                pass

        if pygame.mouse.get_pressed()[2]:
            pos =  pygame.mouse.get_pos()

            try:
                row, col = get_cursor_pos(pos)
                grid[row][col] = (0, 0, 0, 0)

            except IndexError:
                pass

    draw_screen()

    pygame.display.update()
    clock.tick(framerate)

