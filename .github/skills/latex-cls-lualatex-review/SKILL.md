---
name: latex-cls-lualatex-review
description: 'Review LaTeX .cls class files, verify .tex integration, and validate LuaLaTeX compatibility. Use for class-file audits, compiler-specific issues, package conflicts, and minimal compile checks.'
argument-hint: 'Review a LaTeX .cls file for .tex and LuaLaTeX compatibility'
---

# LaTeX Class Review for LuaLaTeX

## When to Use
- Reviewing a LaTeX `.cls` file for correctness
- Verifying that a class works with `.tex` documents
- Checking LuaLaTeX compatibility, package loading, and compiler-specific branches
- Auditing class options, custom macros, layout logic, and package conflicts

## Procedure
1. Identify the class entry points: `\NeedsTeXFormat`, `\ProvidesClass`, `\LoadClass`, `\ProcessOptions`, and any compiler conditionals.
2. Inspect package loading order and look for LuaLaTeX-sensitive packages such as font, graphics, TikZ, hyperlink, and icon packages.
3. Check for class option handling, macro definitions, and layout calculations that may break in a minimal `.tex` document.
4. Look for likely LuaLaTeX issues:
   - engine checks that miss LuaLaTeX branches
   - font packages that assume pdfLaTeX
   - commands that depend on unavailable glyphs, encodings, or driver assumptions
   - hardcoded file paths or graphics formats
   - undefined control sequences, duplicated definitions, or invalid option forwarding
5. Build a minimal test document that loads the class under LuaLaTeX and exercises the main features used by `.tex` files.
6. Compare the `.cls` behavior against the minimal test and the target document requirements.
7. Report one of three outcomes:
   - passes as-is
   - passes with caveats or documented limitations
   - needs changes, with the smallest concrete fix list

## Quality Criteria
- The class loads cleanly under LuaLaTeX without fatal errors
- A minimal `.tex` file can compile successfully with the class
- Custom commands and environments are defined consistently
- Package ordering and engine-specific branches are defensible
- The final report distinguishes blocking issues from cosmetic or optional concerns

## Review Checklist
- Confirm the class name and file name match
- Confirm option parsing is valid and forwarded options are intentional
- Confirm LuaLaTeX branches are present where needed
- Confirm package requirements are loaded before dependent commands
- Confirm sidebar/layout or macro code does not rely on pdfLaTeX-only assumptions
- Confirm a small `.tex` smoke test exercises the class without extra setup

## Output Format
- Start with a short verdict
- List concrete compatibility findings
- Include the minimal test used to verify behavior
- If changes are needed, describe the exact class-file edits and why they are necessary
