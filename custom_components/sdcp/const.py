"""Constants for sdcp."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

# Integration metadata
DOMAIN = "sdcp"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"

# Platform parallel updates - applied to all platforms
PARALLEL_UPDATES = 1

# Default configuration values
DEFAULT_UPDATE_INTERVAL_SECONDS = 5
DEFAULT_ENABLE_DEBUGGING = False

# Power is driven through the simulated infrared remote items (0x17xx) rather than
# pysdcp-extended's SET_POWER item (0x0130). Sony's VPL-VW1000ES/VW1100ES protocol
# manual lists power as get-only and has no settable power item, so SET_POWER is
# answered with "Item Error: Invalid Item Request" (0x0102). The IR items are
# accepted, and are fire-and-forget: the projector executes them without replying.
IR_COMMAND_POWER_ON = 0x172E
IR_COMMAND_POWER_OFF = 0x172F

# Power status values that mean the lamp is on, or on its way on.
POWER_ON_STATES = frozenset({"power_on", "start_up", "start_up_lamp"})
