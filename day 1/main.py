total = sum((int(line.strip()) // 3) - 2 for line in open("input.txt", "r"))