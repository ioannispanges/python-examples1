def process_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


process_parameters(param1=10, param2="value", param3=[1, 2, 3], param4=True)
