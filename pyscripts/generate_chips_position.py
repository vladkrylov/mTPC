lower_left_corner = 0
lower_right_corner = 1
upper_right_corner = 2
upper_left_corner = 3

chips = [
    ##----------- Row 1 -------------##
    (24, lower_left_corner),
    (25, lower_left_corner),
    (26, lower_left_corner),
    (27, lower_left_corner),
    
    (59, lower_left_corner),
    (58, lower_left_corner),
    (57, lower_left_corner),
    (56, lower_left_corner),
    
    (91, lower_left_corner),
    (90, lower_left_corner),
    (89, lower_left_corner),
    (88, lower_left_corner),
    
    ##----------- Row 2 -------------##
    (31, upper_right_corner),
    (30, upper_right_corner),
    (29, upper_right_corner),
    (28, upper_right_corner),
    
    (60, upper_right_corner),
    (61, upper_right_corner),
    (62, upper_right_corner),
    (63, upper_right_corner),
    
    (92, upper_right_corner),
    (93, upper_right_corner),
    (94, upper_right_corner),
    (95, upper_right_corner),
    
    ##----------- Row 3 ---------------------------------------##
    (19, lower_left_corner),
    (18, lower_left_corner),
    (17, lower_left_corner),
    (16, lower_left_corner),
    
    (51, lower_left_corner),
    (50, lower_left_corner),
    (49, lower_left_corner),
    (48, lower_left_corner),
    
    (83, lower_left_corner),
    (82, lower_left_corner),
    (81, lower_left_corner),
    (80, lower_left_corner),
    
    ##----------- Row 4 -------------##
    (20, upper_right_corner),
    (21, upper_right_corner),
    (22, upper_right_corner),
    (23, upper_right_corner),
    
    (52, upper_right_corner),
    (53, upper_right_corner),
    (54, upper_right_corner),
    (55, upper_right_corner),
    
    (84, upper_right_corner),
    (85, upper_right_corner),
    (86, upper_right_corner),
    (87, upper_right_corner),
    
    ##----------- Row 5 ---------------------------------------##
    (11, lower_left_corner),
    (10, lower_left_corner),
    (9, lower_left_corner),
    (8, lower_left_corner),
    
    (43, lower_left_corner),
    (42, lower_left_corner),
    (41, lower_left_corner),
    (40, lower_left_corner),
    
    (75, lower_left_corner),
    (74, lower_left_corner),
    (73, lower_left_corner),
    (72, lower_left_corner),
    
    ##----------- Row 6 -------------##
    (12, upper_right_corner),
    (13, upper_right_corner),
    (14, upper_right_corner),
    (15, upper_right_corner),

    (44, upper_right_corner),
    (45, upper_right_corner),
    (46, upper_right_corner),
    (47, upper_right_corner),
    
    (76, upper_right_corner),
    (77, upper_right_corner),
    (78, upper_right_corner),
    (79, upper_right_corner),
    
    ##----------- Row 7 ---------------------------------------##
    (0, lower_left_corner),
    (1, lower_left_corner),
    (2, lower_left_corner),
    (3, lower_left_corner),

    (35, lower_left_corner),
    (34, lower_left_corner),
    (33, lower_left_corner),
    (32, lower_left_corner),
    
    (67, lower_left_corner),
    (66, lower_left_corner),
    (65, lower_left_corner),
    (64, lower_left_corner),
    
    ##----------- Row 8 -------------##
    (7, upper_right_corner),
    (6, upper_right_corner),
    (5, upper_right_corner),
    (4, upper_right_corner),
    
    (39, upper_right_corner),
    (38, upper_right_corner),
    (37, upper_right_corner),
    (36, upper_right_corner),
    
    (68, upper_right_corner),
    (69, upper_right_corner),
    (70, upper_right_corner),
    (71, upper_right_corner)
    
    ]

print('<parameter name="ChipIDs" type="IntVec" value="%s"/>' % ' '.join([str(k) for k, v in chips]))
print('<parameter name="chipOrientation" type="IntVec" value="%s"/>' % ' '.join([str(v) for k, v in chips]))

