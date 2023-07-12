vehicles=["bus","car","train"]

print(vehicles[0])
print(vehicles[1])
print(vehicles[2])

vehicles.append("plane")
print(vehicles)

vehicles.pop(2) #removes/pops out item in third postion in array
print(vehicles)

vehicles.insert(2,"boat")
print(vehicles)

vehicles.sort()
print(vehicles)