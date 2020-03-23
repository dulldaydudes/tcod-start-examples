import tcod as libtcod


def get_window_constants():
    window_title = 'Roguelike Example I'
    screen_width = 80
    screen_height = 50
    run_in_full_screen = False
    renderer = libtcod.RENDERER_SDL2
    render_order = "F"
    render_vsync = False
    font_file = 'data/fonts/consolas10x10_gs_tc.png'

    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'font_file': font_file,
        'run_in_full_screen': run_in_full_screen,
        'renderer': renderer,
        'render_order': render_order,
        'render_vsync': render_vsync
    }

    return constants
