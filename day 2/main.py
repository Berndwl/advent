input_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0]
input_list[1] = 12
input_list[2] = 2


def process_opcode(opcode, index=0):
    new_opcode = opcode
    operator = opcode[index]

    number_one = opcode[opcode[index + 1]]
    number_two = opcode[opcode[index + 2]]

    if operator == 99:
        return new_opcode
    elif operator == 1:
        new_opcode[opcode[index + 3]] = number_one + number_two
    elif operator == 2:
        new_opcode[opcode[index + 3]] = number_one * number_two

    return process_opcode(new_opcode, index + 4)


print(process_opcode(input_list))
