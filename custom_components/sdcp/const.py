"""Constants for sdcp."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

# Integration metadata
DOMAIN = "sdcp"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"

# Platform parallel updates - applied to all platforms
PARALLEL_UPDATES = 1

# Default configuration values
DEFAULT_UPDATE_INTERVAL_SECONDS = 30
DEFAULT_ENABLE_DEBUGGING = False
