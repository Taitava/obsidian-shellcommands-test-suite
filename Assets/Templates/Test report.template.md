---
# Do not change these values during testing.
tags:
  - frontmatter-tag
  - this-should-not-appear-twice
yaml_test1:
  first_item: "first value"
  middle_item:
    inner_item: "inner value"
  last_item: "last value"
yaml_test2:
  - first-item
  - second-item
  - last-item
---

# BASIC INFORMATION
Test author: **YOUR_NAME/NICK/LINK_HERE**
Operating system: **OS_name_here OS_version_here**
Obsidian version: **Obsidian_version_here**
Shell commands version: **Shell commands version here**
Test suite version: **Test suite version here**
Test date: **{{date:YYYY-MM-DD}}**

# 0. Preparations

- [ ] Please open up error console and keep it open during the whole test. It can show problems that would otherwise go unnoticed. You only need to monitor _errors_, not _messages_. The console can be opened up by pressing `Ctrl` + `Shift` + `I` (Windows and Linux) or `Cmd` + `Option` + `I` (macOS).

# [[1. Preview and execute shell commands]]
## 1.1. Preview shell commands
Inspect closely that variables have correct values!
- [ ] **Date and time {{date:YYYY-MM-DD HH:mm:ss}} command palette test**
- [ ] **File name {{file_name}} command palette test**: Check that the preview of the command shows escape characters (\` or \\ depending on your OS/shell) in front of spaces, dashes and dots in the file name. This ensures that escaping special characters works correctly.

## 1.2 Execute shell commands
\*) These commands' output handling is done in [realtime mode](https://publish.obsidian.md/shellcommands/Output+handling/Realtime+output+handling). It should not affect the outcome, but expands testing to that output handling mode, too.
- [ ] \* **[Caret position {{caret_position}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=01jk6q6kt5)**: Should give something like `Caret position: 45:60 (line: 45, column:60)`. The real numbers do not matter as they depend on where your caret happens to be.
- [ ] **[Character encoding test](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=ozilge8kih)**: This outputs *Test non-ASCII characters: Å Ä Ö* to *TestResults.md*. **Check that Å Ä Ö show up correctly in the file.** If you see something strange (e.g. �), the test is failed, and you should not tick the checkbox in this test report.
- [ ] **[Test to ignore error code](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=qm8y3vwg8k)**: This command should do absolutely nothing. It tries to change directory (`cd`) to *NonExistingFolder*, which fails with error code `1` (on Windows), or `2` (on Linux) . I'm not sure about the code on Mac. The command is defined to ignore error codes `1` and `2`. Tick this checkbox if nothing happened during the execution, but do not tick, if you saw an error message popping up.
- [ ] **[Test empty command](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=rejgzfrnyz)**: This one should always give an error message saying: *The shell command is empty*. If it  does not give an error message at all, **or if the message is different**, comment here and do not check the box. If the error message was correct, tick this checkbox.
- **Test output insertion** (hotkey F1):
	- This command inserts the following text to a currently active file, at caret position: *Text output test*. Be sure to have this **test report file** active and in **edit mode**. Check that a text insertion/replacement process succeeds:
	- [ ] Place the caret after the colon and execute the command to see how *inserting* works: 
	- [ ] Select some word in this sentence and execute the command to see how *replacing* works.
- [ ] **[Test output to stderr, with exit code 0](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=imsi0fzrit)**: This command should give the following output to an error balloon: *\[0\]: This goes to stderr*. Pay attention to the **\[0\]** part! It should not be *\[null\]*, and the number should not be anything else than zero. This command uses exit code 0, which indicates that the command actually succeeded, but it has the twist that even when the command succeeded, it directed its output to *stderr* instead of the normal *stdout*. SC should be able to differentiate error output despite an exit code 0 that indicates a succeeded shell command execution.
- [ ] **Test output to top** (hotkey F2): Make sure [[TestResults]] file is open and active! This command will insert *TEXT TO TOP* to the currently active file.
- [ ] **Test output to bottom** (hotkey F3): Make sure [[TestResults]] file is open and active! This command will insert *TEXT TO BOTTOM* to the currently active file.
- [ ] **[Test output to status bar](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=5w4m6q8d8e)**: Check that status bar will contain output text. Hover over the status bar with mouse and ensure that more output lines pop up.
- [ ] **[Test output to clipboard](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=5lk1z1h1ds)**: After running the command, paste clipboard content here: 
	- The pasted content should be *Hello clipboard!*. If it's something else, write a comment and do not tick the checkbox.
	- A notification balloon should also appear, telling what was copied to the clipboard. If it does not appear or the content is wrong, write a comment and do not tick the checkbox.
- **Test output to modal** (hotkey F4): Make sure [[TestResults]] file is active when executing the command! After executing the command, click all the *Redirect* buttons in the output modal, and see that each of them outputs the text MODAL OUTPUT in the correct channel:
	- [ ] *Status bar*
	- [ ] *Current file: caret position*
	- [ ] *Current file: top*
	- [ ] *Current file: bottom*
	- *Open files* does not need to be tested here.
	- [ ] *Clipboard*
- [ ] **[Test output using Open a file 1](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=5hvv4ee88g)**: This opens [[Welcome.md]] file in a new pane. Check that the file opens **and** that a new pane is created.
- [ ] **Test output using Open a file 2** (hotkey F5): Keep the previously opened pane focused! This opens [[README.md]] file and places the caret on line 2, column 3. Make sure the file opens in the current pane (which previously had [[Welcome.md]] open) **and** that the caret is placed in the mentioned position.
- **Test output using Open a file 3** (hotkey F6): Keep the previously opened pane focused! This opens [[Welcome.md]] again, this time with three selections:
	- [ ] Line 4 is selected completely. I.e. *Welcome!* is selected.
	- [ ] Line 7 contains a selection between columns 6 to 10. I.e. *test* is selected.
	- [ ] Line 7 also starts a selection 10 columns before the end of the line, and the selection extends to line 6, column 5. I.e. *improved*, two newlines and *This* are selected.
	- The above-mentioned  selected texts might be slightly inaccurate in case the content of [[Welcome.md]] changes after writing this test.
- **Test output using Open a file 4** (hotkey F7): Keep the previously opened pane focused! This opens and creates a new file named *A file that did not exist before.md* in the *Sandbox* folder.
	- [ ] Before executing the command, make sure the file **does not exist**.
	- [ ] Execute the command and make sure the file creation succeeds.
	- [ ] Finally, delete the file. You can now close the newly created tab, it's not needed anymore.
- [ ] **[Test output using Open a file 5](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=awn0zh7t5u)**: This should open [[Welcome.md]] in a new **tab**. No selections are made.
- [ ] **[Test output using Open a file 6](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tlq9kj69h5)**: This should open [[Welcome.md]] in a new **window**. No selections are made.
- [ ] **[Test $& variable](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=asdmfqbx5d)**: Symbol pair `$&` has caused problems in variable parsing when they appear in a variable's value (and some other `$` combinations too). Outputs:
	- `Test $& variable: $&` when the test is correct. (Tick the checkbox).
	- `Test $& variable: {{!passthrough:$&}}` when the test fails. Do not tick, leave a comment.
- [ ] **[Two 🐓 emojis](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=sr8mp9lpbb)**: This test should output two 🐓 emojis correctly. The first one has been written directly in the shell command, while the second one comes via a `{{passthrough:🐓}}` variable, which might break the emoji if variable parsing regular expressions fail. [Relates to bug #171](https://github.com/Taitava/obsidian-shellcommands/issues/171)
	- Incorrect result: `🐓��`
	- Correct result: 🐓🐓
- [ ] **[Escaping test](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=dk2axoxhd0)**: This command tests that an escaped `>>` symbol pair does not cause output to be written into [[TestResults]]. So, this test **should not output anything to TestResults.md**. Instead, the test is passed, if it creates a notification balloon saying: *This should NOT be written to TestResults.md!!! >> TestResults.md*.
- [ ] **[Test PATH additions](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=g7gauo1ds6)**: Opens up a modal showing the content of the `PATH` environment variable.
	- On Windows the output should contain two additional directories:
		1. *WindowsExtraPath1* should be present **near the beginning** of the output. Not as the first directory, but after a PowerShell directory.
		2. *WindowsExtraPath2* should be present **at the end** of the output.
	- On linux (and macOS) the output should contain one additional directory:
		- *LinuxAndMacExtraPath* should be present **at the end** of the output.
	- The reason for outputs being different in different operating systems is that in order to test two different appending mechanisms, I needed to use two different operating system settings fields. I can't make separate test shell commands for these, because the `PATH` additions are implemented to happen for all shell commands, and no shell command specific settings exist for them.
- [ ] **Remove PATH additions temporarily** in the settings (cut the text in the field to make it empty, you need to re-insert it afterward). Then execute [Test PATH additions](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=g7gauo1ds6) again and see that shell command execution works even when there's no PATH additions defined. `0.19.0` had a bug that caused execution to fail silently in this case. Finally, **add the PATH additions back**.
- [ ] **[Test multiline shell command](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=y2dtq5wuxy)**: This should output the following, each word on its own line:
	```markdown
	Multiline
	shell
	command
	```
- [ ] **[A long-running shell command](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=2jk7adqi4s)**: You should see a notification saying: *Executing: A long-running shell command*. The notification should appear around a couple of seconds after starting the execution (because it's only shown when a shell command execution takes an extended period of time). The notification should disappear the same time when the shell command finishes execution and outputs: *Waited for 5 seconds.*
- [ ] **Test output wrapping** (hotkey F12): Keep [[TestResults.md]] focused when executing this. This writes the following output text: *Output wrapped in callout.* The output should also show texts *Executed on* and *File name*. Check that all the variables work ok, and that special characters in the *date* and *file name* values are **not escaped**.
- [ ] **[Test globally default values](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=umqymtjrfc)**: Tests variables that are not accessible at the moment, but that do have default values defined:
	- `{{event_title}}` (not available because no event is triggered here). Default value: `This is a global default value for {{event_title}}.`
	- A custom variable. Default value: `This is a global default value for a custom variable.`
	- Make sure the command outputs the default values like they are presented above.
- File/folder menu items:
	- [ ] Right-click _Content note_ file in left navigation, and then click **Test file menu event variables**. Check that an OK result appears in [[TestResults.md]].
	- [ ] Right-click _Test guides_ folder in left navigation, and then click **Test folder menu event variables**. Check that an OK result appears in [[TestResults.md]].
	- The above aim to test most `{{event_\*}}` variables. E.g. `{{event_tags}}` is not tested by any other test (but I can't remember why).
- [ ] Editor menu test: Right click somewhere in the editor on click *Test editor menu event*. Check that an OK result appears in [[TestResults.md]].

- **Realtime tests**:
	- Each of these tests should output five lines to their specific output channels. There should always be one second pause between each line appearing. If all the lines appear at once, do not tick a checkbox!
	- [ ] **[Realtime test: Notification balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tm2ulm7r2m)**
	- [ ] **[Realtime test: Error balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=st8k313wkf)**
	- [ ] **Realtime test: Current file: caret position** (hotkey F8): Make sure [[TestResults.md]] has focus when executing this!
	- [ ] **Realtime test: Current file: top** (hotkey F9): Make sure [[TestResults.md]] has focus when executing this!
	- [ ] **Realtime test: Current file: bottom** (hotkey F10): Make sure [[TestResults.md]] has focus when executing this!
	- [ ] **[Realtime test: Open files](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=x9mb2l65cf)**: Will open a new Obsidian window and five tabs, all of which will contain [[Welcome.md]]. One second should pass between each tab opening.
	- [ ] **[Realtime test: Status bar](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=9a98pvcn6p)**: Status bar will show always the latest line, but hover over it to see all lines.
	- [ ] **[Realtime test: Ask after execution](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=vn29xcs8xs)**: See that output lines appear to the modal with one second pause between each line. No need to click any redirection buttons.
	- [ ] **[Realtime test: Clipboard](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=risjcw3y5m)**: You should see five notifications telling that output has been copied to clipboard.
```
Paste the clipboard content here after the execution has finished:

```
- **Terminate long-running shell commands**
	- These tests do not need their own shell commands, they just borrow other shell commands. You should be able to stop their execution before they end themselves.
	- [ ] **[Realtime test: Notification balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tm2ulm7r2m)**: A stop icon shows up in notification balloon that shows output text. Click it to stop the execution before _Realtime 5_ line is outputted.
	- [ ] **[Realtime test: Notification balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tm2ulm7r2m)**: Execute it again, but this time stop it from an icon in another notification balloon with content _Executing: Realtime test: Notification balloon_. This balloon appears after the shell command been executing a couple of seconds.
	- [ ] **[Realtime test: Ask after execution](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=vn29xcs8xs)**: Stop the executing by clicking a stop icon in the modal.

## 1.3. Automated tests
#inline-tag
This test covers testing multiple variables, speeding up the testing process.
1. Copy this to clipboard: TESTCLIPBOARD
	- It will be used to test the `{{clipboard}}` variable.
2. Select this text: TESTSELECTION
	- It will be used to test the `{{selection}}` variable.
3. Execute [Normal variable tests](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=zonkcdyhxn) by pressing  `Ctrl`/`Cmd` + `-` .
4. The test outputs a table to [[TestResults.md]].
- [ ] Check this checkbox if the summary is **ALL PASSED**.

# [[2. The rise and fall of a temporary shell command]]
This test section is removed in order to shorten the test process. It was just UI testing.

# [[3. Miscellaneous settings]]
Go to shell commands settings and follow the below instructions to test each of these settings:
## 3.1. Working directory
1. [ ] At the beginning, *Working directory* should be *Sandbox*. If it's not, change it.
2. Go through the following values for *Working directory* and run a shell command named **[Test working directory](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=h1i3hjdujv)** (hotkey F11). (This will insert working directories into [[TestResults]]):
	- [ ] *Sandbox*. Execute the command and ensure that the result in [[TestResults]] is an absolute path to *Sandbox*.
	- [ ] (An empty value, so that we refer to the vault's root folder.) Execute the command and ensure that the result in [[TestResults]] is an absolute path to this vault's root folder.
	- [ ] On Windows: *C:\WINDOWS\Temp*. On Linux: */tmp*. On Mac: I'm not sure, maybe */tmp* too. (We need to test an absolute directory too. This test should not write anything in the working directory, but still use a temporary folder just in case. The test does write into a file in the Sandbox folder, but should not write elsewhere regardless of what the working directory happens to be). Execute the command and ensure that the result in [[TestResults]] is an absolute path to the aforementioned temp folder.
	- [ ] *NonExistingFolder*. The idea is to check that you will get the following error message when you execute the command: *Working directory does not exist*.
	- [ ] *Welcome.md*. The idea is to check that you will get the following error message when you execute the command: *Working directory exists but is not a folder*.
3. [ ] Finally, make sure that you change *Working directory* back to *Sandbox*.

## 3.2. Preview variables in command palette
This setting should be on by default.
1. [ ] Open up command palette, type *execute* and check quickly that all commands that start with *Shell commands: Execute:* have parsed all their possible variables (= there are no `{{`/`}}` structures visible). Exception: Some variables cannot be parsed in every situation, such as `{{selection}}` when the active pane is not in edit mode, or `{{file_name}}` when the focus is on graph view. It's ok if these exceptional variables are not parsed, but you should check that most variables are parsed.
2. [ ] Go to shell command settings, and turn *Preview variables in command palette* off.
3. [ ] Open up command palette again, type *execute* and check quickly that all commands that start with *Shell commands: Execute:* have variable names visible, meaning that `{{`/`}}` structures should be visible.
4. [ ] Go to shell command settings, and turn *Preview variables in command palette* back on.
- [ ] In the settings panel, pay attention to scrolling. SC's settings panel should remember the last scroll position when reopened. Tick this checkbox if it did remember. Exception: the scroll position is forgotten when Obsidian is restarted.

# 4. Operating system specific commands
- [ ] **[Test operating system specific command](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=rw1rhziprx)**: This test will ensure that a shell command can run a correct version of it in each operating system. It should output one of these depending on your current OS. If it gives a wrong text, do not tick this checkbox.
	- *Windows command version executed.*
	- *Linux command version executed.*
	- *macOS command version executed.*

For the next tests, you need to **only run commands that are designed for your operating system**. For those tests that are not meant for your current operating system, just delete them.
- Windows:
	- [ ] **[Test Windows shell: CMD](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=1w4y2bpbmk)**: This command is executed explicitly with CMD, and it should output an absolute path to *cmd.exe* file.
	- [ ] **[Test Windows shell: PowerShell 5](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=hml8qvuqrs)**: Uses explicitly PowerShell, and it's old version 5. Should output *PS5 version: 5*, if the last version number is something else than *5*, then something is wrong. (PowerShell 5 might output strange extra characters that look like big dots. Just ignore them, the problem is known.)
	- [ ] **[Test Windows shell: PowerShell Core](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=r1erl29mnq)**: Uses explicitly PowerShell, and it's new version 6 or 7 (or even greater in the future). Should output *PSCore version: 6* (or 7 or above), if the last version number is *5*, then something is wrong.
- Linux / macOS:
	- [ ] **[Test Linux/Mac shell: Bash](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=cxircsux3k)**: Uses explicitly Bash, and it should output an absolute path to a Bash binary file.
	- [ ] **[Test Linux/Mac shell: Dash](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=pm9qf3zrfy)**: Uses explicitly Dash, and it should output an absolute path to a Dash binary file.
	- [ ] **[Test Linux/Mac shell: Zsh](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=0wuvfv0nzr)**: Uses explicitly Zsh (Z shell) and it should output an absolute path to a Zsh binary file.

# 5. Events
There a few shell commands defined for testing events. They are excluded from the command palette, so they cannot be executed the normal way.

1. [ ] Execute **[Trigger event tests](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=wnc4ycj2gv)**. It will trigger certain events automatically, and a group of test shell commands will react to the events. Results are stored in custom variables named like `{{_test_event_*}}`. Wait until the process is finished: You'll see a notification balloon telling that you can continue to the next step.
2. There are some events that need to be manually triggered from Obsidian:
	1. [ ] In the _Sandbox_ folder, move _MovableFolder_ to _MoveToHere_ folder.
	2. [ ] In the same folder, move _MovableNote.md_ file to _MoveToHere_ folder.
	3. [ ] Rename _RenameableFolder_ to _RenamedFolder_.
	4. [ ] Rename _RenameableNote.md_ to _RenamedNote.md_.
	- Please note that these actions need to be done **in Obsidian**, not in your operating system's file explorer. This is because file/folder moving/renaming events are only detected if the actions are performed by Obsidian. External actions would be seen as file/folder deletions and creations.
  5. [ ] Test [event debouncing](https://publish.obsidian.md/shellcommands/Events/Events+-+debouncing.md) by switching panes rapidly. Check that `Event debounce test at {{date::HH:mm:ss}}` is written to [[TestResults.md]] **not more often** than every **3** seconds. Do not tick the box, if the executions happen in a faster pace.
3. [ ] Test the [Caret moved in editor](https://publish.obsidian.md/shellcommands/Events/Caret+moved+in+editor) event: Move the caret and see that all the following kind of messages pop up:
       - `Caret line or column changed`
       - `Caret line changed`
       - `Caret column changed`
4. [ ] Gather test results by executing **[Finish event tests](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=041i8bhyir)** . (This also removes some temporary files and folders in _Sandbox_).
5. [ ] All test lines show the word **OK**.

# 6. Prompts and custom variables
## 6.1. Prompts
Execute the command **[Test custom variables and a prompt](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=dqnuqf8fo4)**. A prompt will appear to ask a few values.

Check the following things in the prompt:
1. [ ] The prompt's description shows a week day name instead of `{{date:dddd}}`.
2. [ ] The shell command preview text shows inputted values correctly when you type them. Also, the current field's value is bolded in the shell command.
3. [ ] The shell command preview text shows variable names correctly when you click the small toggle icon. Also, the current field's variable name is bolded in the shell command.
4. [ ] *Field using variables* shows the currently active folder's name in its description text.
5. [ ] *Field using variables* has the current year as its default value when the prompt is opened.
6. [ ] Try to submit the prompt values **without** inputting a value to *Mandatory field*. The submission should be **prevented** with an error message requiring the field to be filled.
7. [ ] After the error message, fill the field and check that submitting the prompt works ok.
8. [ ] After submitting the values, [[TestResults.md]] will contain a table showing test results. Tick this checkbox, if you see the text **ALL PASSED**.

## 6.2. Custom variables (via Shell commands URI)
1. *Test Shell commands URI*: This shell command is excluded from Obsidian's command palette, so it can only be executed via the following URI link: [Test Shell commands URI](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=2sb4p6r9b4&_uri_custom_variable_1=Hello&_uri_custom_variable_2=world!). After clicking it, [[TestResults.md]] should have the following new lines:
	- [ ] *Custom variable 1: Hello*
	- [ ] *Custom variable 2: world!*
2. Test setting custom variables via a link without executing a shell command. Click [this link](obsidian://shell-commands?_uri_custom_variable_1=Variable%20values%20set&_uri_custom_variable_2=without%20executing%20anything). Check from the *Custom variables* pane that the following variables have the following values:
	- [ ] *Custom variable 1: Variable values set*
	- [ ] *Custom variable 2: without executing anything*

# 7. Custom shells
If you are running:
 - macOS: There's no custom shell defined for macOS at the moment, so you can delete all subsections.
 - Linux: Remove subsections _7.1. Windows: WSL_ and _7.2. Windows: MinGW-w64_.
 - Windows: Remove subsection _7.3. Linux: Wine + CMD.EXE_.

## 7.1. Windows: WSL
Execute [WSL test](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=7fn65l4j2m). It opens a prompt (just to cross-test that prompts work with custom shells) which asks for a single value. Type whatever there and execute the shell command. It should output something like this to [[TestResults.md]]:
```
Executing WSL in /mnt/v/Lajitellut/Obsidian-tietokannat/Shell commands test:
Hello from WSL!
You wanted to output this: Your Name
Variable escaping should use unix style escaping: +-*/*
WSL executed.
```
- [ ] Check that the folder path on the first line begins with `/mnt/`. If not, _path translation_ does not work.
- [ ] Check that `You wanted to output this:` is followed by the value you submitted in the prompt.
- [ ] Check that `+-*/` appears **without** escaping characters.
  - This would be incorrect: `` `+`-`*`/`* `` If this appears, then the custom shell uses a wrong escaping character.

## 7.2. Windows: MinGW-w64
Execute [MinGW-w64 test](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=a437tpl07p). It should output something like:
```
Hello from MinGW-w64!
Vault path: /v/Lajitellut/Obsidian-tietokannat/Shell commands test
Variable escaping should use unix style escaping: +-*/*
```
- [ ] Check that the folder path on the second line begins with `/v/` (`v` can be a different character). If not, _path translation_ does not work.
- [ ] Check that `+-*/*` appears **without** escaping characters.
  - This would be incorrect: `` `+`-`*`/`* `` If this appears, then the custom shell uses a wrong escaping character.

## 7.3. Linux: Wine + CMD.EXE
Execute [Wine + CMD.EXE test](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=9b3bkhu159). It should output this:
```
Hello from CMD.EXE via Wine!  
```
- [ ] Wine gave correct output.

# 8. When there is no settings file
This section will test that the plugin works correctly when no `data.json` settings file exist. The plugin should load default settings.

1. [ ] Execute the command **[Open the plugin folder in system explorer](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=fsmbhs5vqc)**.
2. [ ] Make sure with git that there are no uncommitted changes to `.obsidian/plugins/obsidian-shellcommand/data.json`.
3. [ ] Rename `data.json` to `disabled-data.json`.
4. [ ] Restart Obsidian by pressing Ctrl/Cmd + R.
5. [ ] Make sure the plugin loads correctly:
	- [ ] The settings modal shows *Shell commands* on the left side list.
	- [ ] There are no shell commands at all shown in the plugin's settings view.
6. [ ] If the plugin created a new `data.json` file, delete it. If it didn't create it, it's ok, just tick this checkbox.
7. [ ] Rename `disabled-data.json` back to `data.json`.
8. [ ] Restart Obsidian again.
9. [ ] Ensure that the settings now have the normal list of shell commands.

# 9. Clean up
- [ ] Execute **[FINISH TEST](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=796vz9pyd6)** command, which will add your test results to the bottom of this file.
- The command will rename this test report file:
	- It removes the *(incomplete)* mark.
	- It adds the version number of Shell commands in parentheses, e.g. *(0.5.0)*.
	- It adds operating system/platform name, e.g. *Windows*, *Linux* or *Mac*.
	- It adds *ok* if **all** tests were successful, or *FAILED*.
	- Examples of a final file name:
		- *2021-09-26 (0.4.0) Windows ok.md*
		- *2021-09-26 (0.4.0) Linux FAILED.md*
		- *2021-11-06 (0.7.0-beta1) Linux ok.md*
- [ ] Check with Git that the only changes made in this vault/repository is your newly added report file. Other files - if edited(/created) - should have returned to their original states at this point.
- [ ] **Check that the test results appeared to the bottom of this file!** `0.18.2` test on Windows had a weird problem that [[TestResults.md]] was cleared, but its content was not copied over to the report file before the clearing.
- Finally, you should commit this new report file.

# 9. Results
%% Needs to have an empty line below the Results heading. Otherwise, test results will start at the same line with the heading.%%
