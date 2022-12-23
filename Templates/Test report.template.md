---
# Do not change these values during testing.
test_suite_version: 0.18.0
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
- [ ] **Date and time {{date:YYYY-MM-DD HH:mm:ss} } to file**
- [ ] **File name {{file_name}} to file**: Check that the preview of the command shows escape characters (\` or \\ depending on your OS/shell) in front of spaces, dashes and dots in the file name. This ensures that escaping special characters works correctly.

## 1.2 Execute shell commands
\*) These commands' output handling is done in [realtime mode](https://publish.obsidian.md/shellcommands/Output+handling/Realtime+output+handling). It should not affect the outcome, but expands testing to that output handling mode, too.
- [ ] **[Caret paragraph {{caret_paragraph}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=1bj54ofqvt)**
- [ ] **[Caret position {{caret_position}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=01jk6q6kt5)**: Should give something like `Caret position: 45:60 (line: 45, column:60)`. The real numbers do not matter as they depend on where your caret happens to be.
- [ ] **[Clipboard {{clipboard}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=w8cgzuq66x)**: (You can copy this to clipboard: TESTCLIPBOARD).
- [ ] **[Date and time {{date:YYYY-MM-DD HH:mm:ss} } to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=cvdgs01k3r)**: Check that the **seconds** are the same as they were during preview!
- [ ] **[File extension {{file_extension:with-dot}}/{{file_extension:no-dot}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=hcia4yjtcp)**: The result should be: *File extension: with dot: 
.md / no dot: md*
- [ ] **[File name {{file_name}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=kj1jupcn7k)**: Check that the file name does not contain any escape characters like: \` or \\.
- [ ] **[Absolute file path {{file_path:absolute}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=wj9xk8hlaq)**: If you are on **Mac or Linux**, please ensure that the path starts with `/`, e.g. `/Users/.../SomeFile.md`. If it's without a leading `/` (e.g. `Users/.../SomeFile.md`), then there is a bug. Add a comment here and leave the checkbox unchecked. On Windows: Check that directories are separated by `\`, not `/`.
- [ ] **[Relative file path {{file_path:relative}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=vcj4wpa02y)**
- [ ] **[File URI {{file_uri}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=hkcskjz8cb)**
- [ ] **[Folder name {{folder_name}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=4gzrhksyp7)**
- [ ] **[Absolute folder path {{folder_path:absolute}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=4kac7s6v56)**: **Same check** as with *Absolute file path* above.
- [ ] **[Relative folder path {{folder_path:relative}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=435bcuiz11)**
- [ ] **[New note folder name {{new_note_folder_name}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=0708g3m0bg)**: Should be *Performed tests*.
- [ ] **[Absolute new note folder path {{new_note_folder_path:absolute}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=8j40a7ah1h)**
- [ ] **[Relative new note folder path {{new_note_folder_path:relative}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=zyglscbzhx)**
- [ ] \* **[Selection {{selection}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=3ng31p6gr0)**: Edit mode needs to be on! (You can select this text: TESTSELECTION).
- [ ] \* **[Tags {{tags}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=7avhlqk80e)**. #inline-tag #this-should-not-appear-twice . If this tag appears twice in the result, leave a comment and do not tick the box.
- [ ] \* **[Title {{title}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=acmo3jqv6g)**
- [ ] \* **[Vault path {{vault_path}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=ltxwi1hu05)**
- [ ] \* **[Workspace {{workspace}} to file](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=qf19834h9s)**
- [ ] **[Test {{file content}}](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=au049jz2sy)**: You should see the current file's content **with YAML**. (This test and the similar one below uses `stdin` to pass the variable content to shell, so the `stdin` feature gets tested, too).
- [ ] **[Test {{note content}}](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=zcxdt1jp1f)**: You should see the current file's content **without YAML**.
- [ ] **[Character encoding test](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=ozilge8kih)**: This outputs *Test non-ASCII characters: Å Ä Ö* to *TestResults.md*. **Check that Å Ä Ö show up correctly in the file.** If you see something strange (e.g. �), the test is failed and you should not tick the checkbox in this test report.
- [ ] **[Test to ignore error code](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=qm8y3vwg8k)**: This command should do absolutely nothing. It tries to change directory (`cd`) to *NonExistingFolder*, which fails with error code `1` (on Windows), or `2` (on Linux) . I'm not sure about the code on Mac. The command is defined to ignore error codes `1` and `2`. Tick this checkbox if nothing happened during the execution, but do not tick, if you saw an error message popping up.
- [ ] **[Test empty command](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=rejgzfrnyz)**: This one should always give an error message saying: *The shell command is empty*. If it  does not give an error message at all, **or if the message is different**, comment here and do not check the box. If the error message was correct, tick this checkbox.
- **Test output insertion**:
	- This command inserts the following text to a currently active file, at caret position: *Text output test*. Be sure to have this **test report file** active and in **edit mode**. Check that a text insertion/replacement process succeeds:
	- [ ] Place the caret after the colon and execute the command to see how *inserting* works: 
	- [ ] Select some word in this sentence and execute the command to see how *replacing* works.
- [ ] **[Test output to stderr, with exit code 0](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=imsi0fzrit)**: This command should give the following output to an error balloon: *\[0\]: This goes to stderr*. Pay attention to the **\[0\]** part! It should not be *\[null\]*, and the number should not be anything else than zero. This command uses exit code 0, which indicates that the command actually succeeded, but it has the twist that even when the command succeeded, it directed its output to *stderr* instead of the normal *stdout*. SC should be able to differentiate error output despite of an exit code 0 that indicates a succeeded shell command execution.
- [ ] **Test output to top**: Make sure [[TestResults]] file is open and active! This command will insert *TEXT TO TOP* to the currently active file.
- [ ] **Test output to bottom**: Make sure [[TestResults]] file is open and active! This command will insert *TEXT TO BOTTOM* to the currently active file.
- [ ] **[Test output to status bar](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=5w4m6q8d8e)**: Check that status bar will contain output text. Hover over the status bar with mouse and ensure that more output lines pop up.
- [ ] **[Test output to clipboard](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=5lk1z1h1ds)**: After running the command, paste clipboard content here: 
	- The pasted content should be *Hello clipboard!*. If it's something else, write a comment and do not tick the checkbox.
	- A notification balloon should also appear, telling what was copied to the clipboard. If it does not appear or the content is wrong, write a comment and do not tick the checkbox.
- **Test output to modal**: Make sure [[TestResults]] file is active when executing the command! After executing the command, click all of the *Redirect* buttons in the output modal, and see that each of them outputs the text MODAL OUTPUT in the correct channel:
	- [ ] *Status bar*
	- [ ] *Current file: caret position*
	- [ ] *Current file: top*
	- [ ] *Current file: bottom*
	- *Open files* does not need to be tested here.
	- [ ] *Clipboard*
- [ ] **[Test output using Open a file 1](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=5hvv4ee88g)**: This opens [[Welcome.md]] file in a new pane. Check that the file opens **and** that a new pane is created.
- [ ] **Test output using Open a file 2**: Keep the previously opened pane focused! This opens [[README.md]] file and places the caret on line 2, column 3. Make sure the file opens in the current pane (which previously had [[Welcome.md]] open) **and** that the caret is placed in the mentioned position.
- **Test output using Open a file 3**: Keep the previously opened pane focused! This opens [[Welcome.md]] again, this time with three selections:
	- [ ] Line 4 is selected completely. I.e. *Welcome!* is selected.
	- [ ] Line 7 contains a selection between columns 6 to 10. I.e. *test* is selected.
	- [ ] Line 7 also starts a selection 10 columns before the end of the line, and the selection extens to line 6, column 5. I.e. *improved*, two newlines and *This* are selected.
	- The above-mentioned  selected texts might be slightly inaccurate in case the content of [[Welcome.md]] changes after writing this test.
- **Test output using Open a file 4**: Keep the previously opened pane focused! This opens and creates a new file named *A file that did not exist before.md* in the *Sandbox* folder.
	- [ ] Before executing the command, make sure the file **does not exist**.
	- [ ] Execute the command and make sure the file creation succeeds.
	- [ ] Finally delete the file. You can now close the newly created tab, it's not needed anymore.
- [ ] **[Test output using Open a file 5](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=awn0zh7t5u)**: This should open [[Welcome.md]] in a new **tab**. No selections are made.
- [ ] **[Test output using Open a file 6](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tlq9kj69h5)**: This should open [[Welcome.md]] in a new **window**. No selections are made.
- [ ] **[Test $& variable](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=asdmfqbx5d)**: Symbol pair `$&` has caused problems in variable parsing when they appear in the variable's value (and some other `$` combinations too). Outputs:
	- `Test $& variable: $&` when the test is correct. (Tick the checkbox).
	- `Test $& variable: {{!passthrough:$&}}` when the test fails. Do not tick, leave a comment.
- [ ] **[Two 🐓 emojis](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=sr8mp9lpbb)**: This test should output two 🐓 emojis correctly. The first one has been written directly in the shell command, while the second one comes via a `{{passthrough:🐓}}` variable, which might break the emoji if variable parsing regular expressions fail. [Relates to bug #171](https://github.com/Taitava/obsidian-shellcommands/issues/171)
	- Incorrect result: `🐓��`
	- Correct result: 🐓🐓
- [ ] **[Escaping test 1](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=xkrjqxs3mv)**: This command tests a wide range of special characters that should be escaped. Two things are tested: **a)** The special characters should not do anything special, they should not prevent the test from outputting all the characters; **b)** When the characters are output to [[TestResults]], they should be presented there **without** any escaping characters (`\` or `` ` ``), with the exception that `\` and `` ` `` do appear in the result as individual test characters - they just should not appear in fron of every other special character.
	- Wrong output: ``Escaping test 1: \<\>\,\.\-\;\:\§\+\´\½\!\'\"\#\¤\%\&\/\(\)\=\?\`\@\`\£\$\€\{\[\]\}\\\\\¨\^\~\*\å\ä\ö\*`` (a shell should remove the escape characters).
	- Wrong, if the command tried to do something strange.
	- Correct output: ``Escaping test 1: 
