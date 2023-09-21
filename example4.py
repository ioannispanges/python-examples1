def display_info(**kwargs):
    if "name" in kwargs:
        print("Name:", kwargs["name"])
    if "age" in kwargs:
        print("Age: ", kwargs["age"])
    if "location" in kwargs:
        print("Location: ", kwargs["location"])


display_info(name="Alice", age=25, location="New York ")


