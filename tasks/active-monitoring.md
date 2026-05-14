# Active Monitoring Task

## Goals

Implement active operational polling when projector reaches operational lifecycle state.

## Requirements

- enable operational polling only during active mode
- poll:
  - HDMI input
  - calibration preset
  - dynamic range
  - lamp hours
- recommended interval: 15 seconds
- operational entities available during active mode

## Constraints

- actual lifecycle state definitions must come from `pysdcp_extended.protocol`
- no polling during passive mode
