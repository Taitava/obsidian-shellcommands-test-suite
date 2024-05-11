import os
import sys
import urllib.parse
import webbrowser

arguments = sys.argv
arguments.pop(0) # The first argument is the script file's name, so discard it.

eventCode = arguments.pop(0)

vaultPath = os.getcwd()
sandboxFolderName = "Sandbox"
sandboxFolderPath = os.path.join(vaultPath, sandboxFolderName)

# Define tests for each event. Each event test is contained in a lamda function to only call input() when it's really needed.
eventTests = {
    # FILE TESTS:
    "file-created": lambda : {
        "values": {
            "{{event_file_extension:no-dot}}": {
                "expected": "md",
                "actual": input(),
            },
            "{{event_file_extension:with-dot}}": {
                "expected": ".md",
                "actual": input(),
            },
            "{{event_file_name}}": {
                "expected": "CreatedNote.md",
                "actual": input(),
            },
            "{{event_file_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "CreatedNote.md"),
                "actual": input(),
            },
            "{{event_file_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "CreatedNote.md"),
                "actual": input(),
            },
            "{{event_file_uri}}": {
                "expected": "obsidian://vault/Shell%20commands%20test/Sandbox%2FCreatedNote.md",
                "actual": input(),
            },
            "{{event_folder_name}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": sandboxFolderPath,
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_title}}": {
                "expected": "CreatedNote",
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "file-created",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "file",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_file_created",
    },
    "file-deleted": lambda : {
        "values": {
            "{{event_file_extension:no-dot}}": {
                "expected": "md",
                "actual": input(),
            },
            "{{event_file_extension:with-dot}}": {
                "expected": ".md",
                "actual": input(),
            },
            "{{event_file_name}}": {
                "expected": "DeletableNote.md",
                "actual": input(),
            },
            "{{event_file_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "DeletableNote.md"),
                "actual": input(),
            },
            "{{event_file_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "DeletableNote.md"),
                "actual": input(),
            },
            "{{event_file_uri}}": {
                "expected": "obsidian://vault/Shell%20commands%20test/Sandbox%2FDeletableNote.md",
                "actual": input(),
            },
            "{{event_folder_name}}": {
                # "expected": sandboxFolderName, # FIXME: Folder variables crash when used in file-deleted event. Enable this variable test after fixing the bug.
                "expected": "{{DISABLED-event_folder_name}}", # Temporarily accept a static string.
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                # "expected": os.path.join(sandboxFolderPath, "ParentFolder", "DeletableFolder"), # FIXME too.
                "expected": "{{DISABLED-event_folder_path:absolute}}", # Temporarily accept a static string.
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                # "expected": os.path.join(sandboxFolderName, "ParentFolder", "DeletableFolder"), # FIXME too.
                "expected": "{{DISABLED-event_folder_path:relative}}", # Temporarily accept a static string.
                "actual": input(),
            },
            "{{event_title}}": {
                "expected": "DeletableNote",
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "file-deleted",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "file",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_file_deleted",
    },
    "file-content-modified": lambda: {
        "values": {
            "{{event_file_extension:no-dot}}": {
                "expected": "md",
                "actual": input(),
            },
            "{{event_file_extension:with-dot}}": {
                "expected": ".md",
                "actual": input(),
            },
            "{{event_file_name}}": {
                "expected": "ModifiableNote.md",
                "actual": input(),
            },
            "{{event_file_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "ModifiableNote.md"),
                "actual": input(),
            },
            "{{event_file_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "ModifiableNote.md"),
                "actual": input(),
            },
            "{{event_file_uri}}": {
                "expected": "obsidian://vault/Shell%20commands%20test/Sandbox%2FModifiableNote.md",
                "actual": input(),
            },
            "{{event_folder_name}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": sandboxFolderPath,
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_title}}": {
                "expected": "ModifiableNote",
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "file-content-modified",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "file",
                "actual": input(),
            },
            "{{event_yaml_value:yaml_test}}": {
                # "expected": "testValue", # FIXME: file-content-modified event is triggered before Obsidian has updated cache, so the contents received would be outdated. I need to plan one of the following solutions:
                #                 # a) Changing the current event to use MetadataCache's 'changed' event instead of vault's 'modified' event,
                #                 # b) Creating a completely new event, or
                #                 # c) Adding a setting to the current event, that chooses which event to use. (Edit 2024-05-11: I think this sounds the best, but do research the question below.)
                #                 # Does the MetadataCache's 'changed' event also get triggered for non-Markdown files, e.g. images?
                "expected": "{{DISABLED-event_yaml_value:yaml_test}}",
                "actual": input(),
            },
            "{{event_file_content}}": {
                # "expected": "---\\nyaml_test: testValue\\n---\\nTest content", # FIXME too.
                "expected": "{{DISABLED-event_file_content}}",
                "actual": input(),
            },
            "{{event_note_content}}": {
                # "expected": "Test content", # FIXME too.
                "expected": "{{DISABLED-event_note_content}}",
                "actual": input(),
            },
            # TODO: Add also a test for {{event_tags:, }}. The result should be "tag1, tag2".
        },
        "resultVariable": "_test_event_file_content_modified",
    },
    "file-moved": lambda: {
        "values": {
            "{{event_file_extension:no-dot}}": {
                "expected": "md",
                "actual": input(),
            },
            "{{event_file_extension:with-dot}}": {
                "expected": ".md",
                "actual": input(),
            },
            "{{event_file_name}}": {
                "expected": "MovableNote.md",
                "actual": input(),
            },
            "{{event_file_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "MoveToHere", "MovableNote.md"),
                "actual": input(),
            },
            "{{event_file_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "MoveToHere", "MovableNote.md"),
                "actual": input(),
            },
            "{{event_old_file_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "MovableNote.md"),
                "actual": input(),
            },
            "{{event_old_file_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "MovableNote.md"),
                "actual": input(),
            },
            "{{event_file_uri}}": {
                "expected": "obsidian://vault/Shell%20commands%20test/Sandbox%2FMoveToHere%2FMovableNote.md",
                "actual": input(),
            },
            "{{event_folder_name}}": {
                "expected": "MoveToHere",
                "actual": input(),
            },
            "{{event_old_folder_name}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "MoveToHere"),
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "MoveToHere"),
                "actual": input(),
            },
            "{{event_old_folder_path:absolute}}": {
                "expected": sandboxFolderPath,
                "actual": input(),
            },
            "{{event_old_folder_path:relative}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_title}}": {
                "expected": "MovableNote",
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "file-moved",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "file",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_file_moved",
    },
    "file-renamed": lambda: {
        "values": {
            "{{event_file_extension:no-dot}}": {
                "expected": "md",
                "actual": input(),
            },
            "{{event_file_extension:with-dot}}": {
                "expected": ".md",
                "actual": input(),
            },
            "{{event_file_name}}": {
                "expected": "RenamedNote.md",
                "actual": input(),
            },
            "{{event_old_file_name}}": {
                "expected": "RenameableNote.md",
                "actual": input(),
            },
            "{{event_file_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "RenamedNote.md"),
                "actual": input(),
            },
            "{{event_file_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "RenamedNote.md"),
                "actual": input(),
            },
            "{{event_old_file_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "RenameableNote.md"),
                "actual": input(),
            },
            "{{event_old_file_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "RenameableNote.md"),
                "actual": input(),
            },
            "{{event_file_uri}}": {
                "expected": "obsidian://vault/Shell%20commands%20test/Sandbox%2FRenamedNote.md",
                "actual": input(),
            },
            "{{event_folder_name}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": sandboxFolderPath,
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": sandboxFolderName,
                "actual": input(),
            },
            "{{event_title}}": {
                "expected": "RenamedNote",
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "file-renamed",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "file",
                "actual": input(),
            },
            "{{event_old_title}}": {
                "expected": "RenameableNote",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_file_renamed",
    },

    # FOLDER TESTS:
    "folder-created": lambda : {
        "values": {
            "{{event_folder_name}}": {
                "expected": "CreatedFolder",
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "CreatedFolder"),
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "CreatedFolder"),
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "folder-created",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "folder",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_folder_created",
    },
    "folder-deleted": lambda : {
        "values": {
            "{{event_folder_name}}": {
                "expected": "DeletableFolder",
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "DeletableFolder"),
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "DeletableFolder"),
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "folder-deleted",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "folder",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_folder_deleted",
    },
    "folder-moved": lambda : {
        "values": {
            "{{event_folder_name}}": {
                "expected": "MovableFolder",
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "MoveToHere", "MovableFolder"),
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "MoveToHere", "MovableFolder"),
                "actual": input(),
            },
            "{{event_old_folder_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "MovableFolder"),
                "actual": input(),
            },
            "{{event_old_folder_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "MovableFolder"),
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "folder-moved",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "folder",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_folder_moved",
    },
    "folder-renamed": lambda : {
        "values": {
            "{{event_folder_name}}": {
                "expected": "RenamedFolder",
                "actual": input(),
            },
            "{{event_old_folder_name}}": {
                "expected": "RenameableFolder",
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "RenamedFolder"),
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "RenamedFolder"),
                "actual": input(),
            },
            "{{event_old_folder_path:absolute}}": {
                "expected": os.path.join(sandboxFolderPath, "RenameableFolder"),
                "actual": input(),
            },
            "{{event_old_folder_path:relative}}": {
                "expected": os.path.join(sandboxFolderName, "RenameableFolder"),
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "folder-renamed",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "folder",
                "actual": input(),
            },
        },
        "resultVariable": "_test_event_folder_renamed",
    },

    # MENU TESTS:
    "file-menu-item": lambda : {
        "values": {
            "{{event_file_content}}": {
                "expected": """---
yaml_property: Some value
tags:
  - firstTag
  - secondTag
  - thirdTag
---
This file is used by automated tests.
It doesn't have much content.
It has multiple lines.""",
                "actual": arguments.pop(0),
            },
            "{{event_file_extension:no-dot}}": {
                "expected": "md",
                "actual": input(),
            },
            "{{event_file_extension:with-dot}}": {
                "expected": ".md",
                "actual": input(),
            },
            "{{event_file_name}}": {
                "expected": "Content note.md",
                "actual": input(),
            },
            "{{event_file_path:absolute}}": {
                "expected": os.path.join(vaultPath, "Content note.md"),
                "actual": input(),
            },
            "{{event_file_path:relative}}": {
                "expected": "Content note.md",
                "actual": input(),
            },
            "{{event_file_uri}}": {
                "expected": "obsidian://vault/Shell%20commands%20test/Content%20note.md",
                "actual": input(),
            },
            "{{event_folder_name}}": {
                "expected": ".",
                "actual": input(),
            },
            "{{event_folder_path:absolute}}": {
                "expected": vaultPath,
                "actual": input(),
            },
            "{{event_folder_path:relative}}": {
                "expected": ".",
                "actual": input(),
            },
            "{{event_note_content}}": {
                "expected": """This file is used by automated tests.
It doesn't have much content.
It has multiple lines.""",
                "actual": arguments.pop(0),
            },
            "{{event_tags:, }}": {
                "expected": "firstTag, secondTag, thirdTag",
                "actual": input(),
            },
            "{{event_title}}": {
                "expected": "Content note",
                "actual": input(),
            },
            "{{event_type}}": {
                "expected": "file-menu-item",
                "actual": input(),
            },
            "{{event_type:category}}": {
                "expected": "menu",
                "actual": input(),
            },
            "{{event_yaml_content:with-dashes}}": {
                "expected": """---
yaml_property: Some value
tags:
  - firstTag
  - secondTag
  - thirdTag
---""",
                "actual": arguments.pop(0),
            },
            "{{event_yaml_content:no-dashes}}": {
                "expected": """yaml_property: Some value
tags:
  - firstTag
  - secondTag
  - thirdTag""",
                "actual": arguments.pop(0),
            },
        },
        "resultLabel": "File menu test: ",
    },
}

