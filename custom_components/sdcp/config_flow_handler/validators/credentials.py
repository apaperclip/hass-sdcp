"""
Credential validators.

Validation functions for user credentials and authentication.

When this file grows, consider splitting into:
- credentials.py: Basic credential validation
- oauth.py: OAuth-specific validation
- api_auth.py: API authentication methods
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.sdcp.api import SDCPHomeAssistantApiClient

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant


async def validate_credentials(hass: HomeAssistant, host: str) -> None:
    """
    Validate host by testing SDCP connection.

    Args:
        hass: Home Assistant instance.
        host: The host (IP address or hostname) to validate.

    Raises:
        SDCPHomeAssistantApiClientCommunicationError: If connection fails.
        SDCPHomeAssistantApiClientError: For other API errors.

    """
    client = SDCPHomeAssistantApiClient(host=host)
    await client.async_connect()
    # Test a simple query to ensure the projector responds
    await client.async_get_data()
    await client.async_disconnect()  # May raise authentication/communication errors


__all__ = [
    "validate_credentials",
]
