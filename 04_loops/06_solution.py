input_number = int(input("Give a number to find its factorial: "))
factorial = 1

# for i in range(1, int(input_number) + 1):
#     factorial = factorial*i
# print(factorial)

while input_number > 0:
    factorial = factorial*input_number
    input_number = input_number - 1
print(factorial)