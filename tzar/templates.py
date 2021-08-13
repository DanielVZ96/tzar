import subprocess

from dataclasses import dataclass
from pathlib import Path
from string import Template
from typing import List


from click import echo

from tzar import config


@dataclass
class CLIArguments:
    filename: str
    directory: str
    verbose: bool
    forced_extension: str = ""


@dataclass
class CLITemplate:
    extensions: List[str]
    compress: str = ""
    extract: str = ""
    show: str = ""
    verbose: str = "v"

    def matches_filename(self, file_path: Path, forced_extension: str = "") -> bool:
        suffix = forced_extension or "".join(file_path.suffixes)
        if suffix == "":
            raise ValueError(
                "File contains no extension. You can force to use one by adding the `--extension=` or `-e` parameter"
            )
        return suffix in self.extensions

    def build_command(
        self, command_template, filename: str, directory: str, verbose: bool
    ) -> str:
        verbose_arg = self.verbose if verbose else ""
        template = Template(command_template)
        command = template.substitute(verbose=verbose_arg, directory=directory, filename=filename)
        echo(f"Running: {command}")
        return command

    def run_compress(self, args):
        command = self.build_command(
            self.compress, args.filename, args.directory, args.verbose
        )
        return subprocess.run(command, shell=True).returncode == 0

    def run_extract(self, args):
        command = self.build_command(
            self.extract, args.filename, args.directory, args.verbose
        )
        return subprocess.run(command, shell=True).returncode == 0

    def run_show(self, args):
        command = self.build_command(
            self.extract, args.filename, args.directory, args.verbose
        )
        return subprocess.run(command, shell=True).returncode == 0


@dataclass
class CLITemplateCollection:
    cli_templates: List[CLITemplate]

    @classmethod
    def from_config(cls: "CLITemplateCollection") -> "CLITemplateCollection":
        configs = config.read()
        return cls(
            cli_templates=[CLITemplate(**fields) for c in configs for fields in c.values()]
        )

    def get_templates(self, file_path: Path, forced_extension: str = ""):
        return [
            template
            for template in self.cli_templates
            if template.matches_filename(file_path, forced_extension=forced_extension)
        ]

    def compress(self, args: CLIArguments):
        templates = self.get_templates(
            Path(args.filename), forced_extension=args.forced_extension
        )
        for template in templates:
            if template.run_compress(args):
                echo("Archive compressed successfully!")
                return
        if len(templates) == 0:
            echo("No command found for that file extension.", err=True)
        else:
            echo("All attempts failed!", err=True)

    def extract(self, args: CLIArguments):
        templates = self.get_templates(
            Path(args.filename), forced_extension=args.forced_extension
        )
        for template in templates:
            if template.run_extract(args):
                echo("Archive extracted successfully!")
                return
        if len(templates) == 0:
            echo("No command found for that file extension.", err=True)
        else:
            echo("All attempts failed!", err=True)

    def show(self, args: CLIArguments):
        templates = self.get_templates(
            Path(args.filename), forced_extension=args.forced_extension
        )
        for template in templates:
            if template.run_show(args):
                echo("Archive listed successfully!")
                return
        if len(templates) == 0:
            echo("No command found for that file extension.", err=True)
        else:
            echo("All attempts failed!", err=True)
