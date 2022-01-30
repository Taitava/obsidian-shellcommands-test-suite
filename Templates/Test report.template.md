---
# Do not change these values during testing.
test_suite_version: 0.10.0
tags:
  - frontmatter-tag
  - this-should-not-appear-twice
yaml_test1:
  first_item: first_value
  middle_item:
    inner_item: inner_value
  last_item: last_value
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
Test date: **{{date:YYYY-MM-DD}}**

# [[1. Preview and execute shell commands]]
## 1.1. Preview shell commands
Inspect closely that variables have correct values!
- [ ] **Caret position {{caret_position}} to file**
- [ ] **Clipboard {{clipboard}} to file**: (You can copy this to clipboard: TESTCLIPBOARD).
- [ ] **Date and time {{date:YYYY-MM-DD HH:mm:ss} } to file**
- [ ] **File extension {{file_extension:with-dot}}/{{file_extension:no-dot}} to file**
- [ ] **File name {{file_name}} to file**:  Check that the preview of the command shows escape characters (\` or \\ depending on your OS/shell) in front of spaces, dashes and dots in the file name. This ensures that escaping special characters works correctly. You'll see same escape characters with other commands, too.
- [ ] **Absolute file path {{file_path:absolute}} to file**
- [ ] **Relative file path {{file_path:relative}} to file**
- [ ] **Folder name {{folder_name}} to file**
- [ ] **Absolute folder path {{folder_path:absolute}} to file**
- [ ] **Relative folder path {{folder_path:relative}} to file**
- [ ] **Selection {{selection}} to file**: Edit mode needs to be on! (You can select this text: TESTSELECTION).
- [ ] **Tags {{tags}} to file** #inline-tag
- [ ] **Title {{title }} to file**
- [ ] **Vault path {{vault_path}} to file**
- [ ] **Workspace {{workspace}} to file**

## 1.2 Execute shell commands
Inspect closely that their output to TestResults.md is a) correct, and b) matches what you saw in preview (e.g. `{{date:YYYY-MM-DD HH:mm:ss} }` %% The extra space here is intentional: Obsidian Templates should not parse this variable. %% should have exactly same seconds)!
- [ ] **Caret position {{caret_position}} to file**: Should give something like `Caret position: 45:60 (line: 45, column:60)`. The real numbers do not matter as they depend on where your caret happens to be.
- [ ] **Clipboard {{clipboard}} to file**: (You can copy this to clipboard: TESTCLIPBOARD).
- [ ] **Date and time {{date:YYYY-MM-DD HH:mm:ss} } to file**
- [ ] **File extension {{file_extension:with-dot}}/{{file_extension:no-dot}} to file**: The result should be: *File extension: with dot: 
.md / no dot: md*
- [ ] **File name {{file_name}} to file**: Check that the file name does not contain any escape characters like: \` or \\.
- [ ] **Absolute file path {{file_path:absolute}} to file**: If you are on **Mac or Linux**, please ensure that the path starts with `/`, e.g. `/Users/.../SomeFile.md`. If it's without a leading `/` (e.g. `Users/.../SomeFile.md`), then there is a bug. Add a comment here and leave the checkbox unchecked. On Windows: Check that directories are separated by `\`, not `/`.
- [ ] **Relative file path {{file_path:relative}} to file**
- [ ] **Folder name {{folder_name}} to file**
- [ ] **Absolute folder path {{folder_path:absolute}} to file**: **Same check** as with *Absolute file path* above.
- [ ] **Relative folder path {{folder_path:relative}} to file**
- [ ] **Selection {{selection}} to file**: Edit mode needs to be on! (You can select this text: TESTSELECTION).
- [ ] **Tags {{tags}} to file**. #this-should-not-appear-twice . If this tag appears twice in the result, leave a comment and do not tick the box.
- [ ] **Title {{title }} to file**
- [ ] **Vault path {{vault_path}} to file**
- [ ] **Workspace {{workspace}} to file**
- [ ] **Character encoding test**: This outputs *Test non-ASCII characters: Å Ä Ö* to *TestResults.md*. **Check that Å Ä Ö show up correctly in the file.** If you see something strange (e.g. �), the test is failed and you should not tick the checkbox in this test report.
- [ ] **Test to ignore error code**: This command should do absolutely nothing. It tries to change directory (`cd`) to *NonExistingFolder*, which fails with error code `1` (on Windows), or `2` (on Linux) . I'm not sure about the code on Mac. The command is defined to ignore error codes `1` and `2`. Tick this checkbox if nothing happened during the execution, but do not tick, if you saw an error message popping up.
- [ ] **Test empty shell command**: This one should always give an error message saying: *The shell command is empty*. If it  does not give an error message at all, **or if the message is different**, comment here and do not check the box. If the error message was correct, tick this checkbox.
- [ ] **Test output insertion**:
	- This command inserts the following text to a currently active file, at caret position: *Text output test*. Be sure to have this **test report file** active and in **edit mode**. Check that a text insertion/replacement process succeeds:
	- [ ] Place the caret after the colon and execute the command to see how *inserting* works: 
	- [ ] Select some word in this sentence and execute the command to see how *replacing* works.
- [ ] **Test output to stderr, with exit code 0**: This command should give the following output to an error balloon: *[0]: This goes to stderr*. Pay attention to the **[0]** part! It should not be *[null]*, and the number should not be anything else than zero. This command uses exit code 0, which indicates that the command actually succeeded, but it has the twist that even when the command succeeded, it directed its output to *stderr* instead of the normal *stdout*. SC should be able to differentiate error output despite of an exit code 0 that indicates a succeeded shell command execution.
- [ ] **Test output to top**: Make sure [[TestResults]] file is open and active! This command will insert *TEXT TO TOP* to the currently active file.
- [ ] **Test output to bottom**: Make sure [[TestResults]] file is open and active! This command will insert *TEXT TO BOTTOM* to the currently active file.
- [ ] **Test output to status bar**: Check that status bar will contain output text. Hover over the status bar with mouse and ensure that more output lines pop up.
- [ ] **Test output to clipboard**: After running the command, paste clipboard content here: 
	- The pasted content should be *Hello clipboard!*. If it's something else, write a comment and do not tick the checkbox.
	- A notification balloon should also appear, telling what was copied to the clipboard. If it does not appear or the content is wrong, write a comment and do not tick the checkbox.
- **Test output to modal**: Make sure [[TestResults]] file is active when executing the command! After executing the command, click all of the *Redirect* buttons in the output modal, and see that each of them outputs the text MODAL OUTPUT in the correct channel:
	- [ ] *Status bar*
	- [ ] *Current file: caret position*
	- [ ] *Current file: top*
	- [ ] *Current file: bottom*
	- [ ] *Clipboard*
- [ ] **Test \$& variable**: Symbol pair `$&` has caused problems in variable parsing when they appear in the variable's value (and some other `$` combinations too). Outputs:
	- `Test $& variable: $&` when the test is correct. (Tick the checkbox).
	- `Test $& variable: {{!passthrough:$&}}` when the test fails. Do not tick, leave a comment.
- [ ] **Escaping test 1**: This command tests a wide range of special characters that should be escaped. Two things are tested: **a)** The special characters should not do anything special, they should not prevent the test from outputting all the characters; **b)** When the characters are output to [[TestResults]], they should be presented there **without** any escaping characters (`\` or `` ` ``), with the exception that `\` and `` ` `` do appear in the result as individual test characters - they just should not appear in fron of every other special character.
	- Wrong output: ``Escaping test 1: \<\>\,\.\-\;\:\§\+\´\½\!\'\"\#\¤\%\&\/\(\)\=\?\`\@\`\£\$\€\{\[\]\}\\\\\¨\^\~\*\å\ä\ö\*`` (a shell should remove the escape characters).
	- Wrong, if the command tried to do something strange.
	- Correct output: ``Escaping test 1: 
