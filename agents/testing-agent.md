# Testing Agent

## Responsibilities

Ensure the integration implements lifecycle-aware behavioral testing using Home Assistant testing infrastructure.

## Testing Philosophy

Prefer:
- integration-style behavioral tests
- lifecycle transition testing
- entity availability validation
- coordinator behavior validation
- Home Assistant entity state assertions

Avoid:
- isolated implementation-detail tests
- excessive mocking
- direct private method testing
- standalone unittest.TestCase patterns

## Home Assistant Test Infrastructure

Always prefer the Home Assistant testing infrastructure provided by the integration blueprint.

Use:
- pytest Home Assistant fixtures
- async Home Assistant helpers
- config entry fixtures
- entity registry assertions
- Home Assistant integration testing conventions

Avoid:
- bypassing Home Assistant async infrastructure
- duplicating blueprint fixture behavior
- implementing custom synchronous test harnesses

## Critical Test Areas

Always validate:
- passive/active monitoring transitions
- entity availability semantics
- advertisement handling
- lifecycle transitions
- power vs `status_power` behavior
- polling enable/disable behavior
- reconnect recovery behavior

## Behavioral Contract Validation

Prefer validating:
- observable entity behavior
- lifecycle outcomes
- monitoring behavior
- Home Assistant state semantics

Avoid validating:
- internal private coordinator state
- implementation sequencing details
- private helper internals

## Logging Validation

Where practical, validate:
- monitoring transition logging
- advertisement timeout logging
- lifecycle transition logging
- reconnect logging
