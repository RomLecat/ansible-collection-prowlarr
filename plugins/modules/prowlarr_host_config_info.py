#!/usr/bin/python

# Copyright: (c) 2020, Fuochi <devopsarr@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: prowlarr_host_config_info

short_description: Get information about Prowlarr host config.

version_added: "1.1.0"

description:
    - Get information about Prowlarr host config.
    - Secrets are never returned.

extends_documentation_fragment:
    - devopsarr.prowlarr.prowlarr_credentials

author:
    - Fuochi (@Fuochi)
'''

EXAMPLES = r'''
---
# Gather information about the host config.
- name: Gather information about the host config
  devopsarr.prowlarr.prowlarr_host_config_info:
'''

RETURN = r'''
id:
    description: Resource ID.
    type: int
    returned: always
    sample: 1
bind_address:
    description: Address Prowlarr binds to.
    type: str
    returned: always
port:
    description: HTTP port.
    type: int
    returned: always
ssl_port:
    description: HTTPS port.
    type: int
    returned: always
enable_ssl:
    description: Enable HTTPS.
    type: bool
    returned: always
launch_browser:
    description: Open a browser at startup.
    type: bool
    returned: always
authentication_method:
    description: Authentication method.
    type: str
    returned: always
authentication_required:
    description: When authentication is required.
    type: str
    returned: always
analytics_enabled:
    description: Send anonymous usage and error information.
    type: bool
    returned: always
username:
    description: Authentication username.
    type: str
    returned: always
log_level:
    description: Log level.
    type: str
    returned: always
log_size_limit:
    description: Log file size limit in MB.
    type: int
    returned: always
console_log_level:
    description: Console log level.
    type: str
    returned: always
branch:
    description: Update branch.
    type: str
    returned: always
ssl_cert_path:
    description: Path of the SSL certificate.
    type: str
    returned: always
url_base:
    description: URL base.
    type: str
    returned: always
instance_name:
    description: Instance name.
    type: str
    returned: always
application_url:
    description: Application URL.
    type: str
    returned: always
update_automatically:
    description: Install updates automatically.
    type: bool
    returned: always
update_mechanism:
    description: Update mechanism.
    type: str
    returned: always
update_script_path:
    description: Path of the update script.
    type: str
    returned: always
proxy_enabled:
    description: Use a proxy.
    type: bool
    returned: always
proxy_type:
    description: Proxy type.
    type: str
    returned: always
proxy_hostname:
    description: Proxy hostname.
    type: str
    returned: always
proxy_port:
    description: Proxy port.
    type: int
    returned: always
proxy_username:
    description: Proxy username.
    type: str
    returned: always
proxy_bypass_filter:
    description: Comma separated list of addresses that bypass the proxy.
    type: str
    returned: always
proxy_bypass_local_addresses:
    description: Bypass the proxy for local addresses.
    type: bool
    returned: always
certificate_validation:
    description: Certificate validation.
    type: str
    returned: always
backup_folder:
    description: Backup folder.
    type: str
    returned: always
backup_interval:
    description: Backup interval in days.
    type: int
    returned: always
backup_retention:
    description: Backup retention in days.
    type: int
    returned: always
history_cleanup_days:
    description: Days of history to keep, 0 disables the cleanup.
    type: int
    returned: always
trust_cgnat_ip_addresses:
    description: Trust CGNAT IP addresses as local.
    type: bool
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

SECRETS = ['password', 'password_confirmation', 'api_key', 'ssl_cert_password', 'proxy_password']


def get_host_config(result):
    try:
        return helper.get()
    except prowlarr.ApiException as e:
        module.fail_json('Error getting host config: {}\n body: {}'.format(to_native(e.reason), to_native(e.body)), **result)
    except Exception as e:
        module.fail_json('Error getting host config: {}'.format(to_native(e)), **result)


def run_module():
    global helper
    global module

    # Define available arguments/parameters a user can pass to the module
    module = ProwlarrModule(
        argument_spec={},
        supports_check_mode=True,
    )
    # Init client and result.
    helper = ProwlarrConfigHelper(module.api, '/api/v1/config/host', SECRETS)
    result = dict(
        changed=False,
    )

    # Get resource.
    result.update(helper.view(get_host_config(result)))

    # Exit with data.
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
