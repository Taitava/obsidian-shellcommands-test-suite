#! /usr/bin/python3
import datetime
import os
import sys

# Receive arguments from stdin.
# FIXME: Non-ascii characters do not work correctly.
templateFilePath = input()
targetFilePath = input()
testAuthorName = input()
operatingSystem = input()
obsidianVersion = input()
pluginVersion = input()
testSuiteVersion = input()
openingAttribute = input() # Can be: "current-tab", "new-tab", "new-pane", or "new-window"

if pluginVersion != testSuiteVersion:
    print("Plugin version is " + pluginVersion + ", but the test suite is aimed for version " + testSuiteVersion + ".", file=sys.stderr)
    sys.exit(1)

with open(templateFilePath, "r", encoding="utf-8", newline="\n") as templateFile:
    testReportContent = templateFile.read()

    # Author.
    testReportContent = testReportContent.replace("Test author: **YOUR_NAME/NICK/LINK_HERE**", f"Test author: **{testAuthorName}**")

    # Operating system.
    testReportContent = testReportContent.replace("Operating system: **OS_name_here OS_version_here**", f"Operating system: **{operatingSystem}**")

    # Obsidian version.
    testReportContent = testReportContent.replace("Obsidian version: **Obsidian_version_here**", f"Obsidian version: **{obsidianVersion}**")

    # Shell command version.
    testReportContent = testReportContent.replace("Shell commands version: **Shell commands version here**", f"Shell commands version: **{pluginVersion}**")

    # Date.
    testReportContent = testReportContent.replace("Test date: **{{date:YYYY-MM-DD}}**", f"Test date: **{datetime.datetime.now().date()}**")

    # Write the result to a new file.
    with open(targetFilePath, "w", encoding="utf-8", newline="\n") as targetFile:
       targetFile.write(testReportContent)

# For debugging:
# print(testReportContent)

# Tell Obsidian to open the file:
if openingAttribute == "current-tab":
    # "current-tab" is unknown to the SC plugin in Obsidian, use an empty string instead.
    openingAttribute = ""
if openingAttribute:
    # Precede openingAttribute with a colon :
    openingAttribute = ":" + openingAttribute
print(targetFilePath + openingAttribute)