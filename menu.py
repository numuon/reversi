import pygame
pygame.init()

def clickCheck (click_pos, mode, button_play_rect):
    if button_play_rect.collidepoint(click_pos): # if play is clicked
        # in_menu = False
        # in_reversi = True
        for m in mode:
            if m == 'reversi':
                mode[m] = True
            else:
                mode[m] = False
    # if button_settings_rect.collidepoint(click_pos): # if settings is clicked
    #     # in_menu = False
    #     # in_reversi = True
    #     for m in mode:
    #         if m == 'settings':
    #             mode[m] = True
    #         else:
    #             mode[m] = False
    return mode;

def menuRender(screen):
    
    """
    button_play_rect = button_play_rect.move(speed)
    if button_play_rect.left < 0 or button_play_rect.right > width:
        speed[0] = -speed[0]
    if button_play_rect.top < 0 or button_play_rect.bottom > height:
        speed[1] = -speed[1]"""

    screen.blit(button_play, button_play_rect)

    #pygame.display.flip()

    #pygame.time.delay(10) #delays by 1/100 of a second to slow down movement

button_play = pygame.image.load("button_play.png")#.convert()
button_play_rect = button_play.get_rect(center = (640,400))