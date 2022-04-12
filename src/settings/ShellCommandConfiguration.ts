/*
 * 'Shell commands' plugin for Obsidian.
 * Copyright (C) 2021 - 2022 Jarkko Linnanvirta
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, version 3 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 *
 * Contact the author (Jarkko Linnanvirta): https://github.com/Taitava/
 */

import {OutputChannel, OutputChannelOrder} from "../output_channels/OutputChannel";
import {
    ICommandPaletteOptions,
    IPlatformSpecificString,
    IPlatformSpecificStringWithDefault,
} from "./SC_MainSettings";
import {SC_EventConfigurations} from "../events/SC_EventConfiguration";
import {VariableDefaultValueConfiguration} from "../variables/Variable";
import {
    PreactionConfiguration
} from "../imports";

export interface ShellCommandsConfiguration {
    [key: string]: ShellCommandConfiguration;
}

export interface ShellCommandConfiguration {
    /**
     * Contains operating system specific shell commands.
     *  - key: platform (= OS) name
     *  - value: shell command
     */
    platform_specific_commands: IPlatformSpecificStringWithDefault;
    shells: IPlatformSpecificString;
    alias: string;
    confirm_execution: boolean;
    ignore_error_codes: number[];
    output_channels: {
        stdout: OutputChannel,
        stderr: OutputChannel,
    },
    output_channel_order: OutputChannelOrder;
    events: SC_EventConfigurations;
    command_palette_availability: keyof ICommandPaletteOptions;
    preactions: PreactionConfiguration[];
    variable_default_values: {
        [variable_id_or_name: string]: VariableDefaultValueConfiguration,
    };

    // LEGACY
    /** @deprecated Can only be used for migration. */
    shell_command?: string;
}

export function newShellCommandConfiguration(shell_command: string = ""): ShellCommandConfiguration {
    return {
        platform_specific_commands: {
            default: shell_command,
        },
        shells: {},
        alias: "",
        confirm_execution: false,
        ignore_error_codes: [],
        output_channels: {
            stdout: "ignore",
            stderr: "notification",
        },
        output_channel_order: "stdout-first",
        events: {},
        command_palette_availability: "enabled",
        preactions: [],
        variable_default_values: {},
    }
}