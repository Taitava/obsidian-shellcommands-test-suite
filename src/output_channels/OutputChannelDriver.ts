import SC_Plugin from "../main";
import {App} from "obsidian";
import {OutputStreams} from "./OutputChannelDriverFunctions";
import {OutputStream} from "./OutputChannel";
import {debugLog} from "../Debug";
import {ParsingResult, TShellCommand} from "../TShellCommand";

export abstract class OutputChannelDriver {
    /**
     * Human readable name, used in settings.
     */
    protected abstract readonly title: string;

    protected plugin: SC_Plugin;
    protected app: App;
    protected shell_command_parsing_result: ParsingResult;
    protected t_shell_command: TShellCommand;
    protected accepts_empty_output = false;

    /**
     * Can be overridden in child classes in order to vary the title depending on output_stream.
     * @param output_stream
     */
    public getTitle(output_stream: OutputStream) {
        return this.title;
    }

    public initialize(plugin: SC_Plugin, t_shell_command: TShellCommand, shell_command_parsing_result: ParsingResult) {
        this.plugin = plugin;
        this.app = plugin.app;
        this.t_shell_command = t_shell_command;
        this.shell_command_parsing_result = shell_command_parsing_result;
    }

    protected abstract _handle(output: OutputStreams, error_code: number | null): void;

    public handle(output: OutputStreams, error_code: number | null): void {
        // Qualify output
        if (OutputChannelDriver.isOutputEmpty(output)) {
            // The output is empty
            if (!this.accepts_empty_output) {
                // This OutputChannelDriver does not accept empty output, i.e. empty output should be just ignored.
                debugLog(this.constructor.name + ": Ignoring empty output.");
                return;
            }
        }
        debugLog(this.constructor.name + ": Handling output...");

        // Output is ok.
        // Handle it.
        this._handle(output, error_code);
        debugLog("Output handling is done.")
    }

    /**
     * Can be moved to a global function isOutputStreamEmpty() if needed.
     * @param output
     * @private
     */
    private static isOutputEmpty(output: OutputStreams) {
        if (undefined !== output.stderr) {
            return false;
        }
        return undefined === output.stdout || "" === output.stdout;
    }
}