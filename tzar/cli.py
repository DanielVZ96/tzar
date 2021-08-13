import click

from tzar.templates import CLITemplateCollection, CLIArguments


@click.group()
def cli():
    pass


@cli.command()
@click.argument("source")
@click.argument("destination")
@click.option("--verbose", "-v", is_flag=True, help="Print more output.")
@click.option(
    "--extension", "-e", help="Force the command to use a certain file extension."
)
def extract(source, destination, verbose, extension):
    CLITemplateCollection.from_config().extract(
        CLIArguments(filename=source, directory=destination, verbose=verbose)
    )


@cli.command()
@click.argument("source")
@click.argument("destination")
@click.option("--verbose", "-v", is_flag=True, help="Print more output.")
@click.option(
    "--extension", "-e", help="Force the command to use a certain file extension."
)
def compress(source, destination, verbose, extension):
    CLITemplateCollection.from_config().compress(
        CLIArguments(
            filename=destination,
            directory=source,
            verbose=verbose,
            forced_extension=extension,
        )
    )


@cli.command()
@click.argument("source")
@click.option("--verbose", "-v", is_flag=True, help="Print more output.")
@click.option(
    "--extension", "-e", help="Force the command to use a certain file extension."
)
def list(source, verbose, extension):
    pass

def run():
    cli()

if __name__ == "__main__":
    run()
