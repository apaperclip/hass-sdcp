# SDCP for Home Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

**SDCP for Home Assistant** integrates Sony projectors using the SDCP protocol via the `pysdcp-extended` library.

The integration supports:
- automatic UDP advertisement discovery
- manual IP configuration
- lifecycle-aware monitoring
- Home Assistant entity availability semantics
- projector operational controls

## ✨ Features

- **Automatic Discovery**: Detect compatible Sony projectors using SDCP UDP advertisements
- **Manual Setup**: Configure projectors manually by IP address when broadcasts are unavailable
- **Lifecycle-Aware Monitoring**: Passive monitoring while standby, active monitoring while operational
- **Power Management**: ON/OFF control with projector warmup/cooldown awareness
- **Input Selection**: HDMI input selection and state reporting
- **Calibration Presets**: Select and monitor projector calibration presets
- **Dynamic Range Monitoring**: Monitor and control input dynamic range settings
- **Lamp Diagnostics**: Track projector lamp runtime as a diagnostic sensor
- **Home Assistant Native UX**: Proper entity availability semantics during standby/cooling states

**This integration will set up the following platforms.**

| Platform | Description |
|---|---|
| `media_player` | Projector power control and source selection |
| `select` | HDMI inputs, calibration presets, and dynamic range modes |
| `sensor` | Lamp runtime diagnostic sensor |

## 🚀 Quick Start

### Installation

**Prerequisites:** This integration requires [HACS](https://hacs.xyz/) (Home Assistant Community Store).

1. Add this repository to HACS as a custom repository
2. Install the integration
3. Restart Home Assistant

### Configuration

The integration supports two setup methods:

#### Automatic Discovery

Compatible Sony projectors broadcasting SDCP advertisements will automatically appear in Home Assistant discovery.

#### Manual Configuration

If advertisements are unavailable:

1. Go to **Settings** → **Devices & Services**
2. Click **Add Integration**
3. Search for **SDCP for Home Assistant**
4. Enter the projector IP address

## Monitoring Architecture

The integration uses two monitoring modes:

| Mode | Behavior |
|---|---|
| Passive | Advertisement-driven monitoring while projector non-operational |
| Active | Operational polling while projector operational |

During passive monitoring:
- media_player remains available
- operational entities become unavailable
- operational polling stops

During active monitoring:
- operational polling enabled
- HDMI input monitored
- calibration preset monitored
- dynamic range monitored
- lamp runtime monitored

## Supported Features

### media_player

- Power ON/OFF
- Source selection
- Lifecycle-aware power state handling

### Select Entities

- HDMI input selection
- Calibration preset selection
- Dynamic range mode selection

### Diagnostic Sensors

- Lamp runtime hours

## Discovery Model

The integration supports:

- UDP advertisement discovery
- manual IP fallback
- hybrid advertisement/manual operation

Advertisements are used for:
- passive monitoring
- availability heartbeat
- remote power state detection
- lifecycle updates

## Development

### AI-Assisted Development

This repository uses a structured AI-assisted development architecture.

Primary architecture documents:

- `AGENTS.md`
- `specs/`
- `plans/`
- `tasks/`
- `agents/`

Key specifications:

- `specs/monitoring-model.md`
- `specs/availability-model.md`
- `specs/power-transition-model.md`
- `specs/discovery-design.md`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ by [@apaperclip][user_profile]**

---

[commits-shield]: https://img.shields.io/github/commit-activity/y/apaperclip/hass-sdcp.svg?style=for-the-badge
[commits]: https://github.com/apaperclip/hass-sdcp/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/apaperclip/hass-sdcp.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40apaperclip-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/apaperclip/hass-sdcp.svg?style=for-the-badge
[releases]: https://github.com/apaperclip/hass-sdcp/releases
[user_profile]: https://github.com/apaperclip
