import pygame
import pygameMenu

import game
from algorithm import Algorithm

COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = None
player_alg = Algorithm.PLAYER
en1_alg = Algorithm.DIJKSTRA
en2_alg = Algorithm.DFS
en3_alg = Algorithm.DIJKSTRA
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)


def change_path(value, c):
    global show_path
    show_path = c


def change_player(value, c):
    global player_alg
    player_alg = c


def change_enemy1(value, c):
    global en1_alg
    en1_alg = c


def change_enemy2(value, c):
    global en2_alg
    en2_alg = c


def change_enemy3(value, c):
    global en3_alg
    en3_alg = c


def run_game():
    game.game_init(show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)


def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Bomberman')
    clock = pygame.time.Clock()

    play_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_size_title=TILE_SIZE,
                                font_color=COLOR_BLACK,
                                font_size=int(TILE_SIZE*0.8),
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_color_title=MENU_TITLE_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.7),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Play menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    play_options = pygameMenu.Menu(surface,
                                   bgfun=main_background,
                                   color_selected=COLOR_WHITE,
                                   font=pygameMenu.font.FONT_BEBAS,
                                   font_size_title=TILE_SIZE,
                                   font_color=COLOR_BLACK,
                                   font_size=int(TILE_SIZE*0.8),
                                   menu_alpha=100,
                                   menu_color=MENU_BACKGROUND_COLOR,
                                   menu_color_title=MENU_TITLE_COLOR,
                                   menu_height=int(WINDOW_SIZE[1] * 0.7),
                                   menu_width=int(WINDOW_SIZE[0] * 0.7),
                                   option_shadow=False,
                                   title='Options',
                                   window_height=WINDOW_SIZE[1],
                                   window_width=WINDOW_SIZE[0]
                                   )
    play_options.add_selector("Character 1", [("Player", Algorithm.PLAYER), ("DFS", Algorithm.DFS),
                                              ("DIJKSTRA", Algorithm.DIJKSTRA), ("None", Algorithm.NONE)], onchange=change_player)
    play_options.add_selector("Character 2", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy1)
    play_options.add_selector("Character 3", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy2,  default=1)
    play_options.add_selector("Character 4", [("DIJKSTRA", Algorithm.DIJKSTRA), ("DFS", Algorithm.DFS),
                                              ("None", Algorithm.NONE)], onchange=change_enemy3)
    play_options.add_selector("Show path", [("Yes", True), ("No", False)], onchange=change_path)

    play_options.add_option('Back', pygameMenu.events.BACK)
    play_menu.add_option('Start',
                         run_game)

    play_menu.add_option('Options', play_options)
    play_menu.add_option('Return to main menu', pygameMenu.events.BACK)

    about_menu = pygameMenu.TextMenu(surface,
                                     bgfun=main_background,
                                     color_selected=COLOR_WHITE,
                                     font=pygameMenu.font.FONT_BEBAS,
                                     font_color=COLOR_BLACK,
                                     font_size_title=TILE_SIZE,
                                     font_title=pygameMenu.font.FONT_BEBAS,
                                     menu_color=MENU_BACKGROUND_COLOR,
                                     menu_color_title=MENU_TITLE_COLOR,
                                     menu_height=int(WINDOW_SIZE[1] * 0.7),
                                     menu_width=int(WINDOW_SIZE[0] * 0.7),
                                     onclose=pygameMenu.events.DISABLE_CLOSE,
                                     option_shadow=False,
                                     text_color=COLOR_BLACK,
                                     text_fontsize=int(TILE_SIZE*0.4),
                                     title='About',
                                     window_height=WINDOW_SIZE[1],
                                     window_width=WINDOW_SIZE[0]
                                     )
    about_menu.add_line("Player_controls: ")
    about_menu.add_line("Movement:_Arrows")
    about_menu.add_line("Plant bomb:_Space")
    about_menu.add_line("Author:_Michal_Sliwa")
    about_menu.add_line("Sprite: ")

    about_menu.add_line("https://opengameart.org/content")
    about_menu.add_line("/bomb-party-the-complete-set")

    main_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_size_title=TILE_SIZE,
                                font_color=COLOR_BLACK,
                                font_size=TILE_SIZE,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_color_title=MENU_TITLE_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.6),
                                menu_width=int(WINDOW_SIZE[0] * 0.6),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Main menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    main_menu.add_option('Play', play_menu)
    main_menu.add_option('About', about_menu)
    main_menu.add_option('Quit', pygameMenu.events.EXIT)
    while True:

        clock.tick(FPS)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        main_menu.mainloop(events)

        pygame.display.flip()


menu_loop()
