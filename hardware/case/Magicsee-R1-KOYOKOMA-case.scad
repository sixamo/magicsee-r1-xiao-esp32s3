// Magicsee R1 / XIAO ESP32S3 receiver case
// Target: KOYOKOMA USB-C male-to-male, Amazon ASIN B0CZ9HRKK4
// TEST PRINT: adapter appearance may vary by production lot.

part = "layout"; // "bottom", "lid", "gauge", or "layout"

adapter_total = 27.0;
adapter_w = 11.0;
adapter_h = 6.0;
usb_c_projection = 7.0;
adapter_body = adapter_total - 2 * usb_c_projection;
xiao_l = 21.0;
xiao_w = 17.8;

fit = 0.30;
wall = 1.60;
floor_h = 1.60;
lid_h = 2.20;
lip_h = 1.40;
lip_t = 1.00;

case_x = 54.0;
case_y = 22.0;
bottom_z = 7.4;
adapter_x = wall;
board_x = adapter_x + adapter_body;
antenna_x = board_x + xiao_l + 1.0;

module bottom() {
  difference() {
    cube([case_x, case_y, bottom_z]);
    translate([wall, wall, floor_h])
      cube([case_x-2*wall, case_y-2*wall, bottom_z-floor_h+1]);
    translate([-0.5, (case_y-9.4)/2, floor_h+0.7])
      cube([wall+1, 9.4, 4.0]);
  }
  board_y = (case_y-xiao_w)/2;
  translate([board_x, board_y-0.7, floor_h]) cube([xiao_l,0.8,0.7]);
  translate([board_x, board_y+xiao_w-0.1, floor_h]) cube([xiao_l,0.8,0.7]);
  guide_y = (case_y-(adapter_w+2*fit))/2;
  translate([adapter_x, guide_y-0.8, floor_h]) cube([adapter_body,0.8,2]);
  translate([adapter_x, guide_y+adapter_w+2*fit, floor_h]) cube([adapter_body,0.8,2]);
}

module lid() {
  difference() {
    union() {
      cube([case_x, case_y, lid_h]);
      difference() {
        translate([wall+fit, wall+fit, lid_h])
          cube([case_x-2*(wall+fit), case_y-2*(wall+fit), lip_h]);
        translate([wall+fit+lip_t, wall+fit+lip_t, lid_h-0.1])
          cube([case_x-2*(wall+fit+lip_t),
                case_y-2*(wall+fit+lip_t), lip_h+0.2]);
      }
    }
    translate([board_x+3, (case_y-9)/2, -1])
      cube([13,9,lid_h+lip_h+2]);
    translate([antenna_x+4, case_y-wall-0.5, lid_h-0.2])
      cube([5,wall+1,2]);
  }
}

module gauge() {
  difference() {
    cube([8,15,10]);
    translate([-1,(15-adapter_w-2*fit)/2,(10-adapter_h-2*fit)/2])
      cube([10,adapter_w+2*fit,adapter_h+2*fit]);
  }
}

if (part == "bottom") bottom();
else if (part == "lid") lid();
else if (part == "gauge") gauge();
else {
  bottom();
  translate([0,case_y+8,0]) lid();
  translate([case_x+8,0,0]) gauge();
}
