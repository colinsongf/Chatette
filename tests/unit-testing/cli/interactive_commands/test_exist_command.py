"""
Test module
Tests the functionalities present in module
`chatette.cli.interactive_commands.exist_command`.
"""

from chatette.cli.interactive_commands.command_strategy import CommandStrategy
from chatette.cli.interactive_commands.exist_command import ExistCommand

from test_command_strategy import get_facade


def test_obj():
    cmd = ExistCommand("")
    assert isinstance(cmd, CommandStrategy)
    assert cmd.command_tokens == []

    cmd = ExistCommand("exist ~ /a/")
    assert isinstance(cmd, CommandStrategy)
    assert cmd.command_tokens == ["exist", "~", "/a/"]


def test_execute(capsys):
    cmd = ExistCommand('exist alias "sorry"')
    assert cmd.command_tokens == ["exist", "alias", '"sorry"']
    facade = get_facade()
    cmd.execute(facade)
    captured = capsys.readouterr()
    assert "alias: 'sorry'\nmodifiers:\n\tNone\nVariations: 0" in captured.out

    cmd = ExistCommand('exist ~ /o/g')
    assert cmd.command_tokens ==  ["exist", "~", "/o/g"]
    cmd.execute(facade)
    captured = capsys.readouterr()
    assert "alias: 'can you'\nmodifiers:\n\tNone\nVariations: 0" in captured.out
    assert "alias: 'sorry'\nmodifiers:\n\tNone\nVariations: 0" in captured.out
