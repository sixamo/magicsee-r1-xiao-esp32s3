Magicsee R1 USB receiver v1.0.2 for Seeed Studio XIAO ESP32S3

REQUIREMENTS
- Windows 10 or 11
- Seeed Studio XIAO ESP32S3
- The supplied external antenna must be connected before pairing
- A data-capable USB-C cable for flashing

FLASHING
1. Connect the XIAO by USB.
2. Double-click FLASH-MAGICSEE-R1.bat.
3. Hold the XIAO B button.
4. Tap the XIAO R button once.
5. Wait one second, then release B.
6. Do not disconnect USB until FLASH COMPLETED is displayed.

PAIRING
1. Wait 10 seconds after flashing.
2. Press the XIAO B button once.
3. Hold Magicsee R1 M+B until the R1 LED flashes rapidly.
4. Wait for the flashing to stop.

The controller appears as Magicsee R1. Steam may show its generic SInput name.

INPUT BEHAVIOR
- Fixed four-way output on the USB left analog stick
- Event-driven USB output; no periodic re-publication of the last direction
- No diagonal synthesis or rotation prediction
- Center is applied when the R1 sends direction value 0x50
- Continuous circular movement and lower diagonals are not reliably available
  from the R1 M+B report stream

Source and licenses:
https://github.com/sixamo/magicsee-r1-xiao-esp32s3
