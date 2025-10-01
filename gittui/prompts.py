import questionary


def main_main():
    return questionary.select(
        "Choose an action:",
        choices=[
            "Initialize new repository",
            "Clone a repository",
            "Open an exisiting repository",
            "Git Configuration",
            "Quit",
        ],
    ).ask()
