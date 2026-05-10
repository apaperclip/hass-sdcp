"""Sensor platform for sdcp."""

from __future__ import annotations

from typing import TYPE_CHECKING

from custom_components.sdcp.const import PARALLEL_UPDATES as PARALLEL_UPDATES
from homeassistant.components.sensor import SensorEntityDescription

from .power_state import ENTITY_DESCRIPTIONS as POWER_STATE_DESCRIPTIONS, SDCPHomeAssistantPowerStateSensor

if TYPE_CHECKING:
    from custom_components.sdcp.data import SDCPHomeAssistantConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

# Combine all entity descriptions from different modules
ENTITY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (*POWER_STATE_DESCRIPTIONS,)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: SDCPHomeAssistantConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    # Add power state sensor
    async_add_entities(
        SDCPHomeAssistantPowerStateSensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in POWER_STATE_DESCRIPTIONS
    )
