def calculate_fuel_recursed(fuel, fuel_sum=0):
    new_fuel = (fuel // 3) - 2
    if new_fuel > 0:
        fuel_sum += new_fuel
        return calculate_fuel_recursed(new_fuel, fuel_sum)
    else:
        return fuel_sum


print(sum(x for x in [calculate_fuel_recursed(int(line.strip())) for line in
                      open("input.txt", "r")]))

