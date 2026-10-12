#!/usr/bin/python

# Copyright: (c) 2020, Fuochi <devopsarr@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: prowlarr_ui_config

short_description: Manages Prowlarr UI config.

version_added: "1.1.0"

description:
    - Manages Prowlarr UI config.
    - Only the options that are set are managed. Every other setting is left untouched.

options:
    first_day_of_week:
        description: First day of the week (0 is Sunday).
        type: int
    calendar_week_column_header:
        description: Calendar week column header format.
        type: str
    short_date_format:
        description: Short date format.
        type: str
    long_date_format:
        description: Long date format.
        type: str
    time_format:
        description: Time format.
        type: str
    show_relative_dates:
        description: Show relative dates (Today, Yesterday).
        type: bool
    enable_color_impaired_mode:
        description: Enable the color impaired mode.
        type: bool
    ui_language:
        description: UI language.
        type: str
    theme:
        description: UI theme.
        type: str

extends_documentation_fragment:
    - devopsarr.prowlarr.prowlarr_credentials

author:
    - Fuochi (@Fuochi)
'''

EXAMPLES = r'''
---
# Change some UI config settings
- name: Change some UI config settings
  devopsarr.prowlarr.prowlarr_ui_config:
    first_day_of_week: 1
    theme: "dark"
'''

RETURN = r'''
id:
    description: Resource ID.
    type: int
    returned: always
    sample: 1
first_day_of_week:
    description: First day of the week (0 is Sunday).
    type: int
    returned: always
calendar_week_column_header:
    description: Calendar week column header format.
    type: str
    returned: always
short_date_format:
    description: Short date format.
    type: str
    returned: always
long_date_format:
    description: Long date format.
    type: str
    returned: always
time_format:
    description: Time format.
    type: str
    returned: always
show_relative_dates:
    description: Show relative dates (Today, Yesterday).
    type: bool
    returned: always
enable_color_impaired_mode:
    description: Enable the color impaired mode.
    type: bool
    returned: always
ui_language:
    description: UI language.
    type: str
    returned: always
theme:
    description: UI theme.
    type: str
    returned: always
'''

from ansible_collections.devopsarr.prowlarr.plugins.module_utils.prowlarr_module import ProwlarrModule
from ansible_collections.devopsarr.prowlarr.plugins.module_utils.prowlarr_config_utils import ProwlarrConfigHelper
from ansible.module_utils.common.text.converters import to_native

try:
    import prowlarr
    HAS_PROWLARR_LIBRARY = True
except ImportError:
    HAS_PROWLARR_LIBRARY = False

OPTIONS = [
    'first_day_of_week',
    'calendar_week_column_header',
    'short_date_format',
    'long_date_format',
    'time_format',
    'show_relative_dates',
    'enable_color_impaired_mode',
    'ui_language',
    'theme',
]

SECRETS = []


def init_module_args():
    # define available arguments/parameters a user can pass to the module
    return dict(
        first_day_of_week=dict(type='int'),
        calendar_week_column_header=dict(type='str'),
        short_date_format=dict(type='str'),
        long_date_format=dict(type='str'),
        time_format=dict(type='str'),
        show_relative_dates=dict(type='bool'),
        enable_color_impaired_mode=dict(type='bool'),
        ui_language=dict(type='str'),
        theme=dict(type='str'),
    )


def read_ui_config(result):
    try:
        return helper.get()
    except prowlarr.ApiException as e:
        module.fail_json('Error getting UI config: {}\n body: {}'.format(to_native(e.reason), to_native(e.body)), **result)
    except Exception as e:
        module.fail_json('Error getting UI config: {}'.format(to_native(e)), **result)


def update_ui_config(want, result):
    result['changed'] = True
    # Only without check mode.
    if not module.check_mode:
        try:
            response = helper.update(want)
        except prowlarr.ApiException as e:
            module.fail_json('Error updating UI config: {}\n body: {}'.format(to_native(e.reason), to_native(e.body)), **result)
        except Exception as e:
            module.fail_json('Error updating UI config: {}'.format(to_native(e)), **result)
        result.update(helper.view(response))
    else:
        result.update(helper.view(want))
    # No need to exit module since it will exit by default either way


def run_module():
    global helper
    global module

    # Define available arguments/parameters a user can pass to the module
    module = ProwlarrModule(
        argument_spec=init_module_args(),
        supports_check_mode=True,
    )

    # Init client and result.
    helper = ProwlarrConfigHelper(module.api, '/api/v1/config/ui', SECRETS)
    result = dict(
        changed=False,
        id=0,
    )

    # Get resource.
    state = read_ui_config(result)
    result.update(helper.view(state))

    # Overlay only the options passed on the current resource.
    want, changed = helper.merge(state, module.params, OPTIONS)

    # Update the resource if needed.
    if changed:
        if module._diff:
            result['diff'] = dict(before=helper.view(state), after=helper.view(want))
        update_ui_config(want, result)

    # Exit with the result.
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
