"""Lamp timer sensor for sdcp."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.sdcp.entity import SDCPHomeAssistantEntity
from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.const import EntityCategory

if TYPE_CHECKING:
    from custom_components.sdcp.coordinator import SDCPHomeAssistantDataUpdateCoordinator

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="lamp_hours",
        translation_key="lamp_hours",
        icon="mdi:timer",
        entity_category=EntityCategory.DIAGNOSTIC,
        native_unit_of_measurement="h",
        has_entity_name=True,
    ),
)


class SDCPHomeAssistantLampHoursSensor(SensorEntity, SDCPHomeAssistantEntity):
    """Lamp hours sensor class."""

    def __init__(
        self,
        coordinator: SDCPHomeAssistantDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entity_description)

    @property
    def native_value(self) -> int | None:
        """Return the native value of the sensor."""
        if not self.coordinator.last_update_success:
            return None
        return self.coordinator.data.get("lamp_hours")

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and self.coordinator.data.get("connected", False)
