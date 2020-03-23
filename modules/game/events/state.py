import tcod


class State(tcod.event.EventDispatch):
    def ev_quit(self, event):
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown):
        if event.sym == tcod.event.K_ESCAPE:
            raise SystemExit()