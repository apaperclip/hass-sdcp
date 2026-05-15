# Discovery Testing Tasks

## Goals

Validate discovery and device association behavior.

## Required Tests

- validate UDP advertisement discovery
- validate discovery flow creation
- validate manual IP configuration
- validate advertisement association with configured devices
- validate DHCP/IP update handling
- validate advertisement timeout handling
- validate fallback passive polling activation

## Requirements

- use Home Assistant async test infrastructure
- use blueprint-provided fixtures where possible
- avoid isolated synchronous testing patterns
