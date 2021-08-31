import click

from tzar.templates import CLITemplateCollection, CLIArguments


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx) if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args


@click.group(
    cls=AliasedGroup,
    epilog="Tip: You can run any subcommand by only using it's first letter(s). E.g. instead of `extract`, just `e`, `ex`, `ext`, etc.",
)
@click.version_option("0.1.4", "--version", "-V")
def cli():
    pass


@cli.command(no_args_is_help=True)
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


@cli.command(no_args_is_help=True)
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


@cli.command(no_args_is_help=True)
@click.argument("source")
@click.option("--verbose", "-v", is_flag=True, help="Print more output.")
@click.option(
    "--extension", "-e", help="Force the command to use a certain file extension."
)
def list(source, verbose, extension):
    CLITemplateCollection.from_config().show(
        CLIArguments(
            filename=source,
            verbose=verbose,
            forced_extension=extension,
        )
    )


def run():
    cli()


if __name__ == "__main__":
    run()
