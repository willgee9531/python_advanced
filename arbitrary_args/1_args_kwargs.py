# Types of Arguments: 1. Positional 2. Default 3. Keyword 4. Arbitrary (varying and undefined amount)
# *args - allows you to pass multiple non-key arguments (unpack into a tuple())
# *kwargs - allows you to pass multiple keyword-arguments (unpack into a dictionary{})
# (*) - unpacking operator

# *args
def add_nums(*args):
    # print(args)
    # print(type(args))

    total = 0
    for arg in args:
        total += arg
    return total

# print(add_nums(1, 4, 7))


def print_name(*args):
    full_name = ""
    for arg in args:
        full_name += arg + " "
    return full_name.strip()

print(print_name("Dr.", "Spongebob", "Harold", "Squarepants", "III"))


# **kwargs
def print_address(**kwargs):
    full_address = ""
    for key, value in kwargs.items():
        full_address += f"{key}: {value}\n"
    return full_address.strip()
    
print(print_address(
    street="123, real st.",
    city="Alimosho",
    state="Lagos",
    zip_code=100278
))