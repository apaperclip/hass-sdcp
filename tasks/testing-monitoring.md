# Monitoring Testing Tasks

## Goals

Validate passive and active monitoring behavior.

## Required Tests

- validate passive monitoring operation
- validate active monitoring operation
- validate passive → active transitions
- validate active → passive transitions
- validate polling enable/disable behavior
- validate temporary power confirmation polling
- validate fallback passive polling behavior

## Requirements

- use Home Assistant async test infrastructure
- leverage integration blueprint fixtures
- validate behavioral outcomes instead of internal implementation details
