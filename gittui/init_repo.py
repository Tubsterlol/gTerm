# gittui/init_repo.py
import subprocess
from pathlib import Path
import questionary
from gittui.ascii_art import load_banner
from rich.console import Console
from rich.panel import Panel

console = Console()


def init_repo():
    console.print(load_banner("init_repo"), style="bold magenta")
    # Select directory
    use_current = questionary.confirm("Initialize repo in current directory?").ask()
    if use_current:
        repo_path = Path.cwd()
    else:
        path_str = questionary.text("Enter the path for your repository:").ask()
        repo_path = Path(path_str).expanduser().resolve()
        if not repo_path.exists():
            console.print(f"[red]Error: Path '{repo_path}' does not exist[/red]")
            return

    console.print(f"Target directory: [cyan]{repo_path}[/cyan]\n")

    commands = []

    # git init
    commands.append(("git init", "Initializes a local Git repository"))

    # Add all files?
    add_files = questionary.confirm("Add all files to initial commit?").ask()
    if add_files:
        commands.append(("git add .", "Adds all files and directories to staging"))

    # Initial commit?
    do_commit = questionary.confirm("Create initial commit?").ask()
    if do_commit:
        commit_msg = questionary.text(
            "Enter commit message:", default="Initial commit"
        ).ask()
        commands.append((f'git commit -m "{commit_msg}"', "Commits staged changes"))

    # Show commands summary
    panel_content = "\n".join([f"{cmd} → {desc}" for cmd, desc in commands])
    console.print(
        Panel(panel_content, title="Commands that are going to run", expand=False)
    )

    # Final confirmation
    proceed = questionary.confirm("Run these commands?").ask()
    if not proceed:
        console.print("[yellow]Aborted by user[/yellow]")
        return

    # Run commands
    for cmd, _ in commands:
        console.print(f"[green]Running:[/green] {cmd}")
        subprocess.run(cmd, shell=True, cwd=repo_path)

    console.print("[bold green]Repository initialized successfully![/bold green]\n")
