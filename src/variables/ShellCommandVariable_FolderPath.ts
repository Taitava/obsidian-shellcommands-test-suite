import {addShellCommandVariableInstructions} from "./ShellCommandVariableInstructions";
import {getVaultAbsolutePath, normalizePath2} from "../Common";
import {ShellCommandVariable} from "./ShellCommandVariable";

export class ShellCommandVariable_FolderPath extends ShellCommandVariable{
    name = "folder_path";
    has_argument = true;
    getValue(mode: string): string|null {
        let active_file = this.app.workspace.getActiveFile();
        if (active_file) {
            if (active_file.parent) {
                let folder = active_file.parent;
                switch (mode) {
                    case "absolute":
                        return normalizePath2(getVaultAbsolutePath(this.app) + "/" + folder.path);
                    case "relative":
                        if (folder.isRoot()) {
                            // Obsidian API does not give a correct folder.path value for the vault's root folder.
                            // TODO: See this discussion and apply possible changes if something will come up: https://forum.obsidian.md/t/vault-root-folders-relative-path-gives/24857
                            return ".";
                        } else {
                            // This is a normal subfolder
                            return normalizePath2(folder.path); // Normalize to get a correct slash between directories depending on platform. On Windows it should be \ .
                        }
                    default:
                        this.newErrorMessage(`Unknown mode "${mode}"! Use "absolute" or "relative".`);
                        return null; // null indicates that getting a value has failed and the command should not be executed.
                }
            } else {
                this.newErrorMessage("The current file does not have a parent for some strange reason.");
                return null; // null indicates that getting a value has failed and the command should not be executed.
            }
        } else {
            this.newErrorMessage("No file is active at the moment. Open a file or click a pane that has a file open.");
            return null; // null indicates that getting a value has failed and the command should not be executed.
        }
    }
}
addShellCommandVariableInstructions(
    "{{folder_path:relative}} or {{folder_path:absolute}}",
    "Gives path to the current file's parent folder, either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.",
);