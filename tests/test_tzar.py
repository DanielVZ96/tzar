from pathlib import Path
from unittest import mock

from tzar.templates import CLITemplate


def test_matches_filename():
    matches_filename = CLITemplate(extensions=[".zip"]).matches_filename(
        Path("fake-file.1.0.0.zip")
    )
    assert matches_filename

    matches_filename = CLITemplate(
        extensions=[".tar", ".tar.gz", ".bz2", ".xz"]
    ).matches_filename(Path("fake-file.1.0.0.zip"))
    assert not matches_filename

    matches_filename = CLITemplate(
        extensions=[".tar", ".tar.gz", ".bz2", ".xz"]
    ).matches_filename(Path("fake-file.1.0.0.tar.gz"))
    assert matches_filename

    matches_filename = CLITemplate(
        extensions=[".tar", ".tar.gz", ".bz2", ".xz"]
    ).matches_filename(Path("fake-file.tar.gz"))
    assert matches_filename

    matches_filename = CLITemplate(
        extensions=[".tar", ".tar.gz", ".bz2", ".xz"]
    ).matches_filename(Path("fake-file.tar"))
    assert matches_filename


@mock.patch("os.makedirs")
def test_build_command(mock_makedirs):
    built_command = CLITemplate(
        extensions=[".tar", ".tar.gz", ".bz2", ".xz"]
    ).build_command(
        "tar xf${verbose} ${filename} -C ${directory}", "test.tar", "", False
    )
    assert built_command == "tar xf test.tar -C test"
    mock_makedirs.assert_called_with("test", exist_ok=True)

    built_command = CLITemplate(
        extensions=[".tar", ".tar.gz", ".bz2", ".xz"]
    ).build_command(
        "tar xf${verbose} ${filename} -C ${directory}", "test.tar.gz", "", False
    )
    assert built_command == "tar xf test.tar.gz -C test"
