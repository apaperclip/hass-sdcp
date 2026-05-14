# Availability Model

## Core Availability Concepts

The integration distinguishes between:

- `device_available`
- `operational_available`

## device_available

Represents:
- advertisements being received
- projector reachable on network

The media_player entity uses `device_available`.

## operational_available

Represents:
- projector operational subsystem available
- operational SDCP commands supported

Operational entities use `operational_available`.

## Passive Monitoring

During passive monitoring:

```python
device_available = True
operational_available = False
```

Operational entities become unavailable and operational polling stops entirely.

## Active Monitoring

During active monitoring:

```python
device_available = True
operational_available = True
```

All entities available.

## Network Loss

If advertisements stop:

```python
device_available = False
operational_available = False
```

All entities unavailable.
