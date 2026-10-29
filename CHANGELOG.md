# Changelog

## v1.0.1 — 2026-10-29

- Outputs the R1 direction as fixed cardinal positions on the USB left analog stick.
- Decodes only the hardware-captured three-byte report format: `04 buttons direction`.
- Removes experimental diagonal synthesis, rotation prediction, center-delay logic,
  and diagnostic output.
- Applies center immediately when the R1 sends direction value `0x50`.
- Preserves all six verified button mappings, USB name, pairing behavior, and
  per-board identity.

Known limitation: the R1 emits the same `0x50` value during some continuous
rotations and when physically centered. Continuous circular motion and lower
diagonals therefore cannot be reconstructed reliably from M+B reports.

## v1.0.0 — 2026-10-29

First hardware-verified public release.

- Supports Magicsee R1 M+B BLE mode on Seeed Studio XIAO ESP32S3.
- Exposes a stable four-way digital D-pad with held-direction behavior.
- Maps all six R1 buttons for Windows and Steam.
- Uses the USB product name `Magicsee R1` and preserves per-board identity.
- Verified with two separate R1/XIAO receiver pairs on Windows 11 and Steam.
- Includes an automatic Windows COM-port flasher and merged firmware image.
- Includes a parametric KOYOKOMA USB-C adapter case as an unverified test print.

The case files are not part of the hardware-verified firmware claim. Print the
adapter fit gauge before printing the complete enclosure.
