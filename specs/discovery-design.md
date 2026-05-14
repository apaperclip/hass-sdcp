# Discovery Design

## Overview

The integration supports two discovery paths:

- UDP advertisement auto-discovery
- manual IP configuration

The architecture is advertisement-first with manual fallback support.

## Automatic Discovery

Sony projectors broadcast UDP advertisement packets approximately every 30 seconds.

Advertisements are used for:
- automatic discovery
- lifecycle updates
- availability heartbeat
- passive monitoring
- external power state detection

## Advertisement Listener

The integration should implement a shared global UDP listener.

The listener is responsible for:
- receiving advertisement packets
- parsing SDCP advertisement payloads
- updating coordinator lifecycle state
- triggering Home Assistant discovery flows

Only one listener should exist globally.

The integration MUST NOT create one listener per projector.

## Discovery Flow

When an unknown projector advertisement is received:

```text
Advertisement Received
        ↓
Unknown projector detected
        ↓
Trigger Home Assistant discovery flow
```

## Manual Configuration

The integration must support manual host/IP configuration.

This is required because many networks:
- block broadcasts
- isolate VLANs
- suppress multicast/broadcast traffic
- filter UDP advertisements

Manual configuration allows the integration to function without advertisements.

## Hybrid Discovery Model

Manual configuration does NOT disable advertisement handling.

If advertisements later appear:
- advertisements continue updating lifecycle state
- advertisements refresh availability
- advertisements may refresh IP metadata

This creates a hybrid architecture:

| Function | Source |
|---|---|
| initial connectivity | manual IP |
| lifecycle updates | advertisements |

## Device Identity

The integration should identify projectors using stable identifiers such as:
- serial number
- MAC address
- protocol device identifier

The integration SHOULD NOT rely solely on IP address.

## DHCP Handling

If a projector IP changes:
- advertisements may update current IP metadata
- coordinator should refresh connection target

## Fallback Passive Monitoring

If:
- advertisements are unavailable
- manual IP configuration exists

then the integration may perform very low-frequency passive status checks.

Recommended:
- `get_status_power()` only
- 60-120 second interval

This fallback exists only for networks where advertisements are unavailable.

## Preferred Monitoring Model

Preferred architecture:

```text
Advertisement-driven passive monitoring
```

Fallback architecture:

```text
Manual IP + low-frequency passive status checks
```

## Availability Semantics

Advertisements are the preferred source for:
- passive availability
- lifecycle updates
- remote-control power changes
- standby detection

Operational polling should still remain disabled during passive monitoring.
