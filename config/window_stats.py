import tcod


def get_window_constants():
    # Title for the window
    window_title = 'Roguelike Example I'
    screen_width = 80
    screen_height = 50
    run_in_full_screen = False
    # look in tcod.console_init_root for further informations
    renderer = tcod.RENDERER_SDL2
    render_order = "F"
    render_vsync = False

    # Font Setup
    font_file = 'data/fonts/consolas10x10_gs_tc.png'
    font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
    char_horiz = 0
    char_vertic = 0

    # Credit section for tcod
    credit_x_pos = 56
    credit_y_pos = 46
    credit_alpha_enabled = True

    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'run_in_full_screen': run_in_full_screen,
        'renderer': renderer,
        'render_order': render_order,
        'render_vsync': render_vsync,
        'font_file': font_file,
        'font_flags': font_flags,
        'char_horiz': char_horiz,
        'char_vertic': char_vertic,
        'credit_x_pos': credit_x_pos,
        'credit_y_pos': credit_y_pos,
        'credit_alpha_enabled': credit_alpha_enabled
    }

    return constants
