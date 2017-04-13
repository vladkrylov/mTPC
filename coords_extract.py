import re

from sys import argv

with open("/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/GearLAL.xml") as gear_file:
    lines = gear_file.readlines()
    det_section = [l for l in lines if l.startswith("<!--Module: 2; Octoboard")]
    
    coords = [re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", l) for l in det_section]
    
    for i in range(len(coords)):
        # stripe "-" in chip numbers
        if coords[i][-4][-1] == "-":
            coords[i][-4] = coords[i][-4][:-1]
        
        # 0.xxx correction in angle
        if "." not in coords[i][-1]:
            coords[i][-1] = "0." + coords[i][-1]


    board_id = -1
    print("gear_coords = {")
    for i in range(len(coords)):
        new_board_id = int(coords[i][-5])
        if new_board_id != board_id:
            board_id = new_board_id
            if board_id != 1:
                print("                  },")
            print("               %s: {" % board_id)
        print("                   %s: (%s, %s, %s)," % tuple(coords[i][-4:]))
    
    print("                  }")
    print("              }")
     