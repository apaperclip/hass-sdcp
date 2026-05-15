# Testing Strategy

## Goals

The integration prioritizes lifecycle-aware behavioral testing over isolated implementation-detail testing.

Testing should validate:
- lifecycle transitions
- entity availability semantics
- monitoring mode transitions
- discovery behavior
- coordinator behavior
- Home Assistant integration semantics

## Home Assistant Test Infrastructure

The integration should leverage the Home Assistant testing infrastructure provided by the integration blueprint.

Tests should:
- use Home Assistant pytest fixtures
- use async Home Assistant test helpers
- follow Home Assistant integration testing conventions
- integrate with provided blueprint test scaffolding
- use config entry fixtures where appropriate
- validate Home Assistant entity state behavior

The integration SHOULD NOT:
- bypass Home Assistant test infrastructure
- rely primarily on isolated synchronous unit tests
- duplicate existing Home Assistant fixture behavior
- implement standalone unittest.TestCase patterns

## Preferred Test Style

The integration prioritizes:
- integration-style behavioral testing
- lifecycle transition validation
- entity state validation
- availability semantics validation
- coordinator update behavior

over:
- isolated implementation-detail testing
- private method testing
- excessive mocking
- helper micro-tests

## Critical Test Areas

| Area | Required Coverage |
|---|---|
| discovery | UDP advertisement handling |
| lifecycle | passive/active transitions |
| availability | entity unavailable semantics |
| power | logical power vs `status_power` |
| polling | polling enable/disable behavior |
| recovery | advertisement timeout handling |
| transitions | startup/cooldown behavior |
| entities | state restoration behavior |
| diagnostics | lamp runtime sensor updates |

## Lifecycle Transition Testing

Tests should validate:

| Scenario | Expected Result |
|---|---|
| ON → warming | media_player ON, operational entities unavailable |
| warming → active | active polling starts |
| active → cooling | operational polling stops |
| cooling → standby | passive monitoring enabled |
| advertisement timeout | entities unavailable |
| standby advertisement | passive monitoring maintained |
| operational advertisement | active monitoring enabled |

## Discovery Testing

Tests should validate:
- UDP advertisement discovery
- manual IP configuration
- hybrid advertisement/manual operation
- fallback passive polling activation
- advertisement association with configured devices
- DHCP/IP update handling

## Availability Testing

Tests must validate Home Assistant entity availability semantics.

Required scenarios:
- operational entities unavailable during passive mode
- media_player remains available during passive mode
- operational entities restore after active transition
- advertisement timeout marks entities unavailable
- reconnect recovery restores availability

## Monitoring Tests

Tests should validate:
- passive monitoring operation
- active monitoring operation
- monitoring mode transitions
- polling enable/disable behavior
- temporary power confirmation polling
- fallback passive polling behavior

## Logging Validation

Tests should validate important lifecycle logging behavior where practical.

Important areas:
- monitoring transitions
- advertisement timeout events
- lifecycle transitions
- reconnect attempts

## Testing Priorities

### Highest Priority

- lifecycle transitions
- availability semantics
- passive/active monitoring behavior
- advertisement handling
- power transition handling

### Medium Priority

- select entities
- lamp runtime sensor
- reconnect logic

### Lower Priority

- utility helpers
- parsing helpers
- trivial data transformations

## Home Assistant Requirements

Tests should:
- use async Home Assistant helpers
- validate entity registry behavior
- validate config entry setup
- validate coordinator updates
- avoid excessive internal mocking

## Behavioral Contract Validation

Tests should validate behavioral contracts instead of internal implementation details.

Preferred:
- entity availability behavior
- lifecycle outcomes
- monitoring state behavior

Avoid:
- testing private methods directly
- testing internal implementation sequencing
- asserting coordinator internal private state unnecessarily
