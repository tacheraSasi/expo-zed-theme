import json
from pathlib import Path

LIGHT_THEME_JSON = ""
DARK_THEME_JSON = ""

try:
    with open("vscode-expo-light.json", "r", encoding="utf-8") as file:
        LIGHT_THEME_JSON = file.read()
    with open("vscode-expo-dark.json", "r", encoding="utf-8") as file:
        DARK_THEME_JSON = file.read()
except FileNotFoundError:
    print("The file does not exist.")

def hex_to_rgba(hex_str, alpha=1.0):
    """Convert #rrggbb or #rrggbbaa to Zed rgba format [r, g, b, a] (0-255)"""
    hex_str = hex_str.lstrip("#")
    if len(hex_str) == 8:
        r, g, b, a = (
            int(hex_str[0:2], 16),
            int(hex_str[2:4], 16),
            int(hex_str[4:6], 16),
            int(hex_str[6:8], 16) / 255,
        )
    else:
        r, g, b = int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16)
        a = alpha
    return [r, g, b, a]


def get_color(colors, key, default="#000000"):
    v = colors.get(key)
    if v is None or v == "#00000000":
        return None
    return hex_to_rgba(v)


def map_syntax(token_colors):
    """Very rough mapping from common TextMate scopes → Zed syntax keys"""
    syntax = {}

    for rule in token_colors:
        fg = rule.get("settings", {}).get("foreground")
        if not fg:
            continue
        scopes = rule["scope"] if isinstance(rule["scope"], list) else [rule["scope"]]

        for scope in scopes:
            if "comment" in scope:
                syntax["comment"] = hex_to_rgba(fg)
            elif "keyword" in scope and "control" in scope:
                syntax["keyword"] = hex_to_rgba(fg)
            elif "keyword" in scope:
                syntax["keyword"] = hex_to_rgba(fg)
            elif "string" in scope:
                syntax["string"] = hex_to_rgba(fg)
            elif "constant.numeric" in scope or "constant.character" in scope:
                syntax["constant.numeric"] = hex_to_rgba(fg)
            elif "constant" in scope:
                syntax["constant"] = hex_to_rgba(fg)
            elif "variable" in scope and "parameter" in scope:
                syntax["variable.parameter"] = hex_to_rgba(fg)
            elif "variable" in scope:
                syntax["variable"] = hex_to_rgba(fg)
            elif "function" in scope or "entity.name.function" in scope:
                syntax["function"] = hex_to_rgba(fg)
            elif "type" in scope or "entity.name.type" in scope:
                syntax["type"] = hex_to_rgba(fg)
            elif "property" in scope or "support.type.property-name" in scope:
                syntax["property"] = hex_to_rgba(fg)
            elif "punctuation" in scope or "meta.brace" in scope:
                syntax["punctuation"] = hex_to_rgba(fg)

    # Fill missing with reasonable defaults if needed
    syntax.setdefault("comment", hex_to_rgba("#808080"))
    syntax.setdefault("keyword", hex_to_rgba("#c678dd"))
    syntax.setdefault("string", hex_to_rgba("#98c379"))
    syntax.setdefault("function", hex_to_rgba("#61afef"))
    syntax.setdefault("type", hex_to_rgba("#e5c07b"))
    syntax.setdefault("variable", hex_to_rgba("#e06c75"))
    syntax.setdefault("punctuation", hex_to_rgba("#abb2bf"))

    return syntax


def convert_to_zed(theme_json, name, appearance):
    data = json.loads(theme_json)
    colors = data["colors"]
    token_colors = data.get("tokenColors", [])

    zed = {
        "editor.background": get_color(colors, "editor.background")
        or [255, 255, 255, 255],
        "editor.foreground": get_color(colors, "editor.foreground")
        or [30, 30, 30, 255],
        "editor.line_number": get_color(colors, "editorLineNumber.foreground"),
        "editor.active_line_number": get_color(
            colors, "editorLineNumber.activeForeground"
        ),
        "editor.selection.background": get_color(colors, "editor.selectionBackground"),
        "editor.inactive_selection.background": get_color(
            colors, "editor.inactiveSelectionBackground"
        ),
        "editor.inlay_hint.background": get_color(colors, "editorInlayHint.background"),
        "editor.inlay_hint.foreground": get_color(colors, "editorInlayHint.foreground"),
        "editor.subheader.background": get_color(
            colors, "editorGroupHeader.tabsBackground"
        ),
        "editor.active_line.background": get_color(
            colors, "editor.lineHighlightBackground", 0.3
        ),
        "editor_gutter.background": get_color(colors, "editorGutter.background"),
        "terminal.background": get_color(colors, "terminal.background")
        or get_color(colors, "editor.background"),
        "terminal.foreground": get_color(colors, "terminal.foreground")
        or get_color(colors, "editor.foreground"),
        "border": get_color(colors, "panel.border")
        or get_color(colors, "sideBar.border"),
        "border.focused": get_color(colors, "panelTitle.activeBorder")
        or get_color(colors, "focusBorder"),
        "tab_bar.background": get_color(colors, "editorGroupHeader.tabsBackground"),
        "tab.active_background": get_color(colors, "tab.activeBackground"),
        "tab.inactive_background": get_color(colors, "tab.inactiveBackground"),
        "status_bar.background": get_color(colors, "statusBar.background"),
        "title_bar.background": get_color(colors, "titleBar.activeBackground"),
        "sidebar.background": get_color(colors, "sideBar.background"),
        "panel.background": get_color(colors, "panel.background"),
        "scrollbar.thumb.background": get_color(colors, "scrollbarSlider.background"),
        "scrollbar.thumb.hover_background": get_color(
            colors, "scrollbarSlider.hoverBackground"
        ),
        "syntax": map_syntax(token_colors),
    }

    # Terminal ANSI colors (fallback to defaults if missing)
    ansi_map = {
        "black": "terminal.ansiBlack",
        "red": "terminal.ansiRed",
        "green": "terminal.ansiGreen",
        "yellow": "terminal.ansiYellow",
        "blue": "terminal.ansiBlue",
        "magenta": "terminal.ansiMagenta",
        "cyan": "terminal.ansiCyan",
        "white": "terminal.ansiWhite",
        "bright_black": "terminal.ansiBrightBlack",
        "bright_red": "terminal.ansiBrightRed",
        "bright_green": "terminal.ansiBrightGreen",
        "bright_yellow": "terminal.ansiBrightYellow",
        "bright_blue": "terminal.ansiBrightBlue",
        "bright_magenta": "terminal.ansiBrightMagenta",
        "bright_cyan": "terminal.ansiBrightCyan",
        "bright_white": "terminal.ansiBrightWhite",
    }

    for zed_key, vscode_key in ansi_map.items():
        col = get_color(colors, vscode_key)
        if col:
            zed[f"terminal.{zed_key}"] = col

    # Final structure
    return {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Expo",
        "author": "Generated from VS Code Expo theme",
        "themes": [
            {
                "name": name,
                "appearance": appearance,
                "style": {k: v for k, v in zed.items() if v is not None},
            }
        ],
    }


# Convert both
light_zed = convert_to_zed(LIGHT_THEME_JSON, "Expo Light", "light")
dark_zed = convert_to_zed(DARK_THEME_JSON, "Expo Dark", "dark")

# Save to files
Path("expo-light-zed.json").write_text(json.dumps(light_zed, indent=2))
Path("expo-dark-zed.json").write_text(json.dumps(dark_zed, indent=2))

print("Created:")
print("  expo-light-zed.json")
print("  expo-dark-zed.json")
print("\nYou can now copy them to ~/.config/zed/themes/")
