from cppyy import NULL

gear_coords = {
               1: {
                   1: (-79.77632, 57.03601, 0.01),
                   2: (-65.38573, 57.2241, 0.01045),
                   3: (-50.84527, 57.37637, 0.01117),
                   4: (-36.39533, 57.39247, 0.00404),
                   5: (-50.70365, 85.69349, 3.15167),
                   6: (-65.24755, 85.64375, 3.15079),
                   7: (-79.88347, 85.45852, 3.16),
                   8: (-94.22249, 85.33533, 3.1525),
                  },
               2: {
                   1: (-87.03459, 16.20416, 0.00661),
                   2: (-72.65197, 16.28334, 0.00451),
                   3: (-58.16382, 16.28351, 0.0029),
                   4: (-43.50703, 16.42828, 0.01228),
                   5: (-57.80204, 44.74118, 3.14856),
                   6: (-72.2894, 44.65592, 3.14359),
                   7: (-86.87542, 44.57215, 3.15017),
                   8: (-101.2889, 44.54186, 3.14568),
                  },
               3: {
                   1: (-80.51588, -24.55607, 0.01241),
                   2: (-65.98125, -24.74233, 0.01665),
                   3: (-51.24028, -24.76987, 0.00635),
                   4: (-36.63222, -24.75659, 0.00042),
                   5: (-50.72232, 3.63711, 3.14365),
                   6: (-65.17437, 3.66417, 3.13966),
                   7: (-79.63428, 3.84193, 3.12803),
                   8: (-94.63804, 3.9707, 3.14359),
                  },
               4: {
                   1: (-86.91317, -65.4561, 0.00203),
                   2: (-72.42711, -65.36378, 0.00601),
                   3: (-58.05696, -65.35341, 0.00119),
                   4: (-43.61041, -65.4277, 0.00507),
                   5: (-57.56028, -36.98363, 3.14651),
                   6: (-72.13536, -36.97664, 3.14745),
                   7: (-86.70482, -37.10114, 3.15065),
                   8: (-101.11513, -37.15713, 3.14549),
                  },
               5: {
                   1: (-11.78767, 57.28363, 0.00189),
                   2: (2.71682, 57.11754, 0.00443),
                   3: (17.29473, 57.16187, 0.00109),
                   4: (31.88023, 57.1971, 0.00593),
                   5: (17.84039, 85.48269, 3.14404),
                   6: (3.30722, 85.62762, 3.13324),
                   7: (-11.2518, 85.54824, 3.13567),
                   8: (-25.90918, 85.62083, 3.14369),
                  },
               6: {
                   1: (-18.42531, 16.10248, 0.00632),
                   2: (-3.94267, 16.25253, 0.00678),
                   3: (10.64114, 16.3097, 0.00294),
                   4: (25.1262, 16.3608, 0.00154),
                   5: (11.05966, 44.74591, 3.13903),
                   6: (-3.51115, 44.69122, 3.14279),
                   7: (-18.0927, 44.55154, 3.14944),
                   8: (-32.73703, 44.41199, 3.15035),
                  },
               7: {
                   1: (-12.09616, -24.79751, 0.00523),
                   2: (2.4292, -24.74731, 0.0139),
                   3: (16.96581, -24.60023, 0.00904),
                   4: (31.31151, -24.51526, 0.01528),
                   5: (17.12493, 3.75818, 3.15432),
                   6: (2.7263, 3.76396, 3.15294),
                   7: (-11.92279, 3.64976, 3.16063),
                   8: (-26.32926, 3.49544, 3.15251),
                  },
               8: {
                   1: (-19.04772, -65.51615, 0.00068),
                   2: (-4.57888, -65.58901, 0.00115),
                   3: (10.04819, -65.53949, 0.00301),
                   4: (24.58186, -65.4512, 0.00414),
                   5: (10.40158, -37.14963, 3.14715),
                   6: (-4.14387, -37.19475, 3.14749),
                   7: (-18.6422, -37.13362, 3.13921),
                   8: (-33.16701, -37.15795, 3.1484),
                  },
               9: {
                   1: (86.22099, 89.50069, 3.14549),
                   2: (71.70684, 89.47225, 3.14499),
                   3: (57.24348, 89.48012, 3.14247),
                   4: (42.75884, 89.55627, 3.13968),
                   5: (56.9969, 52.94827, 0.00194),
                   6: (71.42386, 52.91088, 0.00216),
                   7: (85.98341, 52.9258, 0.00034),
                   8: (100.48618, 52.94796, 0.00112),
                  },
               10: {
                   1: (49.45251, 16.02725, 0.00744),
                   2: (64.083, 15.97818, 0.00214),
                   3: (78.54311, 15.96102, 0.00348),
                   4: (92.96048, 15.91899, 0.00162),
                   5: (78.94323, 44.33578, 3.14117),
                   6: (64.49023, 44.33083, 3.14254),
                   7: (50.1046, 44.3594, 3.14082),
                   8: (35.64041, 44.49646, 3.13856),
                  },
               11: {
                   1: (56.24573, -24.78985, 0.01133),
                   2: (70.60041, -24.94718, 0.01543),
                   3: (85.11327, -25.10218, 0.01325),
                   4: (99.62472, -25.15542, 0.0079),
                   5: (85.98235, 3.35179, 3.13101),
                   6: (71.61355, 3.48977, 3.1268),
                   7: (56.99793, 3.63163, 3.1247),
                   8: (42.47345, 3.71308, 3.13561),
                  },
               12: {
                   1: (49.1929, -65.74068, 0.00904),
                   2: (63.68032, -65.90074, 0.01201),
                   3: (78.2152, -65.96673, 0.00493),
                   4: (92.71399, -66.05526, 0.00563),
                   5: (79.06237, -37.52212, 3.13015),
                   6: (64.53857, -37.44692, 3.13507),
                   7: (49.98333, -37.37736, 3.13183),
                   8: (35.61612, -37.13484, 3.12738),
                  }
              }
