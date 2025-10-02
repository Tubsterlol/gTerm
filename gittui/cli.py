#!/usr/bin/env python3

from gittui.ascii_art import load_banner
from gittui.prompts import ask_action
from gittui.init_repo import init_repo
from rich.console import Console

console = Console()


def run():
    # Startup banner
    console.print(load_banner("welcome"), style="bold cyan")

    while True:
        choice = ask_action()

        if choice == "Quit" or choice is None:
            console.print("Goodbye! :(", style="bold green")
            break
        else:
            # Action banner for the chosen operation
            banner_file = ""
            if choice == "Initialize new repository":
                banner_file = "init_repo"
                init_repo()
            elif choice == "Clone a repository":
                banner_file = "clone_repo"
                # call clone function here
            elif choice == "Open existing repository":
                banner_file = "open_repo"
                # call open repo function here
            elif choice == "Git Configuration":
                banner_file = "config"
                # call config function here

            if banner_file:
                console.print(load_banner(banner_file), style="bold magenta")
