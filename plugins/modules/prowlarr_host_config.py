#!/usr/bin/python

# Copyright: (c) 2020, Fuochi <devopsarr@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: prowlarr_host_config

short_description: Manages Prowlarr host config.

version_added: "1.1.0"

description:
    - Manages Prowlarr host config.
    - Only the options that are set are managed. Every other setting is left untouched.

options:
    bind_address:
        description: Address Prowlarr binds to.
        type: str
    port:
        description: HTTP port.
        type: int
    ssl_port:
        description: HTTPS port.
        type: int
    enable_ssl:
        description: Enable HTTPS.
        type: bool
    launch_browser:
        description: Open a browser at startup.
        type: bool
    authentication_method:
        description: Authentication method.
        type: str
        choices: [ "none", "basic", "forms", "external" ]
    authentication_required:
        description: When authentication is required.
        type: str
        choices: [ "enabled", "disabledForLocalAddresses" ]
    analytics_enabled:
        description: Send anonymous usage and error information.
        type: bool
    username:
        description: Authentication username.
        type: str
    password:
        description: Authentication password. If I(password_confirmation) is not set, it is set to the same value.
        type: str
    password_confirmation:
        description: Authentication password confirmation.
        type: str
    log_level:
        description: Log level.
        type: str
    log_size_limit:
        description: Log file size limit in MB.
        type: int
    console_log_level:
        description: Console log level.
        type: str
    branch:
        description: Update branch.
        type: str
    api_key:
        description: API key of the instance. Changing it invalidates the key used by the module itself.
        type: str
    ssl_cert_path:
        description: Path of the SSL certificate.
        type: str
    ssl_cert_password:
        description: Password of the SSL certificate.
        type: str
    url_base:
        description: URL base.
        type: str
    instance_name:
        description: Instance name.
        type: str
    application_url:
        description: Application URL.
        type: str
    update_automatically:
        description: Install updates automatically.
        type: bool
    update_mechanism:
        description: Update mechanism.
        type: str
        choices: [ "builtIn", "script", "external", "apt", "docker" ]
    update_script_path:
        description: Path of the update script.
        type: str
    proxy_enabled:
        description: Use a proxy.
        type: bool
    proxy_type:
        description: Proxy type.
        type: str
        choices: [ "http", "socks4", "socks5" ]
    proxy_hostname:
        description: Proxy hostname.
        type: str
    proxy_port:
        description: Proxy port.
        type: int
    proxy_username:
        description: Proxy username.
        type: str
    proxy_password:
        description: Proxy password.
        type: str
    proxy_bypass_filter:
        description: Comma separated list of addresses that bypass the proxy.
        type: str
    proxy_bypass_local_addresses:
        description: Bypass the proxy for local addresses.
        type: bool
    certificate_validation:
        description: Certificate validation.
        type: str
        choices: [ "enabled", "disabledForLocalAddresses", "disabled" ]
    backup_folder:
        description: Backup folder.
        type: str
    backup_interval:
        description: Backup interval in days.
        type: int
    backup_retention:
        description: Backup retention in days.
        type: int
    history_cleanup_days:
        description: Days of history to keep, 0 disables the cleanup.
        type: int
    trust_cgnat_ip_addresses:
        description: Trust CGNAT IP addresses as local.
        type: bool

extends_documentation_fragment:
    - devopsarr.prowlarr.prowlarr_credentials

author:
    - Fuochi (@Fuochi)
'''

EXAMPLES = r'''
---
# Change some host config settings
- name: Change some host config settings
  devopsarr.prowlarr.prowlarr_host_config:
    analytics_enabled: false
    log_level: "info"
    history_cleanup_days: 30
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

