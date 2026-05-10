"""
Options flow schemas.

Schemas for the options flow that allows users to modify settings
after initial configuration.

When adding many options, consider grouping them:
- basic_options.py: Common settings (update interval, debug mode)
- advanced_options.py: Advanced settings
- device_options.py: Device-specific settings
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import voluptuous as vol

from custom_components.sdcp.const import DEFAULT_ENABLE_DEBUGGING, DEFAULT_UPDATE_INTERVAL_SECONDS
from homeassistant.helpers import selector


def _get_update_interval_default(defaults: Mapping[str, Any]) -> int:
    """Get the default update interval in seconds.

    Supports legacy stored values in hours via update_interval_hours.
    """
    if "update_interval_seconds" in defaults:
        return int(defaults["update_interval_seconds"])

    legacy_value = defaults.get("update_interval_hours")
    if legacy_value is not None:
        return int(float(legacy_value) * 3600)

    return DEFAULT_UPDATE_INTERVAL_SECONDS


def get_options_schema(defaults: Mapping[str, Any] | None = None) -> vol.Schema:
    """
    Get schema for options flow.

    Args:
        defaults: Optional dictionary of current option values.

    Returns:
        Voluptuous schema for options configuration.

    """
    defaults = defaults or {}
    return vol.Schema(
        {
            vol.Optional(
                "update_interval_seconds",
                default=_get_update_interval_default(defaults),
            ): selector.NumberSelector(
                selector.NumberSelectorConfig(
                    min=30,
                    max=86400,
                    step=30,
                    unit_of_measurement="s",
                    mode=selector.NumberSelectorMode.BOX,
                ),
            ),
            vol.Optional(
                "enable_debugging",
                default=defaults.get("enable_debugging", DEFAULT_ENABLE_DEBUGGING),
            ): selector.BooleanSelector(),
            vol.Optional(
                "custom_icon",
                default=defaults.get("custom_icon"),
            ): selector.IconSelector(),
        },
    )


__all__ = [
    "get_options_schema",
]
