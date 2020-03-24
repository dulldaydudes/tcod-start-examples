import tcod
import tcod.console
import tcod.event
from config.window_stats import get_window_constants
from modules.game.events.state import State


def main():
    # I don't like a bunch of var at the start of every file and/or class - so every long living var
    # well be defined within the config folder - grouped by dev who will return an list with the necessessary  values
    constants = get_window_constants()

    # FONT loading for the tile-set
    tcod.console_set_custom_font(
        constants['font_file'],
        constants['font_flags'],
        constants['char_horiz'],
        constants['char_vertic']
    )

    # main window
    console = tcod.console_init_root(
        constants['screen_width'],
        constants['screen_height'],
        constants['window_title'],
        constants['run_in_full_screen'],
        constants['renderer'],
        constants['render_order'],
        constants['render_vsync']
    )

    # Key and mouse-events handling
    state = State()
    credits_end = False

    # the main game loop
    while not tcod.event == tcod.event.Quit:
        # clear everything
        console.clear()
        # Honour to whom honour is due
        if not credits_end:
            credits_end = tcod.console_credits_render(
                constants['credit_x_pos'],
                constants['credit_y_pos'],
                constants['credit_alpha_enabled']
            )

        # Key, mouse and other events
        for event in tcod.event.get():
            state.dispatch(event)

        # bring new painted content to the front
        tcod.console_flush()


# hey ho - let's go
if __name__ == "__main__":
    main()
