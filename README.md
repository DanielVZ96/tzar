# Tzar: Tar, Zip, Anything Really

Easy compression and extraction for any compression or archival format.

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

TODO

## TODO

- [ ] Add a ton of new file formats
- [ ] Document config file
- [ ] Document code
- [ ] Interactive prompt
- [ ] Tests (Don't judge, I'm coding this in the spare time I have during my lunch breaks.)

## Authors

- [@danielvalenzuela](https://www.github.com/danielvz96)
