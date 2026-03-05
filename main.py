import json
from pathlib import Path

# ----------------------------------------------------------------------
# Your VS Code theme data (embedded directly)
# ----------------------------------------------------------------------
DARK_THEME_JSON = """{
  "$schema": "vscode://schemas/color-theme",
  "type": "dark",
  "colors": {
    "activityBar.activeBackground": "#18191b",
    "activityBar.background": "#0c0d0e",
    "activityBar.border": "#111113",
    "activityBar.foreground": "#b0b4ba",
    "activityBarBadge.background": "#0090ff",
    "badge.background": "#004074",
    "breadcrumb.background": "#18191b",
    "button.background": "#2870bd",
    "dropdown.background": "#111113",
    "editor.background": "#111113",
    "editor.selectionBackground": "#2e3135",
    "editor.selectionHighlightBackground": "#2e3135",
    "editor.wordHighlightBackground": "#2e3135",
    "editorBracketHighlight.foreground1": "#696e77",
    "editorBracketHighlight.foreground2": "#696e77",
    "editorBracketHighlight.foreground3": "#696e77",
    "editorBracketHighlight.foreground4": "#696e77",
    "editorBracketHighlight.foreground5": "#696e77",
    "editorBracketHighlight.foreground6": "#696e77",
    "editorBracketHighlight.unexpectedBracket.foreground": "#696e77",
    "editorCodeLens.foreground": "#b0b4ba",
    "editorGroup.border": "#363a3f",
    "editorGroupHeader.tabsBackground": "#0c0d0e",
    "editorGutter.foldingControlForeground": "#777b84",
    "editorLineNumber.foreground": "#696e77",
    "editorWidget.background": "#111113",
    "focusBorder": "#00000000",
    "input.background": "#18191b",
    "inputOption.activeBackground": "#0d2847",
    "inputOption.activeForeground": "#70b8ff",
    "list.activeSelectionBackground": "#212225",
    "list.focusBackground": "#2e3135",
    "list.focusOutline": "#00000000",
    "list.hoverBackground": "#272a2d",
    "list.inactiveSelectionBackground": "#18191b",
    "menu.background": "#111113",
    "menu.border": "#212225",
    "menu.separatorBackground": "#212225",
    "panel.background": "#0c0d0e",
    "panel.border": "#212225",
    "panelTitle.activeBorder": "#70b8ff",
    "peekView.border": "#43484e",
    "peekViewEditor.background": "#18191b",
    "peekViewResult.background": "#111113",
    "peekViewResult.lineForeground": "#777b84",
    "peekViewResult.matchHighlightBackground": "#003362",
    "peekViewResult.selectionBackground": "#2e3135",
    "peekViewTitleDescription.foreground": "#777b84",
    "pickerGroup.border": "#363a3f",
    "pickerGroup.foreground": "#777b84",
    "sash.hoverBorder": "#363a3f",
    "scrollbar.shadow": "#0c0d0e",
    "scrollbarSlider.activeBackground": "#2e3135",
    "scrollbarSlider.background": "#212225",
    "scrollbarSlider.hoverBackground": "#272a2d",
    "settings.checkboxBackground": "#0c0d0e",
    "settings.checkboxBorder": "#363a3f",
    "settings.dropdownBackground": "#0c0d0e",
    "settings.dropdownBorder": "#363a3f",
    "settings.modifiedItemIndicator": "#2870bd",
    "settings.numberInputBackground": "#0c0d0e",
    "settings.numberInputBorder": "#363a3f",
    "settings.sashBorder": "#363a3f",
    "settings.textInputBackground": "#0c0d0e",
    "settings.textInputBorder": "#363a3f",
    "sideBar.background": "#0c0d0e",
    "sideBar.border": "#212225",
    "sideBarSectionHeader.background": "#0c0d0e",
    "sideBarSectionHeader.border": "#111113",
    "sideBarTitle.foreground": "#777b84",
    "statusBar.background": "#0c0d0e",
    "statusBar.border": "#212225",
    "statusBar.debuggingBackground": "#a35829",
    "statusBar.noFolderBackground": "#8457aa",
    "statusBarItem.remoteBackground": "#2870bd",
    "tab.activeBackground": "#18191b",
    "tab.border": "#111113",
    "tab.inactiveBackground": "#0c0d0e",
    "titleBar.activeBackground": "#0c0d0e",
    "titleBar.border": "#111113",
    "titleBar.inactiveBackground": "#0c0d0e",
    "tree.indentGuidesStroke": "#363a3f"
  },
  "tokenColors": [
    { "scope": "comment.line", "settings": { "foreground": "#777B84" } },
    { "scope": "comment.block", "settings": { "foreground": "#777B84" } },
    { "scope": "constant.numeric", "settings": { "foreground": "#FFCA16" } },
    { "scope": "constant.language", "settings": { "foreground": "#DE51A8" } },
    { "scope": "constant.other.variable", "settings": { "foreground": "#3DD68C" } },
    { "scope": "editorBracketMatch.border", "settings": { "foreground": "#696E77" } },
    { "scope": "entity.name.tag", "settings": { "foreground": "#F76B15" } },
    { "scope": "entity.name.type", "settings": { "foreground": "#3DD68C" } },
    { "scope": "entity.name.type.class", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "entity.name.type.module", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "entity.other", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "entity.other.attribute-name", "settings": { "foreground": "#E5484D" } },
    { "scope": "entity.scope.name", "settings": { "foreground": "#0090FF" } },
    { "scope": "keyword.control", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "keyword.control.flow", "settings": { "foreground": "#DE51A8" } },
    { "scope": "keyword.control.new", "settings": { "foreground": "#E5484D" } },
    { "scope": "keyword.other", "settings": { "foreground": "#DE51A8" } },
    { "scope": "keyword.operator", "settings": { "foreground": "#777B84" } },
    { "scope": "keyword.operator.assignment", "settings": { "foreground": "#696E77" } },
    { "scope": "keyword.operator.expression", "settings": { "foreground": "#F76B15" } },
    { "scope": "keyword.operator.logical", "settings": { "foreground": "#777B84" } },
    { "scope": "keyword.operator.rest", "settings": { "foreground": "#696E77" } },
    { "scope": "keyword.operator.spread", "settings": { "foreground": "#696E77" } },
    { "scope": "keyword.operator.type.annotation", "settings": { "foreground": "#696E77" } },
    { "scope": "keyword.operator.ternary", "settings": { "foreground": "#777B84" } },
    { "scope": "keyword.operator.new", "settings": { "foreground": "#E5484D" } },
    { "scope": "meta.brace", "settings": { "foreground": "#696E77" } },
    { "scope": "meta.definition.variable", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "meta.definition.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "meta.definition.method", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "meta.definition.property", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "meta.function-call", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "meta.import", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "meta.object-literal.key", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "punctuation.accessor", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.bracket", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.definition", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.definition.annotation", "settings": { "foreground": "#FFCA16" } },
    { "scope": "punctuation.definition.block", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.definition.parameters", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.definition.string", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.section", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.separator", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.separator.dot-access", "settings": { "foreground": "#696E77" } },
    { "scope": "punctuation.terminator.statement", "settings": { "foreground": "#696E77" } },
    { "scope": "storage.modifier", "settings": { "foreground": "#E5484D" } },
    { "scope": "storage.modifier.import", "settings": { "foreground": "#B0B4BA" } },
    { "scope": "storage.type", "settings": { "foreground": "#DE51A8" } },
    { "scope": "storage.type.annotation", "settings": { "foreground": "#FFCA16" } },
    { "scope": "storage.type.generic", "settings": { "foreground": "#0090FF" } },
    { "scope": "storage.type.function.arrow", "settings": { "foreground": "#696E77" } },
    { "scope": "string.quoted", "settings": { "foreground": "#FFCA16" } },
    { "scope": "string.template", "settings": { "foreground": "#FFCA16" } },
    { "scope": "support.type.primitive", "settings": { "foreground": "#F76B15" } },
    { "scope": "support.type.property-name", "settings": { "foreground": "#F76B15" } },
    { "scope": "support.type.builtin", "settings": { "foreground": "#DE51A8" } },
    { "scope": "variable.object.property", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "variable.other", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "variable.other.constant", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "variable.other.macro.argument", "settings": { "foreground": "#DE51A8" } },
    { "scope": "variable.parameter.probably", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "variable.language", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.java entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.java keyword.control.new", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.java storage.modifier", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.java storage.modifier.extends", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.java storage.modifier.implements", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.java storage.type", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.java storage.type.primitive", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.java storage.type.generic", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.java punctuation.terminator", "settings": { "foreground": "#777B84" } },
    { "scope": "source.kotlin keyword.control.new", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.kotlin storage.modifier", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.kotlin variable.parameter.function", "settings": { "foreground": "#FFCA16" } },
    { "scope": "source.kotlin entity.other.inherited-class", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "source.kotlin punctuation.seperator", "settings": { "foreground": "#777B84" } },
    { "scope": "text.html.markdown fenced_code.block.language", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "text.html.markdown markup.bold", "settings": { "foreground": "#DE51A8" } },
    { "scope": "text.html.markdown markup.italic", "settings": { "foreground": "#3DD68C" } },
    { "scope": "text.html.markdown markup.strikethrough", "settings": { "foreground": "#E5484D" } },
    { "scope": "text.html.markdown markup.inline.raw.string", "settings": { "foreground": "#FFCA16" } },
    { "scope": "text.html.markdown markup.underline.link", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "text.html.markdown meta.paragraph", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "text.html.markdown punctuation.definition.heading", "settings": { "foreground": "#0090FF" } },
    { "scope": "text.html.markdown string.other.link.title", "settings": { "foreground": "#3DD68C" } },
    { "scope": "text.html.markdown meta.separator", "settings": { "foreground": "#777B84" } },
    { "scope": "source.mdx meta.paragraph", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "source.mdx punctuation.definition.heading", "settings": { "foreground": "#0090FF" } },
    { "scope": "source.mdx string.other.begin.code.fenced", "settings": { "foreground": "#777B84" } },
    { "scope": "source.mdx string.other.end.code.fenced", "settings": { "foreground": "#777B84" } },
    { "scope": "source.mdx variable.ordered.list", "settings": { "foreground": "#777B84" } },
    { "scope": "source.mdx variable.unordered.list", "settings": { "foreground": "#777B84" } },
    { "scope": "source.mdx markup.code", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "source.mdx string.other.number", "settings": { "foreground": "#777B84" } },
    { "scope": "source.mdx meta.separator", "settings": { "foreground": "#777B84" } },
    { "scope": "source.mdx support.class.component", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.objc entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.objc entity.name.function.preprocessor", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.objc keyword.other.property.attribute", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.objc meta.bracketed", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.objc meta.function-call", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "source.objc storage.type", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.objc support.class.cocoa", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.objc support.other.protocol", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.ruby constant.other.symbol.hashkey", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.ruby entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.ruby support.class", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.ruby variable.parameter.function", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.shell entity.name.command", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.shell support.function.builtin", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.swift entity.name.type", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.swift support.function.any-method", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.swift keyword.control.new", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.swift meta.parameter-clause", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.swift meta.function-call", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "source.swift entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.swift meta.definition.function.body", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "source.swift meta.definition.type.body", "settings": { "foreground": "#EDEEF0" } },
    { "scope": "source.swift meta.inheritance-clause", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.swift punctuation.definition.attribute", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.swift storage.modifier", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.swift support.type", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.swift support.function", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "source.swift variable.parameter.function", "settings": { "foreground": "#FFCA16" } },
    { "scope": "source.swift meta.function-result", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.swift variable.language.generic-parameter", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.ts punctuation.definition.block.tag.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.ts storage.type.class.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.tsx punctuation.definition.block.tag.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.tsx storage.type.class.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "text.xml entity.other.attribute-name.localname", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.gdscript constant.language", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.gdscript entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.gdscript entity.name.type.class", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.gdscript entity.other.inherited-class", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.gdscript keyword.language", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.gdscript keyword.control", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.gdscript support.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.gdscript variable.parameter.function", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.dart entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.dart keyword.declaration", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.dart punctuation", "settings": { "foreground": "#777B84" } },
    { "scope": "source.dart other.source", "settings": { "foreground": "#777B84" } },
    { "scope": "source.dart string.interpolated", "settings": { "foreground": "#FFCA16" } },
    { "scope": "source.dart string.quoted", "settings": { "foreground": "#FFCA16" } },
    { "scope": "source.dart string.template", "settings": { "foreground": "#FFCA16" } },
    { "scope": "source.dart support.class", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.dart variable.parameter", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.dart storage.modifier", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.dart storage.type.annotation", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.dart meta.embedded.expression", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.cs keyword.type", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.cs keyword.type.void", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.cs entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.cs variable.other.object.property", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "source.cs punctuation", "settings": { "foreground": "#777B84" } },
    { "scope": "source.diff meta.diff.header", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.diff meta.diff.header.from-file", "settings": { "foreground": "#EC5D5E", "background": "#201314" } },
    { "scope": "source.diff meta.diff.header.from-file punctuation.definition", "settings": { "foreground": "#8C333A" } },
    { "scope": "source.diff meta.diff.header.to-file", "settings": { "foreground": "#3DD68C", "background": "#121B17" } },
    { "scope": "source.diff meta.diff.header.to-file punctuation.definition", "settings": { "foreground": "#28684A" } },
    { "scope": "source.diff meta.diff.range", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "source.diff markup.inserted.diff", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.diff markup.deleted.diff", "settings": { "foreground": "#EC5D5E" } },
    { "scope": "source.diff punctuation.definition.inserted.diff", "settings": { "foreground": "#28684A" } },
    { "scope": "source.diff punctuation.definition.deleted.diff", "settings": { "foreground": "#8C333A" } },
    { "scope": "source.diff punctuation.definition.range.diff", "settings": { "foreground": "#8457AA" } },
    { "scope": "source.rust entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.rust keyword.control.flow", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.rust entity.name.namespace", "settings": { "foreground": "#FF801F" } },
    { "scope": "source.rust meta.attribute.rust", "settings": { "foreground": "#E5484D" } },
    { "scope": "source.rust punctuation", "settings": { "foreground": "#777B84" } },
    { "scope": "source.zig entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.zig keyword.control.flow", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.zig keyword.default", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.zig keyword.structure", "settings": { "foreground": "#DE51A8" } },
    { "scope": "source.zig keyword.storage", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "source.zig keyword.type", "settings": { "foreground": "#9A5CD0" } },
    { "scope": "source.zig keyword.type.c", "settings": { "foreground": "#3DD68C" } },
    { "scope": "source.zig support.function.builtin.zig", "settings": { "foreground": "#FF801F" } },
    { "scope": "source.zig punctuation", "settings": { "foreground": "#777B84" } },
    { "scope": "token.info-token", "settings": { "foreground": "#6796E6" } },
    { "scope": "token.warn-token", "settings": { "foreground": "#CD9731" } },
    { "scope": "token.error-token", "settings": { "foreground": "#F44747" } },
    { "scope": "token.debug-token", "settings": { "foreground": "#B267E6" } }
  ]
}"""