def performTest():
    if eventCode not in eventTests:
        print("Unrecognized event code: " + eventCode, file=sys.stderr)
        sys.exit(1)
    eventTest = eventTests[eventCode]() # () calls a lambda function.
    errorMessages = []
    for variableName in eventTest["values"]:
        expectedValue = eventTest["values"][variableName]["expected"]
        actualValue = eventTest["values"][variableName]["actual"]
        if type(expectedValue) == list:
            # expectedValue is an array of possible values. I.e. testValue can be any of the array's values.
            # This is not utilized at the moment, but have it just in case future tests could use it.
            assertionPassed = actualValue in expectedValue
            expectedValueResult = " OR ".join(expectedValue)
        else:
            # Normal single value test.
            assertionPassed = actualValue == expectedValue
            expectedValueResult = expectedValue
        if not assertionPassed:
            errorMessages.append(variableName + " must be " + expectedValueResult + ". Now it is: " + actualValue)
    if "resultVariable" in eventTest:
        # The result should be stored in a variable.
        resultText = "OK" if len(errorMessages) == 0 else "\\n\\n".join(errorMessages)
        resultText = resultText.replace("\\n", "\\n> ") # Add a "> " part after every linebreak, because the result text will be used in a callout block.
        # Use \\n instead of \n to produce a literal \n for JSON. JSON parsing in Obsidian will turn it into a real newline.
        print('{"' + eventTest["resultVariable"] + '": "' + resultText + '"}')
    elif "resultLabel" in eventTest:
        # The result should be written into a file.
        resultText = "OK" if len(errorMessages) == 0 else "\n".join(errorMessages)
        with open(os.path.join('Sandbox', 'TestResults.md'), 'a') as testResultsFile:
            testResultsFile.write(eventTest["resultLabel"] + resultText + "\n")

performTest()
