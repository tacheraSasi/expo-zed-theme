import json
from pathlib import Path

# Load your files
LIGHT_THEME_JSON = ""
DARK_THEME_JSON = ""

try:
    with open("vscode-expo-light.json", "r", encoding="utf-8") as file:
        LIGHT_THEME_JSON = file.read()
    with open("vscode-expo-dark.json", "r", encoding="utf-8") as file:
        DARK_THEME_JSON = file.read()
except FileNotFoundError:
    print("One or both files not found: vscode-expo-light.json / vscode-expo-dark.json")
    exit(1)

def hex_to_zed_color(hex_str, alpha=1.0):
    """Convert #rrggbb or #rrggbbaa → Zed-compatible hex string or null"""
    if not hex_str or hex_str == "#00000000":
        return None

    hex_str = hex_str.lstrip('#').lower()
    
    # Handle 8-digit with alpha
    if len(hex_str) == 8:
        r, g, b, a = hex_str[0:2], hex_str[2:4], hex_str[4:6], hex_str[6:8]
        # If alpha is ff → just return rgb
        if a == "ff":
            return f"#{r}{g}{b}"
        # Otherwise keep rgba (Zed supports it in some places, but safer to skip)
        return None  # or implement rgba → hex if needed

    # Standard 6-digit
    if len(hex_str) == 6:
        return f"#{hex_str}"
    
    return None  # invalid → null in Zed

def get_color(colors, key, default=None):
    v = colors.get(key)
    if v is None:
        return default
    return hex_to_zed_color(v)

def map_syntax(token_colors):
    syntax = {}
    for rule in token_colors:
        fg = rule.get("settings", {}).get("foreground")
        if not fg:
            continue
        scopes = rule["scope"] if isinstance(rule["scope"], list) else [rule["scope"]]
        for scope in scopes:
            color = hex_to_zed_color(fg)
            if not color:
                continue
            if "comment" in scope:
                syntax["comment"] = color
            elif "keyword" in scope:
                syntax["keyword"] = color
            elif "string" in scope:
                syntax["string"] = color
            elif "constant.numeric" in scope or "constant" in scope:
                syntax["constant.numeric"] = color
            elif "variable.parameter" in scope:
                syntax["variable.parameter"] = color
            elif "variable" in scope:
                syntax["variable"] = color
            elif "function" in scope or "entity.name.function" in scope:
                syntax["function"] = color
            elif "type" in scope or "entity.name.type" in scope:
                syntax["type"] = color
            elif "property" in scope:
                syntax["property"] = color
            elif "punctuation" in scope or "meta.brace" in scope:
                syntax["punctuation"] = color

    # Sensible defaults if missing
    defaults = {
        "comment": "#777B84",
        "keyword": "#9A5CD0",
        "string": "#FFCA16",
        "function": "#3B9EFF",
        "type": "#3DD68C",
        "variable": "#EDEEF0",
        "constant.numeric": "#FFCA16",
        "punctuation": "#696E77"
    }
    for k, v in defaults.items():
        syntax.setdefault(k, v)

    return syntax

def convert_to_zed(theme_json, name, appearance):
    try:
        data = json.loads(theme_json)
    except json.JSONDecodeError as e:
        print(f"JSON error in {name}: {e}")
        return None

    colors = data.get("colors", {})
    token_colors = data.get("tokenColors", [])

    zed_style = {
        "editor.background": get_color(colors, "editor.background", "#111113" if appearance == "dark" else "#ffffff"),
        "editor.foreground": get_color(colors, "editor.foreground", "#bbbbbb" if appearance == "dark" else "#333333"),
        "editor.line_number": get_color(colors, "editorLineNumber.foreground"),
        "editor.active_line_number": get_color(colors, "editorLineNumber.activeForeground"),
        "editor.selection.background": get_color(colors, "editor.selectionBackground"),
        "editor.subheader.background": get_color(colors, "editorGroupHeader.tabsBackground"),
        "editor_gutter.background": get_color(colors, "editorGutter.background"),
        "terminal.background": get_color(colors, "terminal.background"),
        "terminal.foreground": get_color(colors, "terminal.foreground"),
        "border": get_color(colors, "panel.border") or get_color(colors, "sideBar.border"),
        "border.focused": get_color(colors, "panelTitle.activeBorder") or get_color(colors, "focusBorder"),
        "tab_bar.background": get_color(colors, "editorGroupHeader.tabsBackground"),
        "tab.active_background": get_color(colors, "tab.activeBackground"),
        "tab.inactive_background": get_color(colors, "tab.inactiveBackground"),
        "status_bar.background": get_color(colors, "statusBar.background"),
        "title_bar.background": get_color(colors, "titleBar.activeBackground"),
        "sidebar.background": get_color(colors, "sideBar.background"),
        "panel.background": get_color(colors, "panel.background"),
        "scrollbar.thumb.background": get_color(colors, "scrollbarSlider.background"),
        "scrollbar.thumb.hover_background": get_color(colors, "scrollbarSlider.hoverBackground"),
        "syntax": map_syntax(token_colors),
    }

    # Add some terminal ANSI colors if present
    ansi_keys = {
        "terminal.black": "terminal.ansiBlack",
        "terminal.red": "terminal.ansiRed",
        "terminal.green": "terminal.ansiGreen",
        "terminal.yellow": "terminal.ansiYellow",
        "terminal.blue": "terminal.ansiBlue",
        "terminal.magenta": "terminal.ansiMagenta",
        "terminal.cyan": "terminal.ansiCyan",
        "terminal.white": "terminal.ansiWhite",
        "terminal.bright_black": "terminal.ansiBrightBlack",
        "terminal.bright_red": "terminal.ansiBrightRed",
        # ... add more if you want
    }

    for zkey, vkey in ansi_keys.items():
        col = get_color(colors, vkey)
        if col:
            zed_style[zkey] = col

    return {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Expo",
        "author": "Generated from VS Code Expo theme",
        "themes": [
            {
                "name": name,
                "appearance": appearance,
                "style": {k: v for k, v in zed_style.items() if v is not None}
            }
        ]
    }

# Convert and save
light_theme = convert_to_zed(LIGHT_THEME_JSON, "Expo Light", "light")
dark_theme  = convert_to_zed(DARK_THEME_JSON,  "Expo Dark",  "dark")

if light_theme:
    Path("expo-light-zed.json").write_text(json.dumps(light_theme, indent=2))
    print("Created: expo-light-zed.json")

if dark_theme:
    Path("expo-dark-zed.json").write_text(json.dumps(dark_theme, indent=2))
    print("Created: expo-dark-zed.json")

print("\nDone. Copy them to ~/.config/zed/themes/")