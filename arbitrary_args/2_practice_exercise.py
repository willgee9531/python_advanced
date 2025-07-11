def print_details(*args, **kwargs):
    full_name = ""
    full_address = ""

    for arg in args:
        full_name += arg + " "
    
    # for key, value in kwargs.items():
    #     full_address += f"{key}: {value}\n"

    full_address += f"{kwargs.get('street')}\n"
    full_address += f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}" if 'zip' in kwargs  else f"{kwargs.get('city')}, {kwargs.get('state')}"

    return f"{full_name.strip()}\n{full_address.strip()}"

print(print_details(
    "Mr.", "Godwin", "Williams", "Chibuzor",
    street="123 Real st. ",
    zip=100278,
    state="Lagos",
    city="Alimosho"
))