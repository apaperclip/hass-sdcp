# Logging and Diagnostics

## Goals

The integration must support increasing logging verbosity for troubleshooting without code changes.

Logging and diagnostics are considered part of the integration operational contract.

The integration should provide sufficient observability for:
- lifecycle transitions
- advertisement handling
- monitoring mode changes
- entity availability changes
- polling behavior
- SDCP communication failures

## Logging Categories

| Category | Purpose |
|---|---|
| discovery | UDP advertisements and discovery flow |
| coordinator | lifecycle state management |
| polling | active monitoring behavior |
| availability | entity availability transitions |
| protocol | SDCP requests and responses |
| power | logical power and `status_power` transitions |

## Logging Levels

### INFO

INFO logging should be used for:
- integration startup
- projector discovery
- manual configuration setup
- major lifecycle events

### DEBUG

DEBUG logging should be used for:
- advertisement packets received
- advertisement parsing
- lifecycle transitions
- monitoring mode changes
- active polling transitions
- availability changes
- power transition confirmation polling
- protocol timing
- protocol request/response summaries

### WARNING

WARNING logging should be used for:
- advertisement timeout events
- polling failures
- recoverable communication failures
- unexpected lifecycle states

### ERROR

ERROR logging should be used for:
- unrecoverable protocol failures
- invalid packet parsing
- coordinator failures
- unexpected runtime exceptions

## Advertisement Logging

The integration should log:
- advertisement receipt
- advertisement source IP
- advertisement lifecycle state
- advertisement timeout transitions

Advertisement packet payloads should only be logged at DEBUG level.

## Monitoring Transition Logging

The integration should log transitions between:
- passive monitoring
- active monitoring

The logs should include:
- previous mode
- new mode
- triggering lifecycle state

## Availability Logging

The integration should log:
- operational entity availability changes
- device availability changes
- advertisement timeout conditions

## Protocol Logging

The integration should log:
- command execution failures
- protocol timeouts
- reconnect attempts
- temporary power confirmation polling

Protocol request/response payloads should only be logged at DEBUG level.

## Sensitive Data Rules

Logs must not expose:
- credentials
- tokens
- personally identifiable information

## Home Assistant Logger Integration

The integration must use standard Home Assistant logging facilities.

The integration must not use:
- `print()`
- direct stdout logging

Example Home Assistant logger configuration:

```yaml
logger:
  logs:
    custom_components.sdcp: debug
```

## Troubleshooting Expectations

With debug logging enabled, users and developers should be able to determine:

- whether advertisements are arriving
- whether passive or active monitoring is enabled
- current `status_power` lifecycle state
- why entities are unavailable
- whether operational polling is running
- whether power transition confirmation polling is active
- whether fallback passive polling is active
- whether advertisement timeouts occurred
- whether polling failures are occurring
- whether projector lifecycle transitions are progressing
