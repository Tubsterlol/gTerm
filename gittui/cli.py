#!/usr/bin/env python3


from gittui.ascii_art import banner
from gittui.prompts import main_main
from rich.console import Console

console = Console()


def run():
    console.print(banner(), style="bold cyan")

    while True:
        choice = main_main()

        if choice == "Quit" or choice is None:
            console.print("Goodbye! :()", style="bold green")
            break
        else:
            console.print(f"You selected: {choice}", style="yellow")
            # git operations go here


if __name__ == "__main__":
    run()
