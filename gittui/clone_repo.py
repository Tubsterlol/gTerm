import subprocess
from pathlib import Path
import questionary
from gittui.ascii_art import load_banner
from rich.console import Console
from rich.panel import Panel

console = Console()


def clone_repo():
    console.print(load_banner("clone_repo"), style="bold magenta")

    # Ask for repo URL
    repo_url = questionary.text("Enter the repository URL to clone:").ask()
    if not repo_url:
        console.print("[red]Error: No repository URL provided[/red]")
        return

    # Ask where to clone
    use_current = questionary.confirm("Clone repository in current directory?").ask()
    if use_current:
        repo_path = Path.cwd()
    else:
        path_str = questionary.text("Enter the target directory path:").ask()
        repo_path = Path(path_str).expanduser().resolve()
        if not repo_path.exists():
            console.print(f"[red]Error: Path '{repo_path}' does not exist[/red]")
            return

    console.print(f"Target directory: [cyan]{repo_path}[/cyan]\n")

    # Build commands list
    commands = [
        (f"git clone {repo_url}", "Clones the repository into the target directory")
    ]

    # Show commands summary
    panel_content = "\n".join([f"{cmd} → {desc}" for cmd, desc in commands])
    console.print(
        Panel(panel_content, title="Commands that are going to run", expand=False)
    )

    # Confirm
    proceed = questionary.confirm("Run these commands?").ask()
    if not proceed:
        console.print("[yellow]Aborted by user[/yellow]")
        return

    # Run command
    for cmd, _ in commands:
        console.print(f"[green]Running:[/green] {cmd}")
        subprocess.run(cmd, shell=True, cwd=repo_path)

    console.print("[bold green]Repository cloned successfully![/bold green]\n")
