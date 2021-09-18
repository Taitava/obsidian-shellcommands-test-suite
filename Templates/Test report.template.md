# BASIC INFORMATION
Test author: **YOUR_NAME/NICK/LINK_HERE**
Operating system: **OS_name_here OS_version_here**
Obsidian version: **Obsidian_version_here**
Shell commands version: **Shell commands version here**
Test date and start time: **{{date:YYYY-MM-DD HH:mm}}**

# [[1. Preview and execute shell commands]]
## 1.1. Preview shell commands
Inspect closely that variables have correct values!
- [ ] Clipboard {{clipboard}} to file
- [ ] Date and time {{date:YYYY-MM-DD HH:mm:ss}} to file
- [ ] File name {{file_name}} to file
- [ ] Absolute file path {{file_path:absolute}} to file
- [ ] Relative file path {{file_path:relative}} to file
- [ ] Folder name {{folder_name}} to file
- [ ] Absolute folder path {{folder_path:absolute}} to file
- [ ] Relative folder path {{folder_path:relative}} to file
- [ ] Selection {{selection}} to file
- [ ] Title {{title}} to file
- [ ] Vault path {{vault_path}} to file
- [ ] Workspace {{workspace}} to file

## 1.2 Execute shell commands
Inspect closely that their output to TestResults.md is a) correct, and b) matches what you saw in preview (e.g. `{{date:YYYY-MM-DD HH:mm:ss} }` %% The extra space here is intentional: Obsidian Templates should not parse this variable. %% should have exactly same seconds)!
- [ ] Clipboard {{clipboard}} to file
- [ ] Date and time {{date:YYYY-MM-DD HH:mm:ss}} to file
- [ ] File name {{file_name}} to file
- [ ] Absolute file path {{file_path:absolute}} to file
- [ ] Relative file path {{file_path:relative}} to file
- [ ] Folder name {{folder_name}} to file
- [ ] Absolute folder path {{folder_path:absolute}} to file
- [ ] Relative folder path {{folder_path:relative}} to file
- [ ] Selection {{selection}} to file
- [ ] Title {{title}} to file
- [ ] Vault path {{vault_path}} to file
- [ ] Workspace {{workspace}} to file

# [[2. The rise and fall of a temporary shell command]]
1. Go to Shell command settings (`Ctrl/Cmd + ,`).
2. [ ] Create a new shell command. This can be something simple with one variable, like: `echo {{title}}`. The command does not need to actually do anything.
3. [ ] Check that the settings view shows a preview for this shell command, e.g. *echo TestResults*.
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
## Working directory
1. [ ] At the beginning, *Working directory* should be *Sandbox*. If it's not, change it.
2. Go through the following values for *Working directory* and run a shell command named *Test working directory* (this will insert working directories into [[TestResults]]):
3. - [ ] *Sandbox*
4. - [ ] (An empty value, so that we refer to the vault's root folder.)
5. - [ ] On Windows: *C:\WINDOWS\Temp*. On Linux: */tmp*. On Mac: I'm not sure, maybe */tmp* too. (We need to test an absolute directory too. This test should not write anything in the working directory, but still use a temporary folder just in case. The test does write into a file in the Sandbox folder, but should not write elsewhere regardless of what the working directory happens to be).
6. [ ] After you have run the *Test working directory* with all of the above situations, check that [[TestResults]] contains the correct absolute paths.
7. [ ] Finally, make sure that you change *Working directory* back to *Sandbox*.

## Error message duration
The default value of *Error message duration* is 20 seconds.
1. [ ] Execute the command *Doomed to eternal failure*. It just executes *cd NonExistingFolder*, which throws an error: *Command failed: cd NonExistingFolder*. See that the error message shows up and is visible around 20 seconds.
2. [ ] Change *Error message duration* to 1 second, execute the same command again and see that the error message shows up, but disappears quicly.
3. [ ] Change *Error message duration* back to the default value.

## Preview variables in command palette
This setting should be on by default.
1. [ ] Open up command palette, type *execute* and check quickly that all commands that start with *Shell commands: Execute:* have parsed all their possible variables (= there are no `{{`/`}}` structures visible). Exception: Some variables cannot be parsed in every situation, such as `{{selection}}` when the active pane is not in edit mode, or `{{file_name}}` when the focus is on graph view. It's ok if these exceptional variables are not parsed, but you should check that most variables are parsed.
2. [ ] Go to shell command settings, and turn *Preview variables in command palette* off.
3. [ ] Open up command palette again, type *execute* and check quickly that all commands that start with *Shell commands: Execute:* have variable names visible, meaning that `{{`/`}}` structures should be visible.
4. [ ] Go to shell command settings, and turn *Preview variables in command palette* back on.

# Clean up
- [ ] Execute FINISH TEST command, which will add your test results to the bottom of this file.

# Results
%% Needs to have an empty line below the Results heading. Otherwise test results will start at the same line with the heading.%%
