"""Power switch for sdcp."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from custom_components.sdcp.const import POWER_ON_STATES
from custom_components.sdcp.entity import SDCPHomeAssistantEntity
from homeassistant.components.switch import SwitchDeviceClass, SwitchEntity, SwitchEntityDescription

if TYPE_CHECKING:
    from custom_components.sdcp.coordinator import SDCPHomeAssistantDataUpdateCoordinator

ENTITY_DESCRIPTIONS = (
    SwitchEntityDescription(
        key="power",
        translation_key="power",
        device_class=SwitchDeviceClass.SWITCH,
        icon="mdi:projector",
        has_entity_name=True,
    ),
)


class SDCPHomeAssistantPowerSwitch(SwitchEntity, SDCPHomeAssistantEntity):
    """Switch that powers the projector on and off."""

    def __init__(
        self,
        coordinator: SDCPHomeAssistantDataUpdateCoordinator,
        entity_description: SwitchEntityDescription,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator, entity_description)

    @property
    def is_on(self) -> bool:
        """Return true if the projector is on, or warming up towards on."""
        return self.coordinator.data.get("power") in POWER_ON_STATES

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and self.coordinator.data.get("connected", False)

    async def async_turn_on(self, **_: Any) -> None:
        """Turn the projector on."""
        await self.coordinator.config_entry.runtime_data.client.async_set_power(on=True)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **_: Any) -> None:
        """Turn the projector off."""
        await self.coordinator.config_entry.runtime_data.client.async_set_power(on=False)
        await self.coordinator.async_request_refresh()
