# Changelog
All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
Features that are in development, but are not released yet. Does not include stuff that requires longer planning - for those, see [Roadmap on GitHub](https://github.com/Taitava/obsidian-shellcommands/projects/1).

### To be Changed
- [Settings: Make extra options modal scrollable (#84)](https://github.com/Taitava/obsidian-shellcommands/issues/84)

## [0.6.0] - 2021-10-12

### Added
- [New shell command output channels (#68)](https://github.com/Taitava/obsidian-shellcommands/issues/68):
  - Status bar: Good for showing short outputs in a permanent place.
  - Current file, top: Puts the output at the very beginning of a file.
  - Current file, bottom: Puts the output at the very end of a file.
  - Clipboard: So that you can easily paste the output anywhere you like.

### Changed
- [Settings: Scroll position is now remembered (#71)](https://github.com/Taitava/obsidian-shellcommands/issues/71)
- [`{{tags}}` does not include preceding hash (#) characters anymore (#62)](https://github.com/Taitava/obsidian-shellcommands/issues/62). This is a backwards incompatible change (although a small one), and normally these kinds of changes would not be released in a _minor_ version update. But this plugin is still in its 0.x era, so breaking changes are tolerated more than in stable releases. If you want to have your tags prefixed with a hash again, use something like `#{{tags:,#}}` instead of `{{tags:,}}`.
- [Internal: Support multiple parameters for variables (#43)](https://github.com/Taitava/obsidian-shellcommands/issues/43). In the future, allows developing new variables that takes multiple arguments, and/or optional arguments.
- `{{file_path}}` and `{{folder_path}}` will not give an error message anymore if the given argument is not *relative* or *absolute*. Instead, the variable will be left unparsed silently. This change happened during [#43](https://github.com/Taitava/obsidian-shellcommands/issues/43).

## [0.5.1] - 2021-10-09

### Fixed
- [`{{tags}}` does not give duplicate tags anymore (#65)](https://github.com/Taitava/obsidian-shellcommands/issues/65).
- [Error balloon: Exit code was sometimes null (#67)](https://github.com/Taitava/obsidian-shellcommands/issues/67).

## [0.5.0] - 2021-10-02

### Added
- [Shell command output can now be accessed in various ways (#34)](https://github.com/Taitava/obsidian-shellcommands/issues/34):
  - Output can be directed to a chosen channel: a notification balloon, or to currently open note file at caret position, possibly replacing a selection.
  - Output can also be ignored = not displayed anywhere.
  - Separate output channels can be defined for each output stream: stdout and stderr.
  - Output channel definitions can be altered separately for each shell command.
  - Previously stdout was always ignored, and stderr could only be directed into a notification balloon.
- [A setting for how long to display notifications (#58)](https://github.com/Taitava/obsidian-shellcommands/issues/58). Mainly affects when shell command output is directed to a _notification balloon_.
- [A new variable {{tags}}(#51)](https://github.com/Taitava/obsidian-shellcommands/issues/51) (Thank you [FelipeRearden](https://github.com/FelipeRearden) for this idea!)

### Changed
- Error messages do not contain the failed shell command anymore, only exit code number and the actual error message (stderr). This is due to error message simplification that had to be done when implementing new ways to use outputs, including stderr in issue #34.

## [0.4.1] - 2021-09-29

### Fixed
- [Variables `{{file_path:absolute}}` / `{{folder_path:absolute}}` missed leading `/`/`\` slash (#44)](https://github.com/Taitava/obsidian-shellcommands/issues/44)
- [Variable `{{folder_path:relative}}` returned `/` when current file is in vault root (#52)](https://github.com/Taitava/obsidian-shellcommands/issues/52)
- [Turning off 'Preview variables' setting left old previews to command palette (#45)](https://github.com/Taitava/obsidian-shellcommands/issues/45)
- [Entering an alias for a new, empty command did not update the command title in settings (#46)](https://github.com/Taitava/obsidian-shellcommands/issues/46)
- [Prevent executing empty shell commands (#53)](https://github.com/Taitava/obsidian-shellcommands/issues/53)

## [0.4.0] - 2021-09-26

### Added
- [Confirmation before executing a shell command (#35)](https://github.com/Taitava/obsidian-shellcommands/issues/35)
- [Settings: Execute now icon button for each command (#30)](https://github.com/Taitava/obsidian-shellcommands/issues/30)
- [Ignore errors by code (#36)](https://github.com/Taitava/obsidian-shellcommands/issues/36): You can choose not to display error messages for certain exit codes. 

### Changed
- [Working directory: support a relative path (#28)](https://github.com/Taitava/obsidian-shellcommands/issues/28)
- [Internal: Make variables to return error messages in an array, not to display error messages directly (#39)](https://github.com/Taitava/obsidian-shellcommands/issues/39)
- The above internal change also made these changes:
  - Settings: command preview can now show error messages from variables.
  - If one variable fails to parse, parsing the rests of variables is cancelled, so in some cases less error messages are displayed at the same time.

## [0.3.0] - 2021-09-17

### Added
- [{{workspace}} variable (#14)](https://github.com/Taitava/obsidian-shellcommands/issues/14) (Thank you [FelipeRearden](https://github.com/FelipeRearden) for this idea!)
- [Settings: Display hotkeys next to commands. (#21)](https://github.com/Taitava/obsidian-shellcommands/issues/21)

### Changed
- [Settings: Widen the command fields. (#19)](https://github.com/Taitava/obsidian-shellcommands/issues/19)
- [Settings: Shell commands are now deleted with an icon button, not by clearing a text field. (#20)](https://github.com/Taitava/obsidian-shellcommands/issues/20)
- Settings: When opening alias modal, the alias text field has now focus.
- Internal restructuring of code without external implications.
- Small improvement on descriptions of {{file_name}} and {{title}} in the plugin's settings.

## [0.2.0] - 2021-09-11

### Added
- [Alias names for commands (#6)](https://github.com/Taitava/obsidian-shellcommands/issues/6) (Thank you [FelipeRearden](https://github.com/FelipeRearden) for this idea!)
- [Preview variables in command palette (#10)](https://github.com/Taitava/obsidian-shellcommands/issues/10)
- [A setting for how long to display error messages (#7)](https://github.com/Taitava/obsidian-shellcommands/issues/7)

## [0.1.1] - 2021-09-10

### Changed
- [Internal rewriting of how command settings are stored (#8)](https://github.com/Taitava/obsidian-shellcommands/issues/8)
- Settings: Changing or creating commands does not require pressing Apply button anymore. Apply is still needed after removing commands.

### Deprecated
- [`commands` configuration setting (#8)](https://github.com/Taitava/obsidian-shellcommands/issues/8): Version `0.1.1` (and above) will replace this setting in users' `data.json` settings file with a new `shell_commands` setting. This is an internal change, and the plugin will handle it automatically, but it's important to be noted by end users, because users need to upgrade to `0.1.1` (or newer) *before* upgrading to `1.0.0` in the future, because [`1.0.0` will finally remove the migration support for `commands` setting (#9)](https://github.com/Taitava/obsidian-shellcommands/issues/9). That being said, `1.0.0` is not going to be released any time soon, it's just a milestone in the far future (at the time of writing this on 2021-09-09).

### Fixed
- Deleting commands should not cause non-removed commands to change/lose their hotkeys.

## [0.1.0] - 2021-08-29

### Added
- Support for certain in-built variables (see the settings panel - actually I should put the variables to the README.md file too at some point).
- Display execution errors.
- README.md: Usage examples.

### Changed
- Determine vault directory automatically.
- A bit better behaving settings view.

## [0.0.0] - 2021-08-22
- Initial release.

[Unreleased]: https://github.com/Taitava/obsidian-shellcommands/compare/0.6.0...HEAD
[0.6.0]: https://github.com/Taitava/obsidian-shellcommands/compare/0.5.1...0.6.0
[0.5.1]: https://github.com/Taitava/obsidian-shellcommands/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/Taitava/obsidian-shellcommands/compare/0.4.1...0.5.0
[0.4.1]: https://github.com/Taitava/obsidian-shellcommands/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/Taitava/obsidian-shellcommands/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/Taitava/obsidian-shellcommands/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/Taitava/obsidian-shellcommands/compare/0.1.1...0.2.0
[0.1.1]: https://github.com/Taitava/obsidian-shellcommands/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/Taitava/obsidian-shellcommands/compare/0.0.0...0.1.0
[0.0.0]: https://github.com/Taitava/obsidian-shellcommands/releases/tag/0.0.0