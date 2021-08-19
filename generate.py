import json
import enum
import dataclasses
from typing import Optional
import colors


class FontStyle(str, enum.Enum):
    bold = "bold"
    italic = "italic"
    underline = "underline"
    glow = "glow"
    stippled_underline = "stippled_underline"
    squiggly_underline = "squiggly_underline"


@dataclasses.dataclass
class Rule:
    name: str
    scope: str
    foreground: Optional[str] = None
    font_style: Optional[FontStyle] = None


@dataclasses.dataclass
class Theme:
    name: str
    variables: dict[str, str]
    globals: dict[str, str]
    rules: list[Rule]


def make_themes():
    shared_rules = [
        Rule(name="Comment", scope="comment", foreground="var(comment)", font_style=FontStyle.italic),
        Rule(name="String", scope="string", foreground="var(string)"),
        Rule(name="Constant Value", scope="constant", foreground="var(constants)"),
        Rule(name="Constant Name", scope="variable.other.constant|entity.name.constant", foreground="var(constant_name)"),
        Rule(name="Name", scope="storage", font_style=FontStyle.bold),
        Rule(name="Name modifier", scope="storage.modifier", foreground="var(modifier)"),
        Rule(name="Class", scope="entity.name.class", font_style=FontStyle.bold, foreground="var(keyword)"),
        Rule(name="Function", scope="entity.name.function", font_style=FontStyle.bold),
        Rule(name="Keyword", scope="keyword", foreground="var(foreground)", font_style=FontStyle.bold),
        Rule(name="Variable", scope="variable", foreground="var(variable)"),
        Rule(name="Variable - Parameter", scope="variable.parameter", foreground="var(parameter)"),
        Rule(name="Builtin Functions", scope="support.function", foreground="var(builtins)"),
        Rule(name="Builtin Types", scope="support.type", foreground="var(builtins)"),
        Rule(name="Magic Methods", scope="support.function.magic", foreground="var(constant_name)"),
        Rule(name="Magic Names", scope="support.variable.magic", foreground="var(builtins)"),
        Rule(name="Inherited From", scope="entity.other.inherited-class", foreground="var(inherhit_from)"),
        Rule(name="Decorators", scope="punctuation.definition.annotation", foreground="var(comment)"),
        # general markup
        Rule(name="Markup Heading", scope="markup.heading", foreground="var(constant)"),
        Rule(name="Markup Bold", scope="markup.bold", font_style=FontStyle.bold),
        Rule(name="Markup Italic", scope="markup.italic", font_style=FontStyle.italic),
        Rule(name="Markup Link", scope="markup.underline.link", foreground="var(variable)"),
        Rule(name="Markup Link Description", scope="meta.link.inline.description", foreground="var(string)"),
    ]

    shared_globals = {
        "accent": "var(accent)",
        "background": "var(background)",
        "line_highlight": "var(highlight)",
        "foreground": "var(foreground)",
        "caret": "var(foreground)",
        "selection": "var(highlight)",
        "selection_corner_style": "cut",
        "line_diff_width": "8",
        "line_diff_added": "var(git_added)",
        "line_diff_modified": "var(git_changed)",
        "line_diff_deleted": "var(git_deleted)",
        "find_highlight": "var(search_result)",
        "find_highlight_foreground": "var(foreground)",
    }

    dark_theme = Theme(
        name="tamriel - dark",
        variables={
            "accent": colors.orange[5],
            "string": colors.yellow[4],
            "keyword": colors.gray[0],
            "background": colors.dark_brown,
            "foreground": colors.gray[0],
            "constants": colors.red[7],
            "constant_name": colors.orange[6],
            "variable": colors.blue[4],
            "parameter": colors.violet[3],
            "inherhit_from": colors.green[6],
            "modifier": colors.teal[6],
            "comment": colors.gray[6],
            "builtins": colors.blue[6],
            "search_result": colors.pink[9],
            # special colors
            "git_added": colors.green[5],
            "git_deleted": colors.red[5],
            "git_changed": colors.yellow[5],
            # derived colors
            "highlight": "color(var(background) blend(var(foreground) 90%))",
        },
        globals=shared_globals,
        rules=shared_rules,
    )

    light_theme = Theme(
        name="tamriel - light",
        variables={
            "accent": colors.orange[8],
            "string": colors.yellow[9],
            "keyword": colors.gray[9],
            "background": colors.light_brown,
            "foreground": colors.gray[9],
            "constants": colors.red[9],
            "constant_name": colors.orange[8],
            "variable": colors.indigo[8],
            "parameter": colors.violet[8],
            "inherhit_from": colors.green[8],
            "modifier": colors.teal[6],
            "comment": colors.gray[6],
            "builtins": colors.blue[8],
            "search_result": colors.pink[2],
            # special colors
            "git_added": colors.green[7],
            "git_deleted": colors.red[7],
            "git_changed": colors.yellow[7],
            # derived colors
            "highlight": "color(var(background) blend(var(foreground) 90%))",
        },
        globals=shared_globals,
        rules=shared_rules,
    )

    themes_by_filename = {
        "tam-dark": dark_theme,
        "tam-light": light_theme,
    }

    for filename, theme in themes_by_filename.items():
        with open(f"{filename}.sublime-color-scheme", "w+") as fout:
            json.dump(
                dataclasses.asdict(theme),
                fout,
                indent=2,
            )


if __name__ == "__main__":
    make_themes()
