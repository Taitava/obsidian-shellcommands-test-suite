import re
from typing import Union

def performTests(expectedValues: dict, testValues: dict, firstColumnName: str):
    # Print table header.
    firstColumnDashes = "-" * len(firstColumnName)
    print()
    print("| " + firstColumnName + " | Result | Received | Expected |")
    print("| " + firstColumnDashes + " | ------ | -------- | -------- |")

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