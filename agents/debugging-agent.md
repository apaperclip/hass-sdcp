# Debugging Agent

## Responsibilities

Ensure the integration provides sufficient observability for:
- lifecycle transitions
- monitoring state changes
- availability transitions
- advertisement handling
- protocol communication failures

## Logging Rules

### DEBUG Logging

Always log at DEBUG level:
- advertisement receipt
- advertisement lifecycle state parsing
- monitoring mode transitions
- active polling start/stop
- operational availability transitions
- power transition confirmation polling
- fallback passive polling activation
- protocol request/response summaries

### WARNING Logging

Always log at WARNING level:
- advertisement timeout events
- repeated polling failures
- reconnect attempts
- unexpected lifecycle transitions

### ERROR Logging

Always log at ERROR level:
- unrecoverable protocol failures
- invalid advertisement parsing
- unexpected coordinator exceptions

## Home Assistant Requirements

- use standard Home Assistant logger facilities
- never use `print()`
- avoid excessive INFO logging noise

## Troubleshooting Expectations

Logging should allow developers to determine:
- why entities are unavailable
- why monitoring mode changed
- whether advertisements are arriving
- whether polling is operational
- current lifecycle state
- whether power transitions are progressing correctly