OPTIONS = [
    'bind_address',
    'port',
    'ssl_port',
    'enable_ssl',
    'launch_browser',
    'authentication_method',
    'authentication_required',
    'analytics_enabled',
    'username',
    'password',
    'password_confirmation',
    'log_level',
    'log_size_limit',
    'console_log_level',
    'branch',
    'api_key',
    'ssl_cert_path',
    'ssl_cert_password',
    'url_base',
    'instance_name',
    'application_url',
    'update_automatically',
    'update_mechanism',
    'update_script_path',
    'proxy_enabled',
    'proxy_type',
    'proxy_hostname',
    'proxy_port',
    'proxy_username',
    'proxy_password',
    'proxy_bypass_filter',
    'proxy_bypass_local_addresses',
    'certificate_validation',
    'backup_folder',
    'backup_interval',
    'backup_retention',
    'history_cleanup_days',
    'trust_cgnat_ip_addresses',
]

SECRETS = ['password', 'password_confirmation', 'api_key', 'ssl_cert_password', 'proxy_password']


def init_module_args():
    # define available arguments/parameters a user can pass to the module
    return dict(
        bind_address=dict(type='str'),
        port=dict(type='int'),
        ssl_port=dict(type='int'),
        enable_ssl=dict(type='bool'),
        launch_browser=dict(type='bool'),
        authentication_method=dict(type='str', choices=['none', 'basic', 'forms', 'external']),
        authentication_required=dict(type='str', choices=['enabled', 'disabledForLocalAddresses']),
        analytics_enabled=dict(type='bool'),
        username=dict(type='str'),
        password=dict(type='str', no_log=True),
        password_confirmation=dict(type='str', no_log=True),
        log_level=dict(type='str'),
        log_size_limit=dict(type='int'),
        console_log_level=dict(type='str'),
        branch=dict(type='str'),
        api_key=dict(type='str', no_log=True),
        ssl_cert_path=dict(type='str'),
        ssl_cert_password=dict(type='str', no_log=True),
        url_base=dict(type='str'),
        instance_name=dict(type='str'),
        application_url=dict(type='str'),
        update_automatically=dict(type='bool'),
        update_mechanism=dict(type='str', choices=['builtIn', 'script', 'external', 'apt', 'docker']),
        update_script_path=dict(type='str'),
        proxy_enabled=dict(type='bool'),
        proxy_type=dict(type='str', choices=['http', 'socks4', 'socks5']),
        proxy_hostname=dict(type='str'),
        proxy_port=dict(type='int'),
        proxy_username=dict(type='str'),
        proxy_password=dict(type='str', no_log=True),
        proxy_bypass_filter=dict(type='str', no_log=False),
        proxy_bypass_local_addresses=dict(type='bool'),
        certificate_validation=dict(type='str', choices=['enabled', 'disabledForLocalAddresses', 'disabled']),
        backup_folder=dict(type='str'),
        backup_interval=dict(type='int'),
        backup_retention=dict(type='int'),
        history_cleanup_days=dict(type='int'),
        trust_cgnat_ip_addresses=dict(type='bool'),
    )


def read_host_config(result):
    try:
        return helper.get()
    except prowlarr.ApiException as e:
        module.fail_json('Error getting host config: {}\n body: {}'.format(to_native(e.reason), to_native(e.body)), **result)
    except Exception as e:
        module.fail_json('Error getting host config: {}'.format(to_native(e)), **result)


def update_host_config(want, result):
    result['changed'] = True
    # Only without check mode.
    if not module.check_mode:
        try:
            response = helper.update(want)
        except prowlarr.ApiException as e:
            module.fail_json('Error updating host config: {}\n body: {}'.format(to_native(e.reason), to_native(e.body)), **result)
        except Exception as e:
            module.fail_json('Error updating host config: {}'.format(to_native(e)), **result)
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
    helper = ProwlarrConfigHelper(module.api, '/api/v1/config/host', SECRETS)
    result = dict(
        changed=False,
        id=0,
    )

    # Get resource.
    state = read_host_config(result)
    result.update(helper.view(state))

    # Overlay only the options passed on the current resource.
    if module.params['password'] is not None and module.params['password_confirmation'] is None:
        module.params['password_confirmation'] = module.params['password']
    want, changed = helper.merge(state, module.params, OPTIONS)

    # Update the resource if needed.
    if changed:
        if module._diff:
            result['diff'] = dict(before=helper.view(state), after=helper.view(want))
        update_host_config(want, result)

    # Exit with the result.
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
