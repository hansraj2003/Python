def print_kwargs(**kwargs):
    # print("Name: ", name, " Surname: ", surname)
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="Hansraj", surname="Joshi")
print_kwargs( surname="Joshi",name="Hansraj")
print_kwargs(name="Hansraj")
print_kwargs( surname="Joshi",name="Hansraj", designation="Mr.")