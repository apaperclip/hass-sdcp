"""
API package for sdcp.

Architecture:
    Three-layer data flow: Entities → Coordinator → API Client.
    Only the coordinator should call the API client. Entities must never
    import or call the API client directly.

Exception hierarchy:
    SDCPHomeAssistantApiClientError (base)
    ├── SDCPHomeAssistantApiClientCommunicationError (network/timeout)
    └── SDCPHomeAssistantApiClientAuthenticationError (401/403)

Coordinator exception mapping:
    ApiClientAuthenticationError → ConfigEntryAuthFailed (triggers reauth)
    ApiClientCommunicationError → UpdateFailed (auto-retry)
    ApiClientError             → UpdateFailed (auto-retry)
"""

from .client import (
    SDCPHomeAssistantApiClient,
    SDCPHomeAssistantApiClientAuthenticationError,
    SDCPHomeAssistantApiClientCommunicationError,
    SDCPHomeAssistantApiClientError,
)

__all__ = [
    "SDCPHomeAssistantApiClient",
    "SDCPHomeAssistantApiClientAuthenticationError",
    "SDCPHomeAssistantApiClientCommunicationError",
    "SDCPHomeAssistantApiClientError",
]
