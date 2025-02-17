import click

@click.group()
def main():
    pass

@main.command()
def generate():
    pass

@main.command()
def evaluate():
    pass