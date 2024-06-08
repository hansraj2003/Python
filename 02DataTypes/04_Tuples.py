tea_types = ("Black", "Green", "Oolong")
print(tea_types[0])
print(tea_types[0:2])

# tea_types[0] = "Lemon"        
# They are immutable therefore err is shown in the terminal

print(len(tea_types))
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have Green Tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea.count("Herbal"))

(black, green, Oolong) = tea_types
print(black)

print(type(tea_types))