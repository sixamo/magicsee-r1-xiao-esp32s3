# Magicsee R1 USB-C dongle case — KOYOKOMA test print

Target adapter: **KOYOKOMA USB-C male-to-male**, Amazon ASIN
`B0CZ9HRKK4`. The published adapter envelope is approximately
`27 × 11 × 6 mm`.

This package is a **first test-print candidate**, not a physically verified
final case. The seller states that appearance can vary by production lot.

## Files

- `KOYOKOMA-adapter-fit-gauge-TEST.stl` — print this first.
- `Magicsee-R1-KOYOKOMA-bottom-TEST.stl` — lower shell.
- `Magicsee-R1-KOYOKOMA-lid-TEST.stl` — press-fit lid.
- `Magicsee-R1-KOYOKOMA-case.scad` — editable OpenSCAD source.
- `generate_case.py` — reproducible STL generator.

## Print settings

- Material: PLA or PETG
- Nozzle: 0.4 mm
- Layer: 0.20 mm
- Walls: 3
- Infill: 20%
- Supports: none
- Print all supplied STL files in their exported orientation.

## First-fit procedure

1. Print only `KOYOKOMA-adapter-fit-gauge-TEST.stl`.
2. The black adapter body should slide through with light drag.
3. If it does not enter, measure the adapter body width and height with
   calipers. Change `adapter_w`, `adapter_h`, or `fit` in the SCAD source.
4. Only after the gauge fits, print the bottom and lid.

## Assembly notes

- The external USB-C male plug exits the short end of the case.
- The adapter body and XIAO must rest on their printed guides; do not use the
  XIAO USB-C receptacle as the only structural support.
- Use thin removable foam tape for axial preload.
- Put the supplied adhesive antenna in the tail bay, away from the metal USB
  adapter. A lid slot permits external antenna routing if desired.
- The lid opening provides access to the XIAO B/R buttons and status LED.

Nominal outer enclosure: approximately `54 × 22 × 9.6 mm`, plus the exposed
USB-C plug.
