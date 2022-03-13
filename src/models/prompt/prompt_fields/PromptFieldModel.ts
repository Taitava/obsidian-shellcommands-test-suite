import {Setting} from "obsidian";
import {randomInteger} from "../../../Common";
import {createAutocomplete} from "../../../settings/setting_elements/Autocomplete";
import {getVariableAutocompleteItems} from "../../../variables/getVariableAutocompleteItems";
import {
    CustomVariableInstance,
    CustomVariableModel,
    CustomVariableSettingsModal,
    getModel,
    Model,
    ParentModelOneToManyIndexRelation,
    Prompt,
    PromptField,
    PromptField_Text,
    PromptFieldConfiguration,
} from "../../../imports";

export class PromptFieldModel extends Model {

    public getSingularName(): string {
        return "Field";
    }

    protected defineParentConfigurationRelation(prompt_field: PromptField): ParentModelOneToManyIndexRelation {
        return {
            type: "one-to-many-index",
            key: "fields",
            index: prompt_field.prompt_field_index as number,
        };
    }

    public loadInstances(prompt: Prompt): PromptFieldSet {
        const prompt_fields = new PromptFieldSet;
        prompt.configuration.fields.forEach((field_configuration: PromptFieldConfiguration, index) => {
            prompt_fields.add(
                this.createInstance(prompt, field_configuration, index)
            );
        });
        return prompt_fields;
    }

    public newInstance(prompt: Prompt): PromptField {
        // TODO: Move this logic to the base Model class.

        // Setup a default configuration
        const prompt_field_configuration = this._getDefaultConfiguration();

        // Instantiate a PromptField
        const prompt_field = this.createInstance(prompt, prompt_field_configuration, prompt.configuration.fields.length);

        // Store the configuration into the prompt's configuration
        prompt.configuration.fields.push(prompt_field_configuration);

        // Return the PromptField
        return prompt_field;
    }

    private createInstance(prompt: Prompt, prompt_field_configuration: PromptFieldConfiguration, prompt_field_index: number): PromptField {
        // TODO: When the 'type' field gets implemented on PromptFieldConfiguration, implement some kind of switch structure here to create different types of PromptFields.
        return new PromptField_Text(this, prompt, prompt_field_configuration, prompt_field_index)
    }

