import datetime
import sys
from VariableTestFunctions import performTests

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
    "{{_multiline_field}}": """Line1
Line2""",
    "{{_toggle_field}}": "ON",
    "{{_dropdown_field}}": "Correct selection",
    "{{_password_field}}": "123",
}
testValues = {
    "{{_mandatory_field}}": arguments.pop(0),
    "{{_field_with_default_value}}": arguments.pop(0),
    "{{_optional_field}}": arguments.pop(0),
    "{{_field_using_variables}}": arguments.pop(0),
    "{{_multiline_field}}": arguments.pop(0),
    "{{_toggle_field}}": arguments.pop(0),
    "{{_dropdown_field}}": arguments.pop(0),
    "{{_password_field}}": arguments.pop(0),
}

performTests(expectedValues, testValues, "Prompt variable")