class Chip():
    def __init__(self, board, id, x, y, phi):
        self.board = board
        self.id = id
        self.x = x
        self.y = y
        self.phi = phi
        
    def __repr__(self):
        return '<!-- Octoboard: %d; Chip: %d--><module> <offset x_r="%f" y_phi="%f" /><angle value="%f" /></module>\n' % (
            self.board, self.id, self.x, self.y, self.phi)

def reverse_chips_in_boards():
    pass

def reverse_8boards():
    with open("gear_chips.txt") as fin:
        with open("gear_chips_generated.txt", 'w') as fout:
            fout.writelines(reversed(fin.readlines()))
        
def write_chip(f, board, chip):
    f.write()
        
def write_8board(f, board, chips):
    for c in chips:
        print_chip(f, board, chip)
    
def generate_ideal_gear():
    chip_size_mm = 14.08;
    boards = range(1, 12+1)
    
    with open("../GearLALideal.xml", 'w') as out_file:
        out_file.write("""<?xml version="1.0"?>
<gear>
  <!-- 
    GEAR xml file for the end plate of the LP TPC with GEM module
  -->
  <BField type="ConstantBField" x="0.0" y="0.0" z="0.0"/>
  <!--global detectorName="LPTPCDetector" /-->
  <detectors>
    <!-- The TPC has geartype set to TPCParameters -->
    <detector name="TPC" geartype="TPCParameters">
      <parameter name="BField" type="double"> 0.0 </parameter>
      <!-- First set the global parameters -->
      <!-- Drift length in mm -->
      <maxDriftLength value="600.0"/>
      <coordinateType value="cartesian"/>
      <!--driftVelocity value="75200000." / -->
      <!-- readoutFrequency value="4.0e+07" / -->
      <!-- The module section
         The first module has ID 20, for all following
         modules the ID is increased by 1 -->
      <modules moduleIDStartCount="0">
        <!-- The below description is defined as default module. -->
        <default>
          <!-- 40 MHz readout electronics -->
          <readoutFrequency value="40000000"/>
          <PadRowLayout2D type="RectangularPadRowLayout" xMin="-7.0555" xMax="7.0555" yMin="0">
            <row repeat="256" nPad="256" padHeight="0.055" padWidth="0.055" rowHeight="0.055"/>
          </PadRowLayout2D>
        </default>
""")
        chip_ids = range(8, 0, -1)
#         chip_ids = range(1, 9)
        chips_local_x = [(3-i)*chip_size_mm for i in range(4)] + [(i+1)*chip_size_mm for i in range(4)]
        chips_local_y = 4 * [0] + 4 * [2*chip_size_mm]
        chips_local_phi = 4 * [0] + 4 * [3.141593]
        
        print(chips_local_x)
        
        for b in boards:
            FEC = (b-1) / 4
            chips = [Chip(b, i, chips_local_x[i-1] + 4 * chip_size_mm * FEC + 7. * (b%2) + FEC * 12., 
                                chips_local_y[i-1] + (3 - (b-1)%4) * (2*chip_size_mm + 12), 
                                chips_local_phi[i-1])
                     for i in chip_ids]
            out_file.write("".join([repr(c) for c in reversed(chips)]))
            out_file.write("\n")

        out_file.write("""
      </modules>
      <!--Special parameters for HepRep event display-->
      <!--It should be 357. -->
      <parameter name="TPCRadius" type="double"> 357 </parameter>
      <!-- Do not set inner parameter, nothing to draw -->
      <!-- the Inner raius shouldbe 0.0 -->
      <parameter name="TPCInnerRadius" type="double"> 0.0  </parameter>
      <!--parameter name="TPC_cylinder_centre_c0"      type="double" > 0.0 </parameter-->
      <parameter name="TPC_cylinder_centre_c0" type="double"> 1503.615 </parameter>
      <parameter name="TPC_cylinder_centre_c1" type="double"> 0.0 </parameter>
    </detector>
  </detectors>
</gear>
""")

if __name__ == "__main__":
    generate_ideal_gear()


