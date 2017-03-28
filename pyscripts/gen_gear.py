with open("gear_chips.txt") as fin:
    with open("gear_chips_generated.txt", 'w') as fout:
        fout.writelines(reversed(fin.readlines()))