<>,.-;:§+´½!'"#¤%&/()=?`@`£$€{[]}\\¨^~*åäö*``
- [ ] **[Escaping test 2](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=dk2axoxhd0)**: This command tests actually the same thing as *Escaping test 1*, but it focuses more on to test that an escaped `>>` symbol pair does not cause output to be written into [[TestResults]]. So, unlike many other tests, this test **should not output anything to TestResults.md**. Instead, the test is passed, if it creates a notification balloon saying: *This should NOT be written to TestResults.md!!! >> TestResults.md*.
- [ ] **[Test YAML value](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=jr2cpaherx)**: Should output the following to [[TestResults]]: `YAML test: A1. 
first_value A2. inner_value A3. last_value B) first: first-item B) second: second-item B) last: last-item B) count: 3` . If even a single difference is found, leave a comment and do not tick the checkbox.
- [ ] **[Test PATH additions](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=g7gauo1ds6)**: Opens up a modal showing the content of the `PATH` environment variable.
	- On Windows the output should contain two additional directories:
		1. *WindowsExtraPath1* should be present **near the beginning** of the output. Not as the first directory, but after a PowerShell directory.
		2. *WindowsExtraPath2* should be present **at the end** of the output.
	- On linux (and macOS) the output should contain one additional directory:
		- *LinuxAndMacExtraPath* should be present **at the end** of the output.
	- The reason for outputs being different in different operating systems is that in order to test to different appending mechanisms, I needed to use two different operating system settings fields. I can't make separate test shell commands for these, because the `PATH` additions are implemented to happen for all shell commands, and no shell command specific settings exist for them.
