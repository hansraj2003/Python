n = input("Give a number till which you want to sum")
sum_even = 0

for i in range(1, int(n)+1):
    if i%2==0:
        sum_even = sum_even + i


print(sum_even)
    