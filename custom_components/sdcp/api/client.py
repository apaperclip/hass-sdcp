"""
API Client for sdcp.

This module provides the API client for communicating with Sony projectors
via SDCP protocol using the pysdcp-extended library.
"""

from __future__ import annotations

import asyncio
from typing import Any, cast

from pysdcp_extended import ACTIONS, COMMANDS, POWER_STATUS, Projector  # type: ignore[import-untyped]

POWER_STATUS_REVERSE = {value: key.lower() for key, value in POWER_STATUS.items()}


class SDCPHomeAssistantApiClientError(Exception):
    """Base exception to indicate a general API error."""


class SDCPHomeAssistantApiClientCommunicationError(
    SDCPHomeAssistantApiClientError,
):
    """Exception to indicate a communication error with the projector."""


class SDCPHomeAssistantApiClientAuthenticationError(
    SDCPHomeAssistantApiClientError,
):
    """Exception to indicate an authentication error with the projector."""


class SDCPHomeAssistantApiClient:
    """
    API Client for SDCP integration.

    This client wraps the pysdcp-extended library to communicate with Sony projectors
    via SDCP protocol over TCP. It provides a clean interface for the coordinator
    to query projector state and control functions.

    Attributes:
        _host: The IP address or hostname of the Sony projector.
        _client: The pysdcp-extended SDCP client instance.
        _connected: Whether the TCP connection is currently established.
    """

    def __init__(
        self,
        host: str,
    ) -> None:
        """
        Initialize the API Client with projector host.

        Args:
            host: The IP address or hostname of the Sony projector.

        """
        self._host = host
        self._client: Projector | None = None
        self._connected = False

    async def async_connect(self) -> None:
        """
        Prepare the underlying projector client.

        The pysdcp-extended Projector client is synchronous, so we only
        instantiate it here and keep it available for async wrapper calls.
        """
        try:
            self._client = Projector(ip=self._host)
            self._connected = True
        except Exception as exception:
            self._connected = False
            msg = f"Failed to initialize projector client at {self._host}: {exception}"
            raise SDCPHomeAssistantApiClientCommunicationError(msg) from exception

    async def async_disconnect(self) -> None:
        """
        Release the projector client.

        The underlying pysdcp-extended library opens a new socket for each
        command, so there is no persistent connection to close here.
        """
        if self._client is not None:
            self._client = None
            self._connected = False

    @property
    def is_connected(self) -> bool:
        """
        Check if the client is currently connected to the projector.

        Returns:
            True if connected, False otherwise.

        """
        return self._connected

    async def async_get_data(self) -> dict[str, Any]:
        """
        Get current projector data.

        Queries the projector for its current state including power status,
        input selection, lamp hours, and other diagnostic information.

        Returns:
            A dictionary containing the current projector state.

        Raises:
            SDCPHomeAssistantApiClientCommunicationError: If communication fails.
            SDCPHomeAssistantApiClientError: For other API errors.

        """
        if not self._connected or not self._client:
            raise SDCPHomeAssistantApiClientCommunicationError("Not connected to projector")

        try:
            power_code = await asyncio.to_thread(
                self._client._send_command,  # noqa: SLF001
                ACTIONS["GET"],
                COMMANDS["GET_STATUS_POWER"],
            )
            lamp_hours = await asyncio.to_thread(self._client.get_lamp_hours)
        except Exception as exception:
            self._connected = False
            msg = f"Error querying projector at {self._host}: {exception}"
            raise SDCPHomeAssistantApiClientCommunicationError(msg) from exception

        power_state = POWER_STATUS_REVERSE.get(cast(int, power_code), f"unknown_{power_code}")

        return {
            "power": power_state,
            "lamp_hours": lamp_hours,
            "connected": True,
        }
