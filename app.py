import tcod
import tcod.console
import tcod.event
from config.window_stats import get_window_constants
from modules.game.events.state import State


def main():
    constants = get_window_constants()

    tcod.console_set_custom_font(
        constants['font_file'],
        tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
    )

    tcod.console_init_root(
        constants['screen_width'],
        constants['screen_height'],
        constants['window_title'],
        constants['run_in_full_screen'],
        constants['renderer'],
        constants['render_order'],
        constants['render_vsync']
    )

    state = State()

    while not tcod.event == tcod.event.Quit:
        for event in tcod.event.get():
            tcod.console_flush()
            state.dispatch(event)


if __name__ == "__main__":
    main()
