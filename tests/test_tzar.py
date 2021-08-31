from pathlib import Path

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
