def is_inside(point = [], rectangle = []):
    if rectangle[0] <= point[0] <= rectangle[0] + rectangle[2] and rectangle[1] <= point[1] <= rectangle[1]+ rectangle[3]:
        return True
    else:
        return False
point_pos = is_inside([200, 120], [140, 60, 100, 200])
if point_pos:
    print("Your function is corret")
else:
    print("Oops, there's a bug")
# def is_inside(x, y, a, b, width, length):
#     if a <= x <= a + width and b <= y <= b+ length:
#         return True
#     else:
#         return False
# point_pos = is_inside(200, 120, 140, 60, 100, 200)
# if point_pos:
#     print("Your function is corret")
# else:
#     print("Oops, there's a bug")
