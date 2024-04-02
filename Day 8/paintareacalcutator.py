import math
def paint_cal(wall_height , wall_width , coverage_per_can):
    area=(wall_height*wall_width)/coverage_per_can
    round_number=math.ceil(area)
    print(f"You'll need the {area} per area")

wall_height = int(input("enter your height of wall : "))
wall_width = int(input("enter your width of wall :  "))
coverage_per_can = 5
paint_cal(wall_height , wall_width ,coverage_per_can)
