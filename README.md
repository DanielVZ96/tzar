# Tzar: Tar, Zip, Anything Really

Easy compression and extraction for any compression or archival format.

![Demo GIF](../assets/tzar.gif?raw=true)

## Usage/Examples

```bash
tzar compress large-dir compressed.tar.gz
tzar extract compressed.tar.gz large-dir
tzar list compressed.tar.gz
```

It's always `tzar <command> <source> [<destination>]`

## Installation

The package is published in PyPi under `tzar`. You can install it with the following methods

### [Pipx](https://pypa.github.io/pipx/) (recommended)

```bash
pipx install tzar
```

### Pip

```bash
pip3 install tzar
```

### Dev

```
git clone git@github.com:DanielVZ96/tzar
cd tzar
poetry install
export TZAR_CONFIG=$PWD/config
```

## Configuration

Configuration is read from the standard directories for each OS (~/.config/tzar/*.toml). You
 can add any number of toml files to that directory and they will all be read by tzar at runtime.
 
The configuration file has the following format:

``` toml
[command or format]
extract = "command extract ${verbose} ${filename} ${directory}" 
compress = "command compress ${verbose} ${directory} ${filename}" 
show = "command list ${verbose} ${filename}" 
extensions = [".ext1",".ext2"]
verbose = "-v" 

[another command or format]
extract = "another x${verbose} ${filename} ${directory}" 
compress = "another c${verbose} ${directory} ${filename}" 
show = "another list ${verbose} ${filename}" 
extensions = [".anoth"]
verbose = "v" 
```

All commands should have the `extract`, `compress`, `show`, `extensions` and `verbose` values defined.
They are all self explanatory; they define templates for the commands to run, the extensions
for these commands, and how you can ask for a verbose output.

They can all contain the following template variables that will be replaced at runtime:

-`verbose`: Defines how and where to ask for a verbose output (defined in the `verbose =` variable definition). 

-`filename`: The name of the compressed file. Corresponds to `<source>` in the `extract` and `list` subcommands, and to `<destination>` in the `compress` subcommand

-`directory`: The target directory. Corresponds to `<destination>` in the `extract` and `list` subcommands, and to `<source>` in the `compress` subcommand

## Why?

1) Because I think it's simpler

You may think that this should be doable with aliases, but I tried and I couldn't. Maybe you can use the [`fuck`](https://github.com/nvbn/thefuck) app 
or [`tldr`](https://github.com/tldr-pages/tldr) but I still feel it could be simpler to extract files (*wtf does xvzf even mean?*).

2) Because I wanted to try the idea of Code as Configuration

Maybe this sounds crazy, but I started this project by exploring the idea of storing the main behaviour of code in configuration files (in this case TOML), in order to 
ease extensibility, reduce posible errors, and keep things simple. In my dayjob we tried this idea with my colleagues and the result is that changes that previously
spawned several files or lines of code, are now reduced into 2 or 3 hard-to-fuck-up yaml lines. If this project gains traction I may write a blog post about this.

## TODO

- [-] Add a ton of new file formats
- [ ] Document code
- [ ] Interactive prompt
- [ ] Tests (Don't judge, I'm coding this in the spare time I have during my lunch breaks.)

## Authors

- [@danielvalenzuela](https://www.github.com/danielvz96)