LIGHT_THEME_JSON = """{
  "$schema": "vscode://schemas/color-theme",
  "type": "light",
  "colors": {
    "activityBar.activeBackground": "#e0e1e6",
    "activityBar.background": "#f9f9fb",
    "activityBar.border": "#d9d9e0",
    "activityBar.foreground": "#60646c",
    "activityBarBadge.background": "#0090ff",
    "badge.background": "#205d9e",
    "badge.foreground": "#ffffff",
    "breadcrumb.background": "#fcfcfd",
    "button.background": "#0588f0",
    "editor.background": "#ffffff",
    "editor.selectionBackground": "#cdced6",
    "editor.selectionHighlightBackground": "#cdced6",
    "editor.wordHighlightBackground": "#cdced6",
    "editorBracketHighlight.foreground1": "#8b8d98",
    "editorBracketHighlight.foreground2": "#8b8d98",
    "editorBracketHighlight.foreground3": "#8b8d98",
    "editorBracketHighlight.foreground4": "#8b8d98",
    "editorBracketHighlight.foreground5": "#8b8d98",
    "editorBracketHighlight.foreground6": "#8b8d98",
    "editorBracketHighlight.unexpectedBracket.foreground": "#8b8d98",
    "editorGroup.border": "#d9d9e0",
    "editorGroupHeader.border": "#f0f0f3",
    "editorGroupHeader.tabsBackground": "#f0f0f3",
    "editorGutter.foldingControlForeground": "#80838d",
    "editorLineNumber.foreground": "#8b8d98",
    "editorWidget.background": "#ffffff",
    "focusBorder": "#00000000",
    "input.background": "#f0f0f3",
    "inputOption.activeBackground": "#e6f4fe",
    "inputOption.activeForeground": "#0d74ce",
    "list.activeSelectionBackground": "#e0e1e6",
    "list.activeSelectionForeground": "#1c2024",
    "list.focusBackground": "#e0e1e6",
    "list.focusOutline": "#00000000",
    "list.hoverBackground": "#e8e8ec",
    "list.inactiveSelectionBackground": "#f0f0f3",
    "menu.background": "#ffffff",
    "menu.border": "#e8e8ec",
    "menu.separatorBackground": "#e8e8ec",
    "panel.background": "#fcfcfd",
    "panel.border": "#d9d9e0",
    "panelTitle.activeBorder": "#0588f0",
    "peekView.border": "#cdced6",
    "peekViewEditor.background": "#f9f9fb",
    "peekViewResult.background": "#ffffff",
    "peekViewResult.lineForeground": "#80838d",
    "peekViewResult.matchHighlightBackground": "#d5efff",
    "peekViewResult.selectionBackground": "#e0e1e6",
    "peekViewTitleDescription.foreground": "#80838d",
    "pickerGroup.border": "#d9d9e0",
    "pickerGroup.foreground": "#80838d",
    "sash.hoverBorder": "#d9d9e0",
    "scrollbarSlider.activeBackground": "#cdced6",
    "scrollbarSlider.background": "#e8e8ec",
    "scrollbarSlider.hoverBackground": "#e0e1e6",
    "settings.checkboxBackground": "#ffffff",
    "settings.checkboxBorder": "#d9d9e0",
    "settings.dropdownBackground": "#ffffff",
    "settings.dropdownBorder": "#d9d9e0",
    "settings.modifiedItemIndicator": "#0588f0",
    "settings.numberInputBackground": "#ffffff",
    "settings.numberInputBorder": "#d9d9e0",
    "settings.sashBorder": "#d9d9e0",
    "settings.textInputBackground": "#ffffff",
    "settings.textInputBorder": "#d9d9e0",
    "sideBar.background": "#fcfcfd",
    "sideBar.border": "#d9d9e0",
    "sideBar.foreground": "#60646c",
    "sideBarSectionHeader.background": "#fcfcfd",
    "sideBarSectionHeader.border": "#ffffff",
    "sideBarTitle.foreground": "#80838d",
    "statusBar.background": "#fcfcfd",
    "statusBar.border": "#cdced6",
    "statusBar.debuggingBackground": "#ec9455",
    "statusBar.debuggingBorder": "#ec9455",
    "statusBar.debuggingForeground": "#ffffff",
    "statusBar.foreground": "#60646c",
    "statusBar.noFolderBackground": "#be93e4",
    "statusBar.noFolderBorder": "#be93e4",
    "statusBar.noFolderForeground": "#ffffff",
    "statusBarItem.remoteBackground": "#0588f0",
    "tab.activeBackground": "#fcfcfd",
    "tab.border": "#e8e8ec",
    "tab.inactiveBackground": "#f0f0f3",
    "titleBar.activeBackground": "#f0f0f3",
    "titleBar.border": "#d9d9e0",
    "titleBar.inactiveBackground": "#f0f0f3",
    "tree.indentGuidesStroke": "#d9d9e0"
  },
  "tokenColors": [
    { "scope": "comment.line", "settings": { "foreground": "#80838D" } },
    { "scope": "comment.block", "settings": { "foreground": "#80838D" } },
    { "scope": "constant.numeric", "settings": { "foreground": "#AB6400" } },
    { "scope": "constant.language", "settings": { "foreground": "#CF3897" } },
    { "scope": "constant.other.variable", "settings": { "foreground": "#2B9A66" } },
    { "scope": "editorBracketMatch.border", "settings": { "foreground": "#8B8D98" } },
    { "scope": "entity.name.tag", "settings": { "foreground": "#F76B15" } },
    { "scope": "entity.name.type", "settings": { "foreground": "#2B9A66" } },
    { "scope": "entity.name.type.class", "settings": { "foreground": "#0588F0" } },
    { "scope": "entity.name.type.module", "settings": { "foreground": "#0588F0" } },
    { "scope": "entity.other", "settings": { "foreground": "#0588F0" } },
    { "scope": "entity.other.attribute-name", "settings": { "foreground": "#DC3E42" } },
    { "scope": "entity.scope.name", "settings": { "foreground": "#0588F0" } },
    { "scope": "keyword.control", "settings": { "foreground": "#8145B5" } },
    { "scope": "keyword.control.flow", "settings": { "foreground": "#CF3897" } },
    { "scope": "keyword.control.new", "settings": { "foreground": "#E5484D" } },
    { "scope": "keyword.other", "settings": { "foreground": "#CF3897" } },
    { "scope": "keyword.operator", "settings": { "foreground": "#80838D" } },
    { "scope": "keyword.operator.assignment", "settings": { "foreground": "#8B8D98" } },
    { "scope": "keyword.operator.expression", "settings": { "foreground": "#F76B15" } },
    { "scope": "keyword.operator.logical", "settings": { "foreground": "#80838D" } },
    { "scope": "keyword.operator.rest", "settings": { "foreground": "#8B8D98" } },
    { "scope": "keyword.operator.spread", "settings": { "foreground": "#8B8D98" } },
    { "scope": "keyword.operator.type.annotation", "settings": { "foreground": "#8B8D98" } },
    { "scope": "keyword.operator.ternary", "settings": { "foreground": "#80838D" } },
    { "scope": "keyword.operator.new", "settings": { "foreground": "#E5484D" } },
    { "scope": "meta.brace", "settings": { "foreground": "#8B8D98" } },
    { "scope": "meta.definition.variable", "settings": { "foreground": "#1C2024" } },
    { "scope": "meta.definition.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "meta.definition.method", "settings": { "foreground": "#0588F0" } },
    { "scope": "meta.definition.property", "settings": { "foreground": "#0588F0" } },
    { "scope": "meta.function-call", "settings": { "foreground": "#8145B5" } },
    { "scope": "meta.import", "settings": { "foreground": "#1C2024" } },
    { "scope": "meta.object-literal.key", "settings": { "foreground": "#1C2024" } },
    { "scope": "punctuation.accessor", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.bracket", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.definition", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.definition.annotation", "settings": { "foreground": "#AB6400" } },
    { "scope": "punctuation.definition.block", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.definition.parameters", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.definition.string", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.section", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.separator", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.separator.dot-access", "settings": { "foreground": "#8B8D98" } },
    { "scope": "punctuation.terminator.statement", "settings": { "foreground": "#8B8D98" } },
    { "scope": "storage.modifier", "settings": { "foreground": "#DC3E42" } },
    { "scope": "storage.modifier.import", "settings": { "foreground": "#60646C" } },
    { "scope": "storage.type", "settings": { "foreground": "#CF3897" } },
    { "scope": "storage.type.annotation", "settings": { "foreground": "#AB6400" } },
    { "scope": "storage.type.generic", "settings": { "foreground": "#0588F0" } },
    { "scope": "storage.type.function.arrow", "settings": { "foreground": "#8B8D98" } },
    { "scope": "string.quoted", "settings": { "foreground": "#C07F00" } },
    { "scope": "string.template", "settings": { "foreground": "#C07F00" } },
    { "scope": "support.type.primitive", "settings": { "foreground": "#F76B15" } },
    { "scope": "support.type.property-name", "settings": { "foreground": "#F76B15" } },
    { "scope": "support.type.builtin", "settings": { "foreground": "#CF3897" } },
    { "scope": "variable.object.property", "settings": { "foreground": "#1C2024" } },
    { "scope": "variable.other", "settings": { "foreground": "#1C2024" } },
    { "scope": "variable.other.constant", "settings": { "foreground": "#0588F0" } },
    { "scope": "variable.other.macro.argument", "settings": { "foreground": "#CF3897" } },
    { "scope": "variable.parameter.probably", "settings": { "foreground": "#0588F0" } },
    { "scope": "variable.language", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.java entity.name.function", "settings": { "foreground": "#3B9EFF" } },
    { "scope": "source.java keyword.control.new", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.java storage.modifier", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.java storage.modifier.extends", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.java storage.modifier.implements", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.java storage.type", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.java storage.type.primitive", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.java storage.type.generic", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.java punctuation.terminator", "settings": { "foreground": "#80838D" } },
    { "scope": "source.kotlin keyword.control.new", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.kotlin storage.modifier", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.kotlin variable.parameter.function", "settings": { "foreground": "#AB6400" } },
    { "scope": "source.kotlin entity.other.inherited-class", "settings": { "foreground": "#8145B5" } },
    { "scope": "source.kotlin punctuation.seperator", "settings": { "foreground": "#80838D" } },
    { "scope": "text.html.markdown fenced_code.block.language", "settings": { "foreground": "#8145B5" } },
    { "scope": "text.html.markdown markup.bold", "settings": { "foreground": "#CF3897" } },
    { "scope": "text.html.markdown markup.italic", "settings": { "foreground": "#2B9A66" } },
    { "scope": "text.html.markdown markup.strikethrough", "settings": { "foreground": "#DC3E42" } },
    { "scope": "text.html.markdown markup.inline.raw.string", "settings": { "foreground": "#AB6400" } },
    { "scope": "text.html.markdown markup.underline.link", "settings": { "foreground": "#0588F0" } },
    { "scope": "text.html.markdown meta.paragraph", "settings": { "foreground": "#1C2024" } },
    { "scope": "text.html.markdown punctuation.definition.heading.markdown", "settings": { "foreground": "#0588F0" } },
    { "scope": "text.html.markdown string.other.link.title", "settings": { "foreground": "#2B9A66" } },
    { "scope": "text.html.markdown meta.separator", "settings": { "foreground": "#80838D" } },
    { "scope": "source.mdx meta.paragraph", "settings": { "foreground": "#1C2024" } },
    { "scope": "source.mdx punctuation.definition.heading", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.mdx string.other.begin.code.fenced", "settings": { "foreground": "#80838D" } },
    { "scope": "source.mdx string.other.end.code.fenced", "settings": { "foreground": "#80838D" } },
    { "scope": "source.mdx variable.ordered.list", "settings": { "foreground": "#80838D" } },
    { "scope": "source.mdx variable.unordered.list", "settings": { "foreground": "#80838D" } },
    { "scope": "source.mdx markup.code", "settings": { "foreground": "#8145B5" } },
    { "scope": "source.mdx string.other.number", "settings": { "foreground": "#80838D" } },
    { "scope": "source.mdx meta.separator", "settings": { "foreground": "#80838D" } },
    { "scope": "source.mdx support.class.component", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.objc entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.objc entity.name.function.preprocessor", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.objc keyword.other.property.attribute", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.objc meta.bracketed", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.objc meta.function-call", "settings": { "foreground": "#1C2024" } },
    { "scope": "source.objc storage.type", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.objc support.class.cocoa", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.objc support.other.protocol", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.ruby constant.other.symbol.hashkey", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.ruby entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.ruby support.class", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.ruby variable.parameter.function", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.shell entity.name.command", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.shell support.function.builtin", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.swift entity.name.type", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.swift support.function.any-method", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.swift keyword.control.new", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.swift meta.parameter-clause", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.swift meta.function-call", "settings": { "foreground": "#1C2024" } },
    { "scope": "source.swift entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.swift meta.definition.function.body", "settings": { "foreground": "#1C2024" } },
    { "scope": "source.swift meta.definition.type.body", "settings": { "foreground": "#1C2024" } },
    { "scope": "source.swift meta.inheritance-clause", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.swift punctuation.definition.attribute", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.swift storage.modifier", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.swift support.type", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.swift support.function", "settings": { "foreground": "#8145B5" } },
    { "scope": "source.swift variable.parameter.function", "settings": { "foreground": "#AB6400" } },
    { "scope": "source.ts punctuation.definition.block.tag.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.ts storage.type.class.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.tsx punctuation.definition.block.tag.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.tsx storage.type.class.jsdoc", "settings": { "foreground": "#F76B15" } },
    { "scope": "text.xml entity.other.attribute-name.localname", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.gdscript constant.language", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.gdscript entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.gdscript entity.name.type.class", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.gdscript entity.other.inherited-class", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.gdscript keyword.language", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.gdscript keyword.control", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.gdscript support.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.gdscript variable.parameter.function", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.dart entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.dart keyword.declaration", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.dart punctuation", "settings": { "foreground": "#80838D" } },
    { "scope": "source.dart other.source", "settings": { "foreground": "#80838D" } },
    { "scope": "source.dart string.interpolated", "settings": { "foreground": "#AB6400" } },
    { "scope": "source.dart string.quoted", "settings": { "foreground": "#AB6400" } },
    { "scope": "source.dart string.template", "settings": { "foreground": "#AB6400" } },
    { "scope": "source.dart support.class.dart", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.dart variable.parameter", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.dart storage.modifier", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.dart storage.type.annotation", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.dart meta.embedded.expression", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.cs keyword.type.string", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.cs keyword.type.void", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.cs entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.cs variable.other.object.property", "settings": { "foreground": "#8145B5" } },
    { "scope": "source.cs punctuation", "settings": { "foreground": "#80838D" } },
    { "scope": "source.diff meta.diff.header", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.diff meta.diff.header.from-file", "settings": { "foreground": "#CE2C31", "background": "#FFF7F7" } },
    { "scope": "source.diff meta.diff.header.from-file punctuation.definition", "settings": { "foreground": "#EB8E90" } },
    { "scope": "source.diff meta.diff.header.to-file", "settings": { "foreground": "#218358", "background": "#F4FBF6" } },
    { "scope": "source.diff meta.diff.header.to-file punctuation.definition", "settings": { "foreground": "#5BB98B" } },
    { "scope": "source.diff meta.diff.range", "settings": { "foreground": "#8145B5" } },
    { "scope": "source.diff markup.inserted.diff", "settings": { "foreground": "#218358" } },
    { "scope": "source.diff markup.deleted.diff", "settings": { "foreground": "#CE2C31" } },
    { "scope": "source.diff punctuation.definition.inserted.diff", "settings": { "foreground": "#5BB98B" } },
    { "scope": "source.diff punctuation.definition.deleted.diff", "settings": { "foreground": "#EB8E90" } },
    { "scope": "source.diff punctuation.definition.range.diff", "settings": { "foreground": "#BE93E4" } },
    { "scope": "source.rust entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.rust keyword.control.flow", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.rust entity.name.namespace", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.rust meta.attribute.rust", "settings": { "foreground": "#DC3E42" } },
    { "scope": "source.rust punctuation", "settings": { "foreground": "#80838D" } },
    { "scope": "source.zig entity.name.function", "settings": { "foreground": "#0588F0" } },
    { "scope": "source.zig keyword.control.flow", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.zig keyword.default", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.zig keyword.structure", "settings": { "foreground": "#CF3897" } },
    { "scope": "source.zig keyword.storage", "settings": { "foreground": "#8145B5" } },
    { "scope": "source.zig keyword.type", "settings": { "foreground": "#8145B5" } },
    { "scope": "source.zig keyword.type.c", "settings": { "foreground": "#2B9A66" } },
    { "scope": "source.zig support.function.builtin.zig", "settings": { "foreground": "#F76B15" } },
    { "scope": "source.zig punctuation", "settings": { "foreground": "#80838D" } },
    { "scope": "token.info-token", "settings": { "foreground": "#316BCD" } },
    { "scope": "token.warn-token", "settings": { "foreground": "#CD9731" } },
    { "scope": "token.error-token", "settings": { "foreground": "#CD3131" } },
    { "scope": "token.debug-token", "settings": { "foreground": "#800080" } }
  ]
}"""

