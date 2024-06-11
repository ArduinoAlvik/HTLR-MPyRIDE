# <a href="https://viper-ide.org" target="_blank">ViperIDE ⇱</a>

[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md) 
[![GitHub issues](https://img.shields.io/github/issues-raw/vshymanskyy/ViperIDE?style=flat-square&label=issues&color=success)](https://github.com/vshymanskyy/ViperIDE/issues) 
[![GitHub license](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](https://github.com/vshymanskyy/ViperIDE) 

A MicroPython IDE that works directly in the browser, leveraging modern web technologies.

- No software installation required, works out of the box
- Direct USB / Serial connection works on **Windows**, **MacOS**, **Linux**, **Android**, **Chromebook**
- [`WebREPL`](docs/Web-REPL.md) and [`Bluetooth LE`](docs/Bluetooth-REPL.md) connection support
- Covers most of the functionality of `mpremote`

![image](docs/images/screenshot-desktop-chrome.png)

## Tested with

- ESP32, ESP32S3, ESP32C3
- Raspberry Pi Pico (RP2040)
- Micro:bit (nRF51822)
- Micro:bit v2 (nRF52833) with [`CircuitPython`](https://circuitpython.org/board/microbit_v2)
- Air602 (WM W600) with [`robert-hh` port](https://github.com/robert-hh/Shared-Stuff/tree/master/w600_firmware)
- Realtek RTL8721 with [`ambiot` port](https://github.com/ambiot/micropython/releases)

## Features

- **File Editor**
  - Syntax highlighting for `.py`, `.json`, `.pem` (based on `CodeMirror`)
  - Auto expand/minify of `.json` files
  - Viewer mode for `Markdown`
  - `Hex` viewer for binary files
  - Unicode support (`UTF8`)
  - Run file without saving
- **File Manager**
  - Add, remove files and directories
  - Root FS stats display
- **Package Manager**
  - `micropython-lib` index
- **Terminal / REPL**
  - ANSI escape sequences support (based on `xterm.js`)
  - Snippet support - *WIP*
- Improved UX
  - Device and system info display
  - Responsive layout, full screen mode
  - Use of natural sorting

> [!TIP]
> `mpremote` is still a great tool for automation. Learn to use it!

