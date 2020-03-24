import tcod
import tcod.event


class State(tcod.event.EventDispatch):
    def ev_quit(self, event):
        # kill program
        raise SystemExit()

    # key is hit
    def ev_keydown(self, event: tcod.event.KeyDown):
        # esc key
        if event.sym == tcod.event.K_ESCAPE:
            # kill program
            raise SystemExit()