# ----------------------------------------------------------------------
# Conversion helpers
# ----------------------------------------------------------------------
def hex_to_zed_color(hex_str):
    """Convert #rrggbb or #rrggbbaa to Zed hex string (always 6-digit if opaque)."""
    if not hex_str or hex_str == "#00000000":
        return None
    hex_str = hex_str.lstrip('#').lower()
    # 8-digit with alpha
    if len(hex_str) == 8:
        r, g, b, a = hex_str[0:2], hex_str[2:4], hex_str[4:6], hex_str[6:8]
        # If alpha is ff, treat as opaque
        if a == "ff":
            return f"#{r}{g}{b}"
        # Otherwise skip colors with alpha (Zed may not support)
        return None
    # Standard 6-digit
    if len(hex_str) == 6:
        return f"#{hex_str}"
    return None

def get_color(colors, key, default=None):
    val = colors.get(key)
    if val is None:
        return default
    return hex_to_zed_color(val)

def map_syntax(token_colors):
    """
    Convert VS Code tokenColors to Zed's simple syntax map.
    Later scopes override earlier ones; we keep the last encountered color per key.
    """
    # Map of Zed syntax keys to list of scope substrings (matched with 'in')
    scope_map = {
        "comment": ["comment"],
        "constant": ["constant.language", "constant.other"],
        "constant.numeric": ["constant.numeric"],
        "string": ["string"],
        "keyword": ["keyword"],
        "function": ["function", "entity.name.function", "meta.function-call"],
        "type": ["type", "entity.name.type"],
        "variable": ["variable"],
        "variable.parameter": ["variable.parameter"],
        "property": ["property", "meta.property"],
        "punctuation": ["punctuation", "meta.brace", "bracket"],
        "operator": ["operator", "keyword.operator"],
        "constructor": ["constructor"],
        "tag": ["tag", "entity.name.tag"],
        "attribute": ["attribute-name", "entity.other.attribute-name"],
        "number": ["constant.numeric"],  # duplicate mapping for clarity
    }
    syntax = {}
    # Process all rules; later rules override earlier ones
    for rule in token_colors:
        fg = rule.get("settings", {}).get("foreground")
        if not fg:
            continue
        color = hex_to_zed_color(fg)
        if not color:
            continue
        scopes = rule["scope"] if isinstance(rule["scope"], list) else [rule["scope"]]
        for scope in scopes:
            # Find which Zed key this scope belongs to
            for zed_key, patterns in scope_map.items():
                if any(p in scope for p in patterns):
                    syntax[zed_key] = color
                    break  # first match only, prevents overwriting with later matches in same rule
    # Fallback defaults (light/dark will be applied later)
    return syntax

