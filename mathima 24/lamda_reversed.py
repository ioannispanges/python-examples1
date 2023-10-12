leksiko = [
    {'name': 'Alice', 'age': 30},
    {'name': 'John', 'age': 25},
    {'name': 'Charlie', 'age': 35},

]

sorted_data = sorted(leksiko, key=lambda x: x['age'], reverse=True)
print(sorted_data)
