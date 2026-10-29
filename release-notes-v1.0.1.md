# Magicsee R1 USB Receiver v1.0.1

This release replaces the experimental direction-processing variants with a
small, reproducible implementation based on the captured R1 M+B report format.

## Changes

- Outputs fixed Up, Down, Left, and Right positions on the USB left analog stick.
- Applies center immediately when the R1 sends `0x50`.
- Keeps all six verified button mappings.
- Keeps the `Magicsee R1` USB name and per-receiver identity.
- Removes diagonal synthesis, rotation prediction, delayed-center handling, and
  raw diagnostic output.

## Known hardware limitation

The R1 sends the same `0x50` value for physical center and at some points during
continuous circular movement in M+B mode. Continuous rotation and lower
diagonals therefore cannot be reconstructed reliably. This release intentionally
passes the proven cardinal values and center through without speculative timing
logic.

Use the Windows ZIP for automatic COM-port detection and flashing. The merged
binary is also attached for manual flashing at address `0x0`.
