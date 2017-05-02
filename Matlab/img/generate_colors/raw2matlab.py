with open("contrast_colors_raw.txt") as inp_file:
    with open("contrast_colors_matlab.txt", 'w') as out_file:
        #cols = inp_file.readlines()
        out_file.write("col_map = [...\n")
        for l in inp_file:
            r, g, b = [float(x)/255. for x in l.split()]
            out_file.write("[%.1f,%.1f,%.1f],...\n" % (r, g, b))
            
        out_file.write("];\n")
