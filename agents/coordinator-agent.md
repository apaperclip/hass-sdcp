# Coordinator Agent

## Responsibilities

The coordinator is responsible for:
- advertisement handling
- lifecycle state management
- monitoring-mode transitions
- operational polling orchestration
- availability management
- power transition confirmation polling

## Rules

### Passive Monitoring

When `status_power` indicates a passive/non-operational lifecycle state:
- stop operational polling entirely
- operational entities unavailable
- media_player remains available

### Active Monitoring

When `status_power` indicates operational state:
- enable operational polling
- operational entities available

## Availability Rules

The coordinator distinguishes between:
- `device_available`
- `operational_available`

## Power Semantics

The media_player ON/OFF state follows logical `power`, not `status_power`.
