"""Generate a two-piece Magicsee R1 receiver case and adapter fit gauge.

Target adapter: KOYOKOMA USB-C male-to-male, Amazon ASIN B0CZ9HRKK4.
Published envelope: 27 x 11 x 6 mm.  The product listing warns that the
appearance can vary by production lot, so all adapter dimensions are kept as
parameters and this first release is explicitly a test-print candidate.
"""

from pathlib import Path

import trimesh


# Published/measured envelopes, millimetres.
ADAPTER_TOTAL = 27.0
ADAPTER_WIDTH = 11.0
ADAPTER_HEIGHT = 6.0
USB_C_PROJECTION = 7.0
ADAPTER_BODY = ADAPTER_TOTAL - 2 * USB_C_PROJECTION
XIAO_LENGTH = 21.0
XIAO_WIDTH = 17.8

# FDM allowances for a 0.4 mm nozzle.  FIT is per side.
FIT = 0.30
WALL = 1.60
FLOOR = 1.60
LID = 2.20
LIP_HEIGHT = 1.40
LIP_THICKNESS = 1.00

# Layout: adapter body, XIAO, then a metal-free antenna bay.
CASE_X = 54.0
CASE_Y = 22.0
BOTTOM_Z = 7.4
ADAPTER_X = WALL
BOARD_X = ADAPTER_X + ADAPTER_BODY
ANTENNA_X = BOARD_X + XIAO_LENGTH + 1.0


def box(size, origin):
    mesh = trimesh.creation.box(extents=size)
    mesh.apply_translation([
        origin[0] + size[0] / 2,
        origin[1] + size[1] / 2,
        origin[2] + size[2] / 2,
    ])
    return mesh


def difference(base, cutters):
    result = trimesh.boolean.difference([base, *cutters], engine="manifold")
    if result is None:
        raise RuntimeError("Boolean difference failed")
    return result


def union(parts):
    result = trimesh.boolean.union(parts, engine="manifold")
    if result is None:
        raise RuntimeError("Boolean union failed")
    return result


def make_bottom():
    outer = box((CASE_X, CASE_Y, BOTTOM_Z), (0, 0, 0))
    inner = box(
        (CASE_X - 2 * WALL, CASE_Y - 2 * WALL, BOTTOM_Z - FLOOR + 1.0),
        (WALL, WALL, FLOOR),
    )

    # The external male plug is the only part protruding from the enclosure.
    # A generous opening avoids loading the PC port if the adapter moulding is
    # slightly off-centre.
    usb_exit_y = 9.4
    usb_exit_z = 4.0
    usb_exit = box(
        (WALL + 1.0, usb_exit_y, usb_exit_z),
        (-0.5, (CASE_Y - usb_exit_y) / 2, FLOOR + 0.7),
    )
    shell = difference(outer, [inner, usb_exit])

    # Low edge rails locate the XIAO without touching bottom-side components.
    board_y = (CASE_Y - XIAO_WIDTH) / 2
    rails = [
        box((XIAO_LENGTH, 0.8, 0.7), (BOARD_X, board_y - 0.7, FLOOR)),
        box((XIAO_LENGTH, 0.8, 0.7),
            (BOARD_X, board_y + XIAO_WIDTH - 0.1, FLOOR)),
    ]

    # Adapter-body side guides.  They stop short of the top so removal remains
    # possible and use foam tape, not the USB connector, for axial preload.
    guide_y = (CASE_Y - (ADAPTER_WIDTH + 2 * FIT)) / 2
    guides = [
        box((ADAPTER_BODY, 0.8, 2.0),
            (ADAPTER_X, guide_y - 0.8, FLOOR)),
        box((ADAPTER_BODY, 0.8, 2.0),
            (ADAPTER_X, guide_y + ADAPTER_WIDTH + 2 * FIT, FLOOR)),
    ]
    return union([shell, *rails, *guides])


def make_lid():
    plate = box((CASE_X, CASE_Y, LID), (0, 0, 0))
    lip_outer = box(
        (CASE_X - 2 * (WALL + FIT), CASE_Y - 2 * (WALL + FIT), LIP_HEIGHT),
        (WALL + FIT, WALL + FIT, LID),
    )
    lip_inner = box(
        (
            CASE_X - 2 * (WALL + FIT + LIP_THICKNESS),
            CASE_Y - 2 * (WALL + FIT + LIP_THICKNESS),
            LIP_HEIGHT + 0.2,
        ),
        (
            WALL + FIT + LIP_THICKNESS,
            WALL + FIT + LIP_THICKNESS,
            LID - 0.1,
        ),
    )
    lip = difference(lip_outer, [lip_inner])
    lid = union([plate, lip])

    # Combined B/R button and status LED service opening.
    service = box(
        (13.0, 9.0, LID + LIP_HEIGHT + 2.0),
        (BOARD_X + 3.0, (CASE_Y - 9.0) / 2, -1.0),
    )

    # A narrow slot at the tail provides a route for the antenna coax if the
    # supplied adhesive antenna is mounted outside instead of in the tail bay.
    coax_slot = box(
        (5.0, WALL + 1.0, 2.0),
        (ANTENNA_X + 4.0, CASE_Y - WALL - 0.5, LID - 0.2),
    )
    return difference(lid, [service, coax_slot])


def make_fit_gauge():
    # Print this first.  The adapter body should slide through with light drag.
    outer = box((8.0, 15.0, 10.0), (0, 0, 0))
    tunnel = box(
        (10.0, ADAPTER_WIDTH + 2 * FIT, ADAPTER_HEIGHT + 2 * FIT),
        (-1.0, (15.0 - ADAPTER_WIDTH - 2 * FIT) / 2,
         (10.0 - ADAPTER_HEIGHT - 2 * FIT) / 2),
    )
    return difference(outer, [tunnel])


def export_checked(mesh, path):
    if not mesh.is_watertight:
        raise RuntimeError(f"{path.name} is not watertight")
    if mesh.volume <= 0:
        raise RuntimeError(f"{path.name} has invalid volume")
    mesh.export(path)


def main():
    out = Path(__file__).resolve().parent
    meshes = {
        "Magicsee-R1-KOYOKOMA-bottom-TEST.stl": make_bottom(),
        "Magicsee-R1-KOYOKOMA-lid-TEST.stl": make_lid(),
        "KOYOKOMA-adapter-fit-gauge-TEST.stl": make_fit_gauge(),
    }
    for name, mesh in meshes.items():
        export_checked(mesh, out / name)
        print(f"{name}: {mesh.volume:.1f} mm^3, watertight={mesh.is_watertight}")


if __name__ == "__main__":
    main()