<>,.-;:§+´½!'"#¤%&/()=?`@`£$€{[]}\\¨^~*åäö*``
- [ ] **Escaping test 2**: This command tests actually the same thing as *Escaping test 1*, but it focuses more on to test that an escaped `>>` symbol pair does not cause output to be written into [[TestResults]]. So, unlike many other tests, this test **should not output anything to TestResults.md**. Instead, the test is passed, if it creates a notification balloon saying: *This should NOT be written to TestResults.md!!! >> TestResults.md*.
- [ ] **Test YAML value**: Should output the following to [[TestResults]]: `YAML test: A1. 
first_value A2. inner_value A3. last_value B) first: first-item B) second: second-item B) last: last-item B) count: 3` . If even a single difference is found, leave a comment and do not tick the checkbox.
	

# [[2. The rise and fall of a temporary shell command]]
1. Go to Shell command settings (`Ctrl/Cmd + ,`).
2. [ ] Create a new shell command. This can be something simple with one variable, like: `echo {{file_name}}`. The command does not need to actually do anything. No need to assign an alias (yet).
3. [ ] When typing a variable name, use an [autocomplete menu](https://publish.obsidian.md/shellcommands/Variables/Autocomplete/Autocomplete) to do it and check that the menu works correctly.
4. [ ] Check that the settings view shows a preview for this shell command, e.g. *echo TestResults.md*.
5. [ ] Define an alias for the command, e.g. *Echo test*.
6. [ ] Check that the settings view shows the alias text instead of *Command #*.
7. [ ] Go to *Hotkeys* settings and search for this new shell command (make sure it can be found there).
8. [ ] Define the following hotkey for the new shell command: Ctrl/Cmd + M.
9. [ ] Restart Obsidian by pressing Ctrl/Cmd + R (a custom hotkey defined in this test vault). This is to make sure that all settings are stored and loaded correctly.
10. [ ] Go to shell command settings again and check that the new command still exists.
11. [ ] Check that the shell command should display the following hotkey text below the command field: *Ctrl + M* (if you are on Windows/Linux) or *Cmd + M* (if you are on Mac). Pay attention that the *Ctrl*/*Cmd* part must be correct according to your operating system!
12. [ ] Click the delete command button to open a confirmation window.
13. [ ] Check that the confirmation window displays correctly the command's name and alias.
14. [ ] Click *Yes, delete* and ensure that the command was really deleted.
15. [ ] Restart Obsidian again by pressing Ctrl/Cmd + R.
16. [ ] Go to shell command settings again and check that the new command does not exists any more.

# [[3. Miscellaneous settings]]
Go to shell commands settings and follow the below instructions to test each of these settings:
## 3.1. Working directory
1. [ ] At the beginning, *Working directory* should be *Sandbox*. If it's not, change it.
2. Go through the following values for *Working directory* and run a shell command named **Test working directory** (this will insert working directories into [[TestResults]]):
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
- [ ] **Test operating system specific command**: This test will ensure that a shell command can run a correct version of it in each operating system. It should output one of these depending on your current OS. If it gives a wrong text, do not tick this checkbox.
	- *Windows command version executed.*
	- *Linux command version executed.*
	- *Macintosh command version executed.*

For the next tests, you need to **only run commands that are designed for your operating system**. For those tests that are not meant for your current operating system, just delete them.
- Windows:
	- [ ] **Test Windows shell: CMD**: This command is executed explicitly with CMD, and it should output an absolute path to *cmd.exe* file.
	- [ ] **Test Windows shell: PowerShell 5**: Uses explicitly PowerShell and it's old version 5. Should output *PS5 version: 5*, if the last version number is something else than *5*, then something is wrong. (PowerShell 5 might output strange extra characters that look like big dots. Just ignore them, the problem is known.)
	- [ ] **Test Windows shell: PowerShell Core**: Uses explicitly PowerShell and it's new version 6 or 7 (or even greater in the future). Should output *PSCore version: 6* (or 7 or above), if the last version number is *5*, then something is wrong.
- Linux / Macintosh:
	- [ ] **Test Linux/Mac shell: Bash**: Uses explicitly Bash and it should output an absolute path to a Bash binary file.
	- [ ] **Test Linux/Mac shell: Dash**: Uses explicitly Dash and it should output an absolute path to a Dash binary file.
	- [ ] **Test Linux/Mac shell: Zsh**: Uses explicitly Zsh (Z shell) and it should output an absolute path to a Zsh binary file.

# 5. Events
There a a few shell commands defined for testing events. They are excluded from the command palette, so they cannot be executed the normal way. Some of them have already been executed a few times by the time you'll reach this section. The only thing that these commands do, is echoing text to a notification balloon or to the status bar - they do not write anything to files.

Check each one of the the following tests whose message you've already seen during this test session:
1. [ ] *Event: After Obsidian starts*: Displayed every time Obsidian is started/restarted.
2. [ ] *Event: After switching the active pane*: Displayed every time you switch between files and other panes. As this happens very often, the message is displayed on the status bar, not in a notification balloon! For this reason, the message also includes the time, so that you know that it has been executed recently.
3. [ ] *Event: Every 180 seconds*: This message is displayed every 180 seconds.

These require you to do something manually to see them executing:
1. [ ] *Event: Before Obsidian quits*: Displayed **really shortly** every time you close Obsidian. It might be hard to notice this message because Obsidian might quit before the message gets displayed.
2. [ ] *Event: File menu*: In the left navigation menu, click a *file* with the right button of your mouse. You should see an option named *Event: File menu:* with a file name there. (If the option is not present, do not tick this checkbox). Click the option and you should see the same text appearing in a notification balloon.
3. [ ] Event: *Folder menu*: In the left navigation menu, click a *folder* with the right button of your mouse. You should see an option named *Event: Folder menu:* with a folder name there. (If the option is not present, do not tick this checkbox). Click the option and you should see the same text appearing in a notification balloon.
4. [ ] *Event: Editor menu*: In the editor, click text with the right button of your mouse. You should see an option named *Event: Editor menu*. (If the option is not present, do not tick this checkbox). Click the option and you should see the same text appearing in a notification balloon.

# 6. When there is no settings file
This section will test that the plugin works correctly when no `data.json` settings file exist. The plugin should load default settings.

1. [ ] Execute the command **Open the plugin folder in system explorer**.
2. [ ] Make sure with git that there are no uncommitted changes to `.obsidian/plugins/obsidian-shellcommand/data.json`.
3. [ ] Rename `data.json` to `disabled-data.json`.
4. [ ] Restart Obsidian by pressing Ctrl/Cmd + R.
5. [ ] Make sure the plugin loads correctly:
	- [ ] The settings modal shows *Shell commands* in the left side list.
	- [ ] There are no shell commands at all shown in the plugin's settings view.
6. [ ] If the plugin created a new `data.json` file, delete it. If it didn't create it, it's ok, just tick this checkbox.
7. [ ] Rename `disabled-data.json` back to `data.json`.
8. [ ] Restart Obsidian again.
9. [ ] Ensure that the settings now have the normal list of shell commands.

# 7. Clean up
- [ ] Execute **FINISH TEST** command, which will add your test results to the bottom of this file.
- Edit the name of this file:
	- [ ] Remove the *(incomplete)* mark.
	- [ ] Add the version number of Shell commands in parenthesis, e.g. *(0.5.0)*. If you are testing a version that is not yet published as a stable version, please add also a suffix describing the status, e.g. `0.7.0-beta1` (for public betas) or `0.7.0-development` (for non-beta development versions, available only to me).
	- [ ] Add operating system/platform name (without a version), e.g *Windows*, *Linux* or *Mac*.
	- [ ] Add *ok* if **all** tests were successful, or *FAILED* if even just one test failed.
	- **Do not rename before you have executed the *FINISH TEST* command!**
	- Examples of a final file name:
		- *2021-09-26 (0.4.0) Windows ok.md*
		- *2021-09-26 (0.4.0) Linux FAILED.md*
		- *2021-11-06 (0.7.0-beta1) Linux ok.md*
- [ ] Check with Git that the only changes made in this vault/repository is your newly added report file. Other files - if edited(/created) - should have returned to their original states at this point.

# 7. Results
%% Needs to have an empty line below the Results heading. Otherwise test results will start at the same line with the heading.%%
