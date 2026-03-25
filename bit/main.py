import typer

from bit.character import character

app = typer.Typer()


@app.command()
def hello(name: str = typer.Option("World", help="Who to greet")) -> None:
    """Say hello to the user."""
    typer.echo(f"Hello, {name}!")


@app.command()
def char() -> None:
    """Interactive character animation."""
    character()


if __name__ == "__main__":
    app()
