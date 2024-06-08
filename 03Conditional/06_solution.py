distance = 100

if distance < 3:
    activity = "Walk"
elif distance < 15:
    activity = "Bike"
else :
    activity = "Car"

print("You should go by a ", activity)