# ----------------------------------------------------------------------
# Main converter
# ----------------------------------------------------------------------
def convert_to_zed(theme_json, name, appearance):
    try:
        data = json.loads(theme_json)
    except json.JSONDecodeError as e:
        print(f"JSON error in {name}: {e}")
        return None

    colors = data.get("colors", {})
    token_colors = data.get("tokenColors", [])

    # Build style dictionary
    style = {}

    # Editor
    style["editor.background"] = get_color(colors, "editor.background")
    style["editor.foreground"] = get_color(colors, "editor.foreground")  # not in VS Code?
    style["editor.line_number"] = get_color(colors, "editorLineNumber.foreground")
    style["editor.active_line_number"] = get_color(colors, "editorLineNumber.activeForeground")
    style["editor.selection.background"] = get_color(colors, "editor.selectionBackground")
    style["editor_gutter.background"] = get_color(colors, "editorGutter.background")

    # Tabs & headers
    style["tab_bar.background"] = get_color(colors, "editorGroupHeader.tabsBackground")
    style["tab.active_background"] = get_color(colors, "tab.activeBackground")
    style["tab.inactive_background"] = get_color(colors, "tab.inactiveBackground")
    style["border"] = get_color(colors, "panel.border") or get_color(colors, "sideBar.border")
    style["border.focused"] = get_color(colors, "panelTitle.activeBorder") or get_color(colors, "focusBorder")

    # Status & title bars
    style["status_bar.background"] = get_color(colors, "statusBar.background")
    style["title_bar.background"] = get_color(colors, "titleBar.activeBackground")

    # Sidebar, panel
    style["sidebar.background"] = get_color(colors, "sideBar.background")
    style["panel.background"] = get_color(colors, "panel.background")

    # Scrollbar
    style["scrollbar.thumb.background"] = get_color(colors, "scrollbarSlider.background")
    style["scrollbar.thumb.hover_background"] = get_color(colors, "scrollbarSlider.hoverBackground")

    # Terminal (if present)
    term_bg = get_color(colors, "terminal.background")
    if term_bg:
        style["terminal.background"] = term_bg
    term_fg = get_color(colors, "terminal.foreground")
    if term_fg:
        style["terminal.foreground"] = term_fg

    # ANSI terminal colors
    ansi_map = {
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
        "terminal.bright_green": "terminal.ansiBrightGreen",
        "terminal.bright_yellow": "terminal.ansiBrightYellow",
        "terminal.bright_blue": "terminal.ansiBrightBlue",
        "terminal.bright_magenta": "terminal.ansiBrightMagenta",
        "terminal.bright_cyan": "terminal.ansiBrightCyan",
        "terminal.bright_white": "terminal.ansiBrightWhite",
    }
    for zkey, vkey in ansi_map.items():
        col = get_color(colors, vkey)
        if col:
            style[zkey] = col

    # Syntax highlighting
    syntax = map_syntax(token_colors)
    # Apply some sensible defaults if missing
    if appearance == "dark":
        defaults = {
            "comment": "#777B84",
            "keyword": "#9A5CD0",
            "string": "#FFCA16",
            "function": "#3B9EFF",
            "type": "#3DD68C",
            "variable": "#EDEEF0",
            "constant.numeric": "#FFCA16",
            "punctuation": "#696E77",
            "operator": "#777B84",
            "property": "#3B9EFF",
            "constructor": "#3B9EFF",
        }
    else:  # light
        defaults = {
            "comment": "#80838D",
            "keyword": "#8145B5",
            "string": "#C07F00",
            "function": "#0588F0",
            "type": "#2B9A66",
            "variable": "#1C2024",
            "constant.numeric": "#AB6400",
            "punctuation": "#8B8D98",
            "operator": "#80838D",
            "property": "#0588F0",
            "constructor": "#0588F0",
        }
    for key, val in defaults.items():
        syntax.setdefault(key, val)

    style["syntax"] = syntax

    # Remove None values
    style = {k: v for k, v in style.items() if v is not None}

    return {
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
        "name": "Expo",
        "author": "Converted from VS Code Expo theme",
        "themes": [
            {
                "name": name,
                "appearance": appearance,
                "style": style,
            }
        ],
    }

# ----------------------------------------------------------------------
# Convert and save
# ----------------------------------------------------------------------
if __name__ == "__main__":
    light_theme = convert_to_zed(LIGHT_THEME_JSON, "Expo Light", "light")
    dark_theme = convert_to_zed(DARK_THEME_JSON, "Expo Dark", "dark")

    if light_theme:
        Path("expo-light-zed.json").write_text(json.dumps(light_theme, indent=2))
        print("Created: expo-light-zed.json")
    if dark_theme:
        Path("expo-dark-zed.json").write_text(json.dumps(dark_theme, indent=2))
        print("Created: expo-dark-zed.json")

    print("\nDone. Copy the generated files to ~/.config/zed/themes/")