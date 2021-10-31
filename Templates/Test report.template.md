---
# Do not change these values during testing.
test_suite_version: 0.7.0
tags:
  - frontmatter-tag
  - this-should-not-appear-twice
---

# BASIC INFORMATION
Test author: **YOUR_NAME/NICK/LINK_HERE**
Operating system: **OS_name_here OS_version_here**
Obsidian version: **Obsidian_version_here**
Shell commands version: **Shell commands version here**
Test date and start time: **{{date:YYYY-MM-DD HH:mm}}**

# [[1. Preview and execute shell commands]]
## 1.1. Preview shell commands
Inspect closely that variables have correct values!
- [ ] **Clipboard {{clipboard}} to file**: (You can copy this to clipboard: TESTCLIPBOARD).
- [ ] **Date and time {{date:YYYY-MM-DD HH:mm:ss} } to file**
- [ ] **File name {{file_name}} to file**:  Check that the preview of the command shows escape characters (\` or \\ depending on your OS/shell) in front of spaces, dashes and dots in the file name. This ensures that escaping special characters works correctly. You'll see same escape characters with other commands, too.
- [ ] **Absolute file path {{file_path:absolute}} to file**
- [ ] **Relative file path {{file_path:relative}} to file**
- [ ] **Folder name {{folder_name}} to file**
- [ ] **Absolute folder path {{folder_path:absolute}} to file**
- [ ] **Relative folder path {{folder_path:relative}} to file**
- [ ] **Selection {{selection}} to file**: (You can select this text: TESTSELECTION).
- [ ] **Tags {{tags}} to file** #inline-tag
- [ ] **Title {{title }} to file**
- [ ] **Vault path {{vault_path}} to file**
- [ ] **Workspace {{workspace}} to file**

## 1.2 Execute shell commands
Inspect closely that their output to TestResults.md is a) correct, and b) matches what you saw in preview (e.g. `{{date:YYYY-MM-DD HH:mm:ss} }` %% The extra space here is intentional: Obsidian Templates should not parse this variable. %% should have exactly same seconds)!
- [ ] **Clipboard {{clipboard}} to file**: (You can copy this to clipboard: TESTCLIPBOARD).
- [ ] **Date and time {{date:YYYY-MM-DD HH:mm:ss} } to file**
- [ ] **File name {{file_name}} to file**: Check that the file name does not contain any escape characters like: \` or \\.
- [ ] **Absolute file path {{file_path:absolute}} to file**: If you are on **Mac or Linux**, please ensure that the path starts with `/`, e.g. `/Users/.../SomeFile.md`. If it's without a leading `/` (e.g. `Users/.../SomeFile.md`), then there is a bug. Add a comment here and leave the checkbox unchecked. On Windows: Check that directories are separated by `\`, not `/`.
- [ ] **Relative file path {{file_path:relative}} to file**
- [ ] **Folder name {{folder_name}} to file**
- [ ] **Absolute folder path {{folder_path:absolute}} to file**: **Same check** as with *Absolute file path* above.
- [ ] **Relative folder path {{folder_path:relative}} to file**
- [ ] **Selection {{selection}} to file**: (You can select this text: TESTSELECTION).
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
	- A notification balloon should also appear, telling what was copied to the clipboard. If it does not appear or the content if wrong, write a comment and do not tick the checkbox.



# [[2. The rise and fall of a temporary shell command]]
1. Go to Shell command settings (`Ctrl/Cmd + ,`).
2. [ ] Create a new shell command. This can be something simple with one variable, like: `echo {{file_name}}`. The command does not need to actually do anything. No need to assign an alias (yet).
3. [ ] Check that the settings view shows a preview for this shell command, e.g. *echo TestResults.md*.
4. [ ] Define an alias for the command, e.g. *Echo test*.
5. [ ] Check that the settings view shows the alias text instead of *Command #*.
6. [ ] Go to *Hotkeys* settings and search for this new shell command (make sure it can be found there).
7. [ ] Define the following hotkey for the new shell command: Ctrl/Cmd + M.
8. [ ] Restart Obsidian by pressing Ctrl/Cmd + R (a custom hotkey defined in this test vault). This is to make sure that all settings are stored and loaded correctly.
9. [ ] Go to shell command settings again and check that the new command still exists.
10. [ ] Check that the shell command should display the following hotkey text below the command field: *Ctrl + M* (if you are on Windows/Linux) or *Cmd + M* (if you are on Mac). Pay attention that the *Ctrl*/*Cmd* part must be correct according to your operating system!
11. [ ] Click the delete command button to open a confirmation window.
12. [ ] Check that the confirmation window displays correctly the command's name and alias.
13. [ ] Click *Yes, delete* and ensure that the command was really deleted.
14. [ ] Restart Obsidian again by pressing Ctrl/Cmd + R.
15. [ ] Go to shell command settings again and check that the new command does not exists any more.

# [[3. Miscellaneous settings]]
Go to shell commands settings and follow the below instructions to test each of these settings:
## 3.1. Working directory
1. [ ] At the beginning, *Working directory* should be *Sandbox*. If it's not, change it.
2. Go through the following values for *Working directory* and run a shell command named **Test working directory** (this will insert working directories into [[TestResults]]):
3. - [ ] *Sandbox*. Execute the command and ensure that the result in [[TestResults]] is an absolute path to *Sandbox*.
4. - [ ] (An empty value, so that we refer to the vault's root folder.) Execute the command and ensure that the result in [[TestResults]] is an absolute path to this vault's root folder.
5. - [ ] On Windows: *C:\WINDOWS\Temp*. On Linux: */tmp*. On Mac: I'm not sure, maybe */tmp* too. (We need to test an absolute directory too. This test should not write anything in the working directory, but still use a temporary folder just in case. The test does write into a file in the Sandbox folder, but should not write elsewhere regardless of what the working directory happens to be). Execute the command and ensure that the result in [[TestResults]] is an absolute path to the aforementioned temp folder.
6. - [ ] *NonExistingFolder*. The idea is to check that you will get the following error message when you execute the command: *Working directory does not exist*.
7. - [ ] *Welcome.md*. The idea is to check that you will get the following error message when you execute the command: *Working directory exists but is not a folder*.
8. [ ] Finally, make sure that you change *Working directory* back to *Sandbox*.

## 3.2. Error message duration
The default value of *Error message duration* is 20 seconds.
1. [ ] Execute the command **Doomed to eternal failure**. It just executes *cd NonExistingFolder*, which throws an error that the folder does not exist. See that the error message shows up and is visible around 20 seconds.
2. [ ] Change *Error message duration* to 1 second, execute the same command again and see that the error message shows up, but disappears quickly.
3. [ ] Change *Error message duration* back to the default value.

## 3.3. Notification message duration
The default value of *Notification message duration* is 10 seconds.
1. [ ] Execute the command **Hello world!**. It just echoes *Hello world!* in a notification balloon. See that the notification message shows up and is visible around 10 seconds.
2. [ ] Change *Notification message duration* to 1 second, execute the same command again and see that the notification message shows up, but disappears quickly.
3. [ ] Change *Notification message duration* back to the default value.

## 3.4. Preview variables in command palette
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

For the next tests, you need to **only run commands that are designed for your operating system**. For those tests that are not meant for your current operating system, ~~strike them through~~ by `~~surrounding them with tildes~~` and do not tick checkboxes.
- Windows:
	- [ ] **Test Windows shell: CMD**: This command is executed explicitly with CMD, and it should output an absolute path to *cmd.exe* file.
	- [ ] **Test Windows shell: PowerShell 5**: Uses explicitly PowerShell and it's old version 5. Should output *PS5 version: 5*, if the last version number is something else than *5*, then something is wrong. (PowerShell 5 might output strange extra characters that look like big dots. Just ignore them, the problem is known.)
	- [ ] **Test Windows shell: PowerShell Core**: Uses explicitly PowerShell and it's new version 6 or 7 (or even greater in the future). Should output *PSCore version: 6* (or 7 or above), if the last version number is *5*, then something is wrong.
- Linux:
	- [ ] **Test Linux shell: Bash**: Uses explicitly Bash and it should output an absolute path to a Bash binary file.
	- [ ] **Test Linux shell: Zsh**: Uses explicitly Zsh (Z shell) and it should output an absolute path to a Zsh binary file.

# 5. Clean up
- [ ] Execute **FINISH TEST** command, which will add your test results to the bottom of this file.
- Edit the name of this file:
	- [ ] Remove the *(incomplete)* mark.
	- [ ] Add the version number of Shell commands in parenthesis, e.g. *(0.5.0)*.
	- [ ] Add operating system/platform name (without a version), e.g *Windows*, *Linux* or *Mac*.
	- [ ] Add *ok* if **all** tests were successful, or *FAILED* if even just one test failed.
	- **Do not rename before you have executed the *FINISH TEST* command!**
	- Examples of a final file name:
		- *2021-09-26 Windows ok.md*
		- *2021-09-26 Linux FAILED.md*
- [ ] Check with Git that the only changes made in this vault/repository is your newly added report file. Other files - if edited(/created) - should have returned to their original states at this point.

# 6. Results
%% Needs to have an empty line below the Results heading. Otherwise test results will start at the same line with the heading.%%
