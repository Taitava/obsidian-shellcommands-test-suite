import {Setting} from "obsidian";
import {SC_MainSettings} from "../../settings/SC_MainSettings";
import SC_Plugin from "../../main";
import {CustomVariableInstance} from "./CustomVariableInstance";
import {
    IDGenerator,
    Model,
    ParentModelOneToManyRelation,
} from "../../imports";

export class CustomVariableModel extends Model {

    public getSingularName(): string {
        return "Custom variable";
    }

    public readonly id_generator = new IDGenerator();

    constructor(
        plugin: SC_Plugin,
    ) {
        super(plugin);

        // Introduce the ID to an ID generator so that it won't accidentally generate the same ID again when creating new CustomVariableInstances.
    }

    protected defineParentConfigurationRelation(instance: CustomVariableInstance): ParentModelOneToManyRelation {
        return {
            type: "one-to-many",
            key: "custom_variables",
            index: instance.custom_variable_index as number, // TODO: Find a way to avoid using 'as number'.
        };
    }

    public createInstances(parent_configuration: SC_MainSettings): CustomVariableInstance[] {
        const custom_variable_instances: CustomVariableInstance[] = [];
        parent_configuration.custom_variables.forEach((custom_variable_configuration: CustomVariableConfiguration, custom_variable_index: number) => {
            custom_variable_instances[custom_variable_index] = new CustomVariableInstance( this, custom_variable_configuration, parent_configuration, custom_variable_index);
        });
        return custom_variable_instances;
    }

    public newInstance(parent_configuration: SC_MainSettings): CustomVariableInstance {
        const custom_variable_configuration: CustomVariableConfiguration = this._getDefaultConfiguration();
        const custom_variable_instance = new CustomVariableInstance(this, custom_variable_configuration, parent_configuration, parent_configuration.custom_variables.length);
        parent_configuration.custom_variables.push(custom_variable_configuration);
        return custom_variable_instance;
        // TODO: Move this logic to the base Model class.
    }

    protected _createSettingFields(instance: CustomVariableInstance, container_element: HTMLElement): Setting {
        return new Setting(container_element)
            .setName("Variable name")
            .setDesc("Must begin with {{_ and end with }} and contain at least one character inside. Allowed characters are letters a-z, numbers 0-9 and an underscore _")
            .addText(text => text
                .setValue(instance.configuration.name)
                .onChange(async (new_name: string) => {
                    // TODO: Find a way to create this kind of trivial onChange() functions in the Model base class.
                    // TODO: If another custom variable has the same name, display a warning in the field's description and do not save. Mention that saving is disabled. Create a validator method for this.
                    // TODO: If the name does not begin with {{_ and end with }} , display a warning in the field's description and do not save. Mention that saving is disabled. Create a validator method for this.
                    instance.configuration.name = new_name;
                    await this.plugin.saveSettings();
                }),
            );
    }

    protected _getDefaultConfiguration(): CustomVariableConfiguration {
        return {
            id: this.id_generator.generateID(),
            name: "{{_}}", // TODO: If the name {{_}} is already in use, append a sequential number, e.g. {{_1}}, {{_2}} etc.
        }
    }
}

export interface CustomVariableConfiguration {
    id: string,
    name: string,
}