# Power Transition Model

## Overview

Sony projectors have long startup and cooldown phases.

The integration separates:

- logical power state
- physical lifecycle state

## Logical Power State

Used for:
- media_player ON/OFF state
- user intent
- immediate UX response

The media_player entity should immediately reflect requested ON/OFF state after power commands.

## status_power

Used for:
- operational availability
- monitoring mode selection
- polling enable/disable
- lifecycle reporting

Actual lifecycle values MUST come from `pysdcp_extended.protocol`.

## Startup Behavior

After power on:
- media_player immediately ON
- operational entities unavailable until operational lifecycle state reached
- temporary confirmation polling enabled

## Cooldown Behavior

After power off:
- media_player immediately OFF
- projector may remain cooling for several minutes
- operational entities unavailable
- passive monitoring enabled

## Confirmation Polling

After explicit ON/OFF commands:
- perform temporary `get_status_power()` checks
- recommended interval: 5 seconds
- recommended timeout: 120 seconds

This is transition verification, not steady-state polling.
