# How to install this test suite vault
While the vault can be downloaded from GitHub as a simple ZIP archive file, I highly recommend you to use [Git](https://git-scm.com) instead. Git is a *version control system*, meaning that it's a tool designed to log changes in files that reside in a specific directory. It also helps out to share changed files between people. Git is quite often used for software projects to keep track of code changes and distribute files between employees, but it can be used for other types of files and projects too. It can also serve as a backup solution to some extent. Git does have a learning curve if you don't know it already, but I think this test suite can be used with quite basic level skills of Git.

Benefits from using Git over downloading this vault as a ZIP file:
- It will be easier for you to update you copy of this vault whenever new changes are added to the original vault.
- It will be easier for you to submit your *test reports*, in case you end up creating them.

This guide will first point you to install git, and then give you instructions on how to clone this vault using Git.

# 1. Install Git
I won't cover git installation very deeply in this guide, to concentrate more on the test suite itself, but I'll provide links with instructions. Generally, Git can be used both via command line, and via graphical user interface client applications ([there are many available](https://git-scm.com/downloads/guis)). While GUI applications can sometimes be handy, this guide will use terminal commands instead due to the following reasons:
 - A user don't have to install a specific GUI client. Cross-platform compatibility is guaranteed when using terminal commands, as for git they are always the same, regardless of operating system.
 - Terminal commands can be faster to use, no need to wander in graphical windows.
 - As the *Shell commands* plugin itself is based on the concept of command-line commands, learning git commands can help develop skills that are useful with *Shell commands*.

You can still use GUI applications to do some things (e.g. commits), if you wish. Using git in command-line does not exclude the ability to use a GUI application, you can switch between them however you like.

## 1.1. For Linux
See command line installation instructions here: https://git-scm.com/download/linux

## 1.2. For macOS
See command line installation instructions here: https://git-scm.com/download/mac

## 1.3. For Windows
This link starts a download automatically, but it also offers you a few choices to select a version that you want to download (32/64-bit, portable or not): https://git-scm.com/download/win

# 2. Install the test suite
## 2.1. Get the repository's URL
1. Visit [Shell commands test suite's repository in GitHub](https://github.com/Taitava/obsidian-shellcommands-test-suite).
2. Click the green *Code* button.
3. Click *SSH*.
4. Click the copy icon.
	![[GitHub-get repository URL.png]]
5. Basically, you should now have the following in your clipboard: `git@github.com:Taitava/obsidian-shellcommands-test-suite.git`

## 2.2. Clone the repository
You need to decide in which directory you'll want to store the test vault. If you already have some Obsidian vaults in some directory, you might want to use that directory as the parent for the test vault.
1. Go to the directory where you'll want to store the test vault.
2. Create a new, empty folder named `Shell commands test suite`. We'll use this folder name through the whole installation guide.
3. Open up a [terminal emulator](https://en.wikipedia.org/wiki/Terminal_emulator) window.
4. In the terminal, go to the `Shell commands test suite` directory (you can use the `cd` command).
5. In the next command, there will be an easily forgotten dot `.` (separated by a space) at the end of the command. Pay close attention to include it in the command
6. Clone the test suite repository by executing the following command: `git clone git@github.com:Taitava/obsidian-shellcommands-test-suite.git .` and do remember the space and dot ` .` at the end! The dot tells Git to clone into the current directory. If you forget the dot, Git will create a new folder named *obsidian-shellcommands-test-suite* in your `Shell commands test suite` folder.
	![[Git clone command.png]]
7. You should now have this vault's files in the `Shell commands test suite` folder. Getting stuff from GitHub onto your machine is this easy. You can check what files your folder contains by issuing the `ls` command in the terminal (works in most Linux/Mac systems and in Windows PowerShell).
	![[Ls command.png]]
1. (You don't need to do this now, but I'll mention this shortly: If you later want to update your copy of the test suite - meaning to download possible new changes from GitHub - you can execute the command `git pull`. It will update your local files to have all the newest changes (unless you have modified the files locally)).

## 2.3 Open the vault in Obsidian
1. Launch Obsidian.
	- (If another Obsidian vault opens up, click *Open another vault* ![[Open another vault icon.png]] icon near the bottom left corner).
2. Click an *Open* button at *Open folder as vault*.
	![[Open folder as vault.png]]
3. Locate the `Shell commands test suite` folder.
	![[Locate Shell commands test suite folder.png]]
4. Click the *Manage workspaces* ![[Manage workspaces icon.png]] icon on the left.
5. Click *Load* next to *MyWorkspace*.

Now you should have [[Welcome]] note visible in both a preview and editor pane, and [[TestResults]] in a third pane. (You don't need to edit the [[Welcome]] note, but you'll need both editor and preview panes when you start to do testing, and you have a [[Test report file]] open).

![[Welcome note visible.png]]

Now the installation continues with installing (an optional) theme and *Shell commands* plugin.

## 2.4. Optional: Install *Red Graphite* theme

![[Red graphite theme.png]]

If you want to use this kind of mostly light background theme with dark sidebars, I can highly recommend you to install *Red Graphite*. It doesn't really matter, what theme you are using with this test vault. 

You can customise all appearance related settings, as `appearance.json` settings file is not stored in Git, to allow users to be able to define the layout based on their opinions.

1. Open Obsidian settings, and click the *Appearance* tab.
2. Change *Base theme* from *Dark* to *Light*.
	![[Theme settings.png]]
3. Under *Themes*, click the *Manage* button.
4. Under *Community themes*, type `red` in the search field.
	![[Community themes search.png]]
5. Click *Use*.

## 2.5. Install shell commands plugin
Testing can happen on two kinds of versions of the *Shell commands* plugin:
- **Stable** versions are available in the Obsidian's community plugins list and upgrading to them (or installing them) is easy.
- **Beta testing** versions are feature upgrades that still need more testing before they will be released as *stable* versions. They cannot be upgraded to (or installed) in the community plugins list, because they are **not** meant for serial use. Anybody can test them, but they need to know that they are testing something that has a higher risk to break things.

You need to decide, what kind of version of SC you will install. Beta installation has more work, and there is not always beta versions available for testing.

Whatever version you pick, you do not need to create your own shell commands. This test vault contains already predefined shell commands that can be used for testing.

### 2.5.1 Install a stable version
For installing a stable version, please see the installation instructions provided in [SC's README.md file](https://github.com/Taitava/obsidian-shellcommands#installation--usage). You can start from heading *Installation & usage*.

### 2.5.2 Install a beta testing version

An installation guide for beta versions is available at [SC's GitHub Discussions section](https://github.com/Taitava/obsidian-shellcommands/discussions/98). You can start from the heading *1.1. Installing BRAT and using it to install a beta version of SC*.

# 3. Install other requirements
# 3.1. Windows
- Install Windows Subsystem for Linux. TODO: Add link to instructions.

# 3.2. Linux
- Install Z-sh: `sudo apt update && sudo apt install zsh`.
- Install Wine: `sudo apt update && sudo apt install wine`.

# 4. Done
After all installations are done, you can start testing as per instructions written in [[Welcome.md]].