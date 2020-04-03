import pygame, sys, time, random

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
done = False
is_blue = True
x = 10
y = 10

check_errors = pygame.init()
objectLocationX = 20
objectLocationY = 20

snake_position = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (width//10))*10, random.randrange(1, (height//10))*10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

def game_over():
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    sys.exit()

pressed = pygame.key.get_pressed() 

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: change_to = 'UP'
            if pressed[pygame.K_DOWN]: change_to = 'DOWN'
            if pressed[pygame.K_LEFT]: change_to = 'LEFT'
            if pressed[pygame.K_RIGHT]: change_to = 'RIGHT'
            if pressed[pygame.K_ESCAPE]: pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'
    if direction == 'UP': snake_position[1] -= y
    if direction == 'DOWN': snake_position[1] += y
    if direction == 'LEFT': snake_position[0] -= x
    if direction == 'RIGHT': snake_position[0] += x

    screen.fill((0, 0, 0))

    snake_body.insert(0, list(snake_position))

    if snake_position[0] == food_pos[0] and snake_position[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10))*10, random.randrange(1, (height//10))*10]
    food_spawn = True

   

    for pos in snake_body:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos[0], pos[1], x, y))

    pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(food_pos[0], food_pos[1], x, y))

    if snake_position[0] < 0 or snake_position[0] > width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(20)