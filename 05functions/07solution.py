def sum_all(*chai):
    print(chai)
    for i in chai:
        print(i*2)
    return sum(chai)
# def sum_all(*args):
#     return sum(args)

print(sum_all(1,2, 3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,6,7,8))