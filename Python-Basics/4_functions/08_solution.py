def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="Shaktiman",power="laser")
print_kwargs(name="Kilwish")
print_kwargs(name="Shaktiman",power="laser", enemy="jackal")

