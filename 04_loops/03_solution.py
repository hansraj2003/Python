n = 10
given_number = 5
multiplication = 1

print(" Table for 5 is: ")
for i in range(1, n + 1):
    if i == 5:
        continue;
    else:
        multiplication = given_number*i
        print(multiplication)

# print(multiplication)