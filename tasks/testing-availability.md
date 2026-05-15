# Availability Testing Tasks

## Goals

Validate Home Assistant entity availability semantics.

## Required Tests

- validate operational entities unavailable during passive mode
- validate media_player remains available during passive mode
- validate operational entities restore during active mode
- validate advertisement timeout availability behavior
- validate reconnect recovery availability behavior

## Requirements

- use Home Assistant entity state assertions
- validate Home Assistant availability semantics
- leverage blueprint-provided async infrastructure
