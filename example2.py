institution_params = {
    "name": "XYZ Corporation",
    "founding_year": 1995,
    "location": "New York",
    "industry": "Finance",
    "total_assets": 5000000000,
    "numbers_of_employees": 1000
}

print("Name:", institution_params["name"])
print("Founding Year:", institution_params["founding_year"])
print("Location:", institution_params["location"])
print("Industry:", institution_params["industry"])
print("Total Assets:", institution_params["total_assets"])
print("Number of Employees:", institution_params["numbers_of_employees"])

institution_params["total_assets"] = 6000000000

institution_params["website"] = "wwww.in.gr"

print("Updated Total Assets", institution_params["total_assets"])
print("Website", institution_params["website"])
