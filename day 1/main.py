# Part 1
print(sum((int(line.strip()) // 3) - 2 for line in open("input.txt", "r")))

# Part 2
def calculate_fuel_recursed(fuel):
    new_fuel = (fuel // 3) - 2
    if new_fuel > 0:
        return new_fuel + calculate_fuel_recursed(new_fuel)
    else:
        return 0


print(sum(x for x in [calculate_fuel_recursed(int(line.strip())) for line in
                      open("input.txt", "r")]))

