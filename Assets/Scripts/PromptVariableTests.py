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
dateAndTime = datetime.datetime.now()
sandboxFolderName = "Sandbox"

# Define correct values and received values.
expectedValues = {
    "{{_mandatory_field}}": "example",
    "{{_field_with_default_value}}": "Default",
    "{{_optional_field}}": "", # Expected to be left empty.
    "{{_field_using_variables}}": dateAndTime.strftime("%Y") + " " + sandboxFolderName,
}
testValues = {
    "{{_mandatory_field}}": arguments.pop(0),
    "{{_field_with_default_value}}": arguments.pop(0),
    "{{_optional_field}}": arguments.pop(0),
    "{{_field_using_variables}}": arguments.pop(0),
}

# TODO: Extract the functions to a separate file. These are now copied from NormalVariableTests.py.
def performTests():
    # Print table header.
    print()
    print("| Prompt variable | Result | Received | Expected |")
    print("| --------------- | ------ | -------- | -------- |")

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