- [ ] **[Test multiline shell command](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=y2dtq5wuxy)**: This should output the following, each word on its own line:
	```markdown
	Multiline
	shell
	command
	```
- [ ] **[A long running shell command](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=2jk7adqi4s)**: You should see a notification saying: *Executing: A long running shell command*. The notification should appear around a couple of seconds after starting the execution (because it's only shown when a shell command execution takes an extended period of time). The notification should disappear the same time when the shell command finishes execution and outputs: *Waited for 5 seconds.*
- [ ] **[Test output wrapping](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=morocg0jlo)**: Opens up a modal showing the following output text: *Output wrapped in code block.* The output should also show texts *Executed on* and *File name*. Check that all of the variables work ok, and that special characters in the *date* and *file name* values are **not escaped**.
- **Realtime tests**:
	- Each of these tests should output five lines to their specific output channels. There should always be one second pause between each line appearing. If all of the lines appear at once, do not tick a checkbox!
	- [ ] **[Realtime test: Notification balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tm2ulm7r2m)**
	- [ ] **[Realtime test: Error balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=st8k313wkf)**
	- [ ] **Realtime test: Current file: caret position**: Make sure [[TestResults.md]] has focus when executing this!
	- [ ] **Realtime test: Current file: top**: Make sure [[TestResults.md]] has focus when executing this!
	- [ ] **Realtime test: Current file: bottom**: Make sure [[TestResults.md]] has focus when executing this!
	- [ ] **[Realtime test: Open files](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=x9mb2l65cf)**: Will open a new Obsidian window and five tabs, all of which will contain [[Welcome.md]]. One second should pass between each tab opening.
	- [ ] **[Realtime test: Status bar](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=9a98pvcn6p)**: Status bar will show always the latest line, but hover over it to see all lines.
	- [ ] **[Realtime test: Ask after execution](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=vn29xcs8xs)**: See that output lines appear to the modal with one second pause between each line. No need to click any redirection buttons.
	- [ ] **[Realtime test: Clipboard](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=risjcw3y5m)**: You should see five notifications telling that output has been copied to clipboard.
```
Paste the clipboard content here after the execution has finished:

```
- **Terminate long running shell commands**
	- These tests do not need their own shell commands, they just borrow other shell commands. You should be able to stop their execution before they end theirselves.
	- [ ] **[Realtime test: Notification balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tm2ulm7r2m)**: A stop icon shows up in notification balloon that shows output text. Click it to stop the execution before _Realtime 5_ line is outputted.
	- [ ] **[Realtime test: Notification balloon](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=tm2ulm7r2m)**: Execute it again, but this time stop it from an icon in another notification balloon with content _Executing: Realtime test: Notification balloon_. This balloon appears after the shell command been executing a couple of seconds.
	- [ ] **[Realtime test: Ask after execution](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=vn29xcs8xs)**: Stop the executing by clicking a stop icon in the modal.


# [[2. The rise and fall of a temporary shell command]]
1. Go to Shell command settings (`Ctrl/Cmd + ,`).
2. [ ] Create a new shell command. This can be something simple with one variable, like: `echo {{file_name}}`. The command does not need to actually do anything.
3. [ ] When typing a variable name, use an [autocomplete menu](https://publish.obsidian.md/shellcommands/Variables/Autocomplete/Autocomplete) to do it and check that the menu works correctly.
4. [ ] Check that the settings view shows a preview for this shell command, e.g. *echo TestResults.md*.
5. [ ] Define an alias for the command, e.g. *Echo test*.
6. [ ] When you opened the modal for defining the alias, the alias field should have been focused automatically.
7. [ ] Check that the settings view shows the alias text instead of *Shell command without alias*.
8. [ ] Go to *Hotkeys* settings and search for this new shell command (make sure it can be found there).
9. [ ] Define the following hotkey for the new shell command: Ctrl/Cmd + M.
10. [ ] Restart Obsidian by pressing Ctrl/Cmd + R (a custom hotkey defined in this test vault). This is to make sure that all settings are stored and loaded correctly.
11. [ ] Go to shell command settings again and check that the new command still exists.
12. [ ] Check that the shell command should display the following hotkey text below the command field: *Ctrl + M* (if you are on Windows/Linux) or *Cmd + M* (if you are on Mac). Pay attention that the *Ctrl*/*Cmd* part must be correct according to your operating system!
13. [ ] Click the delete command button to open a confirmation window.
14. [ ] Check that the confirmation window displays correctly the command's name and alias.
15. [ ] Click *Yes, delete* and ensure that the command was really deleted.
16. [ ] Restart Obsidian again by pressing Ctrl/Cmd + R.
17. [ ] Go to shell command settings again and check that the new command does not exists any more.

# [[3. Miscellaneous settings]]
Go to shell commands settings and follow the below instructions to test each of these settings:
## 3.1. Working directory
1. [ ] At the beginning, *Working directory* should be *Sandbox*. If it's not, change it.
2. Go through the following values for *Working directory* and run a shell command named **[Test working directory](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=h1i3hjdujv)** (this will insert working directories into [[TestResults]]):
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
	- *Macintosh command version executed.*

For the next tests, you need to **only run commands that are designed for your operating system**. For those tests that are not meant for your current operating system, just delete them.
- Windows:
	- [ ] **[Test Windows shell: CMD](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=1w4y2bpbmk)**: This command is executed explicitly with CMD, and it should output an absolute path to *cmd.exe* file.
	- [ ] **[Test Windows shell: PowerShell 5](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=hml8qvuqrs)**: Uses explicitly PowerShell and it's old version 5. Should output *PS5 version: 5*, if the last version number is something else than *5*, then something is wrong. (PowerShell 5 might output strange extra characters that look like big dots. Just ignore them, the problem is known.)
	- [ ] **[Test Windows shell: PowerShell Core](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=r1erl29mnq)**: Uses explicitly PowerShell and it's new version 6 or 7 (or even greater in the future). Should output *PSCore version: 6* (or 7 or above), if the last version number is *5*, then something is wrong.
- Linux / Macintosh:
	- [ ] **[Test Linux/Mac shell: Bash](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=cxircsux3k)**: Uses explicitly Bash and it should output an absolute path to a Bash binary file.
	- [ ] **[Test Linux/Mac shell: Dash](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=pm9qf3zrfy)**: Uses explicitly Dash and it should output an absolute path to a Dash binary file.
	- [ ] **[Test Linux/Mac shell: Zsh](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=0wuvfv0nzr)**: Uses explicitly Zsh (Z shell) and it should output an absolute path to a Zsh binary file.

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
5. [ ] *Event: File created*: Create a new file in *Sandbox*. It will first have the name *Untitled.md*. [[TestResults.md]] should now have a new line saying: *New file created: Untitled.md*.
6. [ ] *Event: File renamed*: Give the new file another name: *NewNote.md*. [[TestResults.md]] should now have a new line saying: *File renamed from Untitled.md to NewNote.md*.
7. [ ] *Event: File content modified*: Write something into the *NewNote.md* file. The status bar should show the following message: *File content modified: NewNote.md*. There is a time at the end to indicate when the change happened.
8. [ ] *Event: Folder created*: Create a new folder in *Sandbox*. It will first have the name *Untitled*. [[TestResults.md]] should now have a new line saying: *New file created: Untitled*.
9. [ ] *Event: Folder renamed*: Give the new folder another name: *NewFolder*. [[TestResults.md]] should now have a new line saying: *Folder renamed from Untitled to NewFolder*.
10. [ ] *Event: File moved*: Move *NewNote.md* to *NewFolder*. [[TestResults.md]] should now have a new line saying: *File moved from Sandbox\NewNote.md to Sandbox\NewFolder\NewNote.md*.
11. [ ] *Event: Folder moved*: Create yet another folder in *Sandbox* and rename it to *ParentFolder*. Move *NewFolder* to *ParentFolder*. [[TestResults.md]] should now have a new line saying: *Folder moved from Sandbox\NewFolder to Sandbox\ParentFolder\NewFolder*.
12. [ ] *Event: File deleted* and *Event: Folder deleted*: Delete *ParentFolder*. Deleting it should also delete *NewFolder* and *NewNote.md*. [[TestResults.md]] should now have the following new lines (the order may differ):
	- *Folder deleted: NewFolder*
	- *File deleted: NewNote.md*
	- *Folder deleted: ParentFolder*

Finally:
- [ ] Go to settings and turn *Enable events* off in the *Events* tab.
- [ ] Try to switch panes. See that *Event: After switching the active pane* should **not** work.
- [ ] Switch the setting back on.
- [ ] Check that *Event: After switching the active pane* now **works**.

# 6. Prompts and custom variables
## 6.1. Prompts
Execute the command **[Test custom variables and a prompt](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=dqnuqf8fo4)**. A prompt will appear to ask a few values.

Check the following things in the prompt:
1. [ ] The prompt's description shows a week day name instead of `{ {date:dddd}}`.
2. [ ] The shell command preview text shows a week day name instead of `{ {date:dddd}}`.
3. [ ] The shell command preview text shows inputted values correctly when you type them. Also, the current field's value is bolded in the shell command.
4. [ ] The shell command preview text shows variable names correctly when you click the small toggle icon. Also, the current field's variable name is bolded in the shell command.
5. [ ] *Field using variables* shows the currently active file's name in it's description text.
6. [ ] *Field using variables* has the current year as its default value when the prompt is opened.
7. [ ] Try to submit the prompt values **without** inputting a value to *Mandatory field*. The submission should be **prevented** with an error message requiring the field to be filled.
8. [ ] After the error message, fill the field and check that submitting the prompt works ok.
9. [ ] Check that a result similar to the following was written to [[TestResults.md]]:
	```
	Day of week: Thursday
	Prompt mandatory field: example
	Prompt field with a default value: Default
	Prompt optional field: 
	Prompt field using variables: 2022 TestResults.md
	```
	Ensure the first line contains a day of week, the second line contains *example*, the third line contains *Default*, the fourth line doesn't contain anything after the colon `:`, and the last line contains the current year and a file name.
10. [ ] Check that the *Custom variables* pane lists the values of custom variables relevant to the four fields of the prompt. Make sure the values are the same as in the output to [[TestResults.md]].

## 6.2. Custom variables (via Shell commands URI)
1. *Test Shell commands URI*: This shell command is excluded from Obsidian's command palette, so it can only be executed via the following URI link: [Test Shell commands URI](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=2sb4p6r9b4&_uri_custom_variable_1=Hello&_uri_custom_variable_2=world!). After clicking it, [[TestResults.md]] should have the following new lines:
	- [ ] *Custom variable 1: Hello*
	- [ ] *Custom variable 2: world!*
2. Test setting custom variables via a link without executing a shell command. Click [this link](obsidian://shell-commands?_uri_custom_variable_1=Variable%20values%20set&_uri_custom_variable_2=without%20executing%20anything). Check from the *Custom variables* pane that the following variables have the following values:
	- [ ] *Custom variable 1: Variable values set*
	- [ ] *Custom variable 2: without executing anything*

# 7. When there is no settings file
This section will test that the plugin works correctly when no `data.json` settings file exist. The plugin should load default settings.

1. [ ] Execute the command **[Open the plugin folder in system explorer](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=fsmbhs5vqc)**.
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

# 8. Clean up
- [ ] Execute **[FINISH TEST](obsidian://shell-commands/?vault=Shell%20commands%20test&execute=796vz9pyd6)** command, which will add your test results to the bottom of this file.
- The command will rename this test report file:
	- It removes the *(incomplete)* mark.
	- It adds the version number of Shell commands in parenthesis, e.g. *(0.5.0)*.
	- It adds operating system/platform name, e.g *Windows*, *Linux* or *Mac*.
	- It adds *ok* if **all** tests were successful, or *FAILED*.
	- Examples of a final file name:
		- *2021-09-26 (0.4.0) Windows ok.md*
		- *2021-09-26 (0.4.0) Linux FAILED.md*
		- *2021-11-06 (0.7.0-beta1) Linux ok.md*
- [ ] Check with Git that the only changes made in this vault/repository is your newly added report file. Other files - if edited(/created) - should have returned to their original states at this point.
- Finally, you should commit this new report file.

# 9. Results
%% Needs to have an empty line below the Results heading. Otherwise test results will start at the same line with the heading.%%
