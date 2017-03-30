from cppyy import NULL
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
        chip_ids = range(8,0,-1)
#         chip_ids = range(1, 9)
        chips_local_x = [(3-i)*chip_size_mm for i in range(4)] + [(i+1)*chip_size_mm for i in range(4)]
        chips_local_y = 4 * [0] + 4 * [2*chip_size_mm]
        chips_local_phi = 4 * [0] + 4 * [3.141593]
        
        print(chips_local_x)
        
        for b in boards:
            FEC = (b-1) / 4
            chips = [Chip(b, i, chips_local_x[i-1] + 4 * chip_size_mm * FEC, 
                                chips_local_y[i-1] + (3 - (b-1)%4) * 2 * chip_size_mm, 
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
</gear>""")

if __name__ == "__main__":
    generate_ideal_gear()


