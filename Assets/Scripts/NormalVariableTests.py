import datetime
import os
import re
import sys
import urllib.parse
from typing import Union

# Get arguments.

arguments = sys.argv
arguments.pop(0) # The first argument is the script file's name, so discard it.

# Helper variables.
dateOnly = datetime.datetime.now().date()
dateAndTime = datetime.datetime.now()
dateAndTimeMinusOneSecond = dateAndTime - datetime.timedelta(seconds=1)
datetimeFormat = "%Y-%m-%d %H:%M:%S"
vaultPath = os.path.dirname(os.getcwd()) # dirname() = get the PARENT directory. Need do this because current working directory is 'Sandbox'. TODO: Modify the executor shell command so that cwd is vault root. I tried to use "cd .." before the "python3" command, but then the execution did nothing: no output in stdout nor stderr, and no error in Obsidian's debug console.
reportFileName = str(dateOnly) + " (incomplete).md"
reportsFolderName = "Performed tests"
reportsFolderPath = os.path.join(vaultPath, reportsFolderName)
yamlContentWithoutDashes = """# Do not change these values during testing.
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
  - last-item"""

# Define correct values and received values.
expectedValues = {
    "{{caret_paragraph}}": "2. Select this text: TESTSELECTION",
    "{{clipboard}}": "TESTCLIPBOARD",
    "{{date:YYYY-MM-DD HH:mm:ss}}": [
        dateAndTime.strftime(datetimeFormat), # Accept either current date & time ...
        # ... OR ...
        dateAndTimeMinusOneSecond.strftime(datetimeFormat), # ... date & time one second ago.
    ],
    "{{file_extension:no-dot}}": "md",
    "{{file_extension:with-dot}}": ".md",
    "{{file_name}}": reportFileName,
    "{{file_path:absolute}}": os.path.join(reportsFolderPath, reportFileName),
    "{{file_path:relative}}": os.path.join(reportsFolderName, reportFileName),
    "{{file_uri}}": "obsidian://vault/Shell%20commands%20test/Performed%20tests%2F" + urllib.parse.quote(reportFileName, safe="()"), # Don't encode parenthesis
    "{{folder_name}}": reportsFolderName,
    "{{folder_path:absolute}}": reportsFolderPath,
    "{{folder_path:relative}}": reportsFolderName, # This should actually be path from vault root, not just the folder name, but in practise they happen to be the same, because the "Performed tests" happens to reside directly in the vault root, so this actually works.
    "{{new_note_folder_name}}": reportsFolderName, # New notes are set up to be created in the reports folder.
    "{{new_note_folder_path:absolute}}": reportsFolderPath,
    "{{new_note_folder_path:relative}}": reportsFolderName, # Same comment as for {{folder_path:relative}} above.
    "{{selection}}": "TESTSELECTION",
    "{{tags}}": "frontmatter-tag, this-should-not-appear-twice, inline-tag",
    "{{title}}": str(dateOnly) + " (incomplete)",
    "{{vault_path}}": vaultPath,
    "{{workspace}}": "MyWorkspace",
    "{{yaml_content:no-dashes}}": yamlContentWithoutDashes,
    "{{yaml_content:with-dashes}}": f"""---
{yamlContentWithoutDashes}
---""",
    "{{yaml_value}}": "first value.inner value.last value.first-item.second-item.last-item.count:3",
    "Escaping test": """>,.-;:§+´½!'"#¤%&/()|=?`@`£$€{[]}\\\\¨^~*åäö*""", # No < because it brokw Markdown table for some reason. # FIXME: This test kinda works, but the output looks very different in Obsidian: `` <\>,.-;:º+┤¢!'"#ñ%&/()=?`@`ú$Ç{[]}\\¿^~*Õõ÷* `` I.e. look really different. That said, I assume the equality test still works - just input or output encoding is wrong.
}
testValues = {
    "{{caret_paragraph}}": arguments.pop(0),
    "{{clipboard}}": arguments.pop(0),
    "{{date:YYYY-MM-DD HH:mm:ss}}": arguments.pop(0),
    "{{file_extension:no-dot}}": arguments.pop(0),
    "{{file_extension:with-dot}}": arguments.pop(0),
    "{{file_name}}": arguments.pop(0),
    "{{file_path:absolute}}": arguments.pop(0),
    "{{file_path:relative}}": arguments.pop(0),
    "{{file_uri}}": arguments.pop(0),
    "{{folder_name}}": arguments.pop(0),
    "{{folder_path:absolute}}": arguments.pop(0),
    "{{folder_path:relative}}": arguments.pop(0),
    "{{new_note_folder_name}}": arguments.pop(0),
    "{{new_note_folder_path:absolute}}": arguments.pop(0),
    "{{new_note_folder_path:relative}}": arguments.pop(0),
    "{{selection}}": arguments.pop(0),
    "{{tags}}": arguments.pop(0),
    "{{title}}": arguments.pop(0),
    "{{vault_path}}": arguments.pop(0),
    "{{workspace}}": arguments.pop(0),
    "{{yaml_content:no-dashes}}": arguments.pop(0),
    "{{yaml_content:with-dashes}}": arguments.pop(0),
    "{{yaml_value}}": arguments.pop(0),
    "Escaping test": arguments.pop(0),
}

def performTests():
    # Print table header.
    print()
    print("| Variable | Result | Received | Expected |")
    print("| -------- | ------ | -------- | -------- |")

    # Perform tests.
    countFailed = 0
    for variableName in expectedValues:
        expectedValue = expectedValues[variableName]
        testValue = testValues[variableName]
        if type(expectedValue) == list:
            # expectedValue is an array of possible values. I.e. testValue can be any of the array's values.
            testEqualsExpected = testValue in expectedValue
        else:
            # Normal single value test.
            testEqualsExpected = testValue == expectedValue
        resultText = "ok" if testEqualsExpected else "**FAILED**"
        print("| " + formatVariableName(variableName) + " | " + resultText + " | " + formatTestValue(testValue) + " | " + formatTestValue(expectedValue) + " |")
        if not testEqualsExpected:
            countFailed += 1
    overallResultText = "ALL&nbsp;PASSED" if countFailed == 0 else str(countFailed) + "&nbsp;FAILED"
    print("| **Summary:** | **" + overallResultText + "** |||")
    print()

def formatTestValue(value: Union[str, list]):
    # If value is a list, convert to string.
    if type(value) == list:
        value = "Either `" + ("`, `".join(value[:-1])) + "` or `" + value[-1] + "`"

    # Convert possible linebreaks to <br>.
    value = re.sub(r"\r\n|\r|\n", "<br>", value)

    # Escape possible | characters.
    value = value.replace("|", "\\|")

    return "<small>" + value + "</small>"

def formatVariableName(variable: str):
    if re.match(r"^\{\{", variable):
        # This is a {{variable}}.
        return "`" + variable + "`"
    else:
        # This actually is not a variable, but e.g. "Escaping text".
        return variable

performTests()