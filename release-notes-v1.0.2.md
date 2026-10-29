# Magicsee R1 USB Receiver v1.0.2

This release fixes direction input continuing after the physical R1 stick is
released.

## Changes

- Removes the 125 Hz re-publication of the last input state.
- Sends USB input only when a new R1 BLE report arrives.
- Retains fixed four-direction output on the USB left analog stick.
- Retains all six verified button mappings, Steer behavior, the `Magicsee R1`
  USB name, pairing behavior, and per-receiver identity.
- Keeps the hardware-captured three-byte report parser and immediate handling
  of center value `0x50`.

The no-repeat behavior was verified on the physical R1/XIAO receiver before
this release.

## Known hardware limitation

The R1 sends the same `0x50` value for physical center and at some points during
continuous circular movement in M+B mode. Continuous rotation and lower
diagonals therefore cannot be reconstructed reliably. The firmware intentionally
passes only the proven cardinal values and center without timing prediction.
