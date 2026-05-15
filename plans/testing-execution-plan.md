# Testing Execution Plan

## Goals

Ensure all integration functionality includes:
- automated test coverage
- Home Assistant behavioral validation
- lifecycle-aware validation
- test execution requirements
- successful test completion before merge

The integration should not consider features complete until:
- tests are implemented
- tests execute successfully
- Home Assistant behavioral semantics validated

## Testing Workflow

Implementation workflow:

```text
Architecture Spec
        ↓
Implementation
        ↓
Test Creation
        ↓
Test Execution
        ↓
Behavior Validation
        ↓
Merge Readiness
```

## Required Test Coverage

Every implemented feature should include corresponding tests.

| Feature Area | Required Tests |
|---|---|
| discovery | advertisement discovery and manual configuration |
| monitoring | passive/active monitoring transitions |
| availability | Home Assistant availability semantics |
| power | lifecycle-aware power handling |
| entities | entity state and restoration behavior |
| diagnostics | lamp runtime diagnostic sensor |
| recovery | reconnect and timeout handling |
| logging | important lifecycle logging behavior |

## Required Test Types

### Integration Tests

Primary testing approach.

Validate:
- Home Assistant integration behavior
- lifecycle transitions
- entity state behavior
- config entry setup
- coordinator updates

### Behavioral Tests

Validate:
- passive monitoring behavior
- active monitoring behavior
- availability transitions
- lifecycle-aware entity behavior

### Recovery Tests

Validate:
- advertisement timeout handling
- reconnect behavior
- polling recovery
- fallback passive polling

## Home Assistant Test Infrastructure

Tests should leverage:
- Home Assistant pytest fixtures
- async Home Assistant helpers
- integration blueprint test infrastructure
- config entry fixtures
- Home Assistant entity assertions

Avoid:
- isolated synchronous testing patterns
- excessive mocking
- standalone unittest frameworks

## Test Execution Requirements

Before merge, the following should execute successfully:

- unit and integration test suite
- Home Assistant async integration tests
- lifecycle transition tests
- entity availability tests
- discovery tests

## Success Criteria

A feature is only considered complete when:

- implementation completed
- corresponding tests implemented
- tests execute successfully
- Home Assistant semantics validated
- lifecycle behavior validated
- no regression failures introduced

## CI Expectations

Continuous integration should validate:
- test execution success
- async test correctness
- Home Assistant integration setup
- entity behavior expectations
- lifecycle transition behavior

## AI Development Expectations

AI-generated implementations should:
- create tests alongside implementation
- use Home Assistant test infrastructure
- validate lifecycle behavior
- validate availability semantics
- avoid implementation-detail-only tests

AI-generated changes should not be considered complete without:
- corresponding tests
- successful test execution
- behavioral validation
