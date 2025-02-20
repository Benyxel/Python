cars = {
    "c1": "Honda",
    "c2": "Civic",
    "c3": "RAM",
    "c4": "R150"
}

size = len(cars) +1

adding = int(input("How many cars do you wanna add?: "))
for i in range(adding):
    newCars = input("Input the car Name: ")
    print( )
    cars[f"c{size+i}"] = newCars
print(cars)
