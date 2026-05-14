# Passive Monitoring Task

## Goals

Implement passive monitoring using Sony UDP advertisements.

## Requirements

During passive mode:
- operational polling disabled
- advertisements continue
- media_player remains available
- operational entities unavailable

## Polling Rules

The integration MUST NOT poll:
- HDMI input
- calibration preset
- dynamic range
- lamp hours

while projector is non-operational.
