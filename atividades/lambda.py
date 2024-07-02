
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name = get_full_name('John','Doe',lambda first_name, last_name: f"{first_name} {last_name}") #saída Jhon (first name) Doe (Last name)

print(full_name)

full_name = get_full_name('John','Doe',lambda first_name, last_name: f"{last_name} {first_name}") #saída Doe (Last name) jhon (Frist Name)

print(full_name)