import typer

app = typer.Typer()


@app.command()
def hello(name: str = typer.Option("World", help="Who to greet")) -> None:
    """Say hello to the user."""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
