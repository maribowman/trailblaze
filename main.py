from nicegui import ui
import bbq


def main():
    ui.dark_mode().enable()
    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    main()
