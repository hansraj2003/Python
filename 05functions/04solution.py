def area_and_circumference(radius):
    area = (22/7) * (radius**2)
    circumference = 2 *(22/7)*radius
    return area,circumference

# print(area_and_circumference(7))
a,c = area_and_circumference(7)
print("Area: ", a, "Circumference: ", c)