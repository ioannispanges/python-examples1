global_var = 10


def use_global_var():
    global global_var
    global_var += 5
    print("Inside the function:", global_var)


print("Before the function:", global_var)

use_global_var()

print("After the function", global_var)
