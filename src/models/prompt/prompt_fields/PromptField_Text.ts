import {Setting} from "obsidian";
import {
    PromptField,
} from "../../../imports";

export class PromptField_Text extends PromptField {

    protected value: string;

    public createField(container_element: HTMLElement) {
        return new Setting(container_element)
            .setName(this.configuration.label)
            .addText(text => text
                .setValue(this.configuration.default_value)
                .onChange(value => this.storeValue(value)),
            )
        ;
    }

    protected isFilled(): boolean {
        return this.value.length > 0;
    }
}