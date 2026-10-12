# Copyright: (c) 2020, Fuochi <devopsarr@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import copy
import re

MASK = '********'
SECRET_NAME = re.compile(r'apikey|api_key|password|passkey|cookie|token|secret|pid|rsskey|username', re.IGNORECASE)


def _dump(resource):
    if hasattr(resource, 'model_dump'):
        return resource.model_dump(by_alias=False)
    return copy.deepcopy(resource)


def _clean(value):
    # Drop the unset (None) keys so that both sides of the diff are comparable.
    if isinstance(value, dict):
        return dict((key, _clean(item)) for key, item in value.items() if item is not None)
    if isinstance(value, list):
        return [_clean(item) for item in value]
    return value


def _is_secret(field, live_masked):
    return bool(SECRET_NAME.search(str(field.get('name', '')))) or field.get('name') in live_masked


def _mask_fields(fields, live_masked):
    # Sorted by name and masked: only used in the diff, never sent to the API.
    for field in fields:
        if 'value' in field and _is_secret(field, live_masked):
            field['value'] = MASK
    return sorted(fields, key=lambda field: str(field.get('name', '')))


def _live_masked_names(fields):
    return set(field.get('name') for field in fields if field.get('value') == MASK)


def diff_create(want):
    after = _clean(_dump(want))
    if 'fields' in after:
        after['fields'] = _mask_fields(after['fields'], set())
    return dict(before={}, after=after)


def diff_delete(current):
    before = _clean(_dump(current))
    if 'fields' in before:
        before['fields'] = _mask_fields(before['fields'], set())
    return dict(before=before, after={})


def diff_update(current, want):
    """Current state against desired one, as the modules compare them.

    The top level options are overlaid, the fields are overlaid by name.
    """
    before = _dump(current)
    desired = _dump(want)
    after = copy.deepcopy(before)
    for key, value in desired.items():
        if key != 'fields' and value is not None:
            after[key] = value

    before_fields = before.get('fields') or []
    after_fields = after.get('fields') or []
    for want_field in desired.get('fields') or []:
        for after_field in after_fields:
            if after_field.get('name') == want_field.get('name'):
                after_field['value'] = want_field.get('value')
                break
        else:
            after_fields.append(want_field)
    after['fields'] = after_fields

    live_masked = _live_masked_names(before_fields)
    before = _clean(before)
    after = _clean(after)
    if before_fields:
        before['fields'] = _mask_fields(before['fields'], live_masked)
    if after_fields:
        after['fields'] = _mask_fields(after['fields'], live_masked)
    return dict(before=before, after=after)
