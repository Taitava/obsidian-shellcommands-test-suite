import {SC_Event_FileMenu} from "../../events/SC_Event_FileMenu";
import {EventVariable} from "./EventVariable";

export class Variable_EventTitle extends EventVariable {
    public static variable_name = "event_title";
    public static help_text = "Gives the current file name without a file extension. If you need it with the extension, use {{event_file_name}} instead.";

    protected static supported_sc_events = [
        SC_Event_FileMenu,
    ];

    protected generateValue(): string | null {
        if (!this.checkSC_EventSupport()) {
            return null;
        }

        return (this.sc_event as SC_Event_FileMenu).getFile().basename;
    }
}