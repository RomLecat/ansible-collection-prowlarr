#!/usr/bin/python

# Copyright: (c) 2020, Fuochi <devopsarr@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: prowlarr_ui_config_info

short_description: Get information about Prowlarr UI config.

version_added: "1.1.0"

description: Get information about Prowlarr UI config.

extends_documentation_fragment:
    - devopsarr.prowlarr.prowlarr_credentials

author:
    - Fuochi (@Fuochi)
'''

EXAMPLES = r'''
---
# Gather information about the UI config.
- name: Gather information about the UI config
  devopsarr.prowlarr.prowlarr_ui_config_info:
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

SECRETS = []


def get_ui_config(result):
    try:
        return helper.get()
    except prowlarr.ApiException as e:
        module.fail_json('Error getting UI config: {}\n body: {}'.format(to_native(e.reason), to_native(e.body)), **result)
    except Exception as e:
        module.fail_json('Error getting UI config: {}'.format(to_native(e)), **result)


def run_module():
    global helper
    global module

    # Define available arguments/parameters a user can pass to the module
    module = ProwlarrModule(
        argument_spec={},
        supports_check_mode=True,
    )
    # Init client and result.
    helper = ProwlarrConfigHelper(module.api, '/api/v1/config/ui', SECRETS)
    result = dict(
        changed=False,
    )

    # Get resource.
    result.update(helper.view(get_ui_config(result)))

    # Exit with data.
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
