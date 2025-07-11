from nicegui import ui
import bbq  # noqa: F401


def main():
    ui.dark_mode().enable()
    ui.run(port=6969)


if __name__ in {"__main__", "__mp_main__"}:
    main()