    protected _createSettingFields(prompt_field: PromptField, container_element: HTMLElement): Setting {
        const label_placeholders = [
            "What is your name?",
            "How big is the universe?",
            "How long is eternity?",
            "What is your lucky number?",
            "What is your favorite song?",
            "What is your favorite color?",
            "How many books have you read?",
            "What is the purpose of life?",
        ];
        const default_value_placeholders = [
            ["Bond, James Bond", "John Doe", "Jane Doe", "Mr. Bean"],
            ["Very big, and still expanding", "93 billion light-years"],
            ["Infinite", "Too long to wait for"],
            [String(randomInteger(0, 9)), "I don't have one"],
            ["We are the world (USA for Africa)", "Heal the world (Michael Jackson)", "Imagine (John Lennon)"],
            ["Blue as deep as an ocean", "Red as love", "Grass-green", "Snow-white"],
            ["Thousands", "Many", "Countless", "None"],
            ["Thinking", "Being a being", "42"],
        ];
        const label_placeholder_index: number = randomInteger(0, label_placeholders.length - 1);
        const default_value_placeholders_subset: string[] = default_value_placeholders[label_placeholder_index];

        // Create a list of custom variables
        const custom_variable_options: {[key: string]: string} = {};
        this.plugin.getCustomVariableInstances().forEach((custom_variable_instance: CustomVariableInstance, custom_variable_id: string) => {
            custom_variable_options[custom_variable_id] = custom_variable_instance.getFullName();
        });

        const on_default_value_setting_change = async (new_default_value: string) => {
            prompt_field.configuration.default_value = new_default_value;
            await this.plugin.saveSettings();
        };

        // Create the setting fields
        const setting_group: PromptFieldSettingGroup = {
            heading_setting: new Setting(container_element)
                .setName("") // This will be set down below.
                .setHeading()
            ,
            label_setting: new Setting(container_element)
                .setName("Field label")
                .setDesc("Displayed in the prompt.")
                .addText(text => text
                    .setValue(prompt_field.configuration.label)
                    .setPlaceholder(label_placeholders[label_placeholder_index])
                    .onChange(async (new_label: string) => {
                        prompt_field.configuration.label = new_label;
                        _update_heading()
                        await this.plugin.saveSettings();
                    })
                )
            ,
            default_value_setting: new Setting(container_element)
                .setName("Default value")
                .setDesc("Can be static text, {{variables}} or a combination of both.")
                .addText(text => text
                    .setValue(prompt_field.configuration.default_value)
                    .setPlaceholder(
                        prompt_field.configuration.label ? "" // If the label is defined, do not add a placeholder here, as the label's placeholder is not visible, so this placeholder would not make sense.
                            : default_value_placeholders_subset[randomInteger(0, default_value_placeholders_subset.length - 1)]
                    )
                    .onChange(on_default_value_setting_change)
                )
            ,
            target_variable_setting: new Setting(container_element)
                .setName("Target variable")
                .setDesc("Where the inputted value will be stored in. You can use the variable in a shell command.")
                .addDropdown(dropdown => dropdown
                    .addOption("", "") // An option for a situation when nothing is selected.
                    .addOptions(custom_variable_options)
                    .addOption("new", "Create a new custom variable")
                    .setValue(prompt_field.configuration.target_variable_id)
                    .onChange((new_target_variable_id: string) => {
                        if ("new" === new_target_variable_id) {
                            // Create a new custom variable.
                            const model = getModel<CustomVariableModel>(CustomVariableModel.name)
                            const custom_variable_instance = model.newInstance(this.plugin.settings);
                            this.plugin.saveSettings().then(() => {
                                const modal = new CustomVariableSettingsModal(
                                    this.plugin,
                                    custom_variable_instance,
                                    async () => {
                                        // Variable is created.
                                        dropdown.addOption(custom_variable_instance.getID(), custom_variable_instance.getTitle());
                                        dropdown.setValue(custom_variable_instance.getID());
                                        prompt_field.configuration.target_variable_id = custom_variable_instance.getID();
                                        await this.plugin.saveSettings();
                                    },
                                    async () => {
                                        dropdown.setValue(prompt_field.configuration.target_variable_id); // Reset the dropdown selection.
                                        // Variable creation was cancelled.
                                        model.deleteInstance(custom_variable_instance);
                                        await this.plugin.saveSettings();
                                    },
                                );
                                modal.open();
                            });
                        } else if ("" === new_target_variable_id) {
                            // The target variable cannot be undefined.
                            dropdown.setValue(prompt_field.configuration.target_variable_id); // Reset the dropdown selection.
                            this.plugin.newNotification("A target variable must be selected!");
                        } else {
                            // Use an existing target variable.
                            // Check that this target variable is not reserved.
                            prompt_field.setIfValid("target_variable_id", new_target_variable_id).then(async () => {
                                // It can be used.
                                await this.plugin.saveSettings();
                            }).catch((error_message: string) => {
                                // The target variable is reserved.
                                dropdown.setValue(prompt_field.configuration.target_variable_id); // Reset the dropdown selection.
                                this.plugin.newNotification(error_message);
                            });
                        }
                    })
                )
            ,
            required_setting: new Setting(container_element)
                .setName("Is required")
                .setDesc("If on, the field needs to be filled before the prompt can be submitted.")
                .addToggle(toggle => toggle
                    .setValue(prompt_field.configuration.required)
                    .onChange(async (new_required: boolean) => {
                        prompt_field.configuration.required = new_required;
                        await this.plugin.saveSettings();
                    })
                )
            ,
        };
        _update_heading();

        function _update_heading() {
            setting_group.heading_setting.setName(prompt_field.getTitle());
        }

        // Autocomplete menu
        if (this.plugin.settings.show_autocomplete_menu) {
            // Show autocomplete menu (= a list of available variables).
            const default_value_input_element = setting_group.default_value_setting.controlEl.find("input") as HTMLInputElement;
            createAutocomplete(default_value_input_element, getVariableAutocompleteItems(this.plugin), on_default_value_setting_change);
        }

        return setting_group.heading_setting;
    }

    public validateValue(prompt_field: PromptField, field: keyof PromptFieldConfiguration, value: unknown): Promise<void> {
        switch (field) {
            case "target_variable_id":
                const new_target_variable_id: string = value as string; // A more descriptive name for 'value'.
                // Check that the target variable is not used by other fields of the same Prompt.
                for (const other_prompt_field of prompt_field.prompt.prompt_fields) {
                    if (prompt_field !== other_prompt_field) { // Do not check the same field. Only check other fields.
                        // Check if this other field has the same target variable.
                        if (new_target_variable_id === other_prompt_field.configuration.target_variable_id) {
                            // They have the same target_variable_id.
                            // Return an error message.
                            const target_variable_name = this.plugin.getCustomVariableInstances().get(new_target_variable_id).getFullName();
                            return Promise.reject(`Target variable ${target_variable_name} is already used by another field in the same prompt. Select another variable.`);
                        }
                    }
                }
                // All fields have been checked and no collisions were found.
                return Promise.resolve();

            default:
                // No validation for other fields.
                throw new Error(this.constructor.name + ".validateValue(): No validation is implemented for other fields.");
        }
    }

    private _getDefaultConfiguration(): PromptFieldConfiguration {
        return {
            // type: "text",
            label: "",
            // TODO: Add 'description'
            default_value: "",
            //  TODO: Add 'placeholder'.
            target_variable_id: "",
            required: true,
        }
    }

    protected _deleteInstance(prompt_field: PromptField): void {
        prompt_field.prompt.prompt_fields.delete(prompt_field);
    }
}

export class PromptFieldSet extends Set<PromptField> {}

export interface PromptFieldSettingGroup {
    heading_setting: Setting;
    label_setting: Setting;
    default_value_setting: Setting;
    target_variable_setting: Setting
    required_setting: Setting;
}