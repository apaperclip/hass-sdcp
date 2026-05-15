# Power Transition Testing Tasks

## Goals

Validate projector lifecycle-aware power handling.

## Required Tests

- validate power ON request behavior
- validate power OFF request behavior
- validate logical media_player power semantics
- validate warming lifecycle handling
- validate cooling lifecycle handling
- validate `status_power` lifecycle transitions
- validate temporary power confirmation polling
- validate transition into active monitoring
- validate transition into passive monitoring

## Requirements

- use Home Assistant async test infrastructure
- validate behavioral lifecycle outcomes
- avoid direct private coordinator state testing
